import type { APIRoute } from "astro";
import { json } from "~/lib/cf-helpers";

export const prerender = false;

// Internal: embed product text and upsert into Vectorize.
// Auth: Authorization: Bearer ${REINDEX_SECRET}.
// Set the secret via: npx wrangler secret put REINDEX_SECRET
//
// Body shape:
//   { items: [{ id: string, text: string, metadata?: Record<string, unknown> }] }

const EMBED_MODEL = "@cf/baai/bge-small-en-v1.5";
const EMBED_BATCH = 50;
const UPSERT_BATCH = 100;

type Item = { id: string; text: string; metadata?: Record<string, unknown> };

export const POST: APIRoute = async ({ request, locals }) => {
  const env = locals.runtime.env as Env & { REINDEX_SECRET?: string };

  const auth = request.headers.get("authorization") ?? "";
  const expected = env.REINDEX_SECRET;
  if (!expected || auth !== `Bearer ${expected}`) {
    return json({ ok: false, error: "unauthorized" }, { status: 401 });
  }

  let body: { items?: unknown };
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: "invalid_json" }, { status: 400 });
  }

  const items = Array.isArray(body.items) ? (body.items as Item[]) : [];
  if (items.length === 0) {
    return json({ ok: false, error: "no_items" }, { status: 400 });
  }

  let embedded = 0;
  let upserted = 0;

  for (let i = 0; i < items.length; i += EMBED_BATCH) {
    const batch = items.slice(i, i + EMBED_BATCH);
    const texts = batch.map((b) => b.text);

    const out = (await env.AI.run(EMBED_MODEL, { text: texts })) as {
      data: number[][];
    };
    if (!out.data || out.data.length !== batch.length) {
      return json(
        { ok: false, error: "embed_shape_mismatch", at: i },
        { status: 500 },
      );
    }
    embedded += out.data.length;

    const vectors = batch.map((b, idx) => ({
      id: b.id,
      values: out.data[idx],
      metadata: b.metadata ?? {},
    }));

    for (let j = 0; j < vectors.length; j += UPSERT_BATCH) {
      const slice = vectors.slice(j, j + UPSERT_BATCH);
      await env.VECTORIZE.upsert(slice);
      upserted += slice.length;
    }
  }

  return json({ ok: true, embedded, upserted });
};

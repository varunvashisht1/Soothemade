import type { APIRoute } from "astro";
import { json, rateLimit, clientIp, sha256Hex } from "~/lib/cf-helpers";

export const prerender = false;

// Workers AI embedding model. 384-dim, matches the Vectorize index.
const EMBED_MODEL = "@cf/baai/bge-small-en-v1.5";

type SearchHit = {
  code: string;
  title: string;
  slug: string;
  summary: string;
  category?: string;
  score: number;
};

export const GET: APIRoute = async ({ request, locals, url }) => {
  const env = locals.runtime.env;

  const q = (url.searchParams.get("q") ?? "").trim();
  if (!q) return json({ ok: true, hits: [] });
  if (q.length > 500) {
    return json({ ok: false, error: "query_too_long" }, { status: 400 });
  }

  // Light per-IP rate limit so AI calls can't be flooded.
  const ipHash = await sha256Hex(clientIp(request));
  const allowed = await rateLimit(env.CACHE, `rl:search:${ipHash}`, 30, 60);
  if (!allowed) {
    return json({ ok: false, error: "rate_limited" }, { status: 429 });
  }

  const embed = (await env.AI.run(EMBED_MODEL, { text: [q] })) as {
    data: number[][];
  };
  const vector = embed.data?.[0];
  if (!vector) {
    return json({ ok: false, error: "embed_failed" }, { status: 500 });
  }

  const result = await env.VECTORIZE.query(vector, {
    topK: 6,
    returnMetadata: "all",
  });

  const hits: SearchHit[] = (result.matches ?? []).map((m) => {
    const md = (m.metadata ?? {}) as Record<string, unknown>;
    return {
      code: String(md.code ?? m.id),
      title: String(md.title ?? ""),
      slug: String(md.slug ?? ""),
      summary: String(md.summary ?? ""),
      category: md.category ? String(md.category) : undefined,
      score: m.score,
    };
  });

  return json({ ok: true, hits });
};

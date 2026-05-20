import type { APIRoute } from "astro";
import { json, todayUtc } from "~/lib/cf-helpers";

export const prerender = false;

// Bump a daily view counter for /journal/[slug].
// Client-side fetched after the post renders, so static prerender stays cacheable.
export const POST: APIRoute = async ({ params, locals }) => {
  const env = locals.runtime.env;
  const slug = (params.slug ?? "").trim();
  if (!slug || slug.length > 120) {
    return json({ ok: false, error: "bad_slug" }, { status: 400 });
  }

  await env.DB.prepare(
    `INSERT INTO journal_views (slug, day, count)
     VALUES (?, ?, 1)
     ON CONFLICT(slug, day) DO UPDATE SET count = count + 1`,
  )
    .bind(slug, todayUtc())
    .run();

  return json({ ok: true });
};

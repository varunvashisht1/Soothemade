import type { APIRoute } from "astro";
import { nowSec } from "~/lib/cf-helpers";

export const prerender = false;

// Gated download: /files/dl/<token>. The token is issued by the Stripe webhook
// after a paid checkout and is valid for 30 days (re-downloads allowed within
// the window so buyers who lose the file can fetch it again).
export const GET: APIRoute = async ({ params, locals }) => {
  const env = locals.runtime.env;
  const token = (params.token ?? "").replace(/[^a-f0-9]/gi, "");
  if (token.length < 16) return new Response("Not found", { status: 404 });

  const row = await env.DB.prepare(
    `SELECT product_code, expires_at, used_at FROM download_tokens WHERE token = ?`,
  )
    .bind(token)
    .first<{ product_code: string; expires_at: number; used_at: number | null }>();

  if (!row) {
    return new Response("This download link is not valid.", { status: 404 });
  }

  const now = nowSec();
  if (row.expires_at && now > row.expires_at) {
    return new Response(
      "This download link has expired. Reply to your receipt and we will reissue it.",
      { status: 410 },
    );
  }

  const code = String(row.product_code).toUpperCase();
  const object = await env.FILES.get(`products/${code}.pdf`);
  if (!object) {
    return new Response("That file is not available yet.", { status: 404 });
  }

  // Stamp first use (for analytics); not a hard cap.
  if (!row.used_at) {
    await env.DB.prepare(`UPDATE download_tokens SET used_at = ? WHERE token = ?`)
      .bind(now, token)
      .run();
  }

  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("content-type", "application/pdf");
  headers.set("content-disposition", `attachment; filename="soothemade-${code}.pdf"`);
  headers.set("cache-control", "private, no-store");
  return new Response(object.body, { headers });
};

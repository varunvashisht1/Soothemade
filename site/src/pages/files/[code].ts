import type { APIRoute } from "astro";

export const prerender = false;

// Stream a product PDF from R2 by product code, e.g. /files/P09.
// Tokens (for paid-gated downloads) come in a separate /files/dl/[token]
// route once orders flow exists.
export const GET: APIRoute = async ({ params, locals }) => {
  const env = locals.runtime.env;
  const raw = params.code ?? "";

  // Accept "P09" or "P09.pdf". Normalise.
  const code = raw.replace(/\.pdf$/i, "").toUpperCase();
  if (!/^P\d{2,3}$/.test(code)) {
    return new Response("Not found", { status: 404 });
  }

  const key = `products/${code}.pdf`;
  const object = await env.FILES.get(key);
  if (!object) {
    return new Response("Not found", { status: 404 });
  }

  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("content-type", "application/pdf");
  headers.set("cache-control", "public, max-age=3600");
  headers.set(
    "content-disposition",
    `inline; filename="soothemade-${code}.pdf"`,
  );
  headers.set("etag", object.httpEtag);

  return new Response(object.body, { headers });
};

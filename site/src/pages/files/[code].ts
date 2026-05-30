import type { APIRoute } from "astro";

export const prerender = false;

// Codes that are intentionally free to download by direct link (e.g. a
// lead-magnet freebie). Everything else is paid and must come through a
// purchase token at /files/dl/[token]. Keep this list short and deliberate.
const FREE_CODES = new Set<string>([]);

// Direct-by-code download. Paid products are NOT served here (that would
// bypass checkout); they 404 and must use a purchased /files/dl/[token] link.
export const GET: APIRoute = async ({ params, locals }) => {
  const env = locals.runtime.env;
  const code = (params.code ?? "").replace(/\.pdf$/i, "").toUpperCase();

  if (!/^P\d{2,3}$/.test(code) || !FREE_CODES.has(code)) {
    return new Response("Not found", { status: 404 });
  }

  const object = await env.FILES.get(`products/${code}.pdf`);
  if (!object) return new Response("Not found", { status: 404 });

  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("content-type", "application/pdf");
  headers.set("cache-control", "public, max-age=3600");
  headers.set("content-disposition", `inline; filename="soothemade-${code}.pdf"`);
  headers.set("etag", object.httpEtag);
  return new Response(object.body, { headers });
};

import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import { clientIp, json, rateLimit, sha256Hex } from "~/lib/cf-helpers";
import { createCheckoutSession, type LineItem } from "~/lib/stripe";

export const prerender = false;

// POST { code: "P09" }  or  { codes: ["P09","P11"] }
// -> { ok: true, url: "https://checkout.stripe.com/..." }
export const POST: APIRoute = async ({ request, locals }) => {
  const env = locals.runtime.env;
  const secret = env.STRIPE_SECRET_KEY;
  if (!secret) {
    // Keys not set yet: the client falls back to the notify-me form.
    return json({ ok: false, error: "not_configured" }, { status: 503 });
  }

  let body: { code?: unknown; codes?: unknown };
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: "invalid_json" }, { status: 400 });
  }

  const codes = Array.isArray(body.codes)
    ? (body.codes.filter((c) => typeof c === "string") as string[]).slice(0, 20)
    : typeof body.code === "string"
      ? [body.code]
      : [];
  if (codes.length === 0) {
    return json({ ok: false, error: "no_items" }, { status: 400 });
  }

  const ipHash = await sha256Hex(clientIp(request));
  if (!(await rateLimit(env.CACHE, `rl:checkout:${ipHash}`, 20, 3600))) {
    return json({ ok: false, error: "rate_limited" }, { status: 429 });
  }

  const products = await getCollection("products");
  const items: LineItem[] = [];
  for (const code of codes) {
    const product = products.find((p) => p.data.code === code);
    if (!product) {
      return json({ ok: false, error: "unknown_code", code }, { status: 400 });
    }
    items.push({
      code,
      name: product.data.title,
      amountCents: Math.round(product.data.price * 100),
    });
  }

  const origin = new URL(request.url).origin;
  const firstSlug = products.find((p) => p.data.code === codes[0])!.id;

  try {
    const session = await createCheckoutSession(secret, {
      items,
      successUrl: `${origin}/shop/success?session_id={CHECKOUT_SESSION_ID}`,
      cancelUrl: `${origin}/shop/${firstSlug}`,
    });
    return json({ ok: true, url: session.url });
  } catch {
    return json({ ok: false, error: "stripe_error" }, { status: 502 });
  }
};

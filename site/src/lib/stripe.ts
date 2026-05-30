// Minimal Stripe REST client for the Cloudflare Workers runtime.
// No SDK: we call the API with fetch and verify webhooks with Web Crypto,
// so there is nothing to bundle and no Node polyfills.

const STRIPE_API = "https://api.stripe.com/v1";

export interface LineItem {
  code: string;
  name: string;
  amountCents: number;
}

function formEncode(params: Record<string, string>): string {
  return Object.entries(params)
    .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
    .join("&");
}

/**
 * Create a Stripe Checkout Session with inline price_data (so we never have to
 * pre-create Stripe Products). Returns the hosted-checkout URL to redirect to.
 */
export async function createCheckoutSession(
  secretKey: string,
  opts: { items: LineItem[]; successUrl: string; cancelUrl: string },
): Promise<{ id: string; url: string }> {
  const params: Record<string, string> = {
    mode: "payment",
    success_url: opts.successUrl,
    cancel_url: opts.cancelUrl,
    "payment_method_types[0]": "card",
    customer_creation: "always",
    allow_promotion_codes: "true",
    "metadata[codes]": opts.items.map((i) => i.code).join(","),
  };
  opts.items.forEach((item, i) => {
    params[`line_items[${i}][quantity]`] = "1";
    params[`line_items[${i}][price_data][currency]`] = "usd";
    params[`line_items[${i}][price_data][unit_amount]`] = String(item.amountCents);
    params[`line_items[${i}][price_data][product_data][name]`] = item.name;
    params[`line_items[${i}][price_data][product_data][metadata][code]`] = item.code;
  });

  const res = await fetch(`${STRIPE_API}/checkout/sessions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${secretKey}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: formEncode(params),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`stripe_${res.status}: ${text.slice(0, 300)}`);
  }
  const data = (await res.json()) as { id: string; url: string };
  return { id: data.id, url: data.url };
}

/** Retrieve a Checkout Session (used by the success page as a webhook backstop). */
export async function retrieveSession(
  secretKey: string,
  sessionId: string,
): Promise<{ payment_status: string; customer_details?: { email?: string }; metadata?: { codes?: string }; amount_total?: number; currency?: string } | null> {
  const res = await fetch(`${STRIPE_API}/checkout/sessions/${encodeURIComponent(sessionId)}`, {
    headers: { Authorization: `Bearer ${secretKey}` },
  });
  if (!res.ok) return null;
  return res.json();
}

function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let out = 0;
  for (let i = 0; i < a.length; i++) out |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return out === 0;
}

/**
 * Verify the Stripe-Signature header (the t=,v1= scheme) using HMAC-SHA256.
 * Mirrors Stripe's constructEvent verification without the SDK.
 */
export async function verifyStripeSignature(
  payload: string,
  sigHeader: string,
  secret: string,
  toleranceSec = 300,
): Promise<boolean> {
  if (!sigHeader) return false;
  const parts: Record<string, string> = {};
  for (const piece of sigHeader.split(",")) {
    const [k, v] = piece.split("=");
    if (k && v) parts[k.trim()] = v.trim();
  }
  const t = parts["t"];
  const v1 = parts["v1"];
  if (!t || !v1) return false;

  const ts = parseInt(t, 10);
  if (!Number.isFinite(ts)) return false;
  const now = Math.floor(Date.now() / 1000);
  if (Math.abs(now - ts) > toleranceSec) return false;

  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const sig = await crypto.subtle.sign(
    "HMAC",
    key,
    new TextEncoder().encode(`${t}.${payload}`),
  );
  const expected = Array.from(new Uint8Array(sig))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
  return timingSafeEqual(expected, v1);
}

/** 64-char hex download token (two UUIDs, dashes stripped). */
export function newToken(): string {
  return (
    crypto.randomUUID().replace(/-/g, "") + crypto.randomUUID().replace(/-/g, "")
  );
}

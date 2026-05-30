import type { APIRoute } from "astro";
import { nowSec } from "~/lib/cf-helpers";
import { newToken, verifyStripeSignature } from "~/lib/stripe";

export const prerender = false;

const TOKEN_TTL_SEC = 60 * 60 * 24 * 30; // 30 days to download

// Stripe webhook. Set the endpoint to /api/webhooks/stripe in the Stripe
// dashboard and subscribe to `checkout.session.completed`.
export const POST: APIRoute = async ({ request, locals }) => {
  const env = locals.runtime.env;
  const whSecret = env.STRIPE_WEBHOOK_SECRET;
  if (!whSecret) return new Response("not configured", { status: 503 });

  const payload = await request.text();
  const sig = request.headers.get("stripe-signature") ?? "";
  if (!(await verifyStripeSignature(payload, sig, whSecret))) {
    return new Response("bad signature", { status: 400 });
  }

  let event: { type: string; data: { object: Record<string, unknown> } };
  try {
    event = JSON.parse(payload);
  } catch {
    return new Response("bad json", { status: 400 });
  }

  if (event.type === "checkout.session.completed") {
    await fulfill(env, event.data.object);
  }

  // Always 200 so Stripe stops retrying once we have the event.
  return new Response("ok", { status: 200 });
};

async function fulfill(env: Env, session: Record<string, unknown>) {
  const sessionId = String(session.id ?? "");
  const details = session.customer_details as { email?: string } | undefined;
  const email = details?.email ?? (session.customer_email as string | undefined) ?? null;
  const meta = session.metadata as { codes?: string } | undefined;
  const codes = (meta?.codes ?? "")
    .split(",")
    .map((c) => c.trim())
    .filter(Boolean);
  if (!sessionId || codes.length === 0) return;

  const amountTotal = typeof session.amount_total === "number" ? session.amount_total : null;
  const currency = String(session.currency ?? "usd").toUpperCase();
  const perAmount = codes.length === 1 ? amountTotal : null;
  const ts = nowSec();
  const expires = ts + TOKEN_TTL_SEC;

  for (const code of codes) {
    const externalId = `${sessionId}#${code}`;
    // UNIQUE(platform, external_id) + DO NOTHING makes this idempotent across
    // Stripe's webhook retries. RETURNING yields no row on conflict.
    const order = await env.DB.prepare(
      `INSERT INTO orders (product_code, platform, external_id, email, amount_cents, currency, created_at)
       VALUES (?, 'stripe', ?, ?, ?, ?, ?)
       ON CONFLICT(platform, external_id) DO NOTHING
       RETURNING id`,
    )
      .bind(code, externalId, email, perAmount, currency, ts)
      .first<{ id: number }>();

    if (!order) continue; // already fulfilled

    await env.DB.prepare(
      `INSERT INTO download_tokens (token, product_code, email, order_id, created_at, expires_at)
       VALUES (?, ?, ?, ?, ?, ?)`,
    )
      .bind(newToken(), code, email ?? "", order.id, ts, expires)
      .run();
  }
}

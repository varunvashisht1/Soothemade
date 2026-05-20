import type { APIRoute } from "astro";
import {
  clientIp,
  isEmail,
  json,
  nowSec,
  rateLimit,
  sha256Hex,
} from "~/lib/cf-helpers";

export const prerender = false;

export const POST: APIRoute = async ({ request, locals }) => {
  const env = locals.runtime.env;

  let body: {
    name?: unknown;
    email?: unknown;
    subject?: unknown;
    message?: unknown;
  };
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: "invalid_json" }, { status: 400 });
  }

  const name = typeof body.name === "string" ? body.name.trim().slice(0, 120) : "";
  const email =
    typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  const subject =
    typeof body.subject === "string" ? body.subject.trim().slice(0, 200) : null;
  const message =
    typeof body.message === "string" ? body.message.trim().slice(0, 5000) : "";

  if (!name || !isEmail(email) || !message) {
    return json({ ok: false, error: "invalid_fields" }, { status: 400 });
  }

  const ipHash = await sha256Hex(clientIp(request));

  const allowed = await rateLimit(env.CACHE, `rl:contact:${ipHash}`, 3, 3600);
  if (!allowed) {
    return json({ ok: false, error: "rate_limited" }, { status: 429 });
  }

  await env.DB.prepare(
    `INSERT INTO contact_messages (name, email, subject, message, ip_hash, created_at)
     VALUES (?, ?, ?, ?, ?, ?)`,
  )
    .bind(name, email, subject, message, ipHash, nowSec())
    .run();

  return json({ ok: true });
};

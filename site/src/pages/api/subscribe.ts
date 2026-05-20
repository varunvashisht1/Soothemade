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

  let body: { email?: unknown; source?: unknown };
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: "invalid_json" }, { status: 400 });
  }

  const email =
    typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  const source =
    typeof body.source === "string" ? body.source.slice(0, 64) : null;

  if (!isEmail(email)) {
    return json({ ok: false, error: "invalid_email" }, { status: 400 });
  }

  const ip = clientIp(request);
  const ipHash = await sha256Hex(ip);

  const allowed = await rateLimit(
    env.CACHE,
    `rl:subscribe:${ipHash}`,
    5,
    3600,
  );
  if (!allowed) {
    return json({ ok: false, error: "rate_limited" }, { status: 429 });
  }

  await env.DB.prepare(
    `INSERT INTO subscribers (email, created_at, source, ip_hash)
     VALUES (?, ?, ?, ?)
     ON CONFLICT(email) DO NOTHING`,
  )
    .bind(email, nowSec(), source, ipHash)
    .run();

  return json({ ok: true });
};

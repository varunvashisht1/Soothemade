-- 0001_init.sql
-- Initial schema for soothemade-notes D1 database.
-- Apply locally:  npx wrangler d1 migrations apply soothemade-notes --local
-- Apply remote :  npx wrangler d1 migrations apply soothemade-notes --remote

-- ─────────────────────────────────────────────────────────────────
-- subscribers: newsletter list. ip_hash is sha256, not raw IP.
-- ─────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS subscribers (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  email         TEXT    NOT NULL UNIQUE,
  created_at    INTEGER NOT NULL,
  source        TEXT,
  ip_hash       TEXT,
  status        TEXT    NOT NULL DEFAULT 'active',
  confirmed_at  INTEGER
);

CREATE INDEX IF NOT EXISTS subscribers_created_idx ON subscribers(created_at);
CREATE INDEX IF NOT EXISTS subscribers_status_idx  ON subscribers(status);

-- ─────────────────────────────────────────────────────────────────
-- orders: fulfillment log. UNIQUE(platform, external_id) makes
-- webhook ingestion idempotent.
-- ─────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS orders (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  product_code  TEXT    NOT NULL,
  platform      TEXT    NOT NULL,
  external_id   TEXT    NOT NULL,
  email         TEXT,
  amount_cents  INTEGER,
  currency      TEXT    NOT NULL DEFAULT 'USD',
  created_at    INTEGER NOT NULL,
  UNIQUE (platform, external_id)
);

CREATE INDEX IF NOT EXISTS orders_product_idx ON orders(product_code);
CREATE INDEX IF NOT EXISTS orders_email_idx   ON orders(email);

-- ─────────────────────────────────────────────────────────────────
-- download_tokens: gated PDF delivery via /files/[token].
-- expires_at is the cutoff; used_at is set on first redemption
-- (kept nullable so we can also issue unlimited-use tokens).
-- ─────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS download_tokens (
  token         TEXT    PRIMARY KEY,
  product_code  TEXT    NOT NULL,
  email         TEXT    NOT NULL,
  order_id      INTEGER,
  created_at    INTEGER NOT NULL,
  expires_at    INTEGER NOT NULL,
  used_at       INTEGER,
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE INDEX IF NOT EXISTS dl_tokens_expires_idx ON download_tokens(expires_at);
CREATE INDEX IF NOT EXISTS dl_tokens_email_idx   ON download_tokens(email);

-- ─────────────────────────────────────────────────────────────────
-- journal_views: per-post per-day counter.
-- Primary key (slug, day) makes UPSERT cheap.
-- ─────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS journal_views (
  slug   TEXT    NOT NULL,
  day    TEXT    NOT NULL,
  count  INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (slug, day)
);

CREATE INDEX IF NOT EXISTS journal_views_day_idx ON journal_views(day);

-- ─────────────────────────────────────────────────────────────────
-- contact_messages: contact form inbox. handled_at NULL = unread.
-- ─────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS contact_messages (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT    NOT NULL,
  email       TEXT    NOT NULL,
  subject     TEXT,
  message     TEXT    NOT NULL,
  ip_hash     TEXT,
  created_at  INTEGER NOT NULL,
  handled_at  INTEGER
);

CREATE INDEX IF NOT EXISTS contact_handled_idx ON contact_messages(handled_at);

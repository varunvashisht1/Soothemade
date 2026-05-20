#!/usr/bin/env node
// Build embed payloads for all products and POST to /api/admin/reindex.
//
// Usage (after wrangler secret put REINDEX_SECRET, after deploy):
//   REINDEX_SECRET=... node scripts/index_products_vectorize.mjs
//
// Override target with REINDEX_URL (defaults to https://notes.soothemade.com).

import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const REPO = new URL("..", import.meta.url).pathname;
const PRODUCTS_DIR = join(REPO, "products");
const URL_BASE = process.env.REINDEX_URL ?? "https://notes.soothemade.com";
const SECRET = process.env.REINDEX_SECRET;

if (!SECRET) {
  console.error("Missing REINDEX_SECRET env var.");
  process.exit(1);
}

// Minimal frontmatter extractor. Handles the fields we actually use.
// Trades correctness on exotic YAML for zero dependencies.
function parseFrontmatter(md) {
  const m = md.match(/^---\s*\n([\s\S]*?)\n---\s*\n?/);
  if (!m) return {};
  const lines = m[1].split(/\r?\n/);
  const out = {};
  let currentKey = null;
  let folded = "";
  for (const line of lines) {
    if (currentKey && /^\s+/.test(line)) {
      folded += (folded ? " " : "") + line.trim();
      continue;
    }
    if (currentKey) {
      out[currentKey] = folded;
      currentKey = null;
      folded = "";
    }
    const kv = line.match(/^([a-zA-Z][\w-]*):\s*(.*)$/);
    if (!kv) continue;
    const key = kv[1];
    let val = kv[2].trim();
    if (val === ">-" || val === ">" || val === "|" || val === "|-") {
      currentKey = key;
      folded = "";
      continue;
    }
    val = val.replace(/^["']|["']$/g, "");
    out[key] = val;
  }
  if (currentKey) out[currentKey] = folded;
  return out;
}

function buildItem(slug, fm) {
  const parts = [
    fm.title,
    fm.tagline,
    fm.summary,
    fm.buyer ? `For: ${fm.buyer}.` : null,
    fm.category ? `Category: ${fm.category}.` : null,
  ].filter(Boolean);
  const text = parts.join("\n");

  return {
    id: fm.code,
    text,
    metadata: {
      code: fm.code,
      title: fm.title,
      slug,
      summary: fm.summary ?? "",
      category: fm.category ?? "",
      tagline: fm.tagline ?? "",
      ymyl: fm.ymyl === "true" || fm.ymyl === true,
    },
  };
}

const dirs = readdirSync(PRODUCTS_DIR, { withFileTypes: true })
  .filter((d) => d.isDirectory() && /^P\d{2,3}_/.test(d.name))
  .map((d) => d.name)
  .sort();

const items = [];
for (const dir of dirs) {
  const slug = dir.replace(/^P\d{2,3}_/, "");
  const webMd = join(PRODUCTS_DIR, dir, "web.md");
  let raw;
  try {
    raw = readFileSync(webMd, "utf8");
  } catch {
    console.warn(`skip ${dir}: no web.md`);
    continue;
  }
  const fm = parseFrontmatter(raw);
  if (!fm.code || !fm.title) {
    console.warn(`skip ${dir}: missing code/title`);
    continue;
  }
  items.push(buildItem(slug, fm));
}

console.log(`Indexing ${items.length} products to ${URL_BASE}/api/admin/reindex`);

const res = await fetch(`${URL_BASE}/api/admin/reindex`, {
  method: "POST",
  headers: {
    "content-type": "application/json",
    authorization: `Bearer ${SECRET}`,
  },
  body: JSON.stringify({ items }),
});

const text = await res.text();
console.log(`HTTP ${res.status}`);
console.log(text);
if (!res.ok) process.exit(1);

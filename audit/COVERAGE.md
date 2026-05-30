# Audit Coverage Map

> Why this file exists: em-dashes shipped live on soothemade.com because every
> earlier audit was *scoped* to one area, and the union of their scopes left a
> hole — the hand-written site page copy was never voice-checked. This map makes
> coverage explicit so nothing falls between passes again. **If you add a content
> surface, add it here and to `audit_voice.py`.**

## The single source of truth for brand voice

**`scripts/audit_voice.py`** is the coverage-complete voice lint. It walks
**every** content root and checks extracted *prose* (never code/CSS) against the
full ruleset: em-dashes, prose semicolons, banned AI-tells, filler phrases, and
buzzwords. It is read-only and exits non-zero on any violation.

**Run it before shipping any copy:**

```
python scripts/audit_voice.py
```

A clean run prints `CLEAN` (documented carve-outs are allowlisted in the script).

## What covers what

| Surface | Lives in | Voice lint | Auto-fix scrubber |
|---|---|---|---|
| Product PDFs + listings | `products/P*/content.md`, `web.md` | `audit_voice.py` ✅ | `scrub_ai_punctuation.py` |
| Bundle listings | `products/K*/web.md` | ✅ | `scrub_ai_punctuation.py` |
| Ebook manuscripts | `ebooks/B*/manuscript.md` | ✅ | `scrub_ai_punctuation.py` |
| Journal essays | `content/*.md` | ✅ | `scrub_ai_punctuation.py` |
| Notes site copy | `site/src/**.{astro,ts,md}` | ✅ | `scrub_site_punctuation.py` |
| Umbrella site copy | `site-main/src/**.{astro,ts,md}` | ✅ | `scrub_site_punctuation.py` |

Two scrubbers, because semicolons are load-bearing in JS/CSS:
- **`scrub_ai_punctuation.py`** — markdown only (`products/`, `ebooks/`, `content/`).
  Fixes em-dashes **and** semicolons (safe: it's all prose).
- **`scrub_site_punctuation.py`** — site source (`site/`, `site-main/`).
  Fixes em-dashes **only**; never touches semicolons, so code/CSS stays intact.

## Other audits (and their narrower scopes, for the record)

- `scripts/audit_writing_rules.py` — per-product care-signal scorecard + density. Scope: `products/`.
- `scripts/kindle_verify.py` — KDP file/metadata compliance. Scope: `ebooks/`.
- `audit/` (conversion audit) — commercial: titles, pricing, bundles. Scope: product listings.
- `audit/website-audit.md` — UX/SEO/a11y/perf. Scope: the Notes site structure.

None of those check site-copy voice. `audit_voice.py` is the one that does, across everything.

## Carve-outs (intentional, allowlisted in audit_voice.py)

- **"at the end of the day"** is allowed when literal (time of day), banned when
  idiomatic ("ultimately"). The two literal uses in P08 + P28 are allowlisted.
- **"actually"** and **"harness"** (physical noun, e.g. car-seat harness) are
  voice-defining / legitimate and are not flagged.
- **En-dashes** (`–`, number ranges like `0–3 yrs`) are correct typography and
  are left intact — only em-dashes (`—`) are scrubbed.

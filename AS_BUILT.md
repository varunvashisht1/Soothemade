# AS_BUILT — Soothemade

> ⚠️ **READ THIS FIRST.** Any fresh Claude / Cursor / Copilot / other AI session must onboard from this single document before touching the repo. It is intentionally self-contained — the project memory directory (`~/.claude/projects/.../memory/`) does NOT travel to other tools, so durable context lives here, in git.
>
> ⚠️ **UPDATE THIS WITH EVERY COMMIT** that changes anything structural — brand identity, voice rules, content rules, repo layout, dependencies, tooling, deployment, Canva state, or memory layout. A pure-content commit (e.g. adding a new product `content.md` that uses the existing schema) does **not** require an update.
>
> Drift between repo state and this document defeats its purpose.

---

## 0. Reading guide

You are about to work on **Soothemade**, a small digital-product brand for new parents. Before doing anything:

1. Read this whole file once. It is long on purpose.
2. Then read `PLAN.md` (10-day strategic plan) and `STATUS.md` (where work is now) for narrative context.
3. Then read the `brand/` directory for voice and visual rules.
4. If you are Claude, additionally read `~/.claude/projects/C--Users-varun-Documents-GitHub-Soothemade/memory/MEMORY.md` for session-spanning feedback memories.

After you've finished a change, scan this file's section for that area and amend it. Add a one-line entry to the Changelog at the bottom.

---

## 1. Mission + brand promise

**Promise:** Slow, considered things to use through the unphotographed parts of life.

**What that means in practice:** Printables, planners, cards, journals, and (later) physical books — designed for people in tender life seasons (postpartum, recovery, the first year of parenthood, the eldercare years) who are tired of glossy AI-generated content. The brand competes on **warmth and credibility**, not breadth.

**Pinterest-2026 bet:** The market is rotating from minimalist-Goodnotes toward warm-vintage / lived-in. Soothemade rides that. See `research/04-pinterest-trends/findings.md`.

---

## 2. Brand architecture

| Tier | Name | Domain | Status |
|---|---|---|---|
| **Master brand** | **Soothemade** | `soothemade.com` (owned) | Active; umbrella site is a one-page intro |
| **Active sub-line** | **Soothemade Notes** | `notes.soothemade.com` | Live on Cloudflare Workers |
| Reserved sub-line | Soothemade Kitchen | `kitchen.soothemade.com` | Reserved, not built |
| Reserved sub-line | Soothemade Studio | `studio.soothemade.com` | Reserved, not built |
| Reserved sub-line | Soothemade Field | `field.soothemade.com` | Reserved, not built |
| Reserved sub-line | Soothemade Press | `press.soothemade.com` | Reserved, not built. Books ship under the master `Soothemade` brand instead. |

Sub-lines share: voice, visual identity, brand kit, typography, structural rules. They differ in: audience-specific vocabulary, example scenarios, accent-color emphasis.

**Naming rule:** `Soothemade <Single Noun>`. Don't deviate.

Full architecture doc: [`brand/architecture.md`](./brand/architecture.md).

---

## 3. Persona — LOCKED: Maya

**Locked 2026-05-22:** Option B per `brand/persona.md`. Maya, postpartum doula and mom of two. Every personal note across the 55 product PDFs is signed `*With care, Maya*`. The about page and press kit name her. The brand mark `Soothemade` continues to render on PDF cover + colophon via the render template — Maya is the personal voice, Soothemade is the studio.

| Surface | Voice |
|---|---|
| PDF personal notes (`## A note from me`, `## A note before you start`, etc.) | Maya, first-person scenes, signed `*With care, Maya*` |
| PDF cover + colophon | `Soothemade` brand mark (template-driven) |
| Notes site (`notes.soothemade.com`) | Maya — "made by a person" copy on About |
| Umbrella site (`soothemade.com`) | `*with care, the studio*` — collective voice for the master brand. Maya is the Notes voice; future sub-lines (Kitchen / Studio / Field) will each get their own named voice when they launch. |
| Press kit | Maya as founder bio |

Full original options retained in [`brand/persona.md`](./brand/persona.md) for the record. The lock can be revisited if the brand strategy changes, but the decision is no longer "default unless overridden" — it is the active voice.

---

## 4. Voice rules

Single-sentence voice: **"A slightly-older friend who's been through it, telling you the truth no one else does — without preaching, without sanitizing, without selling you a fix."**

### Tone dials

| Dial | Setting |
|---|---|
| Formality | Casual-warm, not slangy. Contractions yes. No "lol", no emojis. |
| Authority | Lived-in, not credentialed. "Here's what worked for me" beats "Studies show." |
| Emotional register | Direct + tender. Name the hard thing, then sit with it. |
| Optimism | Honest, not toxic-positive. No "everything happens for a reason." |
| Selling | Quiet. Let the work sell itself. No urgency theater. |

### Words to use

`gentle`, `slow`, `spacious`, `enough`, `ordinary`, `steady`, `small`, `quiet`, `fourth trimester`, `postpartum`, `I made this when…`, `I wish someone had told me…`. Address the reader directly with `you` / `your`.

### Words to avoid

`mama`, `mommy`, `bump`, `kiddo`, `little one`, `journey`, `blessed`, `cherish`, `enjoy every moment`, `love language`, `crush it`, `#momlife`, `supermom`, `experts say` (without citing), `studies show` (without citing), `should`, `must`, `have to` (replace with `might want to`).

### Banned phrases (legal / safety)

- Anything that **prescribes** a sleep, feeding, or medical decision.
- "Cures", "treats", "prevents" + any condition.
- "Will help you lose weight" in postpartum-body context.
- **No medicine names anywhere — brand or generic.** No "ibuprofen", no "Tylenol", no "acetaminophen", no "erythromycin", no "pseudoephedrine", no antibiotic names, no specific birth-control brands, no supplement brands. If a medication is relevant, describe by class or purpose ("an over-the-counter pain reliever your provider okays for you", "a fever reducer your provider recommends", "the eye ointment they give all newborns") and route the decision to the provider. This applies to product PDFs, web listings, journal copy, marketing, and any future asset.
- "This is the only way" / "the right way."

### Structural rules

1. First-line hook is a specific concrete observation, never a generality.
2. One idea per paragraph (postpartum brain doesn't track long paragraphs).
3. Concrete > abstract. Name the specific thing.
4. Disclaim once, in a footer: *"This is a planning tool, not medical advice. If something feels wrong, call your provider."*

Full guide: [`brand/voice-guide.md`](./brand/voice-guide.md).

---

## 5. Content rules — NO AI PUNCTUATION

This is a hard project-wide rule:

- ❌ **No em dashes (`—`).** Use commas.
- ❌ **No semicolons (`;`).** Use periods. (New sentence, capitalize next word.)
- ✅ Curly quotes (`"` `'`) are fine — they're standard typography.
- ✅ Hyphens (`-`) and en dashes (`–`) are fine, sparingly.
- ✅ Ellipses are OK but used sparingly.

**Reusable scrubber:** `scripts/scrub_ai_punctuation.py`. Re-run after any AI-assisted content generation:

```bash
python scripts/scrub_ai_punctuation.py
```

Scrubs both `content.md` and `web.md` across all `products/P*_*/`. Idempotent.

If you're writing new content, write it without em dashes and semicolons from the start. Don't rely on the scrubber alone.

### The care contract — see `WRITING-RULES.md`

The repo-root `WRITING-RULES.md` is **the care contract**, not a style guide. The bar: a new parent buys this at 11 p.m. while breastfeeding on a phone. In the first six minutes, the product must make them feel that a person made this, on purpose, for them.

Six care signals (all non-negotiable for shipped products):

1. **Scene anchor in the opening note** — time of day, room, body sensation, specific gesture, or overheard line. Proof that a person was somewhere when they wrote this.
2. **The voice has a face** — every "A note from me" section ends with `*With care, Maya*`. (Umbrella uses `*with care, the studio*`.)
3. **The disclaimer is voiced, not armored** — the legal-required not-medical-advice block must do the legal work *and* be the brand voice. P09 is the model: *"A journal is for noticing patterns. It is not for crisis. If you are in crisis, you need a human, not a page."*
4. **Modest about what it does** — no `transform`, no `unlock`, no `you deserve`, no `breakthrough`. The brand voice is a tired friend, not a wellness app.
5. **Hard things named, not euphemized** — say `mom rage`, `loss`, `the primary witness of someone else's diminishment`. Not `challenging emotions`, not `unexpected outcome`.
6. **Each product is its own shape** — catalog-wide. No more than ~50% of products should share the same `## What this [X] is, and is not` H2 framework.

The hygiene rules (no em-dashes, no semicolons, banned AI-tell vocabulary, banned wellness-overpromise vocabulary, density caps) are in the rules-doc appendix — they serve the six signals, they are not the headline.

**Auditor:** `scripts/audit_writing_rules.py` produces a per-product care scorecard plus catalog-wide patterns (disclaimer reuse, template-form frequency). Read-only. Run before any PDF render batch:

```bash
py scripts/audit_writing_rules.py        # full scorecards
py scripts/audit_writing_rules.py --terse # one line per product
py scripts/audit_writing_rules.py --product P09   # single product
```

The auditor is intentionally tolerant in two places: it strips fenced code blocks (which contain read-aloud scripts and ASCII template fields) and italicized `*"..."*` quote-critiques before scanning for banned vocabulary. The brand's voice rules apply to the brand's voice, not to phrases it is quoting back to puncture.

Catalog status as of 2026-05-22: **55/55 products pass the care contract.** Disclaimer reuse: 0 boilerplate clusters. Form variety: 13% of catalog uses the IS/IS NOT H2 (below the 50% threshold).

---

## 6. Visual identity

### Color palettes

**Palette 1 — Warm vintage** (default; for calm / postpartum / pregnancy products):

| Role | Hex | Description |
|---|---|---|
| Background | `#F5EFE6` | Warm ivory, aged paper |
| Primary text | `#2E2A24` | Deep umber-black |
| Accent 1 | `#B4654A` | Terracotta (headings, dividers) |
| Accent 2 | `#8C9B7A` | Sage olive (callouts, highlights) |
| Accent 3 | `#D4A574` | Wheat (soft section backgrounds) |
| Muted | `#A89A8C` | Stone (footers, fine print) |

**Palette 2 — Bright vintage** (for energetic / toddler-activity products):

| Role | Hex |
|---|---|
| Background | `#FBF6EE` |
| Primary text | `#2E2A24` (same) |
| Vermillion | `#D9532B` |
| Forest moss | `#3B6B5A` |
| Mustard ochre | `#E8B832` |
| Muted plum | `#8265A3` |

**Open hex drift:** `brand/brand.svg` uses sage `#7A8B6F` and wordmark `#3D3935` instead of the doc's `#8C9B7A` and `#2E2A24`. Not resolved. Decide and reconcile before any new brand asset is produced.

**Active PDF palette** (`scripts/templates/product.css` `:root`):

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#EAEEE2` | **light sage paper** (was cream `#F5EFE6`). Set on `body`, `.cover`, `.colophon`, AND on `@page background` so the entire page surface is one continuous sage. |
| `--bg-warm` | `#F0F3E8` | Slightly lighter sage — used as the interior of fill-in `<pre>` blocks so they read as inset, not floating. |
| `--text` | `#2E2A24` | Charcoal body text + drop caps + h3 italic. |
| `--ink-soft` | `#5C5347` | Subtitle, blockquote body. |
| `--accent` | `#8C9B7A` | Sage olive — primary accent (cover title in Caveat, h2 in Caveat, h2 first-letter drop in body context, .cover-ymyl border, blockquote em, em strong, colophon-url, h4 inline labels). |
| `--accent-2` | `#8C9B7A` | Same as accent — blockquote left border, .cover-mark sprig, .colophon-mark sprig. Could diverge later if we want a deeper sage for borders. |
| `--accent-3` | `#A8B894` | Muted sage — fill-in box outlines, cover-divider, h2::after underline rule, hr divider sprig, table borders, pre border. (Was wheat `#D4A574`.) |
| `--muted` | `#B8AC9A` | Stone — meta lines, page chrome (footers, cover meta, colophon fine print). |

PDFs are now a sage-on-sage piece. Cover/body/colophon all in the same light sage paper; box outlines and dividers in muted sage; emphasis (cover title, h2, blockquote border) in primary sage. Charcoal carries the body text and drop caps so hierarchy is visible.

### Typography

| Role | Font | Source |
|---|---|---|
| Display / titles | **Fraunces** | Google Fonts |
| Body / sans | **Inter** | Google Fonts |
| Hand-lettered accent | **Caveat** | Google Fonts |
| Pinterest pin overlays | **Cormorant Garamond** | Google Fonts (free Caslon alternative) |

**Fraunces axes globally pinned to `'opsz' 20, 'SOFT' 0, 'WONK' 0`** so Fraunces stays in calm text-design mode at all sizes. Stops the flamboyant "J" / "Q" / etc. at display sizes. Set in `site/src/styles/tokens.css` (via `--font-script`) and in `scripts/templates/product.css` (via `body { font-variation-settings }`).

**Caveat usage** is broader than the visual-identity doc originally suggested (it said "sparingly — one word per page max"). Current deliberate exceptions:
- Master brand "**Soothemade**" wordmark in nav + footer of site
- Master brand "**Soothemade**" wordmark on PDF cover + colophon
- Cover title of every product PDF (e.g. "A Postpartum Mind Journal")
- h2 section headers inside PDF body
- Page footer `@bottom-center` "Soothemade" mark

The "Notes" sub-line label stays in **Fraunces italic terracotta** beside the Caveat wordmark.

### Logo system

All assets live in `brand/` at repo root.

| File | Variant | Use case |
|---|---|---|
| `brand/brand.svg` | Primary — sage sprig + charcoal italic-serif "soothemade" wordmark on cream `#F5EFE6` card | Default brand mark, light surfaces, print |
| `brand/brand-on-dark.svg` | Sage sprig + cream wordmark, transparent | Dark surfaces, hero overlays |
| `brand/brand-mono-dark.svg` | All charcoal `#3D3935`, transparent | Single-color print, stamps, formal contexts |
| `brand/brand-mono-cream.svg` | All cream `#F5EFE6`, transparent | Watermarks, very dark backgrounds |
| `brand/brand-sprig.svg` | Icon-only sprig, `currentColor` | Theme-adaptive sprig icon for site components |
| `site/public/favicon.svg` | Sage sprig with `prefers-color-scheme` (cream on dark UI, sage on light UI) | Browser tab favicon |

All four `brand-*.svg` variants are also uploaded to Canva — see Section 12.

### Visual rules (the "AI-mill smell test")

Before any visual ships, it must satisfy:

- No drop shadows anywhere
- No gradient buttons or backgrounds — flat colors only
- No purple-pink-orange "AI image" palette
- No symmetric mandalas or over-perfect florals
- Paper texture / warmth visible somewhere
- Looks like it was made by a person, not a stock template

Full visual identity: [`brand/visual-identity.md`](./brand/visual-identity.md).

---

## 7. Tech stack

| Layer | Tech | Why |
|---|---|---|
| Site | **Astro 5** | Static-first, server output on Cloudflare Workers, great DX |
| Hosting | **Cloudflare Workers Static Assets** | Free tier, edge, atomic deploys, custom domain |
| Site styles | Vanilla CSS + custom-property theme tokens | No framework lock-in, easy to read |
| Site fonts | Google Fonts (Fraunces, Inter, Caveat) | Free, embeddable |
| Product PDFs | **Python + WeasyPrint + Jinja2 + Markdown** | HTML/CSS → print-quality PDF |
| PDF render env | **Docker image `soothemade-render`** | Reproducible across machines, no Windows GTK pain |
| PDF preview | poppler-utils via Docker (`soothemade-render-preview`) | Convert PDF → PNG for visual diff |
| Ebook (.epub) | **Pandoc + WeasyPrint** via `soothemade-ebook` Docker image | Markdown manuscript → .epub. Cover rendered HTML→PDF→PNG at 1600×2560 via WeasyPrint + pdftoppm. |
| Content scrubber | Python (stdlib) | Punctuation cleanup |
| Marketing collateral | **Canva** via Canva MCP | Pinterest pins, IG posts, ad creative |
| AI agents | Claude Code (worktree-based) | Multi-session coding agent |

---

## 8. Repository layout

```
.
├── AS_BUILT.md                ← THIS FILE
├── PLAN.md                    Durable 10-day plan
├── README.md                  Repo overview
├── STATUS.md                  Where work currently is (read second)
├── brand/                     Brand identity assets + docs
│   ├── README.md
│   ├── architecture.md        Master + sub-brand model
│   ├── persona.md             3 persona options (default = Maya)
│   ├── voice-guide.md         Voice + tone + words to use/avoid
│   ├── visual-identity.md     Palettes, typography, rules
│   ├── brand.svg              Canonical brand mark (sprig + wordmark)
│   ├── brand-on-dark.svg      For dark surfaces
│   ├── brand-mono-dark.svg    Single-color charcoal
│   ├── brand-mono-cream.svg   Single-color cream
│   └── brand-sprig.svg        Icon-only sprig, currentColor
├── content/                   Pillar blog posts (Jekyll-ready MD)
├── design/                    Design studies (HTML)
│   ├── brand-variants.html    Logo variant side-by-side preview
│   ├── notes-site-studies.html        10 homepage directions
│   └── notes-apothecary-dark.html     3 dark Apothecary variants
├── products/                  One folder per product (see § 9)
│   ├── P01_sensory-play-cards/
│   ├── P02_saying-no-scripts/
│   ├── P03_slow-motherhood-planner/
│   ├── P04_partner-postpartum-playbook/
│   ├── P05_screen-free-challenge/
│   ├── P06_csection-recovery-planner/
│   └── P09_ppd-anxiety-journal/
├── publishing/                Operations runbook + 52-week calendar
├── research/                  6-stream market research + REPORT.md
├── scripts/                   Render + scrubber pipelines
│   ├── render.py              Markdown + Jinja → WeasyPrint PDF
│   ├── scrub_ai_punctuation.py
│   └── templates/
│       ├── product.html.j2    Master PDF template
│       └── product.css        Master PDF stylesheet
├── site/                      Astro site (notes.soothemade.com)
│   ├── package.json
│   ├── astro.config.mjs
│   ├── wrangler.toml          CF Workers config
│   ├── DEPLOY.md              Deploy playbook
│   ├── public/
│   │   └── favicon.svg
│   └── src/
│       ├── components/        Nav, Footer, Hero, ProductCard, etc.
│       ├── content.config.ts  Content collections schema
│       ├── data/
│       │   ├── featured-products.ts
│       │   └── theme.json     Active theme + overrides
│       ├── layouts/
│       │   └── BaseLayout.astro
│       ├── lib/
│       │   └── theme.ts       Theme loader
│       ├── pages/             Routes
│       └── styles/
│           ├── global.css
│           ├── tokens.css     Base design tokens (fonts, scale, etc.)
│           └── themes/
│               ├── charcoal.css
│               ├── forest.css         (default)
│               └── mossy.css
├── site-main/                 Astro site (soothemade.com — umbrella)
│   ├── package.json
│   ├── astro.config.mjs
│   ├── wrangler.toml          CF Workers config (no data bindings)
│   ├── DEPLOY.md              Deploy playbook
│   ├── README.md
│   ├── public/
│   │   ├── favicon.svg
│   │   └── robots.txt
│   └── src/
│       ├── components/        Nav, Footer, Hero, LineCards, Manifesto, etc.
│       ├── content.config.ts  Journal collection
│       ├── content/journal/   Umbrella essays (markdown)
│       ├── data/
│       │   ├── lines.ts       Sub-line definitions (Notes live; others coming)
│       │   └── theme.json
│       ├── layouts/
│       │   └── BaseLayout.astro
│       ├── lib/theme.ts
│       ├── pages/             Routes — /, /lines, /journal, /about, etc.
│       └── styles/
│           ├── global.css
│           ├── tokens.css
│           └── themes/
│               ├── daylight.css       (default)
│               ├── charcoal.css
│               ├── forest.css
│               └── mossy.css
└── toolkit/                   Pro-mode prompts + customer-service + KB
```

### Worktree convention

This repo is worked from **git worktrees** rooted under `.claude/worktrees/<name>`, one per branch. The directory `.claude/` is gitignored. The "real" working tree (main repo) is `C:/Users/varun/Documents/GitHub/Soothemade/` and is usually on `main`.

Typical session:

```bash
# Create a feature branch worktree
git worktree add .claude/worktrees/<slug> -b claude/<slug>

# When done: commit, push, merge to main, then remove the worktree
git worktree remove .claude/worktrees/<slug>
```

---

## 9. Product folder structure

Every product under `products/Pnn_<slug>/` has:

| File | What it is | Required |
|---|---|---|
| `README.md` | Internal context, why this exists | yes |
| `content.md` | Main body content rendered into the PDF | yes |
| `web.md` | YAML frontmatter (title, code, specs, summary, ymyl) + optional web body | yes |
| `product.pdf` | Rendered PDF (regenerate via `scripts/render.py`) | yes (committed) |
| `etsy-listing.md` | Etsy listing draft (title + tags + description) | when listed |
| `marketing.md` | Pinterest pin copy + caption variants | when marketed |
| `mockup-spec.md` | Mockup brief for Etsy listing images | optional |
| `gumroad-sales-page.md` | Long-form sales page | optional |
| `pinterest-pins.md` | Per-pin caption variants | optional |

`web.md` frontmatter schema (consumed by `scripts/render.py` and by Astro content collections):

```yaml
---
title: "A Postpartum Mind Journal"
code: "P09"
specs: "60 PAGES · NOTICING TOOL"
summary: "A 60-page noticing-and-tracking journal..."
tagline: "..."
ymyl: true   # if true, cover gets the "not medical advice" disclaimer block
---
```

---

## 10. Product PDF system

### Render pipeline

```
products/Pnn_*/content.md  +  products/Pnn_*/web.md
                           |
                           ↓
         scripts/render.py (markdown + jinja → HTML)
                           |
                           ↓
                 scripts/templates/
                 ├── product.html.j2
                 └── product.css
                           |
                           ↓
                       WeasyPrint
                           |
                           ↓
                products/Pnn_*/product.pdf
```

`render.py` reads the sibling `web.md` frontmatter to drive the cover (title, code, specs, summary, ymyl flag). The first `<h1>` of `content.md` is stripped to avoid duplication. A back-cover colophon is appended automatically.

### Key design decisions

- **`@page` background:** cream `#F5EFE6`. The whole page IS cream paper, not a cream box on a white sheet.
- **`@page` margins:** `1.0in 0.85in 1.0in 0.85in` (top / right / bottom / left). Visual-identity.md's "1in minimum" is honored.
- **Cover title:** **Caveat 40pt, terracotta `#B4654A`**, italic-feel. Set to `font-weight: 600`.
- **Cover wordmark:** "**Soothemade**" Caveat 30pt + "**Notes**" Fraunces italic 20pt terracotta, flex-baseline aligned.
- **Cover meta line:** `<code> · <specs>` in Inter 9pt uppercase, stone color.
- **Cover subtitle:** Fraunces italic 14pt, ink-soft.
- **YMYL block** (only if `ymyl: true`): "A planning and tracking tool, not medical advice" in terracotta caps with terracotta border-top + border-bottom.
- **Body headings:**
  - `h2`: **Caveat 34pt, terracotta**, with `page-break-before: always`. Each section starts on a fresh page.
  - `h3`: Fraunces italic 15pt, sage olive.
  - `h4`: Inter 9.5pt uppercase, terracotta.
- **Body text:** Inter 11pt, ink color, line-height 1.65.
- **Drop cap:** First letter after each `h2` is enlarged Fraunces 20pt in `var(--text)` (charcoal). Intentionally NOT the accent color — h2 already carries the accent above, so the drop cap stays charcoal for hierarchy. Inline-larger, not a true floating drop cap (WeasyPrint can't float `::first-letter`).
- **`hr` divider:** Inline SVG sprig with horizontal lines, sage. Uses canonical sprig geometry. A `<hr>` immediately followed by a `<h2>` is hidden via `hr:has(+ h2) { display: none }` — `<h2>` already starts a new page, the divider would either be redundant or get orphaned on its own page.
- **Pull-quotes (`blockquote`):** Fraunces italic 14.5pt, sage left-border.
- **Page footer (`@bottom-*`):**
  - left: `notes.soothemade.com` in Inter 8.5pt stone
  - center: `Soothemade` in Caveat 12pt stone
  - right: page number in Inter 9pt stone
  - All suppressed on the cover (`@page :first`) and on the colophon (`@page colophon`).
- **Colophon back cover:** Sprig + Soothemade wordmark + brand promise + URL + fine print, all centered.

### Templates

- `scripts/templates/product.html.j2` — structure (cover → body → colophon)
- `scripts/templates/product.css` — all styling

Edit either of these only when you're changing the *system*, not per-product styling.

### PDF design rules (must be satisfied on every render)

These rules exist to keep every product feeling like a hand-set, premium print artifact rather than an AI-mill PDF. Any new design change must preserve them.

1. **No page may contain only one element.** A page must never render with only a divider, only a heading, or only one widow line. Specifically:
   - `<hr>` immediately before `<h2>` is hidden (above).
   - `<h2>`, `<h3>`, `<h4>` carry `page-break-after: avoid` so headings can't be stranded.
   - `<p>` immediately followed by `<pre>`, `<blockquote>`, or with `<strong>` as its only child carries `page-break-after: avoid` so labels stay with the visual element they introduce.
   - `<pre>` and `<blockquote>` carry both `page-break-before: avoid` (stick with previous content) and `page-break-inside: avoid` (don't split).

2. **Visual hierarchy is achieved by colour AND family, not size alone.** Adjacent heading levels must use distinct colours. Current treatment:
   - **h2** — Caveat in `var(--accent)`. Big visual moment. Triggers a new page.
   - **h3** — Fraunces italic in `var(--text)` (charcoal). Sub-section within a page.
   - **h4** — Inter uppercase in `var(--accent)`. Small inline label.
   - Never make h3 the same colour as h2.

3. **Section breaks**: `<h2>` always triggers a new page (`page-break-before: always`). Never use `<hr>` immediately before an `<h2>` — the system hides it, but writing one signals you might be misunderstanding the structure.

4. **Colour discipline — maximum ~4 colours per page.** Cream paper, charcoal body text, one accent (sage/whatever), one tertiary (wheat for sprigs/borders). Drop caps and section labels use the accent, but body emphasis (`<strong>`, `<em>`) stays in `var(--text)` so paragraphs don't strobe.

5. **Type discipline.** Three families, each with a role:
   - **Caveat** — brand identity only. Wordmark "Soothemade", cover title, h2 section headers, page footer center mark, signature signoffs.
   - **Fraunces** — structural typography. Subtitles, h3 sub-headers, blockquotes, drop caps, table headers, inline `<strong>` emphasis.
   - **Inter** — body, captions, table data, footer chrome.

6. **No AI-tell punctuation.** Em dashes and semicolons are banned from product content. Enforced by `scripts/scrub_ai_punctuation.py`; new content must not reintroduce them.

7. **Symbol discipline — no emoji.** The Docker render image has Inter + Fraunces + Caveat + DejaVu + Liberation, no emoji font. Modern colour-emoji codepoints (`🙂` `😐` `🌧` `❤` etc.) render as tofu boxes — and they're an AI-mill smell anyway.

   **Allowed symbols (verified to render in the font stack):**
   - `○` (U+25CB OPEN CIRCLE) — for "circle one of these" rating / option rows
   - `☐` (U+2610 BALLOT BOX) — for checkboxes / task lists (also OK to write as markdown task lists via `- [ ]`)
   - `·` (U+00B7 MIDDLE DOT) — separator between meta-items
   - `—` is banned (AI-tell). Use `,` instead.
   - `–` (en dash) — OK for ranges like "5–10 minutes"
   - Curly quotes `"` `'` — OK

   **Banned**: any emoji from the `U+1F300`–`U+1F9FF` block or `U+1FA00`–`U+1FAFF`. Plus any pictograph in `U+2600`–`U+27BF` that hasn't been confirmed to render. Confirm new symbols by rendering a test page before committing them in product content.

   **Known-bad codepoints + safe replacements** (encountered during the 2026-05-20 bulk render audit):
   - `❤` / `❤️` (U+2764 + variation selector) → use `♥` (U+2665 BLACK HEART SUIT). Heart suit is in DejaVu/Liberation and renders as a small filled heart.
   - `❌` (U+274C NEGATIVE SQUARED CROSS MARK) → use `✗` (U+2717 BALLOT X). Ballot X is in DejaVu/Liberation and renders as a small × symbol.
   - `🙂` / `😐` / `🌧` (face emoji + weather emoji from U+1F000+ blocks) → use `○` (U+25CB OPEN CIRCLE). Matches "circle one" intent.
   - `⚠` (U+26A0 WARNING SIGN) → renders correctly as a small filled triangle in DejaVu fallback. Acceptable.

7. **Single source of truth for design tokens.** All colours / fonts live in the `:root` of `scripts/templates/product.css`. Hardcoded hex values in component CSS are forbidden except in `@page` (which can't use custom properties).

8. **Page footers uniform**: URL left, brand mark Caveat center, page number right. Suppressed on cover (`@page :first`) and colophon (`@page colophon`).

9. **Margins ≥ visual-identity.md minimum**: currently `1.0in 0.85in 1.1in 0.85in` (top right bottom left). Don't bump unless you also bump `--bg` to cover the new margin or the page will show white edges.

10. **Render reproducibility**: render via the `soothemade-render` Docker image. If you can't reproduce a render on a fresh checkout with `python scripts/render.py --all`, the change is broken.

11. **No divider line at the start or end of a code-block container.** Code blocks (``` … ```) get a box border via the `pre` style. A `─────────` divider character line at the very top or very bottom of the code block would render as a *second* parallel line right next to the border — doubled lines, clunky weight. The container border is doing that job. Internal divider lines that separate sections *within* the container are fine and encouraged.

When designing or QAing a render, walk through every page and check each rule. A failed rule = block the merge.

---

## 11. Render commands

Docker is the canonical environment because Windows + WeasyPrint native is painful (requires GTK install).

### One-time: build the Docker image

```bash
docker build -t soothemade-render - <<'EOF'
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 libpangoft2-1.0-0 fontconfig fonts-dejavu fonts-liberation \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir weasyprint markdown jinja2 python-frontmatter
WORKDIR /work
EOF
```

This image bakes in all WeasyPrint native deps + the Python packages. Reusable.

### Render one product

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
  -v "/c/Users/varun/Documents/GitHub/Soothemade:/work" \
  soothemade-render \
  python scripts/render.py products/P09_ppd-anxiety-journal/
```

(`MSYS_NO_PATHCONV=1` disables Git Bash's path translation. On Linux/macOS, drop the prefix.)

### Render all 7

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
  -v "/c/Users/varun/Documents/GitHub/Soothemade:/work" \
  soothemade-render \
  python scripts/render.py --all
```

### Convert a rendered PDF to PNG (for preview)

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
  -v "/c/Users/varun/Documents/GitHub/Soothemade:/work" \
  soothemade-render bash -c "\
    apt-get update -qq >/dev/null && \
    apt-get install -y -qq poppler-utils >/dev/null 2>&1 && \
    pdftoppm -r 140 -png -f 1 -l 1 \
      /work/products/P09_ppd-anxiety-journal/product.pdf /work/p09_preview"
```

Output: `p09_preview-01.png` (page 1). For multi-page, use `-l 3` etc.

### Scrub AI punctuation

```bash
python scripts/scrub_ai_punctuation.py
```

Rules per line:
- Line-leading `— ` → stripped (signature use)
- ` — ` → `, ` (inline interrupter → comma)
- `—` → `,` (catch-all)
- `; ` → `. `
- `;` → `.`

### Gotchas

- **File locked / "PermissionError" on product.pdf:** the user has the PDF open in a viewer. Windows file lock. Close and retry.
- **`unexpected EOF` during `docker run`:** Docker daemon flaked. `docker info` to check. May need to restart Docker Desktop.
- **`apt-get install` looks stuck:** first run can take 30–60s for the package cache. Subsequent runs hit cache. Use `--quiet` for silent install (won't show progress) or remove `-q` to see download bars.

---

## 12. Site — notes.soothemade.com

### URL + worker

| Surface | Where |
|---|---|
| Live custom domain | `https://notes.soothemade.com` |
| Workers preview URL | `https://soothemade-notes.iamvashisht1.workers.dev` |
| Cloudflare Worker name | `soothemade-notes` |
| Cloudflare account | iamvashisht1@gmail.com |

### Astro structure

- **Pages:** `site/src/pages/` — `index.astro`, `about.astro`, `cart.astro`, `contact.astro`, `freebies.astro`, `policy.astro`, `press.astro`, `wholesale.astro`, `shop/index.astro`, `shop/[slug].astro`, `journal/index.astro`, `journal/[slug].astro`.
- **Layout:** `site/src/layouts/BaseLayout.astro` — head, fonts, theme attribute, OG + canonical, favicon link.
- **Components:** `Nav.astro`, `Footer.astro`, `Hero.astro`, `Manifesto.astro`, `ProductCard.astro`, `ProductGrid.astro`, `CategoryRow.astro`, `JournalRow.astro`, `Newsletter.astro`, `BotanicalLeaf.astro` (decorative leaf icon — separate from brand mark), `SoftStub.astro`.
- **Content collections:** `site/src/content.config.ts` maps Markdown to typed schemas.

### Theme system

All three themes are **dark**. Light cards sit on dark page surfaces.

| Theme | Surface | Card | Sage | Accent |
|---|---|---|---|---|
| `forest` (default) | `#1c2418` | `#f1ead4` | `#a8b88a` | `#d68a72` |
| `charcoal` | `#15150e` | `#1f1f17` | `#b2c08a` | `#e2a78f` |
| `mossy` | `#25241a` | `#d6cdb0` | `#a8a672` | `#c87963` |

Selecting:
- Edit `site/src/data/theme.json`:
  ```json
  { "preset": "forest", "overrides": {} }
  ```
- Or set `preset: "custom"` and use `overrides` to override individual tokens.

Theme is applied via `data-theme="<preset>"` on `<html>`. CSS variables (`--ink`, `--sage`, `--accent`, etc.) cascade from there.

Files: `site/src/lib/theme.ts` (loader) + `site/src/styles/themes/*.css` (palette per preset) + `site/src/styles/tokens.css` (base type/spacing/motion tokens).

### Logo wiring on the site

- **`Nav.astro`** (top of every page): inline SVG sprig (theme-adapts via `currentColor`) + "**Soothemade**" Caveat 30pt + "*Notes*" Fraunces italic 21pt terracotta, baseline-aligned in a flex container.
- **`Footer.astro`** (bottom of every page): inline SVG sprig above the wordmark in the brand block. Same Caveat + Fraunces italic treatment.
- **Favicon:** `site/public/favicon.svg`, linked in `BaseLayout.astro`. Has built-in `prefers-color-scheme` rule so it adapts to dark / light browser chrome.

### Site dev

```bash
cd site
npm install   # one-time
npm run dev   # local dev server at http://localhost:4321
```

### Umbrella site — `soothemade.com`

A second Astro app, `site-main/`, hosts the master-brand umbrella site
at the apex domain. Per `brand/architecture.md`, the umbrella has no
products of its own; it tells the brand story and routes to sub-lines
(currently Notes; future Kitchen / Studio / Field). It is a fully
independent codebase — Notes is just a hyperlink from it.

| Surface | Where |
|---|---|
| Live custom domain | `https://soothemade.com` + `www.soothemade.com` |
| Cloudflare Worker name | `soothemade-main` |
| Data layer | none (read-only brand site) |
| Default theme | `apothecary` — warm-black hero + cream paper + single amber/brass accent (the original `daylight` cream theme is preserved in `themes/daylight.css` as an alternate) |

Brand source of truth: `brand/umbrella-story.md` — the master narrative
all umbrella copy ladders back to. The Notes voice guide still applies;
the umbrella voice is the same voice widened from parenthood-specific
to master-brand.

Pages: `/`, `/lines`, `/journal`, `/journal/[slug]`, `/about`,
`/freebies`, `/contact`, `/policy`, `/press`, `/newsletter`, `/404`.

The newsletter form on the umbrella POSTs to the Notes worker's
`/api/subscribe` endpoint with `source=umbrella` — single subscriber
list, tagged by entry point.

### Umbrella design patterns (post-apothecary)

The umbrella picked up several visual + structural patterns after the
initial scaffold. The gradient-tile pattern also applies on Notes.

- **Gradient tile sections.** Every section on the umbrella home is
  its own dark gradient tile with a slightly different warm undertone
  — hero (warm-black + amber), dear-stranger (umber + amber), rooms
  (moss + sage), manifesto (brass-bronze), letters (darker warm),
  newsletter (amber close-out), footer (deepest). Polaroid room covers
  stay cream — the only paper moments. Token set: `--apo-tile-*` in
  `themes/apothecary.css`. Notes uses the same pattern on the homepage
  with `forest`-palette gradients.
- **Cream-on-dark type tokens.** `--apo-paper` (full), `--apo-paper-dim`
  (body on dark), `--apo-paper-soft` (citations), `--apo-paper-faint`
  (meta lines), plus `--apo-rule-light` + `--apo-rule-strong` for
  hairlines. Use these instead of raw `--ink-*` on gradient tiles.
- **`<Nav variant="overlay">`.** Transparent + light-text nav over the
  dark hero. Default (interior pages) is cream + dark text. The
  umbrella home uses `overlay`; interior umbrella pages render a
  `page-header` band with its own gradient instead.
- **"Dear stranger" letter pattern.** First-person letter from the
  studio replaces a third-person about-strip between hero and the
  rooms section. Narrow column (~620 px), Caveat signature.
- **Date marker eyebrow.** `— Spring · MMXXVI —` (or quarter
  equivalent) replaces repetitive "from the studio" eyebrows. Anchors
  the page as correspondence rather than a meta-labelled section.

```bash
cd site-main
npm install
npm run dev   # local at http://localhost:4321
npm run deploy
```

Full deploy playbook: `site-main/DEPLOY.md`.

---

## 13. Deployment

**Cloudflare Workers** via the Workers Static Assets feature (NOT Cloudflare Pages, despite some legacy references).

### Auto-deploy (active)

Cloudflare's **"Connect to Git"** integration is wired up via the CF dashboard (Workers & Pages → `soothemade-notes` → Settings → Builds → Connect Git). It triggers on push to `main`:

- Production branch: `main`
- Build command: `cd site && npm install && npm run build`
- Deploy command: `cd site && npx wrangler deploy`

Push to `main` → CF builds + deploys automatically.

### Manual deploy (fallback)

If auto-deploy ever fails or you want an ad-hoc deploy:

```bash
cd site
npm run deploy   # = astro build && wrangler deploy
```

Requires `npx wrangler login` (one-time). Currently authenticated as `iamvashisht1@gmail.com` with workers write scope.

### Rollback

Workers retain prior deployments. Roll back without re-pushing:

```bash
cd site
npx wrangler deployments list
npx wrangler rollback <deployment-id>
```

### `wrangler.toml`

`site/wrangler.toml` declares the worker name, compatibility date, and assets directory. The `routes = [{ pattern = "notes.soothemade.com", custom_domain = true }]` block is commented out — the custom domain is attached via the CF dashboard instead. Don't uncomment it without coordinating with the dashboard config.

### `notes.soothemade.com` custom domain

Attached via CF dashboard → Workers → `soothemade-notes` → Settings → Domains & Routes → "Add Custom Domain". CF provisions the DNS record + SSL automatically.

---

## 14. Canva integration

The Canva MCP is available when connected. It is used as a **design generator**, not as a brand-kit-paperwork tool. (Past mistake: leading with brand-kit walkthroughs instead of generating designs. See memory file `feedback_canva_as_design_generator.md`.)

### Brand kit

- **Brand kit ID:** `kAHKILw9XGg`
- **Name in Canva:** currently `1` (placeholder; recommend renaming to `Soothemade` in the Canva UI for clarity)

When generating any new Canva design, pass `brand_kit_id: "kAHKILw9XGg"` so Canva auto-applies the brand palette / fonts / logo.

### Uploaded brand assets

| Asset | Canva asset ID | Source file | Use for |
|---|---|---|---|
| Soothemade Brand Mark | `MAHKIAtzV9Q` | `brand/brand.svg` | Light surfaces, default |
| Soothemade Brand Mark — On Dark | `MAHKIOhXSrM` | `brand/brand-on-dark.svg` | Dark mode, dark hero, photo overlays |
| Soothemade Brand Mark — Mono Dark | `MAHKIBw3ykg` | `brand/brand-mono-dark.svg` | Single-color print, formal contexts |
| Soothemade Brand Mark — Mono Cream | `MAHKIP6lrpc` | `brand/brand-mono-cream.svg` | Watermarks, very dark BGs |

Pass these as `asset_ids` in `generate-design` calls so the canonical mark appears in the output, not an AI-generated facsimile.

### Re-upload pattern

To upload a new variant or a refreshed mark, the source must be reachable via a public URL. The simplest pattern: commit + push the SVG to the repo, then upload via:

```
https://raw.githubusercontent.com/varunvashisht1/Soothemade/<sha>/brand/<file>.svg
```

Pin to a commit SHA, not a branch, for immutability.

---

## 15. Development workflow

### Branch naming

Feature branches: `claude/<descriptive-slug>` (typically auto-generated, e.g. `claude/heuristic-cannon-21916d`).

### Commit conventions

- **One topic per commit.** Don't mix structural changes with content changes.
- **Detailed commit messages.** Include why, not just what. Reference open issues / decisions.
- **Co-author tag** for AI-assisted commits:
  ```
  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
  ```
- **HEREDOC for multi-line messages** to preserve formatting:
  ```bash
  git commit -m "$(cat <<'EOF'
  subject

  body...

  Co-Authored-By: ...
  EOF
  )"
  ```

### Merge strategy

`--no-ff` with descriptive merge commit messages. Keeps the "this line of work landed" record visible in the log.

Don't use squash-merge inside this workflow (the early PRs #1, #2 were squash-merged via GitHub UI; downstream branches still carry the unsquashed history which made one prior merge messy. Future merges should be `--no-ff` against `main`).

### Don'ts

- ❌ `git push --force` (destructive). Don't use unless explicitly directed.
- ❌ `--no-verify` to skip hooks. Don't.
- ❌ Direct commits on `main` without going through a branch + merge.
- ❌ Committing `node_modules/`, `dist/`, `.claude/`, `*.tmp.pdf`, preview PNGs (`p09_*.png`, etc.). These are gitignored or should be cleaned before commit.

---

## 16. Memory & external context

Project-specific memory lives at:

```
~/.claude/projects/C--Users-varun-Documents-GitHub-Soothemade/memory/
```

Files there:

- `MEMORY.md` — index of memory files
- `feedback_canva_as_design_generator.md` — when asked to "use Canva", lead with `generate-design`, not UI walkthroughs
- `reference_canva_brand_assets.md` — Canva brand kit ID + uploaded asset IDs (mirror of § 14)
- `project_cloudflare_deploy.md` — CF auto-deploy is wired via Git integration (mirror of § 13)
- `directive_as_built_doc.md` — directive that AS_BUILT.md is the single source of truth, must be kept current

These memories **do not travel** to other AI tools (Cursor, Copilot, ChatGPT, etc.) — they only inform Claude Code sessions on this machine. That's specifically why this AS_BUILT.md file exists: any AI can pick it up from the repo.

---

## 17. Roadmap / open items

### Currently shipped products (7)

P01–P06 + P09. See `STATUS.md` for the full content list and `research/06-problem-product-matrix/top-30.md` for the 30-product roadmap.

### Wave 2 remaining

P07 (Positive-Discipline Phrase Cards), P08 (Back-to-Work Planner), P10–P15 (Twin Pregnancy, NICU Journal, Tantrum Decoder, BLW, Last Two Weeks, Family Traditions).

### Wave 3

P16–P30. Untouched.

### Pillar blog posts

B01 done. B02–B30 to write. Topics in `research/03-blog-serp/findings.md`.

### Pending decisions

- **Hex drift:** brand.svg sage (`#7A8B6F`) and wordmark (`#3D3935`) vs visual-identity.md (`#8C9B7A`, `#2E2A24`). Pick one source of truth.
- **Persona:** A / B / C (default B). Owner has not explicitly locked.
- **`brand/assets/` vs flat `brand/`:** visual-identity.md:132 says assets will live in `brand/assets/`, but they're actually flat in `brand/`. Pick a convention and align.
- **Canva brand kit name:** currently "1". Recommend rename to "Soothemade" via Canva UI.

### Pending renders

P01–P06 PDFs are one step behind: they were rendered before the Caveat-h2 change landed. P09 has the Caveat h2. Render command:

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
  -v "/c/Users/varun/Documents/GitHub/Soothemade:/work" \
  soothemade-render python scripts/render.py --all
```

After running, commit the seven `product.pdf` files.

---

## 18. Changelog

One line per commit that changes structural project state. Most-recent first.

- **2026-05-30** — **Commercial conversion audit of the whole catalog (127-agent workflow). Reviewable recommendations in `audit/`, nothing applied to live listings yet.** Owner asked for "another audit, same purpose that it sells the best, find issues and suggest changes people would pay for" using the strongest model. Prior audits (care-contract, writing-rules) maxed prose quality; this one targets the **conversion surface** instead (titles, hooks, price, bundles, differentiation) because that is where pre-first-customer revenue is won or lost. Run as a multi-agent Workflow: pipeline of 55 printable audits each adversarially verified (110 agents), 12 ebook fold-in agents, 4 cross-catalog synthesis agents (bundles, pricing, routing, cannibalization), 1 executive-report agent. 127 agents, ~5.6M tokens, ~15 min. **Headline findings:** (1) **Title invisibility is the catalog-wide #1 leak** — nearly every product leads with a brand-voice phrase buyers never type ("Saying No," "Cue Decoder," "Slow Motherhood") and buries the searchable terms in the slug/body; 94 high-severity issues, the vast majority title-related. (2) **42 products are underpriced** — flagships parked below thinner siblings (P49 $7→$12, P04 $9→$14, P25 $9→$14, P32 $9→$14, P52/P48 →$16); single-price catalog sum $645→$752 recommended. (3) **Zero bundles existed** — 14 proposed at ~55-70% of a-la-carte (Fourth Trimester, Postpartum Mind, Big Feelings, Caregiving, etc.) plus a megabundle as a high price anchor. (4) **38-row buyer-routing guide** ("which one do I need?") to convert catalog depth from confusion into navigation. (5) **11 cannibalization clusters** mapped with title fixes (tightest collision: P46 vs P50 eldercare, P09 vs P21 postpartum-mental-health). **Artifacts:** `audit/conversion-audit.md` (executive report), `title-rewrites.{md,csv}` (all 55 old→new titles + keywords + price), `per-product-issues.md` (full per-product diagnosis, 281KB), `bundle-matrix.md`, `pricing-model.md`, `which-product-guide.md`, `cannibalization-map.md`. **Known limitations (flagged in the report's editor's notes, NOT yet fixed):** the adversarial verifier optimized keyword coverage harder than brand voice, so ~12 of the 49 corrected titles over-rotated into Etsy keyword-stuffing that breaks the calm voice (worst: P03 ends "Postpartum Journal, Used Badly"; P31 uses pipe-stuffing) and need a voice pull-back pass; and the synthesis agent's megabundle came in underpriced at $65 (too low to anchor — should be ~$189). **Nothing applied to live listings** — `web.md` frontmatter, `featured-products.ts`, and prices are unchanged. These are reviewable recommendations pending owner approval, because titles + prices are brand/commercial decisions, not mechanical edits.

- **2026-05-28** — **KDP automation pack. All 12 ebooks now ready for the manual KDP upload at ~10 min per book.** Owner asked what could be automated for kindle listing with the constraint "you do your work, I will do mine later, give me steps." Honest framing established up front: the KDP upload form itself is NOT automatable (no public API, browser automation violates Amazon TOS, account-ban risk is real). What IS automatable: everything around it. Shipped Tier 1 + Tier 2 of the automation menu. **Per-book deliverables (12 books × 2 new files):** every `ebooks/Bnn_*/` now contains `kindle-upload.md` (full KDP form-fill: searchable subtitle, ~1700-2000 char description in brand voice, 7 long-tail keywords, 3 primary categories + 7 expansion targets, territory pricing grid, launch sequence reference) plus `cover-kdp.jpg` (KDP-preferred JPG, converted from `cover.png` via ImageMagick at quality 92, ~110-150KB each). The B01 subtitle alone went from poetic-but-invisible *"What to say when you don't have the energy to find your own words"* to keyword-loaded *"What to Say When Family Drops By in the First Six Weeks. A Postpartum Companion for New Parents Setting Boundaries."* (140 chars, under KDP's 200 cap) — same brand voice, front-loaded with the phrases Kindle searchers actually type. Every book's keywords are 7 long-tail phrases (e.g. `what to say to family after baby is born`) not single words, because Kindle's search index since 2020 favors phrases. Categories chose 3 slots per book with off-pattern / low-competition slots noted explicitly. **Repo-level deliverables (`kdp/`):** `COMMON-FIELDS.md` (DRM=No, KU=Yes 90-day exclusive, 70% royalty, 13-marketplace pricing grid, day-1-to-day-90 launch sequence, and a 13-week free-promo schedule that sequences the 60 free days available across 12 books so no two books compete in the same week); `author-central-bio.md` (one-time Author Central setup); `launch-tracker.csv` (12-row spreadsheet for the owner to fill in as books go live: ASIN, publication date, KU dates, free-promo days used, first review, review count, 30/90-day revenue); `arc-outreach-template.md` (two tiered email templates — Tier 1 doulas/IBCLCs/therapists, Tier 2 mom-bloggers/Substack writers — plus explicit don't-ask-for-5-star-reviews TOS guidance); `reddit-launch-posts.md` (5 community-first draft posts for r/Mommit, r/BabyBumps, r/Daddit, r/postpartum, r/AgingParents, each framed as personal contribution with the book in a footnote, plus subreddit-by-subreddit rules table); `pinterest-pin-briefs.md` (15 pin briefs across hero books B01/B07/B11 with the "Tuesday at 4pm" pin from B07 nominated as the hero pin to make 10 variants of); `draft2digital-metadata.csv` (post-KU distribution sheet with BISAC codes + pricing for Kobo/Apple/Google/Barnes-Noble when KU exclusivity ends). **Verification tooling:** new `scripts/kindle_verify.py` walks every `ebooks/B*/`, checks cover PNG + cover JPG (dimensions ≥ 1600×2560, aspect ~1.6, file size < 50MB), epub structure (valid zip, mimetype = `application/epub+zip`, has .opf package), and upload pack content (subtitle ≤ 200 chars, 7 keyword slots, 3+ categories). Read-only, re-runnable, exits non-zero on errors. Windows console UTF-8 fix included. Final run: all 12 books pass green. **The owner-facing runbook:** new `KDP-RUNBOOK.md` at repo root walks the human through Phase 1 (account setup with W-9 / W-8BEN + bank), Phase 2 (run the verifier), Phase 3 (per-book upload, ~10 min each), Phase 4 (Author Central + free promos + ARC + Reddit + Pinterest), Phase 5 (day-30/60/90 checkpoints with explicit go/no-go decision logic for KU renewal at day 90). Total owner time budget: ~3-4 hours for upload work, ongoing during launch. **Explicit non-goals in the runbook:** no sales API integration (not worth it at this scale), no review-buying services (TOS violation), no replying to every review (looks defensive). **Honest framing on books vs printables:** the runbook + the upstream brand-growth analysis both note that books have a higher conversion bar than printables (attention purchase vs utility purchase), so books are Stage 2 of the distribution playbook, not Stage 1 — Stage 1 is Etsy printables. KDP work ships now as "ambient inventory": get the books live, earn KU page-reads passively, focus active marketing on whichever printable becomes the Etsy hero. **Hero candidates flagged for active KDP push:** B01 (gift-able, concrete, highest first-review velocity), B07 (most Pinterest-shareable manifesto), B10 (highest search-volume keyword set — "first six weeks postpartum"), B11 (longest shelf-life because eldercare buyers search year-round, not seasonally).
- **2026-05-28** — **Critical analysis + polish pass on all 12 ebook PDFs.** Read-the-product audit of the just-shipped bibliography surfaced five PDF-render issues that the earlier per-book commits had not caught (the per-book pipeline rendered, the bibliography commit verified content, but no single pass had sat with the typography across the whole shelf). **Issues found:** (1) long H1 chapter titles wrapped to three lines on chapter-start pages — most visible on B01 ch1 *"Why 'No' Is Hard Postpartum"*, B11 ch1, B12 ch1 — the 110px Caveat was eating the line. (2) Inline `code` (e.g. `notes.soothemade.com` in cross-sells, URLs in back matter) rendered as Inter monospace inside a sage-tinted box, which broke the body voice mid-paragraph and read as terminal output rather than prose. (3) Body text at 36px ran a touch large for the 1600×2560 Kindle aspect — pages flipped thinner than they read and felt under-set. (4) `@page` margins at 200px all sides gave a wider gutter than the design needed and the top margin felt floaty on chapter-start pages. (5) Chapter-end whitespace was confirmed acceptable — it is the forced gap from `page-break-before: always` on the next `h1`, no fix needed. **Fix:** one `book.css` update authored against B01 and copied verbatim into the other 11 books, then `render_ebook.py --skip-cover --skip-epub` re-rendered all twelve `book.pdf` files. **Type scale changes:** h1 110px→82px font-size, line-height 1.08, `text-wrap: balance`, `max-width: 92%`, `hyphens: manual` (two-line max on every chapter title in the bibliography); h2 56px→46px with tighter 70px top margin (was 90px); h3 32px→26px to match the calmer body; body 36px→32px, line-height 1.6, `hyphens: auto`. **Inline code rule changed entirely:** inline `code` now renders as italic Fraunces matching body voice — transparent background, no border, no padding, color `var(--ink-soft)`. Multi-line `pre` blocks keep the sage-paper box for actual script/template content. **Page margins** tightened to 180px top, 200px left/right/bottom (was 200 all sides). **Effect:** page counts dropped 15-32% per book as the tighter type pulled prose together — B01 32→26, B07 19→16, B10 22→15, B11 28→19. **Visual verification** via Docker pdftoppm preview on B01 p4 + p12 (H1 wrapping fixed), B05 p17 (the `notes.soothemade.com` cross-reference reads as prose now, no monospace box), B07 p5 (chapter start clean). Caveat / Fraunces / Inter still loading from Google Fonts via the `soothemade-ebook` image — no font-stack changes. EPUBs were not re-rendered (this is a print-typography concern; the EPUB CSS is its own file and Kindle/Apple Books re-flow type per device anyway).
- **2026-05-28** — **Bibliography complete. Shipped B02-B12 (11 ebooks) bringing Soothemade's books to twelve.** Sequential adaptation pass over the rest of the planned ebook lineup, each book produced as a separate commit on `claude/B02-B12-bibliography` before merging. **The twelve:** B01 *30 Scripts for the Postpartum Visitor* (from P02), B02 *The Field Guide to Asking for Help* (from P49), B03 *How to Read Your Baby* (from P34 Newborn Cue Decoder), B04 *Big Feelings* (from P13 Toddler Big Feelings Cards), B05 *The Pregnancy Safety Reference* (from P51), B06 *Birth Is Scary* (from P52 Birth Anxiety Workbook), B07 *Slow Motherhood* (from P03), B08 *The Partner's Postpartum Playbook* (from P04), B09 *Nine Months You Are Also Living* (from P55 Partner Pregnancy Companion), B10 *The First Six Weeks* (from P07 Newborn Survival Planner), B11 *Caregiving, the First 90 Days* (from P46 Eldercare First 90 Days), B12 *The Long Caregiving Stretch* (from P50 Family Caregiver Workbook). **Adaptation by tier:** Tier 1 (B02-B05, B08) were 90%+ read-text and converted with light editing + book-shaped front/back matter. Tier 2 (B06-B07, B09-B12) required real rewriting to strip fillable workbook scaffolding and replace it with narrative chapters. The 30-script/40-card products (B02, B03, B04) kept the source content verbatim, the planner products (B07, B10, B11, B12) became essay-driven chapters. Tier 3 source products (P08, P11, P35, P36, P41, P53, P56) are pure journals and were intentionally held — converting them would strip the writing space that is the product. **Per-book outputs:** each B-folder contains README, OUTLINE (B01 only), manuscript.md, metadata.yaml, cover.html, cover.png (1600×2560, Soothemade brand language), epub.css, book.css, book.epub, book.pdf. All twelve covers share the same template (sage paper, sprig, Caveat title in primary sage, Fraunces italic subtitle, sage divider, Soothemade wordmark at bottom). All twelve metadata.yaml files list `author: Soothemade` and `publisher: Soothemade` (per the post-B01 brand cleanup). All twelve manuscripts carry the locked Maya voice in the "A note from Maya" front matter, with `*With care, Maya*` signoffs preserved from the source products. **Crisis lines included** in every back matter (US 988 + PSI 1-833-852-6262 + MMH 1-833-943-5746; UK Samaritans; Canada 9-8-8; Australia PANDA/Lifeline as appropriate); B11/B12 add the eldercare-specific lines (Eldercare Locator 1-800-677-1116, Family Caregiver Alliance 1-800-445-8106, Alzheimer's Assoc 1-800-272-3900). **Cross-sells** between books wired in each back matter (e.g. B01 ↔ B02, B11 ↔ B12, partner books ↔ postpartum books). **Pipeline:** all rendered via `soothemade-ebook` Docker image, the `render_ebook.py` script unchanged from B01 except for the addition of PDF output (now ships both .epub and .pdf per book). AI-punctuation scrubber walked every manuscript, autofixed any em-dashes/semicolons that slipped in. **Pricing direction held at $4.99 per book** (Kindle 70% royalty bracket) for the whole bibliography; KDP upload and distribution are user-driven, not in this commit. **The Tier 3 holdout list** documented above in case the brand later decides to ship those as journal-style books (e.g. as printable PDF only via Notes, since the writing space is the product).
- **2026-05-28** — **Dropped the "Soothemade Press" sub-brand. Books ship under just "Soothemade." Maya removed from the front cover.** Same-day follow-up to the B01 launch commit. Owner call: one brand is simpler than two, and the customer-facing "publisher" field on Kindle reads cleaner as plain `Soothemade`. AS_BUILT § 2 reverted, Press is back to "Reserved, not built" with a note that books ship under the master brand. **Cover changes:** "A Soothemade Press Book" → "A Soothemade Book" (top plate); removed the `Maya` + `Soothemade` author block from below the divider (Maya is the voice inside the book, not the byline on the cover, mirroring the existing PDF cover convention where the brand mark is on the cover and Maya signs the content); "Soothemade Press" → "Soothemade" (bottom plate, terracotta "Press" italic span deleted). **Metadata changes:** `author: Maya` → `author: Soothemade`, `publisher: Soothemade Press` → `publisher: Soothemade` (both in metadata.yaml and the manuscript YAML header). **Manuscript back-matter changes:** "About Soothemade Press" page renamed to "About Soothemade" with the framing rewritten to describe books as part of the apothecary (alongside printables/planners/cards) rather than a separate imprint. Closing line "A Soothemade Press book. Made slowly, in plain language." → "A Soothemade book. Made slowly, in plain language." The "Also from Soothemade" cross-sell page already used the right framing; B02 mention rewritten from "the second title from Soothemade Press" to "the second Soothemade title, coming next." README, OUTLINE, epub.css comments all swept for Press references. Cover re-rendered (130KB after the removal, slightly smaller than the 152KB version). Book.epub re-rendered. Visual verification: cover inspected, cleaner without the author block, sage divider now anchors visually to the bottom plate without competing typography in between.
- **2026-05-28** — **Launched Soothemade Press. First ebook (B01) shipped: *30 Scripts for the Postpartum Visitor*.** New imprint, new product line, new repo top-level: `ebooks/`. The Press is the books-format arm of Soothemade, parallel to Notes (printables). Brand-architecture status moves from "Reserved" to "Active sub-line" in § 2. Adaptation strategy: each book is its own product, not "a PDF without the lines" — the conversion from fillable journal to readable book is a real rewrite that adds book-shaped front matter (title page, dedication, TOC, expanded "note from Maya"), per-chapter intros that frame the material, and back matter (about Maya, about the Press, cross-sells, expanded crisis-line page). B01 source: P02 "Saying No" Script Pack (postpartum/Wave 1 anchor). 16 chapters: dedication + 10 numbered chapters + back matter. ~7,500 words. Front-matter is voice-of-Maya, body is the 30 scripts verbatim (the core product stays untouched), each chapter has a 150-250 word intro that gives reading flow vs the printable's standalone-page format. New tooling: `soothemade-ebook` Docker image extends `soothemade-render-preview` with pandoc + imagemagick. `scripts/render_ebook.py` is a thin wrapper that (a) renders `cover.html` → PNG at 1600×2560 via WeasyPrint + pdftoppm, (b) runs pandoc with `--epub-cover-image` + `--css epub.css` + metadata.yaml, (c) outputs `book.epub` (163KB for B01). Pandoc cwd-fix: command runs inside the book dir so the metadata.yaml's relative paths (`cover-image: cover.png`, `css: epub.css`) resolve. AI-punctuation scrubber updated to walk `ebooks/B*_*/manuscript.md` as well as `products/`. **Cover design language:** sage paper (#EAEEE2), Caveat title in primary sage (#8C9B7A), Fraunces italic subtitle in ink-soft (#5C5347), muted-sage divider, Caveat author signoff with Inter small-caps imprint plate below, custom SVG sprig at top, "Soothemade Press" wordmark at bottom in Caveat + Fraunces italic terracotta (the same "Notes" treatment but with Press in terracotta). Visual verification: cover.png inspected, brand-consistent with the existing PDF cover language, would-be-recognizable on a Kindle shelf next to the 11 future titles in the planned bibliography. **Bibliography roadmap (12 books):** Tier 1 read-ready (B1 P02 ✓, B2 P49 Asking for Help, B3 P34 Newborn Cue Decoder, B4 P13 Big Feelings, B5 P51 Pregnancy Safety Reference). Tier 2 needs adaptation (B6 P52 Birth Anxiety, B7 P03 Slow Motherhood manifesto, B8 P04 Partner Postpartum, B9 P55 Partner Pregnancy, B10 P07 Newborn Survival, B11 P46 Eldercare First 90 Days, B12 P50 Family Caregiver). Tier 3 hold (P08/P11/P35/P36/P41/P53/P56 are pure journals, do not convert). Pricing direction: $4.99 per book on Kindle (70% royalty bracket). KDP upload + distribution are user-driven, not in this commit.
- **2026-05-22** — **Replaced the PMP-imported rules with a Soothemade-native care contract. Locked the persona to Maya. Catalog-wide signature swap. All 55 PDFs re-rendered. Catalog now scores 55/55 against the care contract.** The earlier same-day commit adopted `varunvashisht1/VarunVashisht-Web/WRITING-RULES.md` as a literal contract. That was the wrong framing: the PMP doc was an *example* of what a quality contract looks like, not the contract itself. The right contract for Soothemade is the one in the rewritten `WRITING-RULES.md` — six care signals organized around whether a paying customer feels cared for. The signals: (1) scene anchor in the opening note (concrete time / room / body / overheard line); (2) the voice has a face (`*With care, Maya*` signoff); (3) disclaimer voiced not armored (P09 is the model); (4) modest about what it does (no `transform`, `unlock`, `you deserve`, `breakthrough`); (5) hard things named not euphemized (`mom rage`, `loss`, `the primary witness of someone else's diminishment`); (6) each product is its own shape (catalog-wide form variety check). **Persona locked to Maya** (Option B in `brand/persona.md`, previously default-not-locked). All 92 personal-note signoffs across 55 product `content.md` files swapped from `*Soothemade*` to `*With care, Maya*` via `.tmp/apply_maya_signoff.py` (dry-run + apply pattern). Mirrors the umbrella's `*with care, the studio*` pattern, adapted to remove the banned em-dash. The brand mark `Soothemade` continues to render on PDF cover + colophon via the template — Maya is the personal voice, Soothemade is the studio. **Targeted content fixes:** P23 `content.md:25` "I screamed at my three-year-old in the laundry room when he was four" — dropped the trailing "when he was four" continuity error (the most-quoted opening sentence in the catalog now reads cleanly). P04 `content.md:279` "Other parents look like they're crushing it. They're not." → "Other parents look like they have it figured out. They don't." — preserves the voice-defining puncture without the wellness-mill `crushing it` phrase. P55 `content.md:657` worksheet field "WHAT I WANT FOR MYSELF, IN THIS NEW CHAPTER" → "WHAT I WANT FOR MYSELF, ONCE THE BABY IS HERE" — plainer, less generic-wellness. P54 `content.md:9-11` opening rewritten to add scene anchors — "You have a 10am meeting tomorrow, an OB appointment Thursday afternoon, and you have not told anyone at the office yet" — the only product that was failing Signal 1. **Auditor rebuilt** (`scripts/audit_writing_rules.py`) from a regex-hygiene checker into a per-product care scorecard. Six signals scored. Code blocks (read-aloud scripts, ASCII template fields) and `*"..."*` quoted critiques are stripped before scanning for banned vocabulary — the rules apply to the brand's voice, not to phrases the brand is quoting back to puncture. **All 55 PDFs re-rendered** via Docker `--all`; `pdfs/` flat-folder mirror updated. **Final state:** 55/55 products pass all four per-product signals. Catalog-wide: 0 disclaimer-reuse clusters of 4+ products (disclaimers are already varied). 7/55 (13%) of products use the `## What this [X] is, and is not` H2 framework — well below the 50% template-uniformity threshold.
- **2026-05-22** — **Adopted extended writing-quality rules from the PMP audit lineage. Catalog-wide PDF audit + 7 targeted fixes across 6 products.** New repo-root doc `WRITING-RULES.md` adapts `varunvashisht1/VarunVashisht-Web/WRITING-RULES.md` (the quality gates that produced the audited PMP V8 Study Guide) to Soothemade. Imports 20 banned AI-tell terms, the filler-phrase ban, density rules (paragraphs ≤600 chars, sentences ≤50 words), substance + rhythm + repetition rules. Documents Soothemade-specific carve-outs inline: (a) `actually` is preserved as voice-defining ("what actually moves supply", "meals you actually like" — the brand's truth-vs-performance wedge); (b) `harness` as a physical noun stays (car-seat harness, high-chair harness); (c) literal time-of-day uses of "at the end of the day" stay; (d) American spelling held (audience is US new parents, crisis lines are US-based — British would clash); (e) PMP's "Industry Term (Plain question)" pattern does not fit Soothemade's intimate voice and is skipped. New auditor `scripts/audit_writing_rules.py` is read-only, walks every `content.md` + `web.md`, flags violations with file + line + matched text. Catalog-wide audit (55 products, 110 files) found only the long tail — Soothemade's existing voice guide and punctuation scrubber had already driven content to a high baseline. Seven content fixes applied: (1) P30 `content.md:401` "biggest leverage point" → "biggest single thing you can do". (2) P50 `content.md:772` "Leveraging employer's EAP" → "Using employer's EAP". (3) P41 `content.md:21` "fertility journey" → "fertility". (4) P06 `content.md:337` "going forward" → "from here". (5) P09 `content.md:332` "going forward" → "from here". (6) P34 `content.md:195` 51-word "Call the pediatrician if" criteria-list sentence split into 5 sentences. (7) P35 `content.md:15` 51-word "It is the place to write down" list-as-sentence split into 6 sentences. P26 `web.md` body also had a borderline 51-word inclusive-list sentence split into two (web body doesn't affect PDF — Astro only). Seven PDFs re-rendered via Docker (`P06`, `P09`, `P30`, `P34`, `P35`, `P41`, `P50`); flat-folder mirror at `pdfs/` updated. Zero em-dashes, zero semicolons, zero `comprehensive`/`holistic`, zero `in order to`, zero `in terms of`, zero `due to the fact that`, zero `ultimately`, zero `basically` found anywhere in PDF source — the brand was already very close to the PMP bar.
- **2026-05-21** — **Premium gradient-tile treatment across both sites + umbrella voice tightening (consolidated entry, 5 commits).** Captures five commits that landed on `main` without their own changelog entries; recorded here retroactively as part of a consolidation pass. The whole arc reshapes the page-shape grammar on both sites from "flat surface with sections that have different copy" to "sequence of dark gradient tiles, each with a distinct warm undertone." (1) **Dear stranger letter** (`059490d`): replaced the third-person "about-strip" between the umbrella hero and rooms with a short first-person letter — *"Dear stranger, thank you for finding us..."* — three paragraphs, narrow ~620 px column, Caveat signature *"with care, the studio."* Same position as the about-strip; voice instead of description. (2) **Date marker eyebrow** (`f3612bd`): replaced repetitive *"— from the studio —"* eyebrows with `— Spring · MMXXVI —`. Anchors the page as correspondence (a letter has a date, not a meta-section-label) while keeping the eyebrow rhythm. (3) **Umbrella gradient tiles** (`4698602`): every section on the umbrella home is now its own dark gradient tile — hero (warm-black + amber), dear-stranger (umber + amber), rooms (deep moss + sage), manifesto (brass-bronze), letters (darker warm), newsletter (amber close-out), footer (deepest). Polaroid room covers stay cream — the only paper moments. Added `--apo-tile-{letter,rooms,quote,letters,news,footer}` token sets in `themes/apothecary.css`. Added cream-on-dark type tokens: `--apo-paper-dim` (78%), `--apo-paper-soft` (62%), `--apo-paper-faint` (42%), plus `--apo-rule-light` + `--apo-rule-strong`. Color-scheme switched from light → dark so browser chrome adapts. (4) **Notes homepage premium gradient** (`5bf78af`): same gradient-tile pattern brought to `site/`'s homepage. Hero, CategoryRow, Manifesto, JournalRow, Newsletter, ProductGrid, Footer all restyled. Added matching tokens in `themes/forest.css` so the gradients work in the default Notes palette. Inner pages not yet redone in this commit. (5) **Premium across every page** (`167e024`): rolled the gradient + cream-on-dark treatment to remaining pages on both sites — `about`, `contact`, `policy`, `press`, `newsletter`, `lines`, `journal` + `journal/[slug]` on umbrella; `about`, `contact`, `policy`, `journal` + `journal/[slug]`, `shop` + `shop/[slug]` on Notes. Introduced a shared `.page-header` band component pattern: gradient strip with eyebrow + h1, used as the consistent top of every interior page. `SoftStub.astro` updated on both sites. Build passes on both: umbrella 1050 KiB / 222 KiB gz, Notes builds all 75 product routes. Both sites deployed; live URLs unchanged. Net effect: the umbrella reads as a sequence of photographs pinned in a dark gallery, with polaroids the only paper moments; Notes reads as the same brand seen at night.
- **2026-05-20** — **Scaffolded the umbrella site `site-main/` for `soothemade.com`.** A second Astro app, fully independent from `site/`. Honors `brand/architecture.md`'s "no products at the umbrella" rule — the umbrella tells the master-brand story and routes out to sub-lines via hyperlinks (Notes is the only live one; Kitchen / Studio / Field appear as "in the workshop" placeholder cards). New brand source-of-truth doc `brand/umbrella-story.md` extends the Notes voice guide from parenthood-specific to master-brand level around the themes the founder set: slowness, nature-as-pace, peaceful-as-restraint, "loving yourself" without using the words. Pages: `/` (hero → brand lede → line cards → manifesto → journal preview → newsletter), `/lines` (full sub-line index), `/journal` + `/journal/[slug]` (umbrella essays, distinct from Notes' parenthood journal — seeded with three: "On weather-paced work," "The hour before anyone else is up," "What we mean by slow"), `/about`, `/freebies`, `/contact`, `/policy`, `/press`, `/newsletter`, `/404`. New `daylight` theme (cream + moss + terracotta, light variant) as default; Notes' three dark themes preserved as alternates for continuity. New `LineCards` component renders sub-lines from `src/data/lines.ts` — Notes as a live external link with `↗` arrow, others as quiet "Hear when it opens" CTAs to the letter. Reused-from-Notes components (Hero, Manifesto, Newsletter, JournalRow, BotanicalLeaf, SoftStub, BaseLayout) copied with light retargeting; nav and footer rewritten for the umbrella. Newsletter posts to Notes' `/api/subscribe` with `source=umbrella` — single subscriber list, tagged by entry point. Worker `soothemade-main` is intentionally bindings-free (no D1/R2/KV/Vectorize/AI). Build verified: 1050 KiB / 222 KiB gzipped. Tagline locked: "Made for the parts of life no one is photographing."
- **2026-05-21** — **Umbrella site redesigned: shop-window shape, Apothecary palette.** Replaced the initial daylight-cream centered-everything umbrella with a photographic shop-window homepage. New theme `apothecary` (warm-black hero, cream paper, single amber/brass accent — Aesop-coded restraint) added at `site-main/src/styles/themes/apothecary.css` and set as the default in `theme.json`. Component rewrites: `Hero.astro` is now a 92vh dark "photograph" scene (left text column, right glass-blur photo-tag overlay describing what's currently in the window), `LineCards.astro` renders the four rooms as slightly-rotated polaroid cards with Caveat room-stamps in the corner, `Nav.astro` gains an `overlay` variant (transparent + light text over the hero) alongside the default (cream + dark text for interior pages), `JournalRow.astro` reshaped from 3-up card grid into a single-column letters list with date metadata · title · arrow. `Newsletter.astro` reshaped to a single bordered input + dark button row. `Manifesto.astro` palette-adjusted. New `about-strip` section between hero and rooms in `index.astro`. The room covers use a tight 4-tone deep-warm-black set (red-brown / bronze / green-ink / true black) — same family, subtle differences, the Apothecary mood. Caveat is used heavier than before for "Soothemade" wordmark in nav + footer, the photo-tag title, and the polaroid room stamps. Live at `https://soothemade-main.iamvashisht1.workers.dev` (Version 3fc4a4cd, build 1028 KiB / 218 KiB gz, 23 ms cold start). The original daylight theme + earlier components are preserved in git history. Design studies that informed the decision live in `design/umbrella-*.html` (~20 HTML files documenting 3 shape directions, 5 magazine palette variations, 5 shop-window shape variations, and 4 premium palette pushes for the photographic shape).
- **2026-05-21** — **Umbrella site `soothemade-main` live + wrangler bumped to v4 in both projects.** The umbrella scaffolded yesterday is now deployed at `https://soothemade-main.iamvashisht1.workers.dev` (custom domain `soothemade.com` + `www.soothemade.com` still to be attached via CF dashboard). Fixed a missing `.assetsignore` in `site-main/public/` (mirror of `site/public/.assetsignore`): wrangler refuses to upload the adapter's `_worker.js/` server bundle as a public asset by default — the file lists `_worker.js` + `_routes.json` so Astro copies it to `dist/` on every build and wrangler skips them. Bumped `wrangler` from `^3.99.0` to `^4.0.0` in both `site/` and `site-main/` (`wrangler@4.93.0` resolved). Validated both projects: `npm run build` clean, `wrangler deploy --dry-run` resolves all bindings on Notes (CACHE/DB/VECTORIZE/FILES/AI/ASSETS) and just ASSETS on umbrella. Re-deployed umbrella on wrangler 4 end-to-end (20 ms worker startup). Notes worker untouched in code; the wrangler bump will land via the existing CF Git auto-deploy on this push.
- **2026-05-20** — **Data layer verified end-to-end. Vectorize fully populated (55/55), search returns semantically-correct hits.** Followup to the data-layer rollout below. Set fresh `REINDEX_SECRET` via piped `wrangler secret put` (the no-copy-paste pattern documented in memory `feedback_no_copy_paste_for_secrets.md`). Ran the indexer; first pass landed 50/55 vectors due to Vectorize async-propagation latency, second idempotent pass topped up to 55/55. Smoke tests: `GET /files/P09.pdf` streams from R2 (HTTP 200, 197 KB). `GET /api/search?q=...` returns correct top hits for natural-language queries: "scared about going back to work" → P31 Returning-to-Work (0.605), "twins" → P33 Twin Pregnancy (0.668), "elder care for my parent" → P46 Eldercare (0.638), "keepsake letters to my baby" → P56 Letters to Baby (0.779), "I am pregnant and anxious" → P52 Birth Anxiety (0.636). Also fixed a Windows path bug in `scripts/index_products_vectorize.mjs`: `new URL(...).pathname` returns `/C:/Users/...` on Windows which `join()` then mangled into `C:\C:\Users\...`; replaced with `fileURLToPath` from `node:url`. Operational note: Vectorize V2 `upsert` is async, `vectorCount` may briefly trail the worker's `upserted:N` response by a few seconds to a few minutes; re-run the indexer to top up — it's idempotent on ID.
- **2026-05-20** — **Full Workers data layer wired up. Site is now a complete Worker, not just a static-assets site.** Provisioned + bound four new CF resources: **D1** database `soothemade-notes` (`ddbaf6ed-f1e1-49a3-b88d-609a448daae1`, APAC) with initial schema covering subscribers / orders / download_tokens / journal_views / contact_messages, **R2** bucket `soothemade-notes-files` populated with all 55 product PDFs under `products/Pnn.pdf` keys, **KV** namespace `CACHE` (`d370c098ad334796aa4e461bcaf12c1f`) for rate limiting + catalog cache, **Vectorize** index `soothemade-products` (384-dim bge-small-en-v1.5, cosine), plus the existing **Workers AI** binding for embedding generation. New endpoints: `POST /api/subscribe` (KV rate-limit + D1 upsert), `POST /api/contact` (KV rate-limit + D1 insert), `GET /api/search?q=` (Workers AI embed → Vectorize query, returns semantic matches across the catalog), `GET /files/[code].pdf` (R2 stream), `POST /api/journal/[slug]/view` (D1 counter), `POST /api/admin/reindex` (auth-gated bulk embed + upsert). Search wired into `/shop` page as a calm text-input above the category chips, voice-matched (no "AI" label, no spinners). Internal script `scripts/index_products_vectorize.mjs` POSTs all 55 products' web.md frontmatter to `/api/admin/reindex` to populate Vectorize. Workers AI strictly used for buyer discovery (embeddings), never for generating customer-facing copy — brand voice is anti-AI-mill. Build passes (1.4 MiB / 295 KiB gz). Full operating reference: §19.
- **2026-05-20** — **Shipped 6 more pregnancy products at full quality (P51-P56). Catalog now 55. Pregnancy gap-filling: safety reference, birth anxiety, trimester emotional, work navigation, partner-during-pregnancy, letters-to-baby keepsake.** User-requested batch. P51 The Pregnancy Safety Reference (pregnancy/YMYL extra-careful, 30 pages, the MOST YMYL-sensitive product in the catalog given how it touches safety territory; explicitly organizes questions rather than giving verdicts; NO medication names, NO definitive safety/danger statements, NO dose thresholds; categories: food + drink + activity + environment + medication-class-by-purpose + workplace + travel; the "what they say but actually" page deconstructs common internet patterns; "if I already did this thing" calm framework; question-list template for the provider). P52 The Birth Anxiety Workbook (pregnancy/YMYL, 40 pages, treats birth fear as data not weakness, anti-platitude framing with "trust your body" + "women have done this for thousands of years" explicitly listed as the unhelpful patterns; fear inventory across 8 categories + ~50 named fears; six 2-page fear workbooks for pain / loss-of-control / mom-complications / baby-complications / interventions / the-unknown; scripts page for telling the team you are scared; night-before-labor handwritten-note-to-myself-in-labor; "I am not okay" perinatal mental-health routing with PSI 1-833-852-6262 + MMH 1-833-943-5746). P53 Trimester-by-Trimester Emotional Companion (pregnancy, non-YMYL, 30 pages, intentional companion-by-contrast to P08's data-heavy weekly; "this is the slow journal" framing with explicit "you can write the angry thing about your mother or your partner" ground rules; 5 prompted pages per trimester focused on identity shifts + pre-baby grief + social changes + the body-as-experience-not-data; "I am happy AND I am grieving" two-true-things-at-once permission). P54 The Pregnancy + Work Planner (pregnancy, non-YMYL, 30 pages, pre-announcement research with FMLA/PWFA/ADA/PUMP Act named for US users + "your country has equivalents" for non-US; when-to-tell decision with pros+cons by trimester; 4 manager scripts including the calm + anxiety + supportive + possibly-unsupportive versions; HR conversation script with questions HR may not volunteer; accommodations checklist across physical/schedule/environmental/job-duties with provider-letter language; mat-leave prep handoff document template; "what if I don't come back" page with 6 options including phased exit). P55 The Partner-During-Pregnancy Companion (partner category, non-YMYL, 30 pages, written FOR the non-birthing partner DURING pregnancy as the bookend to P04 which is postpartum; trimester-by-trimester guidance with what's happening + how to be useful + the partner's own experience; the partner's own grief + fear page that most partners do not give themselves time for; things-to-say + things-to-NEVER-say reference page; partner mental health page with PSI explicitly noted as serving partners). P56 Letters to Baby, a Pregnancy Keepsake Journal (pregnancy, non-YMYL, 40 pages, the lyrical heart-y one; 13 prompted letters with extensive blank writing space; Before-I-knew-you, Day-I-found-out, First-appointment, Telling-people, First-time-I-felt-you, Your-name-the-story, What-our-family-is-like, What-the-world-is-like-in-this-year, What-your-other-parent-is-like, What-I-want-you-to-know-about-your-grandparents, Last-week, Night-before-you-came, First-time-I-saw-you; 40-line "things I want to remember to tell you" running list across 2 pages; pocket pages for ultrasound photo + hospital bracelet with cut-line slots; skip-page for Letter 9 if single-parent / chosen-family). All 6 PDFs visual-verified via pdftoppm preview. 4,800+ lines of brand-voiced content. Zero medication names. Crisis lines included for US + UK + Canada + Australia where applicable.
- **2026-05-20** — **Shipped 6 more products at full quality (P45-P50). Catalog now 49. THE ELDERCARE NICHE IS OFFICIALLY OPEN.** Second autonomous batch, this one with visual PDF verification enabled (built new `soothemade-render-preview` Docker image with poppler-utils baked in, used pdftoppm to PNG preview each cover and one body page for the YMYL products). P45 Twin Postpartum First Six Weeks (postpartum/YMYL, 40 pages, companion to P33, day-by-day for week 1 then weekly for weeks 2-6, two-baby side-by-side feed-and-diaper log template, "who has which baby" overnight rotation page, partner page with explicit signal-watching since twin parents have elevated postpartum mood disorder rates, "I am not okay" 8-question check with 3-question call-now trigger). P46 Eldercare First 90 Days Planner (family/YMYL, 40 pages, **THE FIRST ELDERCARE PRODUCT IN THE CATALOG**, opens the niche Soothemade's brand promise has reserved but never served, first-call-list + day-by-day week 1 + weekly through week 13 + medication-log-by-purpose + financial+legal paperwork checklist with elder-law-attorney note + 6-option "where they will live" decision page + sibling-conflict workbook with old-family-wounds surfacing + caregiver "I am not okay either" page + crisis lines including Eldercare Locator 1-800-677-1116 + optional legacy-work page). P47 Stay-at-Home Parent Transition Planner (family, non-YMYL, 30 pages, four-part partner money conversation including the spousal-IRA "page most planners skip" + the "what if we split" preplanning + three day-shape templates by kid age + friend-network rebuilding + "mine things" identity-preservation inventory + SAMHSA substance-use line included given documented at-home alcohol pattern). P48 Adoption Wait + Welcome Pack (pregnancy, non-YMYL, 30 pages, "this is its own pregnancy" framing, home-study prep + financial planning with tax-credit + grief page for paths that included infertility + when-a-match-falls-through with respectful-of-birth-family language + match-call page + welcome-day plan with separate sections for infant vs older-child placement + birth-family communication first-letter guidance + "how we will talk about our family" page with the four-language patterns to AVOID: "real mom/dad", "gave up/away", "lucky", "our own"). P49 The Asking for Help Script Pack (family, non-YMYL, 20 pages, **COMPANION TO P02 SAYING NO**, 30 scripts across 8 categories: meals/childcare/eldercare/errands/emotional support/money/home help/visit, the 4-part structure-of-a-good-ask: specific person + specific request + specific time + easy exit, "when they say no" + "when they say yes" + thank-you script library). P50 The Family Caregiver Workbook (family/YMYL, 40 pages, **THE 50TH PRODUCT**, sister to P46 for ongoing caregiving past 90 days, monthly care-team coordinator log + respite-care planning page named as the most important page + "I am angry" page with the often-unwritten "angry at my loved one" sub-page + "I cannot do this forever" reckoning page + four-page sibling-conflict workbook + couples-counseling reservation page + your-own-health appointment-scheduling page + financial caregiving + hospice considerations with the "hospice is not giving up" de-stigmatizing framing + caregiver crisis lines including Family Caregiver Alliance 1-800-445-8106 + Alzheimer's Association 1-800-272-3900). All 6 PDFs visual-verified via pdftoppm preview. Tooling: built `soothemade-render-preview` Docker image extending the base render image with poppler-utils, persisted for future visual-verification runs. Thumbnails for P33-P50 (18 products without lifestyle JPGs) remain pending per the existing thumbnail-batch brief.
- **2026-05-20** — **Thumbnail audit + P06 dropped from SHIPPED_CODES.** Audited all 32 lifestyle thumbnails programmatically (file size, dominant-colour share, unique-colour count, warmth balance). User-flagged P06 (C-Section Recovery Planner) removed from `site/src/lib/cover-image.ts` SHIPPED_CODES — now falls back to jar glyph. Programmatic audit also surfaced **P07** (51% flat sage — composition reads empty), **P20** (only cool/blue thumbnail, warmth -22 vs avg +20 — may be intentional for Pregnancy Loss), **P32** (warmest at +47 — possible AI-orange smell), and a cluster of small-file washed-out renders (P04/P15/P18/P23/P24, all ≤58KB). These remain in SHIPPED_CODES pending user decision. **P33-P44 ship without thumbnails this round** — jar-glyph fallback until proper photos exist, per user decision to defer the thumbnail batch rather than ship duplicates. Canva `generate-design` flow from `publishing/thumbnail-batch-brief.md` did not reproduce on this attempt: with `brand_kit_id` it produced typography cards, without it produced multi-photo collages. Hand-Pillow vector composition (`scripts/draw_thumbnails.py`) prototyped but produced too-sparse layouts (65% flat background) on first pass; kept on disk for future iteration. Current contact sheet at `marketing/mockups/contact_sheet_current.jpg` for future visual triage.
- **2026-05-20** — **Shipped 12 more products at full quality (P33-P44). Catalog now 43.** Autonomous batch via `claude/p33-p44-autonomous-ship` after the previous session hit the 32MB API request cap on a different batch. Constraint set: no Canva calls and no PDF preview reads from this session, so context stayed well under the cap; thumbnails handed off via the new `publishing/thumbnail-batch-brief.md` for a separate dedicated session. P33 Twin Pregnancy Week-by-Week Planner (pregnancy/YMYL, 60 pages, weeks 6-40 with twin-specific concerns + "if NICU" page + village help-schedule template). P34 Newborn Cue Decoder Cards (postpartum, 30 cards across 5 packs — cries, sleep cues, hunger cues, overstimulation, connection cues — plus "when to call the pediatrician"). P35 IVF Cycle Planner + Journal (pregnancy/YMYL, 50 pages, daily stim tracker, monitoring appointment log, retrieval + fertilization + transfer pages, two-week wait, beta day, running cost tally, ZERO medication names tracked by purpose only, equal-weight "if it worked" / "if it didn't" pages). P36 Sleep-Disruption Pattern Journal (early-years/YMYL, 30 pages, explicit "this journal does not tell you what to do" framing, 14-day log, pattern-spotting, NO method recommendations, common developmental ages named without prescription). P37 Pediatrician Visit Prep Cards (early-years, 12 cards from newborn through 24m + when-to-call page, NO vaccine names — "routine vaccines for this visit" routes to pediatrician). P38 Postpartum Freezer Meal Cookbook (postpartum, 24 pages, 30 recipes across 5 categories all freezer-friendly + one-handed-eating compatible, Indian-friendly throughout). P39 VBAC Prep Planner (pregnancy/YMYL, 24 pages, EXPLICITLY neutral — no recommendation either direction, no statistics, 5-entry decision log over pregnancy, equal-weight TOLAC + scheduled-repeat-cesarean planning). P40 Rainbow Baby Planner (pregnancy/YMYL, 30 pages, voice extra-tender, "the previous loss" acknowledgment + memorial pages + anxiety-in-PAL named patterns + anniversary handling + crisis lines US/UK/Canada + the "what if it happens again" page that refuses to pretend the question isn't there). P41 Discreet TTC Fertility Journal (pregnancy, 60 pages, cover titled "A Daily Notes Journal" with interior fields labeled neutrally — "Morning temperature" = BBT, "Body note" = cervical fluid, etc. — so MIL can flip through and see a wellness journal, decode page at front + tear-out at back, 6 months of tracking). P42 Babyproofing Room-by-Room Checklist (early-years, 14 pages, 8 room sections + Poison Control + tier-1/2/3 prioritization, NO brand recommendations). P43 First Birthday Planning Kit (family, 20 pages, 6-week countdown + anti-Pinterest-production framing + 5 low-effort themes + photo shot list with non-cliché options + letter-to-baby-at-one + family quote-book). P44 Toddler Travel Activity Pack (early-years, 30 pages, 8 scavenger hunts car+plane + 4 I Spy templates + 5 traditional sing-along lyrics PD-only + drawing prompts + sticker chart + 5-step "if they are losing it" soothe sequence). All 12 PDFs at 82-178KB each. Thumbnails for the 12 will follow in a separate session per the brief.
- **2026-05-20** — **Shipped 6 more products at full quality (P27-P32). Catalog now 31.** P27 Hospital Bag Checklist (pregnancy, 424 lines, one-page summary, for-her, for-partner, for-baby, going-home, two-weeks-before, the "don't bother" page, phone-line list). P28 NICU Parent Planner (postpartum/YMYL, 515 lines, daily log for rounds, plain-language NICU glossary, weekly questions, pumping companion, partner page, "what I want today" page, phone-list, going-home page, page-for-the-other-ending). P29 'Who Am I Now' Journal (mental-health, 506 lines, starting page, what-I-miss, what-is-new-in-me, twelve identity prompts, monthly-drawing page, friendship map, body page, work page, five-year letter, annual ritual, when-the-journal-isn't-enough page). P30 Sibling Conflict Scripts (family, 501 lines, 40 scripts across 4 categories: she's-touching-me, it's-not-fair, toy-fights, bedtime-hour; plus what-NOT-to-say page, underlying-pattern page, step-in-vs-step-back decision tree, repair scripts). P31 Returning-to-Work Plan (postpartum, 675 lines, two-weeks-before checklist, 3 manager-conversation scripts, first-day plan, new morning/evening routine templates, "I am a different worker now" page, first-week log, 30-day check-in, 90-day decision page, "this isn't working" honest-options page, partner-load conversation). P32 Babysitter & Daycare Handoff Pack (family, 620 lines, one-page summary, full caregiver brief, food page, what-we-do/don't page, signal-and-routine page, in-case-of decision tree, medication page that names ZERO medications, two consent forms, daycare-orientation questions, fun-things-they-like page). 3,241 lines of brand-voiced content. Zero AI-tells. Zero medicine names (caught "EpiPen" in P32 during sanity scan and replaced with "auto-injector required"). All 6 PDFs at 88-124KB each.
- **2026-05-20** — **Shipped 6 more products at full quality (P21-P26). Catalog now 25.** P21 Postpartum Anxiety Companion (mental-health/YMYL, 534 lines, daily noticing log, weekly self-awareness inventory, "what's a thought, what's a worry" worksheet, 10-card grounding library, "what's normal this week" reference for the full first year, when-to-call signs, partner page, appointment prep template). P22 Introducing Solids Planner (early-years, 441 lines, readiness page, gear list, daily eating log, twelve-food starter list, allergen-introduction log, "they hate it" page, purees-vs-finger-foods page, mealtime scripts for grandparents, "I'm overwhelmed" simplest-possible-meal-plan). P23 Mom Rage Workbook (mental-health/YMYL, 535 lines, noticing log, 20-trigger trigger-map, "what was underneath" worksheet, what-the-nervous-system-is-doing page in plain language, in-the-moment scripts including cold-water-on-wrists, 14-script repair library across ages, when-to-call-a-real-provider, partner page). P24 Bedtime Routine Cards (early-years, 376 lines, 30 printable cards across four packs — 12 core steps, 6 tonight-only, 6 emotion-check, 6 choice — plus parent guide on how to introduce). P25 Holiday Boundary Pack (family, 575 lines, pre-gathering worksheet, 20-script library across 10 comment categories, 10-card grounding library, departure script, drive-home debrief, day-after page, "real boundary vs internet boundary" framing). P26 Single-Parent Postpartum Planner (postpartum, 634 lines, village-build page, "who do I call for what" table, night-shift solo plan, US financial-aid index, food plan with porch-drop scripts, page for the friends and family, "what about the other parent" page for the families where that applies, weekly check-in template, page-just-for-you at the back). 3,095 lines of brand-voiced content. Zero AI-tells. Zero medicine names. All 6 PDFs at 105-121KB each.
- **2026-05-20** — **Shipped 6 more products at full quality (P15-P20). Catalog now 19.** P15 Visitor Welcome Packet (postpartum/family, 494 lines, door sign + ground rules + how-to-help list + food-drop menu + kitchen orientation + dog page + visit log + meal-train tracker + partner host role + grandparent script + 'I cannot today' backup + after-the-six-weeks page). P16 Tantrum-in-the-Moment Scripts (early-years, 322 lines, 30 scripts the adult says during a meltdown: 10 for screaming, 10 for hitting/throwing, 10 for going-limp; plus 'what NOT to say' page; plus repair scripts for after). P17 Back-to-Work Pumping Planner (postpartum, 539 lines, pre-return checklist + realistic freezer-stash math + weekly pumping schedule template + supervisor conversation scripts × 6 + 'the pump room is bad' troubleshooting + travel-day plan + caregiver handoff + weekly check-in + 'I'm done' decision page). P18 Toilet Learning Planner (early-years, 524 lines, 12-sign readiness page + gear-decision tree + four-week gentle path + first-three-days log + accident scripts + daycare handoff + grandparent handoff that doesn't shame the way they did it + night phase + regression expectations table + 'I'm more stressed than my kid' page). P19 Sibling Adjustment Pack (family, 508 lines, telling the older one scripts + hospital day plan with the 'arms free at first meeting' detail + first-week script library + during-feeds basket of 20 activities + grandparent-don't-eclipse-the-older-one script + night-shift plan + one-on-one time ritual + page-for-just-the-older-one). P20 Gentle Companion for Pregnancy Loss (pregnancy/YMYL, 713 lines, crisis lines at the top, six permission slips, what-to-say-to-people script library across 8 common scenarios, plain-language physical recovery with zero medication names, three pages-for-the-loss to write or draw on, partner page, page-for-the-people-around-you to print and share, page-for-a-future-pregnancy-whenever-it-comes, anniversary page, what-grief-does-over-time, eight crisis/support hotlines). Total: 3,100 lines of brand-voiced PDF content. Zero AI-tells (no em dashes, no semicolons). Zero medicine names — every reference describes by class or purpose and routes to the provider. All 6 PDFs rendered via Docker pipeline at 98-127KB each. `pdfs/` flat folder auto-updated.
- **2026-05-20** — **Scrubbed all medicine names from existing PDFs (user-imposed safety rule).** Found and replaced 5 brand/generic medication mentions across P06 (csection-recovery), P07 (newborn-survival), P12 (breastfeeding-troubleshooting), P14 (birth-plan-pack): "ibuprofen" ×2, "Tylenol" ×1, "erythromycin" ×1, "pseudoephedrine" ×1. Replacements describe by class or purpose ("over-the-counter pain reliever your provider okays for you", "a fever reducer at home", "Eye ointment", "some cold or allergy medications") and route the decision to the provider. Strengthened Section 4 "Banned phrases (legal/safety)" to explicitly forbid all medicine names brand or generic across all current and future products, including journal copy, marketing, and any future asset. Affected 4 PDFs re-rendered; `pdfs/` flat folder auto-updated via the render.py mirror.
- **2026-05-20** — **Added `pdfs/` flat folder mirror.** Every shipped product's PDF now lives in two places: the canonical `products/Pnn_<slug>/product.pdf` (for the render pipeline) and a flat copy at `pdfs/Pnn_<slug>.pdf` (for easy reach by the human, no nested directory navigation). `scripts/render.py` updated to write the mirror copy automatically on every canonical letter-size render, so new products and re-renders keep `pdfs/` in sync without manual steps. Back-filled all 13 existing PDFs.
- **2026-05-20** — **All 6 new products now have full PDFs rendered.** Authored 2,673 lines of brand-voiced content across P07/P08/P11/P12/P13/P14. P07 Newborn Survival Planner (550 lines, week-by-week through six weeks with feed/diaper log, visitor scripts, '3am google' reference, recovery check-in, pediatrician prep), P08 Pregnancy Week-by-Week (516 lines, every week 6 through 40 with unique angle, trimester reflections, symptom reference, night-before page), P11 Newborn Sleep Log (379 lines, daily template, weekly snapshot, what-we-tried log, four regression pages, nap reset, monthly-is-this-normal, partner handoff), P12 Breastfeeding Troubleshooting (433 lines, YMYL with embedded crisis lines, latch checklist, position library, what-feels-off decision tree, supply reality, pumping companion, combo-feed page, gentle wean, IBCLC handoff), P13 Toddler Big Feelings Cards (297 lines, 40 cards across naming/body/calm-down/reset packs, parent note, kid-who-reads-it-themself page), P14 Birth Plan Pack (498 lines, one-page summary the nurse can read in 8 seconds, comfort menu, partner role, hospital bag list, if-things-change page, first-hour-after). Voice held across all: caring, plain language, specific scenes, no em dashes, no semicolons, no AI-tells. All PDFs rendered via Docker pipeline at 95-130KB each. The 6 new products are now fully shipped at the same quality bar as P01-P09.
- **2026-05-20** — **Catalog scaled from 7 to 13 products.** Added six new product listings: P07 Newborn Survival Planner (postpartum, 40 pages first-six-weeks), P08 Pregnancy Week-by-Week Journal (pregnancy, 80 pages, 2-per-week from week 6-40), P11 Newborn Sleep Log (postpartum, 60 pages tracking), P12 Breastfeeding Troubleshooting Guide (recovery, 28 pages, YMYL), P13 Toddler Big Feelings Cards (early-years, 40 cards ages 2-5), P14 Birth Plan Worksheet Pack (pregnancy, 16 pages). Each got a full brand-voiced `web.md` public listing (~50-80 lines) and a Canva-generated lifestyle thumbnail (sage palette, mostly object-only with contextual hand on P02/P03/P09). `SHIPPED_CODES` in `site/src/lib/cover-image.ts` expanded to 13. Catalog at `/shop` and product detail pages at `/shop/[slug]` both render the new entries with hero images and full listings. **PDF content.md files for the new six are not yet authored** — those products show on the catalog but the Buy button is disabled (no etsyUrl yet); follow-up sessions will write the 300-1000-line per-product PDF bodies and render. Canva design IDs preserved (P07 `DAHKMigkU5U`, P08 `DAHKMrBlWO4`, P11 `DAHKMssGYTg`, P12 `DAHKMjKf2-Q`, P13 `DAHKMnO1hEg`, P14 `DAHKMotcMg0`). Required multiple Canva editing transactions to strip event-flyer text overlays Canva added unprompted; required several re-rolls (P11 came back as an illustration not a photograph, P14 came back as a fitness poster) before getting clean compositions.
- **2026-05-20** — **Bug fix: thumbnails were only visible on the homepage.** The `coverFor` helper was inlined in `index.astro` only, so `/shop` (catalog) and every `/shop/[slug]` (product detail) fell back to jar-glyph placeholders even for shipped products. Extracted `SHIPPED_CODES` + `coverFor` into `site/src/lib/cover-image.ts`. Imported from all three pages. Product detail page now uses the lifestyle photo as the hero image (replaces the cream jar block); falls back to jar when the product isn't yet shipped. Cross-sell cards on detail pages also fixed.
- **2026-05-20** — **Hand variety pass: P01/P04/P05/P06 reworked as object-only still lifes.** First lifestyle pass had a hand in every thumbnail (7 of 7) and two had AI-rendering glitches (P04 had planner text bleeding into the hand; P06 had off-anatomy fingers). Reworked four products as pure object compositions: P01 sage linen with cards orbited by a cream scarf, alphabet block, small plant, stacking pieces; P04 cream surface with playbook + black coffee + men's watch with sage band + fountain pen + eucalyptus; P05 sage linen with cards + vintage analog timer (telling the 30-day story) + 5 muted pencils + wooden blocks + succulent + paper crane; P06 single intimate bedside vignette with planner + tiny vase holding sage posy + glass of water + cream throw + soft curtain, low-angle with depth-of-field. Kept the three contextual hands: P02 (doorbell push is the story), P03 (the writing gesture, user-approved), P09 (journal-writing intimacy). Set now reads as editorial variety not template-fatigue: 4 different surfaces (sage linen × 2, cream/oak × 1, white linen bedside × 1), 3 framings (top-down × 3, low-angle vignette × 1, bedside × 2, door × 1), distinct props per product. P04 required Canva editing transaction to strip 5 webinar-flyer text overlays Canva added (Canva is unreliable about respecting "no text" instructions in prompts). P06 required a second generation pass with explicit "single photograph, not a collage, not a poster" language because Canva's first attempt returned a 4-photo collage with a typography card.
- **2026-05-20** — **Website product thumbnails redone as Canva lifestyle photos (pure photo, no overlay).** Third attempt at the thumbnail surface, this one keeps. Each of the 7 shipped products now has a distinct sage/cream cool-toned lifestyle photograph showing the product in use with real objects + a hand: P01 cards-fanned + baby hand + spoon/grain-bowl, P02 cream door + hand at mailbox + sage "Resting" sign, P03 planner + hand-with-pen + sage mug + eucalyptus on sage linen, P04 planner + hand resting + checklist + sage mug + eucalyptus, P05 cards + child hand + succulent + wooden blocks on sage linen, P06 planner + hand on white bed + slippers + sage tea mug, P09 journal + hand writing + glasses + vase with stem. Generated via Canva `instagram_post` (1080×1350 → resized 800×1000 JPG q85 ~80KB each). No text overlay on the photos — `ProductCard.astro` already shows the tagline + price + product code below, so overlay was redundant and competed at thumbnail size. `coverFor` helper in `site/src/pages/index.astro` simplified to a single `SHIPPED_CODES` set mapping to `/products/Pnn.jpg`. Old PDF-cover PNGs removed from `site/public/products/`. Canva design IDs preserved for future edits (P01 `DAHKML9-cCI`, P02 `DAHKMNULKq8`, P03 `DAHKMGXaFZ0`, P04 `DAHKMI4c9WQ`, P05 `DAHKMAiaWu8`, P06 `DAHKMAdswHo`, P09 `DAHKMJWqjb8`). Raw 1080×1350 originals preserved at `marketing/mockups/raw/Pnn_final.png` for other surfaces (Pinterest, IG). Contact sheet at `marketing/mockups/contact_sheet.jpg`.
- **2026-05-20** — **Reverted website product thumbnails back to PDF cover renders.** The Canva lifestyle mockups had heavy dark-brown text-overlay bands (from the Pinterest-pin layout) that clashed with the forest-green site background — dark-on-dark, the opposite of the brand's calm subtle aesthetic. The PDF cover renders (sage-on-cream paper) sit on the dark green much more harmoniously: they read as a lit, calm paper square, not a heavy block. Canva mockups preserved at `marketing/mockups/raw/Pnn.png` for Pinterest pin reuse where dark-warm-on-dark-warm context works.
- **2026-05-20** — **Website product thumbnails switched from PDF cover renders to Canva lifestyle mockups.** Separation of concerns established: the PDF cover (`products/Pnn/product.pdf` page 1) is the *canonical product* — what the buyer downloads. The *website thumbnail* (`site/public/products/Pnn.png`) is a marketing surface — wooden-table flat-lay mockups generated via Canva `pinterest_pin` (style A from the comparison), exported, downloaded, resized to 600px wide. Six products (P01, P02, P04, P05, P06, P09) use Canva lifestyle mockups; **P03 falls back to its PDF cover render** because Canva couldn't produce a single-photo composition on the planner (three regen attempts returned a 4-photo collage, a pure-typography card, and an off-brand pink-and-green photo). Raw Canva exports preserved at `marketing/mockups/raw/Pnn.png` for Pinterest pin reuse. Tradeoff: Canva mockups have invented book-cover text (close to the brand vibe but not literally the Soothemade brand mark) and Pinterest-style text overlays (e.g. "SAYING NO SCRIPT PACK" at top, "Perfect for professionals" at bottom). Acceptable for a website marketing thumbnail; the buyer arrives on the product detail page and downloads the brand-accurate PDF. *(Reverted same day — see entry above.)*
- **2026-05-20** — **Wired PDF cover renders into the website as product images.** Each shipped product's cover page (1) rendered as a 110-DPI PNG into `site/public/products/P0n.png` (~75-100KB each). `ProductCard.astro` gained an optional `coverImage` prop — when provided, the card frame displays the cover image full-bleed instead of the jar-glyph + label. `index.astro` derives the coverImage path from product code for the 7 shipped products (P01-P06, P09); unshipped products (e.g. P10) fall back to the existing jar-glyph design. `ProductGrid.astro` interface + passthrough updated. Result: homepage catalog shows actual product covers in place of placeholder jars. *(Superseded by the Canva-mockup thumbnail change above for the marketing surface; the wiring still applies.)*
- **2026-05-20** — **Bulk-rendered all 7 products** with the locked sage-on-cream template. Per-product fixes during audit: P02 `❤️`→`♥` (2 instances), P04 `❌`→`✗` (4 instances). P01 `⚠` (81 instances) confirmed to render as a small filled triangle via DejaVu fallback — acceptable. P03/P05/P06/P09 `☐` checkboxes render as small open squares. All 10+1 design rules satisfied across all 7 PDFs.
- **2026-05-20** — Added **known-bad emoji + safe replacements** table to Design rule #7. Documents the codepoint substitutions verified to render in the Docker font stack.
- **2026-05-20** — Added **no-doubled-divider rule** (Design rule #11). Removed redundant `─────` lines at the very top and very bottom of P03's daily-page code block — the `pre` box border was already providing that horizontal line. Doubled lines no more.
- **2026-05-20** — Added **symbol-discipline rule** (Design rule #7). Emoji codepoints (🙂😐🌧 etc.) render as tofu in our font stack; banned from product content. Allowed symbols: `○` (circle-one options), `☐` (checkboxes), `·`, `–`. P03 line 180 emoji rating row replaced with `○` circles.
- **2026-05-20** — **PDF page background shifted from cream to light sage** `#EAEEE2`. `--bg`, `--bg-warm`, and `@page background` all updated; `--accent-3` shifted from wheat `#D4A574` to muted sage `#A8B894` so box outlines and dividers stay in the sage family. Whole PDF now reads as a single sage-on-sage piece (cover/body/colophon paper, box interiors, outlines, dividers, emphasis — all sage-spectrum on charcoal text).
- **2026-05-20** — Codified **PDF design rules** (Section 10, subsection "PDF design rules"). Ten rules covering page integrity, hierarchy, section breaks, colour and type discipline, AI-tell punctuation, render reproducibility. Future renders must satisfy all of them.
- **2026-05-20** — `hr:has(+ h2)` now hidden — eliminates the orphaned-divider-on-its-own-page failure mode at section breaks.
- **2026-05-20** — Drop cap colour changed from accent to `var(--text)` (charcoal). Restores hierarchy: h2 carries the accent above, drop cap stays neutral so paragraphs don't strobe.
- **2026-05-20** — h3 colour changed from `var(--accent-2)` (sage) to `var(--text)` (charcoal italic). With `--accent` and `--accent-2` both at sage, h2 and h3 had collapsed to the same colour; this restores hierarchy.
- **2026-05-20** — `--accent` switched to **sage `#8C9B7A`** (was terracotta `#B4654A`, briefly forest `#3B6B5A`). Sage matches the site's forest-theme sage and removes the warm-orange AI-mill smell.
- **2026-05-20** — `render.py` gained an `--output` flag (single-product mode) so preview renders can bypass a locked canonical `product.pdf`.
- **2026-05-20** — New helper `scripts/color_preview.py` — temporarily swaps `--accent` to each of a few candidate colours, renders + converts to PNG, restores original CSS. Useful for visual side-by-side colour decisions.
- **2026-05-20** — `strong` switched from Inter bold to Fraunces semibold. Labels like "Day N:" stop reading as utility/sans-serif and become hand-set-typography.
- **2026-05-20** — Colophon URL no longer rendered in ALL CAPS (removed `text-transform: uppercase`).
- **2026-05-20** — Orphan prevention extended: `p:has(+ blockquote)` and `p:has(strong:only-child)` now also carry `page-break-after: avoid`. Combined with existing `p:has(+ pre)`, label paragraphs stay with their visual partner.
- **2026-05-20** — Create AS_BUILT.md (initial). Comprehensive as-built record of brand, voice, content rules, site, PDF pipeline, deployment, Canva integration, workflow. Owner directive: update with every structural commit.
- **2026-05-20** — h2 section headers in product PDFs switched from Fraunces 22pt to Caveat 34pt. P09 re-rendered; P01–P06 pending.
- **2026-05-20** — `@page` background painted cream `#F5EFE6` so the entire PDF page (incl. margins) reads as one continuous surface. Margins reverted to 0.85in.
- **2026-05-20** — Footer URL fixed from `soothemade.com/notes` to `notes.soothemade.com`.
- **2026-05-20** — All em dashes + semicolons scrubbed from `products/*/content.md` + `web.md` (416 replacements). New `scripts/scrub_ai_punctuation.py`. Template em dashes also cleaned.
- **2026-05-20** — Caveat applied to product cover title + `@bottom-center` footer mark.
- **2026-05-20** — Caveat applied to "Soothemade" wordmark in site Nav + Footer (`var(--font-script)`).
- **2026-05-19** — Brand sprig + favicon wired into Astro site (Nav, Footer, BaseLayout). `brand/brand-sprig.svg` created. `site/public/favicon.svg` created with `prefers-color-scheme`.
- **2026-05-19** — Cloudflare Git-integration auto-deploy wired up. Push to `main` now auto-builds + deploys via CF dashboard config.
- **2026-05-19** — Three brand mark variants added (`brand-on-dark.svg`, `brand-mono-dark.svg`, `brand-mono-cream.svg`) + variant preview at `design/brand-variants.html`. All uploaded to Canva.
- **2026-05-19** — `brand/brand.svg` adopted as canonical brand mark. Previous `brand/soothemade_06_sprig.svg` removed. Uploaded to Canva as `MAHKIAtzV9Q`.
- *(Earlier commits not back-filled; see `git log`.)*

---

## 19. CF bindings & data layer

The Worker has five bindings beyond the `ASSETS` static fetcher. All are declared in `site/wrangler.toml` and typed via `site/worker-configuration.d.ts` (regenerate with `npx wrangler types`). Routes access them through `Astro.locals.runtime.env.*`.

### Bindings

| Binding | Type | Resource | Purpose |
|---|---|---|---|
| `DB` | D1 | `soothemade-notes` (`ddbaf6ed-f1e1-49a3-b88d-609a448daae1`, APAC) | Subscribers, orders, download tokens, journal view counts, contact messages |
| `FILES` | R2 | `soothemade-notes-files` | Product PDFs at `products/Pnn.pdf`, future image assets |
| `CACHE` | KV | `soothemade-notes-CACHE` (`d370c098ad334796aa4e461bcaf12c1f`) | Rate-limit counters, ephemeral state |
| `VECTORIZE` | Vectorize | `soothemade-products` (384-dim, cosine) | Catalog embeddings for semantic search |
| `AI` | Workers AI | n/a | Embedding generation via `@cf/baai/bge-small-en-v1.5`. Internal/discovery only — never customer-facing copy |

### Endpoints

| Route | Method | Behavior |
|---|---|---|
| `/api/subscribe` | POST | Rate-limit (5/hr/IP), upsert email into `subscribers` |
| `/api/contact` | POST | Rate-limit (3/hr/IP), insert into `contact_messages` |
| `/api/search?q=` | GET | Rate-limit (30/min/IP), embed query, top-6 Vectorize match, return code+title+slug+summary+score |
| `/files/[code].pdf` | GET | Stream `products/[code].pdf` from R2. Accepts `P09` or `P09.pdf` |
| `/api/journal/[slug]/view` | POST | UPSERT increment on `journal_views(slug, day)` |
| `/api/admin/reindex` | POST | Bearer-secret-gated. Embeds payloads + upserts to Vectorize. Used only by the indexer script |

### D1 schema

Defined in `site/db/migrations/0001_init.sql`. Apply remote with:

```bash
cd site
npx wrangler d1 migrations apply soothemade-notes --remote
```

For local development against `wrangler dev`, swap `--remote` for `--local`.

Tables: `subscribers`, `orders`, `download_tokens`, `journal_views`, `contact_messages`. See the migration file for column-level detail. The `orders` table uses `UNIQUE(platform, external_id)` so webhook ingestion is idempotent.

### Secrets

The `/api/admin/reindex` route checks `Authorization: Bearer ${REINDEX_SECRET}`. Set the secret once via:

```bash
cd site
npx wrangler secret put REINDEX_SECRET
```

The secret is per-worker, encrypted at rest in CF. It does NOT live in git.

### Indexing the catalog into Vectorize

The catalog must be embedded once and re-embedded whenever product summaries change. The flow:

1. Local Node script reads each `products/Pnn_*/web.md` frontmatter (title, tagline, summary, buyer, category).
2. Posts the array to `/api/admin/reindex` on the deployed worker.
3. The worker embeds each text via Workers AI (`@cf/baai/bge-small-en-v1.5`) and upserts vectors with metadata into Vectorize.

Run:

```bash
REINDEX_SECRET=<value> node scripts/index_products_vectorize.mjs
```

Override target with `REINDEX_URL=https://soothemade-notes.iamvashisht1.workers.dev` for staging vs. prod.

### Migrating new PDFs into R2

When `pdfs/` gains a new product, run:

```bash
bash scripts/upload_pdfs_to_r2.sh
```

R2 puts overwrite by key, so re-running is safe. Each PDF lands at `products/Pnn.pdf` in the bucket, served by `/files/Pnn.pdf`.

### Brand-voice constraint on Workers AI

Workers AI is wired up but its output **never reaches the customer as copy**. Allowed:

- Embedding queries + catalog text for semantic search (output: 384 floats, never shown)
- Future: internal classification of inbound contact messages (output: a category label, never shown)
- Future: internal-only catalog analysis scripts

Forbidden:

- Generated product descriptions, summaries, journal posts, email body
- Generated marketing copy of any kind
- Any text rendered to a customer surface

This boundary is the brand promise's defense against the AI-mill aesthetic. If we cross it later, it has to be an explicit owner decision, documented here.

### Resource cost reality

All four resources sit on generous free tiers:

- D1: 5 GB storage + 25M reads/day free
- R2: 10 GB storage + 1M Class A ops/mo free, zero egress to Workers
- KV: 1 GB storage + 100k reads/day + 1k writes/day free
- Vectorize: 30M queried vector-dimensions/mo free
- Workers AI: 10k neurons/day free (one search ≈ 1-3 neurons)

Catalog scale (55 products, ~10 reads/day per page) is well under all caps. Re-evaluate when traffic crosses 5k DAU.


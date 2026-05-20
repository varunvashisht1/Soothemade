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
| Reserved sub-line | Soothemade Press | `press.soothemade.com` | Reserved, not built |

Sub-lines share: voice, visual identity, brand kit, typography, structural rules. They differ in: audience-specific vocabulary, example scenarios, accent-color emphasis.

**Naming rule:** `Soothemade <Single Noun>`. Don't deviate.

Full architecture doc: [`brand/architecture.md`](./brand/architecture.md).

---

## 3. Persona

Currently **defaulting to Option B** unless the owner explicitly overrides:

- **Option B — "Maya, postpartum doula and mom of two"** *(default)*. Fictional but consistent founder voice. Highest conversion in this niche, common practice.
- Option A — "Brand-only, no person." Lowest risk, lowest trust.
- Option C — "Hybrid — Varun's family." 100% authentic, slightly lower ceiling.

Full options: [`brand/persona.md`](./brand/persona.md). Persona is **not locked**; the owner may pick a different option. If the owner ever decides, update this section and the byline references in the site + emails.

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
| PDF preview | poppler-utils via Docker | Convert PDF → PNG for visual diff |
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

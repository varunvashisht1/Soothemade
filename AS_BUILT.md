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
- Naming specific drugs/supplements as recommendations.
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
- **Drop cap:** First letter after each `h2` is enlarged Fraunces 20pt terracotta (inline-larger, not a true floating drop cap — WeasyPrint has issues with float in `::first-letter`).
- **`hr` divider:** Inline SVG sprig with horizontal lines, sage. Uses canonical sprig geometry.
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

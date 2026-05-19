# notes.soothemade.com

Astro site, deployed to **Cloudflare Workers** with Static Assets.

## Quick start

```bash
cd site
npm install
npm run dev          # http://localhost:4321
```

## Deploy

```bash
npm run deploy       # builds Astro then `wrangler deploy`
```

First deploy needs a Cloudflare account login: `npx wrangler login`. Custom domain (`notes.soothemade.com`) is wired via Cloudflare → Workers → Custom Domains after the first deploy.

## Theme system

Three preset palettes live in `src/styles/themes/`:

| Preset | File | Vibe |
|---|---|---|
| `forest` (default) | `forest.css` | Deep forest green, cream tincture jars |
| `charcoal` | `charcoal.css` | Near-black, brighter sage, softer terracotta |
| `mossy` | `mossy.css` | Warm dark with brown undertones |

Active theme is set in `src/data/theme.json`:

```json
{
  "preset": "forest",
  "overrides": {
    "--accent": "#e2a78f"
  }
}
```

- **Stock theme**: set `preset` to `forest` / `charcoal` / `mossy`. Leave `overrides` empty.
- **Hybrid**: set `preset` to any base, then override individual CSS variables in `overrides`.
- **Custom**: set `preset` to `custom` to start from Deep Forest and override everything.

The CMS at `/admin/` exposes this as a UI — no JSON editing needed.

## CMS

Decap CMS, git-backed, runs at `/admin/`. Edits commit to GitHub directly.

Default backend is GitHub OAuth via Netlify Identity. To self-host the OAuth proxy on Cloudflare Workers (recommended), see the follow-up milestone — `git-gateway-cloudflare` isn't wired up yet.

For local-only editing during development:

```bash
npx decap-server &
npm run dev
# Visit http://localhost:4321/admin and pick "Work with Test Backend"
```

## Project shape

```
site/
├── astro.config.mjs    # Astro + @astrojs/cloudflare adapter
├── wrangler.toml       # Cloudflare Workers config (bindings TBD)
├── package.json
├── public/
│   └── admin/          # Decap CMS shell + config
└── src/
    ├── components/     # Astro components (Nav, Hero, ProductGrid, …)
    ├── data/
    │   ├── theme.json  # ← THE theme picker (CMS-editable)
    │   └── featured-products.ts  # temp until content collections wired
    ├── layouts/        # BaseLayout
    ├── lib/            # theme loader
    ├── pages/          # routes
    └── styles/         # tokens.css + themes/
```

## What's wired vs. what's pending

| Feature | Status |
|---|---|
| Homepage with full Variant A layout | ✅ |
| Theme system (3 presets + hybrid overrides) | ✅ |
| Decap CMS theme picker | ✅ (UI ready; auth wiring pending) |
| Universal sub-line theme architecture | ⏳ (Notes only for now; `master` sub-line config to come) |
| Astro Content Collections for products + journal | ⏳ |
| `/shop` listing + `/shop/[slug]` detail | ⏳ |
| `/journal` listing + `/journal/[slug]` detail | ⏳ |
| Email capture → Turso → Resend | ⏳ |
| Lead magnet / freebie delivery | ⏳ |
| Stripe direct checkout (Phase 1) | ⏳ |
| R2 signed-download URLs | ⏳ |
| Pinterest Rich Pins meta on product pages | ⏳ |
| Watermarked PDF generation | ⏳ |
| Nightly DB backups → R2 | ⏳ |

# Website Audit — notes.soothemade.com

*How it was audited: this sandboxed environment's headless browser cannot load
external resources (the Google Fonts `<link>` never resolves), so pixel
screenshots time out and are not available here. Instead this audit reads the
rendered DOM (accessibility tree) plus the full component/page/CSS source and
the build output. For a design-system audit that is often more precise than a
screenshot anyway — it measures the actual markup, styles, and structure rather
than one viewport's picture. Where a finding needs a human eye (final color
contrast, emotional landing of the hero), it is marked "verify visually".*

---

## How it looks (the qualitative read)

The design system is genuinely strong and on-brand. It is the "premium
gradient-tile" treatment from the AS_BUILT history: each section is its own dark
gradient panel (warm-black, umber, deep-moss) with cream-on-dark type and soft
radial accent blooms in terracotta and sage. Typography is editorial and
deliberate — Fraunces for serif display, Caveat for the script wordmark, Inter
for the small-caps labels, with a real type-scale and spacing-token system.
Product cards that lack a photo fall back to a tasteful "apothecary label"
(paper-at-dusk gradient with a botanical motif). The homepage flow is calm and
well-sequenced: hero → categories → 8 featured → manifesto → journal → newsletter
→ footer.

In short: it looks like a real brand, not a template. The problems below are
almost all **functional and discoverability** issues, not taste issues.

---

## Findings, ranked by impact

### 🔴 1. Nothing on the site is buyable. Every "Buy" button is a dead link.

`grep etsyUrl|gumroadUrl` across all 69 products = **0 matches**. In
`shop/[slug].astro`, when there is no URL the primary CTA renders as:

```html
<a class="btn btn-primary" href="#hold" aria-disabled="true">Buy on Etsy · $14</a>
```

So a visitor who wants to buy clicks a full-looking "Buy on Etsy · $14" button
and **nothing happens** (it jumps to a non-existent `#hold`). This is the whole
ballgame: the catalog converts at 0% no matter how it looks. There is also a
vestigial `cart.astro` and a 0-product cart concept that goes nowhere.

This is partly consistent with the distribution plan (selling happens on Etsy,
the site is the brand surface) — but a dead button is worse than no button.

**Fix (pick one, now):**
- **(a)** When `etsyUrl` is set, the button already works — so the real fix is
  *listing on Etsy and pasting the URLs in*. That is the launch step.
- **(b)** Until then, the no-URL state should not look like a live Buy button.
  Make it a **"Coming soon — get notified"** capture that drops the email into
  the existing `/api/subscribe` (tagged with the product code). That turns every
  curious pre-launch visitor into a launch-day customer instead of a bounce.

### 🔴 2. The Open Graph / social share image is missing.

`BaseLayout.astro` sets `og:image` and `twitter:image` to `/og-default.png`, but
**that file does not exist** in `public/`. Every time the site is shared on
Pinterest, Facebook, iMessage, WhatsApp, or X, the preview shows a broken or
blank image. For a brand whose entire growth plan is **Pinterest-led**, this is a
silent, serious leak — your shares look broken in exactly the channel you are
betting on.

**Fix:** add a branded 1200×630 `public/og-default.png` (sage paper, wordmark,
tagline). Ideally also a per-product OG image, but one good default first.

### 🔴 3. No `robots.txt`, no `sitemap.xml`.

Neither exists. Google and Pinterest crawlers have no sitemap to read, and 69
product pages + journal posts crawl slower and less completely. Astro has a
first-party `@astrojs/sitemap` integration that is not installed.

**Fix:** install `@astrojs/sitemap`, add a `robots.txt` that points to the
sitemap. ~15 minutes, real SEO coverage.

### 🟠 4. The 14 new bundles are invisible on the site.

The bundles (K01–K14) were added to the catalog, so they appear scattered in the
`/shop` grid mixed among 55 singles — but there is **no "Bundles" filter chip**
(the category filter only has the 7 product categories) and **nothing surfaces
them on the homepage**. The single biggest average-order-value lever is sitting
where no one will find it. A bundle in the "pregnancy" filter looks like just
another single.

**Fix:** add a "Bundles" / "Sets" chip to the `/shop` filter, and a "Save with a
set" row on the homepage. Give bundles a visible "$X, save Y%" treatment.

### 🟠 5. Half the catalog shows a placeholder instead of a photo.

31 product photos exist (`public/products/P01–P33, P44.jpg`). The other ~22
singles (P34–P56) **and all 14 bundles** have no image, so ~37 of 69 cards render
the generic "apothecary label" placeholder. The grid reads half-photographed,
half-blank — which undercuts the premium feel and makes the newer (often
highest-value) products look like stubs.

**Fix:** this is the deferred thumbnail batch. Prioritize photos for the hero
products and the bundles. Until then, the placeholder is tasteful enough to
ship, but it is a visible gap.

### 🟠 6. The disabled Buy button is an accessibility trap.

`<a href="#hold" aria-disabled="true">` is still keyboard-focusable and
clickable — `aria-disabled` does not actually disable an anchor. A screen-reader
or keyboard user can tab to it, activate it, and land nowhere. (Folds into fix #1.)

### 🟡 7. The homepage and catalog are server-rendered on every request.

`astro.config.mjs` sets `output: 'server'`; only `shop/[slug]` opts into
`prerender = true`. So the homepage and `/shop` run the Cloudflare Worker on
every hit instead of serving static HTML. For a catalog that changes rarely,
that is unnecessary latency and Worker cost.

**Fix:** add `export const prerender = true` to `index.astro` and
`shop/index.astro` (move the category filter to client-side or query-less), or
switch to `output: 'static'` with the few API routes kept as server endpoints.

### 🟡 8. No JSON-LD structured data.

Product pages have good `<meta>` / OG tags but no `Product` schema (price,
availability, name, image). Structured data is what gets you rich results and
price chips in Google and feeds Pinterest Rich Pins correctly. The
`pinterest-rich-pin` meta is present but undermined by the missing OG image and
absent structured data.

**Fix:** add a `Product` JSON-LD block to `shop/[slug].astro` and an
`ItemList` to `/shop`.

### 🟡 9. Color contrast on the faint text tiers — verify visually.

The dark theme uses cream-on-dark with tiers `--n-paper-soft` (~62%),
`--n-paper-dim`, and `--n-paper-faint` (~42% opacity). Faint cream text on a
mid-tone gradient is a likely **WCAG AA fail** (needs 4.5:1 for body, 3:1 for
large). The hero body, the italic taglines, and the card `meta-row` are the spots
to check.

**Fix:** verify the dim/faint tiers against their actual backgrounds; lift
opacity where they fall under 4.5:1.

### 🟢 10. Smaller polish

- **No skip-to-content link** for keyboard users (minor a11y).
- **Fonts:** 3 families with many weights, render-blocking (mitigated by
  `display=swap`). Self-hosting or subsetting would speed first paint. Minor.
- **Search** is a genuine differentiator (semantic `/api/search`) but depends on
  the Worker + populated Vectorize index, so it silently does nothing on a static
  preview. Make sure the index stays reindexed as the catalog grows (it just grew
  by 14 bundles + 55 retitles — **the search index should be re-run** so the new
  titles/bundles are findable).

---

## What's already good (leave it)

- The design system, palette, and typography. It looks like a brand.
- SEO fundamentals: per-page `<title>`/description, canonical, OG/Twitter tags.
- Semantic structure, `alt` text on product images, eager hero / lazy card image
  loading.
- The calm homepage IA and the apothecary-label placeholder.
- Page coverage: about, contact, policy, press, freebies, wholesale, journal.

---

## Fix-first sequence (by revenue-per-hour)

1. **Make the Buy state real.** Either list on Etsy and paste URLs in (launch), or
   convert the dead button to a "notify me" email capture. Nothing else matters
   until the site can either sell or capture.
2. **Add `og-default.png`.** One file. Unbreaks every Pinterest/social share.
3. **Install sitemap + robots.txt.** 15 minutes of SEO coverage.
4. **Surface the bundles.** Filter chip + homepage row. The AOV lever.
5. **Re-run the search index** so the new titles + bundles are findable.
6. **Prerender homepage + shop** (or go static). Speed + cost.
7. **Add Product JSON-LD.** Rich results + Pinterest Rich Pins.
8. **Verify contrast** on the faint text tiers; add a skip link.
9. **Photograph** the hero products and bundles (the thumbnail batch).

Items 1–5 are the launch-blockers and the cheap, high-leverage wins. 6–9 are
quality passes that can follow.

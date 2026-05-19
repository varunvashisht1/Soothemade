# Weekly Publishing Checklist

> 15–20 minutes per week. Do on Monday or whichever day works.

## The checklist

### Open the week's folder

1. Open `publishing/calendar.md` — find this week's row.
2. Open the product folder for this week's launch (e.g., `products/P02_saying-no-scripts/`).

### Pre-publish QA (~5 min)

- [ ] `content.md` reads okay — no obvious typos in the first 2 pages
- [ ] `product.pdf` rendered (run `python scripts/render.py products/PXX_...` if not)
- [ ] Mockup images exist in product folder OR on Canva (link in `source/cover.canva-link.txt`)
- [ ] Brand-safe check: no drop shadows, no gradients, palette correct
- [ ] Medical disclaimer present (if YMYL-adjacent)

### Etsy publish (~5 min)

- [ ] Go to https://www.etsy.com/your/shops/me/tools/listings
- [ ] "Add a new listing"
- [ ] Paste title from `etsy-listing.md`
- [ ] Paste description (copy block)
- [ ] Paste all 13 tags
- [ ] Set price (default: as in listing file)
- [ ] Set category: Paper & Party Supplies → Paper → Stationery
- [ ] Upload 5–10 photos (per `mockup-spec.md`)
- [ ] Upload digital file (the `product.pdf`)
- [ ] Section: assign to "Postpartum & Recovery" / "Sensory Play" / etc.
- [ ] Auto-renew: ON
- [ ] Publish

### Gumroad publish (~3 min)

- [ ] Go to https://gumroad.com/products
- [ ] "New product" → Digital product
- [ ] Name, subtitle, price from `gumroad-sales-page.md` (or `marketing.md`)
- [ ] Paste long-form sales body
- [ ] Upload product PDF
- [ ] Upload cover image
- [ ] Add tags
- [ ] Set up after-purchase email (from `marketing.md`)
- [ ] Publish

### Blog post (~5 min)

- [ ] If pillar blog post for this week is in `content/` folder, copy to your Jekyll site
- [ ] Replace any [shop link] placeholders with real Etsy + Gumroad URLs
- [ ] Push the Jekyll repo — GitHub Pages auto-deploys
- [ ] Test the post links

### Pinterest (~3 min)

- [ ] Open Canva → make this week's pins from `pinterest-pins.md` or `marketing.md` specs
- [ ] Upload to Pinterest (manually if API not yet approved)
- [ ] Or queue via Pinterest's native scheduler
- [ ] Add UTM tags to pin URLs: `?utm_source=pinterest&utm_campaign=PXX_launch`

### Log it (~2 min)

- [ ] Add a row to `publishing/metrics.md`:
  - Date
  - Product code
  - Etsy listing URL
  - Gumroad URL
  - Blog post URL
  - Notes (what went smoothly / what didn't)

### Optional but recommended (~5 min)

- [ ] Reply to any Etsy messages from last week
- [ ] Check Pinterest analytics for any pin that's gaining traction
- [ ] Skim email list — write a 2-sentence reply to anyone who responded

## Pro-plan tasks (only when needed)

- New listing variant: `toolkit/prompts/generate-variant.md`
- SEO refresh: `toolkit/prompts/etsy-seo-refresh.md`
- Pin copy: `toolkit/prompts/pinterest-captions.md`
- Customer message: `toolkit/customer-service/*.md` (look up the right template)
- Negative review response: `toolkit/customer-service/negative-review.md`

## If you fall behind

You can skip a week entirely. Catalog is designed for undated drip.

You can launch 2 in a week. No penalty.

You can skip pin batches. Pinterest will still show your stuff in their algorithm even with thin posting.

The schedule is a default — not a contract.

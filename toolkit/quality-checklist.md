# Pre-Publish Quality Checklist

> 10 minutes. Run on every product before pushing to Etsy / Gumroad. No Claude usage required.

## Content

- [ ] Title matches `etsy-listing.md` title field exactly (no surprise SEO change at publish time)
- [ ] First 200 words of content.md read in brand voice (specific opening, no clichés, no "mama"/"journey"/"blessed")
- [ ] Disclaimer present at footer if YMYL-adjacent (any product touching: postpartum mental health, c-section, feeding, sleep, infant safety)
- [ ] No specific medical / legal / financial advice in body (planning prompts only)
- [ ] Persona signoff matches `brand/persona.md` choice
- [ ] Hotline number current (US Maternal Mental Health: 1-833-852-6262)
- [ ] No competitor links accidentally left in
- [ ] No "[BRACKETS]" placeholder text remaining

## Visual

- [ ] PDF rendered without broken layout (run `python scripts/render.py` and visually scan)
- [ ] Page numbers showing
- [ ] Brand palette correct (warm ivory background, terracotta accents)
- [ ] Typography correct (Fraunces for headings, Inter for body)
- [ ] No drop shadows anywhere
- [ ] No gradients anywhere
- [ ] No emoji decoration unless intentional
- [ ] Mockup hero image follows visual identity (no millennial-pink, no AI-image style)

## Mockup / Etsy photos

- [ ] 5–10 photos prepared
- [ ] Hero photo passes the 1-second thumbnail test (legible at small size on phone)
- [ ] At least one sample-page screenshot included
- [ ] At least one use-case scene included
- [ ] iPad mockup included (for digital-format signal)
- [ ] All photos at 2000×2000 minimum

## Listing copy

- [ ] Etsy title under 140 chars, exact tags from listing file
- [ ] 13 tags filled in (don't waste slots)
- [ ] Section assigned in Etsy shop
- [ ] Price matches strategy file
- [ ] Auto-renew ON
- [ ] Materials/attributes complete (file type, pages, US Letter, instant download)

## Gumroad

- [ ] Sales page body pasted (long-form)
- [ ] Cover image uploaded (square 1:1)
- [ ] PDF uploaded
- [ ] After-purchase email set up
- [ ] PWYW min price set (if using)
- [ ] Tags filled in

## Pinterest

- [ ] 5 pins generated per `marketing.md`
- [ ] UTM tags added (`?utm_source=pinterest&utm_campaign=PXX_launch`)
- [ ] Pin titles + descriptions filled in
- [ ] Schedule at least pin #1 to go live within 24 hrs of listing

## Cross-link

- [ ] Internal-linked from at least 1 blog post in `content/`
- [ ] Cross-sells configured on Gumroad
- [ ] Added to bundle if applicable (see `research/06-problem-product-matrix/top-30.md`)

## Tracking

- [ ] Added to `publishing/metrics.md` (date, code, URLs, baseline state)
- [ ] Marked done in product's `README.md`
- [ ] Marked done in this week's row in `publishing/calendar.md`

## Final sanity check

Read the listing as if you were the buyer:
- [ ] Would I buy this? (If no — fix it before publishing)
- [ ] Would I trust this seller? (If no — what's missing?)
- [ ] Does this match the Pinterest pin promise? (If no — the pin or the product is wrong)

If any answer is "no" — pause publishing, fix the gap, then publish.

A delayed launch with the right product beats a fast launch with the wrong one.

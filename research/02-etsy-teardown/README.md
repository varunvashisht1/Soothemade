# 02 — Etsy Top-Seller Teardown

## Goal

Reverse-engineer the digital baby/parent products that are actually selling. Find the gaps.

## Target list

Top 100 grossing baby/parent digital products on Etsy. Categories to cover:

- Pregnancy planners / week-by-week journals
- Hospital bag & birth plan templates
- Baby trackers (feed, sleep, diaper)
- Newborn schedules
- Milestone cards & first-year prints
- Baby shower games & invites
- Postpartum recovery planners
- Nursery checklists & registry guides
- Maternity leave templates
- Baby name guides
- Toddler chore charts / mom scripts
- Baby-led weaning guides
- Pregnancy affirmation cards

## What I'm extracting per listing

| Field | Why |
|---|---|
| Title (full) | Etsy SEO patterns |
| All 13 tags | Tag pool |
| Price | Pricing benchmark |
| # sales (approx via reviews × ~5–10x) | Demand signal |
| # reviews | Trust signal |
| Top review themes (positive) | What customers actually value |
| Top review themes (negative) | Gaps to exploit |
| Shop age | Newbie boost / mature shop pattern |
| # photos | Listing-richness benchmark |
| Mockup style | Visual conventions to match or break |
| Description structure | Sales-page template patterns |

## Output

- `top-listings.md` — table of top 100 with all fields
- `pricing.md` — pricing distribution by category, sweet-spot pricing
- `title-formulas.md` — extracted Etsy title patterns
- `tag-pool.md` — most-used tags per category, plus underused-but-high-intent tags
- `gap-analysis.md` — categories where top sellers have weak listings (= opportunities)
- `review-mining.md` — what buyers complain about (= product features to add)

## Method note

Etsy public search pages are scraped via WebFetch. No login, no API key required. All data from public listings.

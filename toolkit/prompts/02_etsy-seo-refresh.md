# Prompt 02 — Etsy SEO refresh

## Use when

A listing has been live 60–90 days and isn't performing. Or it was performing and tapered off. Etsy SEO benefits from periodic title + tag refreshes.

## Time

5–10 min on Claude Pro

## Prompt (paste into Claude)

```
I'm refreshing the Etsy SEO for one of my digital-products listings.

CURRENT LISTING TITLE:
[Paste current title]

CURRENT 13 TAGS:
[Paste tags as a comma-separated list]

CURRENT PRICE: $[X]

90-DAY PERFORMANCE:
- Views: [X]
- Favorites: [X]
- Sales: [X]
- Click-through rate: [X%]

WHAT THE PRODUCT IS:
[1-paragraph description of product]

WHAT I KNOW IS RISING ON PINTEREST:
[Paste 2-3 relevant rising terms from research/04-pinterest-trends/findings.md
if applicable]

Please analyze and recommend:

1. Whether the title is the bottleneck (low views suggest yes;
   high views + low favorites suggests photos or price)
2. A revised title (~140 chars max) emphasizing 1–2 keywords I should
   be ranking for that aren't currently in the title
3. A revised tag set (13 tags) — keep the top-performing tags, swap
   the bottom 4–5 for more specific or rising terms
4. Whether the price might be a factor (under-priced = looks cheap,
   over-priced = abandons cart) and a recommended action
5. Whether I should keep this listing alive at all, or kill it — give
   a clear recommendation
6. The single sentence I should change in the description to better
   convert clicks
```

## Expected output

A targeted diagnosis, not a full rewrite. Most listings need only 1–2 changes.

## After you run this

1. Update Etsy listing manually (~3 min)
2. Wait 2–3 weeks before judging — Etsy SEO needs time to re-index
3. Log the change in `publishing/metrics.md`

## Decision matrix

| Symptom | Likely cause | Action |
|---|---|---|
| Low views, high CTR if seen | Title isn't ranking | Refresh title + tags |
| High views, low CTR | Photos or thumbnail | New mockup, lead photo |
| High CTR, low conversion | Price or trust | Test $1–2 lower, add review or trust signal |
| All-zero after 90 days | Wrong product-market fit | Kill listing, free up the slot |
| Spike then taper | Pinterest pin fatigue | Refresh pins, not listing |

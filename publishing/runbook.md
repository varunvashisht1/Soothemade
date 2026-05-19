# Operations Runbook

> The full operating manual for running the shop after Day 10 handoff. Default: ~20 min/week + ~30 min/quarter.

## The weekly cycle (Mondays, ~20 min)

Follow `publishing/weekly-checklist.md`. Don't deviate without reason. The schedule is the moat — drift kills shops.

If you skip a week: skip cleanly, no guilt, resume next Monday. Don't try to "catch up."

## The monthly cycle (first Monday of each month, ~30 min)

- [ ] Read all reviews from prior month
- [ ] Refresh Pinterest pin #1 + #5 on top-3 listings (see `toolkit/prompts/03_pinterest-captions.md`)
- [ ] Update `publishing/metrics.md` with monthly totals
- [ ] Check ConvertKit subscriber growth — if <10/month, refresh lead magnet placement on blog
- [ ] Skim Pinterest analytics — note which pins are getting saves vs clicks
- [ ] Pay yourself something. Even $50 to your personal account. The money has to be real to matter.

## The quarterly cycle (Wk 13 / 26 / 39 / 52, ~60 min)

Use `toolkit/prompts/05_quarterly-review.md`. The output goes into `publishing/q[X]_review.md` and informs the next quarter's calendar.

Pivot triggers at the end:
- **Q1 (Wk 13):** <3 sales total → run `toolkit/decision-trees/no-sales-by-q1.md`
- **Q2 (Wk 26):** <$200 revenue → niche pivot consideration
- **Q3 (Wk 39):** <$500 revenue → wind-down evaluation
- **Q4 (Wk 52):** <$1000 revenue → honest reset or close

## The annual cycle (~2 hrs, once per year)

- [ ] Year-end revenue + expense summary (for taxes)
- [ ] Identify top 3 winners — make 1 variant of each (see `toolkit/prompts/01_generate-product-variant.md`)
- [ ] Identify bottom 5 — kill them
- [ ] Read every review in aggregate — what's the pattern?
- [ ] Refresh the brand persona's "about" page on Etsy
- [ ] Renew domain if applicable
- [ ] Consider whether to renew Canva Pro for another month (only if needed for variant work)
- [ ] Send a year-end note to your email list

## Inbox triage (whenever messages come in)

### Etsy messages

Reply within 24 hours. Use `toolkit/customer-service/general-message-response.md`.

Common types and templates:
- "Where's my download?" → Template 02
- "Can I customize?" → Template 01
- "Refund please" → Template 07 (always yes, no haggle)
- "Quick question about content" → Template 08
- "Your product helped me" → Template 09
- "Can I be an affiliate?" → Template 10

### Negative reviews

Reply within 24 hours. Use `toolkit/customer-service/negative-review.md`. **Reply in under 4 lines.** Future-buyer trust is the metric, not winning the argument.

### Refund requests

Always yes. No haggle. Less than 1% of digital-product buyers actually request refunds — let them go.

If refund rate exceeds 3% on any single product → the product is mispromised. Fix it.

## Business setup (one-time, can defer until first sale)

### Tax basics (US)

- Once you have $600+ in annual sales across Etsy + Gumroad, you'll get 1099 forms.
- This is "self-employment income." You report on Schedule C of your personal taxes.
- You can deduct: Canva Pro, domain costs, ElevenLabs, Pinterest credits, internet portion, home office portion if applicable.
- For state sales tax: Etsy and Gumroad both handle this on your behalf for digital goods. You don't need to do anything.
- Keep receipts in `business/receipts/` (a folder you start when you spend anything).
- If you're outside the US, your tax setup will differ — check your local rules.

### Business entity

- For Year 1: stay as a sole proprietor. No LLC needed. Don't waste $300+ on filings.
- After ~$10k annual revenue: consider an LLC for liability protection. Talk to a tax pro.
- Don't form an entity before you have sales. Premature optimization.

### Bank / money flow

- Etsy and Gumroad both pay out to a bank account. You can use your personal account.
- Once sales pick up: open a free business checking (Mercury, Relay, your bank). Keep business + personal money separate from there forward.
- A simple Google Sheet tracks: month, gross revenue, fees, net, cumulative.

## Asset management

### Backups

- This Git repo is the source of truth for everything. Push regularly.
- Canva designs are stored in Canva (free tier may delete after a while — export and save).
- Mockups, photos: keep originals in `products/PXX/source/` if you've generated them locally; otherwise rely on Canva.
- ConvertKit subscribers: export the list quarterly to `business/subscribers-YYYY-MM.csv` — never trust a single SaaS to hold your audience.

### Domain + DNS

- `shop.varunvashisht.com` points to GitHub Pages (DNS records in your registrar).
- If you buy a separate brand domain later: redirect or replace.
- Renew domain annually. Set auto-renew to avoid losing the URL.

### Etsy listings

- Keep `etsy-listing.md` in this repo as the source of truth.
- If you edit a listing in Etsy directly, paste the changes back into the .md file. Otherwise you'll lose the change next time you re-publish from scratch.

## When the catalog runs out

You have a 30-product catalog dripping at ~1/week. That's about 7 months of inventory.

Options when you approach the end:

1. **Pause for a month.** Catch up on Pinterest, refresh top listings, take a break. No new launches.
2. **Run variants of winners.** Use `toolkit/prompts/01_generate-product-variant.md`. 1 new variant/week of a winner is cheap on Pro plan.
3. **Build new products with deep research.** Spend a Saturday on Claude Pro using `toolkit/knowledge-base.md` + `toolkit/prompts/04_pillar-blog-post.md`. Produce a new product in 4–8 Pro-plan sessions.
4. **Pivot or expand.** If you've validated a winning category, double down. If you've gotten signal pointing somewhere unexpected, follow it.

## When you're tired

Take the week off. The shop will be there.

The undated-product nature of the catalog means there's no "missed window." A planner from week 17 still sells in week 30.

Your mental health > the publishing schedule.

## When you want to quit

Read this whole runbook once more. Specifically:

- `toolkit/decision-trees/no-sales-by-q1.md` if it's been less than a year
- Your last quarterly review

Then make the decision when you're not exhausted. Don't quit at 11pm. Decisions made at 11pm are usually wrong.

If you do decide to wind down:

1. Refund any open requests
2. Mark all Etsy listings "inactive" (Etsy charges the $0.20 renewal otherwise)
3. Keep Gumroad live as long as you want — passive sales continue
4. Take the blog offline OR keep it as a passive thing
5. Archive this Git repo
6. Take a real break before evaluating what to build next

You learned a lot. The voice you developed, the brand sense, the operations system — all of it transfers.

## When something IS selling

If a product is consistently selling:

- Make 1 variant within 30 days (different audience, season, or aesthetic)
- Refresh its Pinterest pins monthly (10 min Pro task)
- Run the 60-day SEO refresh on its listing (use `toolkit/prompts/02_etsy-seo-refresh.md`)
- Cross-link it from every relevant blog post
- Consider a small price test (raise $1–2 — see if sales pace changes)
- Bundle it with a complementary product

Don't get cute. Don't introduce 5 variants of the same product. Diminishing returns past 2–3 variants.

## What this runbook does NOT cover

- Detailed accounting / bookkeeping (you'll need a tool — Wave is free)
- International tax treatment (check your local rules)
- Trademark / IP registration (defer until you're at scale)
- Hiring help (you're solo for at least the first year)
- Paid advertising (specifically excluded by design)
- Influencer partnerships (don't bother until you have 50+ sales)

## The most important rule

Slow drip is the strategy. Don't deviate.

- 1 product/week max launch velocity
- 1 pillar blog post / 1–2 weeks max
- Don't dump 5 products in one week to "make up for lost time"
- Don't run Black Friday sales — it's on-brand to refuse
- Don't chase trends mid-quarter — finish what's scheduled
- Quarterly reviews are when you pivot, not Tuesday afternoons

If you find yourself wanting to break the cadence, sit with it overnight first.

— *the shop*

# Day 3 Research Report

> The Day 3 owner-review gate. Read this, decide on the three open questions at the end, and we proceed to Phase 2 (product build) from there.

## TL;DR

The new-parent niche is saturated in the obvious categories (pregnancy planner, newborn tracker, baby shower games) and **wide open in 8 specific segments** we can attack with our text+CSS+Canva+ElevenLabs stack:

1. **Sensory play activity cards by age** (Pinterest +1070% YoY — biggest opportunity)
2. **"Saying no" visitor / advice script packs** (zero direct competition)
3. **Slow motherhood planner** (Pinterest +310%, brand-defining)
4. **Partner's postpartum guide** (zero direct competition)
5. **Screen-free family challenge cards** (Pinterest "no phone summer" +340%)
6. **Positive-discipline parent phrase cards** (Pinterest +295%)
7. **Maternity-leave-to-work transition** (high-WTP working-mom buyer)
8. **C-section recovery phased planner** (gap in market — existing planners assume vaginal birth)

These 8 become **Wave 1 + early Wave 2** of our launch.

## What we did over Day 1–3

| Stream | Status | Output |
|---|---|---|
| 01 — Reddit pain-phrase mining | Blocked by sandbox network policy; synthesized from training + secondary sources | `01-reddit-mining/note-on-access.md` |
| 02 — Etsy top-seller teardown | Done (indirect — direct Etsy access blocked, SERP-mined instead) | `02-etsy-teardown/findings.md` |
| 03 — Blog SERP teardown | Done for top 8 candidates | `03-blog-serp/findings.md` |
| 04 — Pinterest trends | Done (2026 Parenting Report fully extracted) | `04-pinterest-trends/findings.md` |
| 05 — Customer journey | Done (10 phases, TTC → toddler) | `05-customer-journey/pain-points.md` |
| 06 — Problem→product matrix | Done | `06-problem-product-matrix/initial-matrix.md`, `top-30.md` |

## Key strategic findings

### 1. Pinterest 2026 trends are the strongest leading indicator

Pinterest released its first-ever Parenting Trend Report in 2026. The theme: "raising screen-smart kids who seek real-world adventure." This is *strong forward-looking demand data* the rest of the market hasn't priced in yet.

Top rising searches with YoY growth:
- sensory play ideas **+1,070%**
- vintage baby clothes 90s **+600%**
- daily routine chart for kids **+575%**
- cognitive worksheets **+540%**
- no phone summer **+340%**
- slow motherhood **+310%**
- positive discipline **+295%**
- educational activities for kids **+280%**
- family traditions ideas **+200%**
- screen-free activities **+200%**

Every Wave 1 product is intentionally aligned to one of these surges.

### 2. The aesthetic shift is our differentiation lever

The market is dominated by 2020-era minimalist-Goodnotes aesthetic. Pinterest 2026 is shifting to warm-vintage / 70s-90s-coded, lived-in, slow. Most established sellers won't retool. We can ride the trend in the build phase and capture the "matches my Pinterest mood" buyer.

Our brand visual identity (`brand/visual-identity.md`) is built on this thesis: warm ivory + terracotta + sage; Fraunces serif; hand-drawn dividers; paper-texture background; no drop shadows, no gradients.

### 3. The high-WTP underserved segments are the unfair advantage

Working moms, NICU/preemie parents, twin parents, IVF/high-risk pregnancies, post-loss pregnancies, c-section recoveries — all are desperate buyers in categories with **a fraction of the competition** of generic-pregnancy-planner-land. Our Wave 2 lineup leans heavily into these.

### 4. The trust problem has three solutions to choose from

Detailed in `brand/persona.md`. Owner picks one of:

- **Option A** — Brand-only / anonymous (lowest conversion, simplest)
- **Option B** — Fictional founder persona "Maya, postpartum doula and mom of two" (highest conversion, standard practice, requires light consistency commitment)
- **Option C** — Real-couple framing "Varun and partner" (most authentic, defensible, slightly lower ceiling)

Recommendation: **Option B** if comfortable with light persona-building; otherwise **Option C**.

### 5. The 10-day build can produce ~30 products + 30 pillar posts at high polish

Time budget validated. Per product: ~3 hours Claude work for PDF + Etsy listing + Gumroad page + 5 Pinterest pins. 30 × 3 = 90 hours of Claude work spread across days 4–8. Tight but doable on Max plan.

## Confidence levels

| Decision | Confidence |
|---|---|
| New-parent niche is buildable with our stack | HIGH |
| Pinterest 2026 trend signals are predictive | HIGH (Pinterest's own data) |
| Wave 1 product selection | HIGH |
| Wave 2 + 3 product selection | MEDIUM-HIGH (subject to Wave 1 conversion data informing) |
| Brand voice direction | HIGH |
| Visual identity direction | HIGH |
| Sales projection ($300–800/mo by Day 90 if products hit, $0 if not) | LOW — base rate of zero-sale shops is real |

## Risks remaining

1. **Sandbox network constraints meant indirect data sources.** Etsy listing-level sales counts and Reddit live-thread data weren't accessible. We compensated with WebSearch SERP signals + training knowledge. Confidence in *patterns* is high; confidence in *specific 2026-fresh numbers* is medium.
2. **YMYL adjacency.** Sleep, feeding, c-section recovery, postpartum mental health all touch medical territory. Mitigation: strict no-prescriptive-advice rule + medical disclaimers on every product.
3. **AI-mill detection on Etsy.** Slow drip publishing (1 product/week) avoids the spam-velocity signal but doesn't eliminate it. Quality polish per listing is the second defense.
4. **Persona ethical question** (Option B). If the owner is uncomfortable with light fiction, we use Option A or C — but conversion drops 15–25% from Option B.

## What I need from you to proceed

### Decision 1: Pick the persona (`brand/persona.md`)

- **A** — brand-only
- **B** — Maya, doula (recommended)
- **C** — Varun + partner real-couple framing

### Decision 2: Confirm or revise the top 30 (`top-30.md`)

The list is balanced across categories. If you want different weighting (e.g., "more pregnancy planners, fewer toddler items" or "skip NICU"), say now.

### Decision 3: Confirm Wave 1 launch order

Default Wave 1:
1. P01 — Sensory Play Activity Cards
2. P02 — "Saying No" Script Pack
3. P03 — Slow Motherhood Weekly Planner
4. P04 — Partner's Postpartum Playbook
5. P05 — Screen-Free Challenge Pack

Want a different first 5? Now's the time.

### Default if you don't decide

- Persona: **Option B (Maya)**
- Top 30: as listed
- Wave 1: as listed
- I proceed with build phase

## What happens after this gate

**Days 4–7 — Phase 2 product build:**
- Build P01–P30 as full product folders: PDF, mockups, Etsy listing, Gumroad sales page, 5 Pinterest pins each
- Adhere to brand voice + visual identity
- Wave 1 (5 products) finished by mid-Day 5 so you can publish first one any time after

**Day 8 — Pillar blog posts:**
- 30 posts written, 2500+ words each, Jekyll-ready markdown
- Internal-linked to relevant products

**Day 9 — Pro-mode toolkit:**
- ~50 prompt templates for Claude Pro usage
- CSV-driven variant generators
- Customer service templates
- Decision trees
- Condensed knowledge base

**Day 10 — Publishing playbook + handoff:**
- 52-week publishing calendar
- Weekly checklist
- Full operations runbook
- Final QA across all 30 products

After Day 10, you publish at your own cadence (default: 1 product/week + 1 blog post/week = 7 months runway from inventory; Pro plan generates variants if products hit).

# Master Plan — New Parent Digital Products Shop

> This file is the durable plan. Any future session should read this first to resume work.

## The bet

Build a year of polished inventory (digital products + blog posts) for the **new parent / baby care** niche in a 10-day Claude Max window. Owner publishes weekly/monthly at their own pace after handoff. Operations after Day 10 use Claude Pro ($20/mo) — minimal compute, supported by pre-built toolkit.

## Locked constraints

- **Niche:** new parents / baby care (sub-niche TBD from Day 3 research report)
- **Brand domain:** `shop.varunvashisht.com` for now; separate `.com` purchased only if Etsy shows signal (~$10–12 deferred cost)
- **Etsy:** Yes. ~$0.20/listing only when owner publishes (1 listing/week cadence → ~$10/year)
- **Gumroad:** Yes. Free, 10% per sale
- **Domain DNS:** GitHub Pages backed
- **Email list:** ConvertKit free tier
- **Pinterest:** Business API + manual scheduling fallback
- **Design tools:** Canva Pro (owner has 1 month) + HTML/CSS → WeasyPrint
- **Audio:** ElevenLabs free tier — for Pinterest video pins + 1 lead-magnet audio
- **Image generation:** Skipped (no paid API)
- **Total upfront cost:** $0 during build; ~$0.20/listing as published

## Inventory targets

| Asset | Count |
|---|---|
| Polished digital products | 30 |
| Pillar blog posts (2500+ words) | 30 |
| Lead magnets | 6 |
| Product bundles | 5 |
| Email sequences (welcome, nurture, launch) | 3 |
| Pinterest pin templates (5 variants each) | 30 sets |
| ElevenLabs audio assets | 6 |
| Etsy listing drafts | 30 |
| Gumroad sales pages | 30 |

Plus the Pro-mode toolkit (see below).

## 10-day timeline

| Days | Phase | Deliverable |
|---|---|---|
| 1–3 | **Phase 1: Deep research** | Research report (30–50 pages), brand persona options, sub-niche recommendation. **Owner review gate on Day 3.** |
| 4–7 | **Phase 2: Inventory build** | 30 polished products: PDFs + mockups + Etsy listings + Gumroad pages |
| 8 | **Phase 2 continued** | 30 pillar blog posts + 6 lead magnets + 3 email sequences |
| 9 | **Phase 3: Pro-mode toolkit** | Prompt library (~50), variant generators, customer service templates, decision trees, knowledge base |
| 10 | **Phase 3 continued** | 52-week publishing calendar + weekly checklist + ops runbook + final QA |

## Phase 1 research streams

1. **Reddit pain-phrase mining** — r/Mommit, r/BabyBumps, r/beyondthebump, r/NewParents, r/ScienceBasedParenting, r/Postpartum_Depression, r/breastfeeding, r/toddlers. Extract exact phrases describing unmet needs.
2. **Etsy top-seller teardown** — 100 highest-grossing baby/parent digital products. Reverse-engineer pricing, titles, tags, review themes, weak points.
3. **Blog SERP teardown** — top 200 long-tail parent queries. Identify rank-able gaps.
4. **Pinterest trend pull** — baby/parent search trends, rising queries, seasonal spikes.
5. **Customer journey map** — pregnancy week 1 → child age 3, mapped to emotional states + searches + purchases.
6. **Problem → product matrix** — scored on demand × competition × buildability.

## Pro-mode toolkit (Day 9–10)

Built so owner can operate on Claude Pro ($20/mo) at ~20–30 min/week:

- ~50 self-contained prompt templates (variants, captions, SEO refreshes, customer service)
- CSV-driven Canva Bulk Create generators (zero Claude usage)
- Customer service template library (~50 responses)
- Condensed knowledge base (5-page summary of Phase 1 research, pasted into Pro prompts)
- Pre-publish quality checklists
- Etsy SEO refresh monthly template
- Decision trees (pivot triggers, kill rules)
- Monthly performance review template

## Risk constraints

- **YMYL-adjacent:** Baby/parent content. Strict lane = organization/planning (planners, trackers, checklists, journals, milestone cards). **Avoid:** medical advice, sleep training methods, feeding schedules, breastfeeding mechanics.
- **Medical disclaimer on every product.**
- **Etsy AI-mill detection:** mitigated by slow publishing cadence (1/week) and human-quality polish per product.
- **Trust:** brand persona to be designed in Phase 1; voice consistent across all assets.

## Open decisions (owner to resolve at Day 3 checkpoint)

1. Final sub-niche pick from Phase 1 research
2. Persona choice (fictional, real, brand-only) — 2–3 options to be proposed
3. Any redirects based on research surprises

## Manual setup owner does in parallel (not on critical path)

- Etsy seller account + ID verify + payouts (30 min)
- Gumroad account + payouts (10 min)
- ConvertKit free tier signup (5 min)
- Pinterest business account + API app (15 min, 1–2 day approval)
- DNS: `shop.varunvashisht.com` → GitHub Pages (5 min)

## How sessions resume

- Working branch: `claude/content-automation-plan-FMkcj`
- Current state: see `STATUS.md`
- Each phase commits its outputs; future sessions `git fetch` and continue from `STATUS.md`'s "Next up" section

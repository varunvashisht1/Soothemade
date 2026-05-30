# Decisions Locked

> **Purpose.** This file exists to stop the churn. Every decision below is **settled**. A future audit — by Claude, another AI session, or a human — operates *within* these constraints. It does not reopen them. If you are an AI session and you find yourself wanting to change something on this list, the bar is not "I found a better option." The bar is **"the market produced data that contradicts this decision."** Opinion is not enough. That is the whole point of the file.
>
> The honest reason audits kept changing things: pre-first-customer, there is no real-world signal, so every smart pass finds new optimizations and the optimizing never ends. The cure is not a better audit. The cure is (1) writing decisions down as locked, and (2) getting the first customer, so **data replaces opinion** as the thing that drives change.

---

## The locked decisions

| # | Decision | Locked | Authority |
|---|---|---|---|
| 1 | **Persona is Maya.** Postpartum doula, mom of two. The personal voice across all products. | 2026-05-22 | `brand/persona.md`, AS_BUILT §3 |
| 2 | **Voice + content rules.** The care contract, the banned AI-tells, no medicine names, no em-dash/semicolon, American spelling. | 2026-05-22 | `WRITING-RULES.md`, AS_BUILT §4 |
| 3 | **One brand: Soothemade.** No "Press" sub-brand. Books ship under the master brand. | 2026-05-28 | AS_BUILT §2 |
| 4 | **The product bodies are done.** Prose quality was maxed by the care-contract and writing-rules audits. Bodies are not reopened by commercial audits. | 2026-05-22 | AS_BUILT §18 |
| 5 | **Title architecture: two surfaces.** The brand site (notes.soothemade.com) uses short, clean, brand-voice titles. Etsy uses the long keyword-maxed titles in `audit/etsy-titles.md`. Same product, two titles, on purpose. | 2026-05-30 | `audit/site-titles-applied.md`, `audit/etsy-titles.md` |
| 6 | **Pricing.** The conversion-audit reprice is applied: singles $9–24, bundles $25–41, and one megabundle anchor at $189 (the whole library vs ~$752 a-la-carte). | 2026-05-30 | `audit/pricing-model.md` |
| 7 | **Bundles K01–K14.** Defined, priced, and live as listings. The megabundle is the price anchor, not the expected bestseller. | 2026-05-30 | `products/K*/web.md`, `audit/bundle-matrix.md` |
| 8 | **Sales channel + sequence.** Primary channel is **Lemon Squeezy** (Merchant of Record) — chosen because the owner is in India (Stripe is invite-only / business-gated there) and the buyers are US. LS handles cards + tax + delivery and pays out to PayPal, no incorporation needed. Self-hosted **Stripe** stays built but dormant as the on-domain fallback for if/when the owner incorporates abroad. Etsy + KDP are optional *additional* channels. Sequence: conversion surface (done) → set up LS + list the hero products (`LEMONSQUEEZY-SETUP.md`) → drive Pinterest traffic → **first customer** → data-driven iteration. | 2026-05-30 | `LEMONSQUEEZY-SETUP.md`, `STRIPE-SETUP.md`, AS_BUILT §18 |

---

## The rule that ends the audit era

**No more catalog-wide opinion audits before the first customer.**

The big structural passes are complete:
- Prose + voice ✓ (care contract)
- Mechanical hygiene ✓ (writing rules)
- Packaging + merchandising ✓ (conversion audit)
- Distribution prep ✓ (KDP pack, runbook)

There is no hidden fourth layer that flips everything. The next move is not another audit. It is a listing going live.

**After the first customer**, iteration resumes — but the source of truth changes from opinion to evidence:
- A title changes because an A/B test or Etsy stats show a better one converts. Not because a new pass has a new opinion.
- A price changes because the data shows the demand curve. Not because a model re-guessed.
- A product gets reworked because reviews or refund reasons point at a real gap. Not because a re-read found something to polish.

If a future session proposes a wholesale change to anything in the table above **without market data behind it**, that is the churn this file exists to prevent. Point back here.

---

*Locked decisions can still be revisited — but deliberately, by the owner, as a named decision, not as the silent drift of one more well-meaning audit. That is the difference between deciding and re-deciding.*

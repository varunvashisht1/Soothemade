# 06 — Problem → Product Matrix (Synthesis)

## Goal

Take everything from Streams 1–5 and produce a single ranked list of product opportunities. This is what drives the build phase.

## Per-opportunity columns

| Column | Source |
|---|---|
| Problem name | Synthesized from Reddit + Etsy reviews |
| Buyer segment | From customer journey |
| Demand score (1–10) | Reddit phrase frequency × Pinterest trend × SERP volume signal |
| Competition score (1–10) | Etsy listing density + SERP strength (inverted: high = bad) |
| Buildability score (1–10) | How well our text+CSS+Canva stack can produce it |
| Margin score (1–10) | Price ceiling × repeat-purchase likelihood |
| YMYL risk (1–10) | How close to medical/safety advice (lower = safer) |
| Composite score | Weighted average favoring demand × buildability × low YMYL |
| Recommended product format | Planner, tracker, journal, card set, checklist, etc. |
| Pillar blog post topic | The matching SERP cluster |
| Etsy keyword angle | The primary tag we'd lead with |
| Pinterest angle | Visual concept |

## Output

- `matrix.csv` — full scored list, sortable
- `top-30.md` — the 30 products we'll build, ranked + justified
- `kill-list.md` — opportunities I considered and rejected, with reasons (so we don't second-guess later)
- `wave-plan.md` — which 5 ship first (Phase 2 Day 4), which 10 ship next (Days 5–7), which 15 ship last (Days 7–8). Wave order based on confidence + speed to first signal.

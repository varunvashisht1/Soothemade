# Soothemade

> Slow, considered things to use through the unphotographed parts of life.

This repo is the working catalog for **Soothemade** — a group brand of digital and lifetime-of-use goods, expandable across niches. The current line is **Soothemade Notes**: printables, planners, journals, and card decks for new parents.

## What's here

| Path | What it is |
|---|---|
| [`PLAN.md`](./PLAN.md) | The durable plan. Read this first. |
| [`STATUS.md`](./STATUS.md) | Where work currently is. Read this second. |
| [`brand/`](./brand/) | Persona options, voice guide, visual identity, master/sub-brand architecture. |
| [`research/`](./research/) | Six-stream market research. `REPORT.md` is the Day-3 review gate. |
| [`products/`](./products/) | One folder per product. Currently: P01–P06 (Wave 1 + first Wave 2). |
| [`content/`](./content/) | Pillar blog posts in Jekyll-ready Markdown. |
| [`toolkit/`](./toolkit/) | Pro-mode prompts, decision trees, customer-service templates, knowledge base. |
| [`publishing/`](./publishing/) | 52-week calendar, weekly checklist, runbook, metrics scaffold. |
| [`scripts/`](./scripts/) | WeasyPrint PDF render pipeline. |

## Brand architecture

**Soothemade** is the umbrella brand. Each niche becomes a sub-line:

| Sub-brand | Niche | URL |
|---|---|---|
| **Soothemade Notes** | Current: printables for new parents | `notes.soothemade.com` |
| **Soothemade Kitchen** *(future)* | Recipe + meal-prep printables | `kitchen.soothemade.com` |
| **Soothemade Studio** *(future)* | Solopreneur / creator templates | `studio.soothemade.com` |
| **Soothemade Field** *(future)* | Travel + outdoor guides | `field.soothemade.com` |

`soothemade.com` itself hosts the umbrella overview and routes visitors to the right sub-line.

## How sessions resume

Working branch: `claude/content-automation-plan-FMkcj`.

Any new session should:
1. Read `STATUS.md` for current state
2. Read `PLAN.md` for durable plan
3. Continue from STATUS's "Next up" section
4. Commit small, push, update STATUS

## Operations

After the build phase ends, ongoing work is ~20 min/week per [`publishing/weekly-checklist.md`](./publishing/weekly-checklist.md), supported by the Pro-mode toolkit ([`toolkit/`](./toolkit/)).

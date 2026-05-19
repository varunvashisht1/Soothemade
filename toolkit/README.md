# Pro-Mode Toolkit

Built Day 9–10. Designed so the owner can operate the shop on Claude Pro ($20/mo) with ~20–30 min/week of Claude usage.

## Contents

| Folder | What's inside |
|---|---|
| `prompts/` | ~50 self-contained prompt templates. Each ≤ 2000 tokens, no external context required. |
| `templates/` | CSV-driven Canva Bulk Create inputs + WeasyPrint PDF templates for variant generation. |
| `customer-service/` | ~50 pre-written response templates for common Etsy/Gumroad buyer messages. |
| `decision-trees/` | Pivot triggers, kill rules, double-down rules. No Claude usage. |
| `knowledge-base.md` | 5-page condensed summary of Phase 1 research. Paste into Pro prompts to give Claude context without re-research. |
| `quality-checklist.md` | 10-point pre-publish checklist (no judgment, just verification). |

## How owner uses it

Each `prompts/<name>.md` is structured as:

```
## Use when
<one-line trigger>

## Prompt (paste into Claude Pro)
<self-contained prompt with placeholders>

## Expected output
<what to verify>

## Time
<expected Claude usage>
```

Owner copies, fills placeholders, pastes. Done.

# Soothemade — umbrella site (`soothemade.com`)

The master-brand site. Tells the Soothemade story, lists the lines
(sub-brands), and links out to each. Does NOT host any products.

This is a sibling project to `../site/` (the Notes subsite). The two
share visual language and component patterns, but they are independent
codebases. They can diverge.

## What's here

| Path | What it is |
|---|---|
| `src/pages/` | The 8 site pages — `/`, `/lines`, `/journal`, `/journal/[slug]`, `/about`, `/freebies`, `/contact`, `/policy`, `/press`, `/newsletter`, `/404` |
| `src/components/` | Nav, Footer, Hero, Manifesto, Newsletter, JournalRow, LineCards, BotanicalLeaf, SoftStub |
| `src/layouts/BaseLayout.astro` | Document shell — meta, fonts, theme |
| `src/styles/` | tokens + four themes (daylight default, plus forest/charcoal/mossy for continuity) |
| `src/data/lines.ts` | Sub-line definitions (Notes is live; others "in the workshop") |
| `src/content/journal/` | Umbrella-level essays (markdown) |
| `src/lib/theme.ts` | Reads `src/data/theme.json` for active palette |

## Brand source

The single source of truth for umbrella copy is
[`../brand/umbrella-story.md`](../brand/umbrella-story.md). All page
text on this site should ladder back to that document. If you change
the story, change the page copy in the same commit.

The Notes voice guide ([`../brand/voice-guide.md`](../brand/voice-guide.md)) still applies — the umbrella voice is the same voice, just widened from parenthood-specific to master-brand.

## Local development

```bash
npm install
npm run dev
```

Astro will serve at `http://localhost:4321`.

## Deploy

See [`DEPLOY.md`](./DEPLOY.md) for the Cloudflare Workers setup.
TL;DR — the umbrella site has no data-layer bindings on purpose; it's
a static-ish brand site that runs on Workers for SSR + clean rendering.

```bash
npm run deploy
```

## Why a separate project (and not multi-tenant)?

Two reasons:

1. The lines genuinely evolve at different paces. Notes ships products
   weekly. The umbrella ships an essay every few weeks. Coupling deploys
   would slow both down.
2. The data layers are different. Notes has D1, R2, KV, Vectorize, AI
   for the catalog + search. The umbrella does not need any of that.

Components are kept in sync by hand for now. If we ever launch a third
line, we'll factor a shared `packages/ui` workspace.

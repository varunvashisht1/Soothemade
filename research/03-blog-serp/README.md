# 03 — Blog SERP Teardown

## Goal

Identify the long-tail parent queries where:
- Search volume is real
- Current top results are weak (thin, outdated, ad-heavy)
- We can rank with a 2500+ word pillar post

These become the 30 blog post topics.

## Method

1. Seed query list from Reddit phrases (Stream 01) + Etsy buyer questions (Stream 02).
2. For each seed: pull the top 10 SERP results via WebSearch.
3. Score each SERP on weakness: thin content, no schema, no images, ad-heavy, outdated, missing the obvious adjacent question.
4. Cluster queries into 30 pillar topics where 1 post can target a hub of 5–10 related queries.

## Output

- `seed-queries.md` — initial query list with rough volume signal
- `serp-weakness-scores.md` — each query's top SERP scored for beatability
- `pillar-clusters.md` — 30 pillar topics, each with 5–10 related queries it'll target
- `internal-link-map.md` — how the 30 posts link to each other + to products

# Prompt 04 — Generate a pillar blog post

## Use when

You want to add a new pillar blog post to the catalog. This is the most expensive Claude operation; if Pro plan is tight, batch these (1 per month rather than 1 per week).

## Time

15–25 min on Claude Pro (longest prompt in the toolkit)

## Prompt (paste into Claude)

```
I'm writing a pillar blog post for my new-parent digital-products
shop. Voice and constraints below.

BRAND VOICE: A slightly-older friend who's been through it.
First-person, warm-direct, never preachy. Lead with a specific
concrete observation, not a generality. No "mama", "journey",
"blessed", "should/must", hustle vocabulary.

LENGTH: 2500–4000 words
SCHEMA: Article (and HowTo where applicable)
TARGET QUERY CLUSTER: [Paste 5–10 related queries this post should
target — find from research/03-blog-serp/findings.md or your own list]
LEAD QUERY (what should this post rank #1 for): [The single most
important query]
WHO THE READER IS RIGHT NOW: [Describe their emotional state +
specific situation when they'd land on this post]
LINKED PRODUCTS: [List 2–4 products from /products/ to internal-link
to with their slugs]

STRUCTURE:

1. **Lead** (~150 words): Open with a specific moment / observation /
   3am scenario. NOT "Becoming a parent is challenging."
2. **Why this matters now**: ~200 words. Why this question. Why this
   post specifically.
3. **The body** — 5–8 H2 sections, each ~300–500 words. Each H2 should
   answer one of the related queries from the cluster. Mix of:
   - Practical how-to
   - Honest perspective ("here's what I tried that didn't work")
   - Specific scripts / examples
   - One subtle stat or external link to an authoritative source
     (AAP / ACOG / Postpartum.net) — never to a competing shop
4. **What didn't work for me** (a small section, ~150 words): builds
   trust by being honest about limitations
5. **The tools that helped**: ~200 words, here's where 2–4 of our
   products get internal-linked NATURALLY — not as a hard sell
6. **A short FAQ** (3–5 Q&A): captures additional long-tail queries
7. **Closing note**: ~100 words, warm, ends with a soft permission
   ("you don't have to do this perfectly")
8. **Footer disclaimer** if YMYL-adjacent

WHAT TO AVOID:
- Listicle "10 tips for X" formats — those are saturated
- Generic statements that could apply to any parenting post
- Affiliate-style "best products" framing
- Toxic positivity / motivational closing
- "What to expect" tone (overdone)
- Anything that prescribes a medical decision

OUTPUT FORMAT: Provide the post in Markdown, ready to drop into
content/BXX_<slug>.md with Jekyll front-matter at the top:

---
layout: post
title: "[Post title]"
date: [YYYY-MM-DD]
author: [Brand persona name]
categories: [the relevant category]
description: "[Meta description, 150 chars]"
schema: Article
---

# [Post title]

[Post body...]
```

## Expected output

A complete blog post in Markdown, ~2500–4000 words. Pro plan can handle this but it's at the upper end — you may need to break into 2 messages if it's a particularly long topic.

## After you run this

1. Save to `content/BXX_<slug>.md`
2. Add to Jekyll site / push GH Pages
3. Schedule 2–3 Pinterest pins targeting the post (use Prompt 03)
4. Add to internal-link map from other related posts
5. Update `STATUS.md`

## Topic ideas if you're stuck

See `research/03-blog-serp/findings.md` — the 8 highest-confidence pillar topics are listed. Beyond those, check rising Pinterest terms from `research/04-pinterest-trends/findings.md`.

## Pillar-post-cadence rule

Default: 1 pillar post per 2 weeks. More than 1/week looks like AI-mill velocity to Google. Less than 1/month means you're not building SEO compound interest.

# Content (Blog)

30 pillar blog posts (2500+ words each), produced in Phase 2 Day 8. Lives here as Jekyll-ready markdown.

## Structure

```
content/
  B01_<slug>.md       ← Jekyll front-matter + body + internal links to products
  B02_<slug>.md
  ...
  B30_<slug>.md
  _layouts/           ← Jekyll layouts when site stood up
  _assets/            ← shared images (only static ones we create)
```

## Post anatomy

Each post:

- 2500–4500 words
- Targets a hub of 5–10 related queries (from `research/03-blog-serp/pillar-clusters.md`)
- Internal links to 2–4 relevant products in `/products/`
- Medical disclaimer in footer (every YMYL-adjacent post)
- Author byline matching brand persona (see `brand/persona.md`)
- Schema: Article + (Recipe/HowTo where applicable)
- 1 lead-magnet CTA (link to `/publishing/lead-magnets/`)

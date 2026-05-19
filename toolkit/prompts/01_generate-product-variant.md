# Prompt 01 — Generate a product variant

## Use when

A product is selling. You want to create a variant (different audience, season, color, theme) without re-researching the entire market.

## Time

5–8 min on Claude Pro

## Prompt (paste into Claude)

```
You are helping me run a digital products shop in the new-parent /
baby-care niche. The brand voice is in the system prompt below; please
follow it strictly.

BRAND VOICE (one sentence):
"A slightly-older friend who's been through it, telling you the truth
no one else does — without preaching, without sanitizing, without
selling you a fix."

VOICE RULES:
- First person ("I made this when..."), warm-direct, never preachy
- No "mama", "mommy", "bump", "journey", "blessed", "enjoy every
  moment", "experts say", "should/must/have to"
- Concrete > abstract; lead with a specific observation
- Disclaim once at footer if YMYL-adjacent

EXISTING WINNING PRODUCT:
[Paste the product's content.md or summarize: title, format, what's
inside, who it's for. ~200 words.]

I want to make a variant for: [DESCRIBE THE NEW AUDIENCE OR ANGLE
— e.g., "twins parents", "Halloween-themed", "second-time mom",
"Spanish-language"]

Please produce:

1. A revised product title (Etsy-SEO-friendly, ~140 chars max)
2. A revised "What's inside" outline (~10 lines)
3. The first 200 words of revised content.md in our voice
4. 13 revised Etsy tags
5. 3 Pinterest pin headline suggestions
6. One sentence positioning the variant against the original product

Keep changes minimal where the original works. Only modify what the
new audience actually needs different.
```

## Expected output

A focused content delta. Don't expect a full new product — this is for fast-spinning variants where 80% of the original copy carries over.

## After you run this

1. Create new folder: `products/PXXv_variant-name/`
2. Copy original `content.md` + edit only the sections Claude changed
3. Run `python scripts/render.py products/PXXv_variant-name/`
4. New Etsy listing — $0.20 fee
5. New Gumroad page

## Variants that have worked in this niche

- Cultural variants (Indian / Halal / Kosher / Spanish-language)
- Twin / multiples variants
- C-section / VBAC / induction variants
- Specific industry variants (tech / healthcare / military / teaching)
- Holiday / seasonal variants
- Aesthetic variants (boho vs minimal vs vintage)

Don't make more than 4 variants of any single product — diminishing returns and Etsy looks like a spam shop.

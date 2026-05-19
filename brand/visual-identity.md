# Visual Identity

## The strategic bet

Aesthetic differentiation by riding Pinterest 2026's shift: warm-vintage / 70s-90s-coded, lived-in, slow. Most established Etsy sellers are locked into the 2020-era minimalist-Goodnotes aesthetic. They won't retool fast. We can capture the "matches my Pinterest" buyer.

## Mood (single sentence)

**"A well-loved letter, found in a sunlit drawer, written by someone who's been there."**

## Color palette

Two parallel palettes — pick one for "calm products" (planners, journals, postpartum) and one for "energetic products" (toddler activity cards, screen-free challenges).

### Palette 1: "Warm vintage" (default — calm/postpartum/pregnancy products)

| Role | Hex | Description |
|---|---|---|
| Background | `#F5EFE6` | Warm ivory, like aged paper |
| Primary text | `#2E2A24` | Deep umber-black |
| Accent 1 | `#B4654A` | Terracotta — for headings, dividers |
| Accent 2 | `#8C9B7A` | Sage olive — for callouts, secondary highlights |
| Accent 3 | `#D4A574` | Wheat — for soft backgrounds within sections |
| Muted | `#A89A8C` | Stone — for footers, fine print |

### Palette 2: "Bright vintage" (energetic — toddler activity cards, sensory play)

| Role | Hex | Description |
|---|---|---|
| Background | `#FBF6EE` | Off-white kraft |
| Primary text | `#2E2A24` | Deep umber-black (same as P1) |
| Accent 1 | `#D9532B` | Muted vermillion — call to action |
| Accent 2 | `#3B6B5A` | Forest moss — secondary |
| Accent 3 | `#E8B832` | Mustard ochre — highlights |
| Accent 4 | `#8265A3` | Muted plum — special category markers |

Both palettes share the same primary text + background warm tone. Switching between them on different products still feels like the same brand.

## Typography

| Role | Font | Notes |
|---|---|---|
| Display / titles | **Fraunces** (Google Fonts, free) | Soft serif with optical sizing. Set "Soft" axis to 50, "Wonk" axis to 1 for the lived-in feel |
| Body | **Inter** (Google Fonts) | Clean, readable, postpartum-brain-friendly |
| Pinterest pin overlays | **Caslon Antique** or **Cormorant Garamond** (free alternatives) | High-contrast serif, vintage-coded |
| Hand-lettered accent (sparingly) | **Caveat** or **Homemade Apple** | One word per page max — too much hand-lettering looks Etsy-2018 |

All fonts free, web-accessible, and embeddable in PDFs via WeasyPrint.

## Texture & layout principles

1. **Paper texture as background.** Use a subtle paper-grain texture overlay (free PNG asset, applied at 8–12% opacity). Specifically NOT pure white — pure white reads "clinical" / "AI-generated."
2. **Single-column layouts** by default. Postpartum brain doesn't multi-column.
3. **Lots of breathing room.** Margins 1" minimum. Line height 1.6+.
4. **Hand-drawn-style dividers** instead of horizontal rules. Free SVG sets exist (`feathericons`, hand-drawn floral SVGs from Unsplash/SVG Repo).
5. **No drop shadows** anywhere. Drop shadows are the universal "AI mill" tell.
6. **No gradient buttons.** Flat colors only.

## Iconography

- **Hand-drawn line icons only.** Use the free `Lucide` icon set, but adjust stroke width to 1.5 and corner radius up for warmth. Or the free `Feather` icon set as-is.
- **No flat-color icons.** No emoji as decoration.
- **One icon style across all 30 products.** Mixing styles is the biggest tell of an inconsistent shop.

## Mockup conventions

Each product gets 4–6 mockups for Etsy listings + 1 hero mockup for Pinterest:

| Mockup type | What it shows |
|---|---|
| **1. Hero on iPad / Goodnotes** | For digital planners — buyer's primary use case. Use Canva Smart Mockups. |
| **2. Hero on printed paper** | Same product, but laid out on a wooden table with a coffee cup. Trust signal. |
| **3. Detail callouts (2–3 zoom-ins)** | Show one specific feature ("week-by-week pages"), one specific feature ("hospital bag checklist"). |
| **4. "What's included" infographic** | Visual grid of all pages or all cards in the set. |
| **5. Use-case scene** (optional) | Hands holding the planner, partial face cropped, soft natural light. Stock photo (Pexels). |
| **Pinterest hero** | 1000×1500 portrait, product image + 5–9 words headline overlay. |

## Product cover page template

Every PDF product opens with a cover page following the same structure:

```
[Brand logo, top-left, small]
[Optional product number or "Edition: 2026" small grey text, top-right]

[Centered]
[Soft horizontal divider — hand-drawn SVG]
[Title — Fraunces, 48pt, primary text color]
[Subtitle — Inter italic, 16pt, muted]
[Centered]

[Decorative line-art element — 200px wide, terracotta]

[Bottom, centered]
[Brand name — Caveat 18pt — italicized]
[Tagline — Inter 11pt muted]
```

## Pinterest pin template (1000×1500 default)

Two formats:

**Format A: Photo-heavy**
- 60% photo of product (mockup or scene)
- 30% solid color band (terracotta, sage, or mustard) at the bottom
- 10% small brand logo + URL

**Format B: Text-heavy**
- Solid color background (full)
- Large headline (Caslon Antique 64pt)
- Sub-line (Inter 22pt)
- Small product preview thumbnail in corner

5 pin variants per product = mix of A and B with different colors and headline angles.

## The "AI mill smell test"

Before any visual goes to publish, check:

- [ ] No drop shadows
- [ ] No gradients
- [ ] No purple-pink-orange "AI image" color palette
- [ ] No symmetric mandalas / over-perfect florals
- [ ] No mismatched font weights (typically 6+ different fonts → AI tell)
- [ ] Paper texture / warmth visible somewhere
- [ ] Looks like it was made by *a person* not *a stock template*

## Source files

- All Canva templates link in `products/<id>/source/cover.canva-link.txt`
- HTML/CSS interior pages in `products/<id>/source/interior.{html,css}`
- Brand assets (logo SVG, paper texture PNG, divider SVGs) in `brand/assets/` (to be created with first product build)

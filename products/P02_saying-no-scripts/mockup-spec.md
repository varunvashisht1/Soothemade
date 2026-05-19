# Mockup Spec — P02

Generate in Canva (you have Pro for one month — use Smart Mockups). Brand palette in `brand/visual-identity.md`.

## Required assets

| Asset | Size | Use |
|---|---|---|
| Hero mockup (image #1 on Etsy) | 2000×2000 px | Etsy thumbnail + Gumroad cover |
| Sample page screenshots (×3) | 2000×2000 px | Etsy images #2–4 |
| "What's included" infographic | 2000×2000 px | Etsy image #5 |
| iPad mockup | 2000×2000 px | Etsy image #6 (digital-use signal) |
| Use-case scene | 2000×2000 px | Etsy image #8 |
| Pinterest hero | 1000×1500 px | first pin |

## Hero mockup — Canva instructions

1. **Background:** Warm linen tablecloth from Canva stock (search "linen flatlay neutral"). Soft natural-light vibe.
2. **Layer 1:** Cropped photo of someone's hands holding a coffee cup (Pexels free stock — search "coffee morning hands"). Position bottom-right.
3. **Layer 2:** Stack of 3 printed pages from this product, slightly fanned. Use Canva Smart Mockup → "Printed Document" or "Paper Stack."
4. **Layer 3:** Top of the page should show the title "Saying No" in Fraunces Display 48pt, terracotta `#B4654A`. Subtitle "Postpartum boundary scripts" Inter italic 16pt, muted `#A89A8C`.
5. **Optional:** small terracotta hand-drawn divider above the title.
6. **No text overlay on the mockup itself** — let the photo speak.

## Sample page screenshots

Three from the content:

| # | Page topic | Visual focus |
|---|---|---|
| 1 | Section 1 — Hospital visitors | Show 2 full scripts |
| 2 | Section 3 — Unsolicited advice | Show 3 punchy scripts |
| 3 | Template 1 — The pre-baby family text | Show the full template |

Each screenshot:
- Render page via WeasyPrint script (will create in `scripts/`) OR snapshot in Canva
- Frame in light terracotta border (8px), small drop-shadow ABSENT (no drop shadows per brand guide)
- Centered on a sage-olive `#8C9B7A` square background with title overlay "What's inside →"

## "What's included" infographic

2x3 grid showing the 6 sections:

```
┌──────────────────────────────────────────────┐
│                                              │
│  ✦ What's included in this 20-page pack ✦   │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Hospital │  │ First    │  │ Unwanted │  │
│  │ visitors │  │ week     │  │ advice   │  │
│  │ (5)      │  │ (5)      │  │ (8)      │  │
│  └──────────┘  └──────────┘  └──────────┘  │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Family   │  │ Photos & │  │ Body     │  │
│  │ pressure │  │ social   │  │ comments │  │
│  │ (6)      │  │ media (3)│  │ (3)      │  │
│  └──────────┘  └──────────┘  └──────────┘  │
│                                              │
│  + 5 longer templates for the hard ones      │
│                                              │
└──────────────────────────────────────────────┘
```

Colors: cards on ivory `#F5EFE6`; section headers terracotta `#B4654A`; body text dark umber `#2E2A24`.

## iPad mockup

Canva Smart Mockups → search "iPad Pro" → drag PDF page 1 onto the screen. Set on warm-wood desk. Add small coffee cup + a notebook in soft natural light.

## Use-case scene

Stock photo of hands holding a phone (Pexels — search "phone reading text"). Overlay one of the scripts on the phone screen using Canva's screen-overlay feature. The overlaid script:

> *Hey — thanks for thinking of us. We're not seeing visitors right now. I'll text you when we're ready. ❤️*

Caption (small Inter italic, bottom-left): *digital or printed — your call*

## Pinterest hero

See `pinterest-pins.md` — Pin 1 spec.

## Don't do

- ❌ Drop shadows (AI-mill tell)
- ❌ Gradient backgrounds
- ❌ Filter/glow effects
- ❌ Multiple fonts beyond 2 (Fraunces + Inter; Caveat sparingly)
- ❌ Stock photos of "happy mom holding baby" — feels like every other shop
- ❌ Pinterest-style millennial-pink palette (off-brand for us)

## When done

1. Save originals in `products/P02_saying-no-scripts/source/canva-mockups/` (the Canva link, not the PNGs — Canva is the source of truth)
2. Export final PNGs to `products/P02_saying-no-scripts/mockups/`
3. Copy URL of Canva project to `source/cover.canva-link.txt`
4. Mark complete in product `README.md`

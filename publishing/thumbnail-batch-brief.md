# Thumbnail batch brief — P33–P44

> A self-contained handoff for a **second** Claude Code session whose job is to ship the website thumbnails for the 12 products being content-shipped autonomously in a parallel session.
>
> This file is a one-shot brief. You can delete it after the batch lands, or keep it as a template for the next 12.

---

## TL;DR for the second-session Claude

You're shipping **Canva lifestyle photo thumbnails** for products P33 through P44. The other session is writing the PDF content + listings in parallel; your only job here is the website-facing JPG for each product card.

**Wait until the content session is done** before starting (`git log --oneline -15` should show 12 ship commits for P33–P44, all merged to main). Then `git pull` and proceed.

---

## 1. Read these first

1. `AS_BUILT.md` — full project context. Skim **Sections 6 (visual identity), 14 (Canva integration)**, and the recent **Changelog entries from 2026-05-20** about thumbnail iterations (hand-variety pass, object-only pivot, "single photograph not a collage" lessons).
2. `~/.claude/projects/.../memory/feedback_canva_as_design_generator.md` — when working with Canva, lead with `generate-design`, not UI/brand-kit walkthroughs.
3. `~/.claude/projects/.../memory/reference_canva_brand_assets.md` — the brand-kit + asset IDs you must pass.

---

## 2. Which products + their concepts

Each product folder will exist by the time you start (the content session creates them). Read `products/Pnn_<slug>/web.md` for the title + summary to anchor each Canva prompt.

| Code | Slug (folder) | Concept |
|---|---|---|
| P33 | twin-pregnancy-week-by-week | Twin pregnancy planner, week 6→40 |
| P34 | newborn-cue-decoder-cards | 30-card deck — cry / sleep / hunger / overstim cues |
| P35 | ivf-cycle-planner | IVF cycle tracker + emotional journal (medications by class only) |
| P36 | sleep-disruption-journal | Pure logging tool, no method recs |
| P37 | pediatrician-visit-prep-cards | 12-card deck, one per well-baby visit through 2y |
| P38 | postpartum-freezer-meal-cookbook | 30 one-handed-eating recipes |
| P39 | vbac-prep-planner | VBAC emotional + practical prep |
| P40 | rainbow-baby-planner | Pregnancy after loss — extra tracking + memorial pages |
| P41 | discreet-ttc-fertility-journal | Cycle tracking that doesn't look like fertility tracking |
| P42 | babyproofing-room-by-room | Room-by-room hazard checklist |
| P43 | first-birthday-planning-kit | 6-week countdown for the 1st birthday |
| P44 | toddler-roadtrip-flight-pack | Activity packet for travel days |

> If the content session changed any slugs, trust what's on disk over this table. `ls products/ | grep ^P3` to confirm.

---

## 3. The Canva recipe (per product)

The brand kit is connected. For each product:

### 3a. Generate

Call `generate-design` with:

- **`brand_kit_id`**: `kAHKILw9XGg`
- **`asset_ids`**: `["MAHKIAtzV9Q"]` (Soothemade Brand Mark for light surfaces). Use `MAHKIOhXSrM` (On Dark variant) only if your composition is on a dark surface.
- **`design_type`**: `instagram_post` (Canva resolves to 1080×1350, which matches the existing thumbnail aspect 4:5).
- **Prompt template** (substitute the product specifics):

  ```
  Photographic top-down still life. Soft naturalistic daylight, slight shadow.
  Sage linen or warm-cream paper surface.
  A {{product type — printable booklet, card deck, journal}} sits in the center,
  alongside 3-4 ordinary objects that fit the product's mood:
  {{e.g. a ceramic mug of tea, a small eucalyptus sprig, a pen, a folded sage cloth}}.
  Cool-toned sage and cream palette only — no warm-orange, no purple-pink, no AI-image colors.
  No people, no hands. No text overlays, no captions, no logos, no badges.
  Single photograph, not a collage, not a poster, not a magazine spread.
  Warm vintage hand-set printable aesthetic. Premium, calm, lived-in.
  ```

  **Why this exact phrasing matters**: prior batches learned that Canva returns illustrations / fitness posters / 4-photo collages / typography-card outputs unless you explicitly forbid each. Don't shorten the prompt.

### 3b. Inspect for failure modes

Before exporting, call `get-design-thumbnail` to preview. Known fail modes and what to do:

| Fail mode | Symptom | Fix |
|---|---|---|
| Text overlays (Canva adds Pinterest-style headlines unprompted) | "PERFECT FOR YOU" or product-name caps band visible | `start-editing-transaction` → `perform-editing-operations` to delete text elements → `commit-editing-transaction`. If editing transactions are fragile, just re-roll. |
| Collage / 4-photo grid | Multiple framed photos in one composition | Re-roll with even more emphatic "ONE photograph, not multiple photographs" language. |
| Wrong palette (warm-orange or purple-pink "AI image" smell) | Visibly orange or magenta-pink | Re-roll with explicit "cool-toned sage and cream ONLY, no orange, no pink, no purple". |
| Illustration / poster / typography-card | Not a photograph | Re-roll. Add "photographic, not illustrative, not graphic design". |
| Hand or person visible | Per the hand-variety pass we ship object-only | Re-roll with "no people, no hands, object-only still life". |
| Brand mark wrong / missing / AI-faked logo | Logo on cover isn't the real Soothemade sprig | Confirm you passed `asset_ids: ["MAHKIAtzV9Q"]` — Canva should auto-place the brand mark. If it's still wrong, regenerate. |

If a product takes more than 3 re-rolls without a clean output, **fall back to the PDF cover render**: remove that P-code from `SHIPPED_CODES` in `cover-image.ts` so the site uses the jar-glyph or the cover PNG (precedent: P03 in the 2026-05-20 changelog).

### 3c. Export + resize

1. `export-design` → PNG, save raw to `marketing/mockups/raw/Pnn_obj_c1.png` (preserves the 1080×1350 original for Pinterest reuse).
2. Resize to website-ready JPG (800×1000, quality 85). Python one-liner:

   ```python
   from PIL import Image
   im = Image.open("marketing/mockups/raw/Pnn_obj_c1.png").convert("RGB")
   im = im.resize((800, 1000), Image.LANCZOS)
   im.save("site/public/products/Pnn.jpg", "JPEG", quality=85, optimize=True)
   ```

   Target file size: ~50-130KB. If it's bigger, the source had too much detail — quality 80 is acceptable; below that, regenerate.

---

## 4. Wire to the site

After all 12 thumbnails are in place at `site/public/products/P33.jpg` through `P44.jpg`, edit `site/src/lib/cover-image.ts`:

```typescript
export const SHIPPED_CODES = new Set([
  // ... existing codes ...
  "P33", "P34", "P35", "P36", "P37", "P38",
  "P39", "P40", "P41", "P42", "P43", "P44",
]);
```

(The content session will have already added some/all of these — read the file first and only add what's missing.)

---

## 5. Commit pattern

**One commit, 12 thumbnails.** Precedent: the P15-P20 and P21-P26 batches each shipped thumbnails in their main product commit, but for a thumbnail-only session a single bundled commit reads cleanest in the log:

```
Site: ship lifestyle thumbnails for P33-P44

12 Canva-generated thumbnails wired into the site:
- P33 Twin Pregnancy ... [one line per product describing the composition]

Each was sage/cream cool-toned, photographic top-down or low-angle still life,
object-only (no people), no text overlays. Raw 1080×1350 PNGs preserved at
marketing/mockups/raw/Pnn_obj_c1.png. Site JPGs at 800×1000 q85.

SHIPPED_CODES in site/src/lib/cover-image.ts updated.

Canva design IDs (for future edits):
- P33 DAH... / P34 DAH... [list each design ID returned by generate-design]
```

Include the Canva design IDs in the commit so the next session can re-open them.

---

## 6. Update AS_BUILT.md changelog

Add one bullet:

```
- 2026-MM-DD — Shipped Canva lifestyle thumbnails for P33-P44. 12 product cards now have real cover photos on the site (previously falling back to the jar glyph). One-paragraph summary of any deviations or fallbacks.
```

---

## 7. Verification before you call it done

```bash
ls site/public/products/P{33,34,35,36,37,38,39,40,41,42,43,44}.jpg  # all 12 exist
ls marketing/mockups/raw/P{33,34,35,36,37,38,39,40,41,42,43,44}_obj_c1.png  # all 12 raw
cd site && npm run dev
# visit http://localhost:4321/shop and visually confirm each new card shows the thumbnail, not the jar
```

If any card is still showing the jar glyph, check `SHIPPED_CODES` includes its P-code.

---

## 8. Hard rules (same as the content session)

- **No drop shadows**, **no gradients**, **no purple-pink-orange "AI image" palette**, **no symmetric mandalas**.
- **No emoji in any composition.**
- **One coherent aesthetic** across all 12 — they should look like one photo shoot, not 12 random Canva outputs.
- **The brand mark visible on the product in the photo must be the real sprig (passed via `asset_ids`)**, never an AI-rendered fake.

---

*Brief written by the content-shipping session before going autonomous on P33-P44.*

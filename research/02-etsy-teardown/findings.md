# Etsy Teardown — Day 1 Findings

> **Data source note:** Direct Etsy listing pages return 403 to our crawler. Findings here are synthesized from Etsy SERP titles + descriptions surfaced via Google search, supplemented by Claude's training knowledge of this category. A future session with eRank/Marmalead data, or a manual user-supplied data pull, will tighten the numbers. The qualitative patterns below are reliable; specific sales counts are not.

## Market segments observed

| Segment | Title patterns | Price band (digital) | Saturation | Differentiator opportunities |
|---|---|---|---|---|
| **Pregnancy planner** | "Digital Pregnancy Planner 2026", "Hyperlinked", "Goodnotes", "Canva editable" | $2.14–$11.04 sale / $7.13–$25 list | **Very high** — established sellers, mature catalog | Hyperlinked iPad version is table stakes; differentiation via niche (twins, IVF, geriatric pregnancy, high-risk) |
| **Hospital bag checklist** | "Editable Canva Template", "Minimalist", "Boho", "Mom + Baby + Partner" | $3–8 | **High** | Differentiation via lifestyle aesthetic (boho vs minimal vs maximalist) + edge cases (c-section, induction, NICU prep) |
| **Birth plan** | "Birth Plan Template", "Birth Preferences", "Doula" | $4–10 | **High** | Includes affirmations or visual icons (less common); home birth / hospital birth / birth center variants |
| **Newborn tracker (feed/sleep/diaper)** | "Newborn Daily Care Log", "Feeding & Sleep Tracker", "Diaper Log" | $2–7 | **Saturated** | Format innovation: 24-hour wheel vs grid; dad-friendly version; partner/grandparent handoff |
| **Milestone tracker** | "Baby Milestone Tracker", "0–3 Years", "Memory Keeper", "First Steps" | $4–12 | **High** | Developmental focus (motor/social/cognitive split) vs photo-album focus; pediatrician-aligned schedules |
| **Postpartum recovery planner** | "Postpartum Planner & Journal", "302 pages", "Healing", "Self-Care" | $7–25 (page count drives price) | **Medium — gaps exist** | Mental health specialization, secular vs faith-based split, c-section-specific, breastfeeding-specific |
| **Postpartum affirmation cards** | "45 Printable Affirmations", "Botanical Mom", "Encouragement Cards" | $3–10 | **Medium** | Card count is the value driver (20 → 30 → 45). Anxiety-specific deck is rarer. PND-specific deck rarer still. |
| **Baby shower games (bundles)** | "8/15 Printable Games Bundle", "Bingo + Predictions + Scattergories" | $4–10 | **Saturated** | Bundle size is the differentiator. Themed bundles (sip & see, gender reveal, drive-by). Adult-only humor bundles. |
| **Maternity leave planner** | "Excel Template", "Back to Work Checklist", "Work Handover" | $4–12 | **Low — underserved** | This is a buyer with money (working mom). Excel-format opportunity. Industry-specific variants (tech, healthcare, education). |
| **Twin / multiples planner** | "Twin Pregnancy Planner", "Twin Schedule", "Multiples Necessities" | $5–15 | **Low — underserved** | Specialty niche, low listing density, high desperation. NICU+twins is even narrower. |
| **NICU parent journal** | "Preemie Journal", "Micro Preemie", "NICU Journey Tracker" | $7–18 | **Low — underserved** | High emotional intensity, willing-to-pay, low competition. Theme variants (ocean, farm) seen — visual differentiation matters. |
| **Daycare / nanny daily sheet** | "Nanny Notes", "Daycare Daily Report", "Babysitter Cheat Sheet" | $2–7 | **Medium** | Emergency contact + medical consent + routine in one is winning format. Multi-child families = gap. |
| **Toddler routine / visual schedule** | "Visual Schedule Cards", "Morning Routine Chart", "ADHD Daily Routine" | $4–12 | **Medium** | ADHD/SPD-tagged version is hot. Picture cards format dominates. Family-meeting/chore-pay variants exist but thin. |
| **Baby-led weaning** | "BLW Meal Planner", "First 100 Foods", "8-Week Meal Plan", "Allergen Introduction" | $5–15 | **Medium-high** | "First 100 Foods" is the breakthrough format. Allergen-introduction tracker is gap. Cultural cuisine BLW (Indian, Asian, Mediterranean) = gap. |

## Pricing benchmarks

- Single-page printable: **$2–5**
- Multi-page tracker / checklist: **$4–8**
- Editable Canva template: **$5–12**
- Comprehensive planner / journal (50+ pages): **$10–25**
- Premium bundle (3–5 products): **$15–35**
- Course-adjacent (8-week meal plan with recipes etc.): **$20–40**

## Title formula patterns (what's working)

```
[Adjective?] [Category] [Specifier], [Sub-feature], [Sub-feature], [Format] | [Audience]
```

Examples observed:
- *"Hospital Bag Checklist Printable | Editable Minimalist Birth Packing List Template Editable on Canva Printable Hospital Bag List Boho Baby"*
- *"Baby Led Weaning Food List, Weekly Meal Planner and Grocery List | Baby First 100 Foods Printable | First Foods Digital Download Bundle"*
- *"NICU Mom Ocean, NICU Journal Printable, NICU Planner, Baby Planner Nurse Nicu Mom Micro Preemie Newborn Nicu Journey Tracker, Under Water"*

Title patterns:
1. Lead with the *category keyword* (Etsy SEO prioritizes left-most words)
2. Include 3–5 keyword synonyms (Etsy treats title and tags as a combined keyword pool)
3. Reference format ("Printable", "PDF Download", "Canva Editable", "Instant Download")
4. Audience tag at the end ("First Time Mom Gift", "Twin Mom Gift", "Boho Baby")
5. Aesthetic word ("Minimalist", "Boho", "Botanical", "Watercolor") drives style-matching browsers

## Common features per category (what to include in our products)

**Pregnancy planner must-haves:**
- Trimester-by-trimester checklists
- Weekly journal (weeks 6–40)
- Appointment + symptom tracker
- Hospital bag checklist (often included as bonus)
- Baby shower planning page
- Registry checklist
- Pediatrician interview questions
- Birth plan template (often bundled)

**Postpartum recovery planner must-haves:**
- Daily/weekly self-care planner
- Mood + symptom tracker
- Feeding + diaper log (first 40 days)
- Visitor management
- Recovery milestone tracker
- Mental health check-ins
- Meal/freezer-stocking planner
- Gratitude prompts

**Newborn tracker must-haves:**
- Time + duration + side (left/right breast)
- Bottle volume + formula type
- Diaper: wet / soiled with timestamp
- Sleep: start / end / location
- Medications + temperature
- Visitor / handoff notes

## Identified gaps (= our opportunities)

1. **Postpartum mental-health-specific journals** — most postpartum planners are general-wellness; few are explicitly anxiety/PND-focused with CBT-style prompts.
2. **Maternity leave planning for specific industries** — tech, healthcare, teaching, federal employees have very different leave structures. Generic templates miss this.
3. **Twin pregnancy week-by-week** — most twin planners are general; very few have twin-specific weekly tracking (twins develop differently).
4. **NICU parent emotional support kit** — bundle of journal + affirmation cards + visitor management + medical translator.
5. **Cultural/dietary BLW** — Indian-first-foods, halal BLW, kosher BLW, vegan BLW — basically zero listings.
6. **"Slow motherhood" planner** — Pinterest trend (+310%); no Etsy listings explicitly framed this way.
7. **Screen-free activity printables** for toddlers — Pinterest +200% YoY; under-monetized on Etsy.
8. **Visual sensory play activity cards** by age — Pinterest "sensory play" +1070%; massive gap.
9. **Vintage/retro nursery prints** — Pinterest "vintage baby clothes 90s" +600%; "1970s childhood toys" +200%. Aesthetic opportunity.
10. **C-section recovery specifically** — most postpartum planners assume vaginal birth; c-section-specific recovery (5-week phased) is a gap.
11. **Dad / non-birthing-parent companion planners** — virtually all of this market is mom-targeted. Even a thin "Partner Support Playbook" would have zero competition.
12. **Multi-child handoff sheet** — single-child nanny/daycare sheets dominate. 2+ kid versions are rare.
13. **Postpartum partner support guide** — "what to do for the new mom" — surprisingly underserved.

## Negative signals (skip these)

- **Pure pregnancy week-by-week journals** — saturated. Don't try to compete head-on.
- **Generic baby shower bingo** — too many free PDFs, race to the bottom.
- **"My First Year Journal" photo album** — saturated, all look the same, hard to differentiate without paid image gen.
- **Sleep training schedules** — YMYL, controversial, easy 1-star reviews.
- **Feeding schedule recommendations by age** — YMYL (pediatric advice), pediatricians push back, refund risk.

## Aesthetic patterns (what visual style wins)

Repeated visual keywords across top listings:
- **Boho** (terracotta + cream + sage)
- **Minimalist** (black on white, thin serif)
- **Botanical** (line-art leaves, watercolor florals)
- **Watercolor** (loose washes, soft palette)
- **Bright modern** (millennial neutrals + a punch color)
- **Vintage retro** (NEW per Pinterest 2026 trends — 70s/90s aesthetic surging)

Our `brand/visual-identity.md` should pick 1–2 of these as primary brand aesthetic and apply consistently across all 30 products.

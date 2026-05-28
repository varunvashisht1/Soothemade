# KDP Runbook — Your Steps

The automation pack in `kdp/` and `ebooks/B*_*/kindle-upload.md` covers
everything that can be prepared in advance. **This file is what only you can do.**

Total time budget: ~3-4 hours spread over week 1, then ongoing during launch.

---

## Phase 1 · Account setup (one-time, ~45 minutes)

### Step 1 — Create or sign in to KDP

- Go to **https://kdp.amazon.com**
- Sign in with your Amazon account (same one you use for shopping is fine, or
  create a dedicated `soothemade@...` email if you prefer separation)
- Click "Get Started"

### Step 2 — Tax interview

KDP will not pay you a single cent until this is done. Allow 30 minutes.

- US-based: W-9 form. You'll need your SSN or EIN.
- International: W-8BEN form. You may be able to claim a tax treaty rate
  (e.g. India = 15% withholding instead of 30%).
- The form is in KDP under **Account → Tax Information**.

### Step 3 — Bank + payment

- KDP pays monthly via direct deposit, ~60 days after the month closes.
- Add your bank in **Account → Getting Paid**.
- Currency: choose USD for the primary, set additional ones for non-US
  marketplaces if you want separate payouts.

### Step 4 — Publisher name

- In **Account → Publisher Name**, enter `Soothemade`.
- This appears on the buyer's purchase page as "Publisher."

### Step 5 — Verify identity (if asked)

KDP sometimes requests a photo of a government ID. Upload via the secure
portal. Usually approved within 24 hours.

---

## Phase 2 · Run the verifier (one-time, ~1 minute)

Before any upload, sanity-check the files:

```
python scripts/kindle_verify.py
```

Expected output: `All books pass.` If any book fails, fix and re-run.

---

## Phase 3 · Upload each book (~10 minutes per book × 12 = ~2 hours)

**Recommended order:** B01 first (highest-effort manuscript, best test case),
then in numerical order through B12.

For each book:

1. **Open the book's upload pack:**
   - `ebooks/B01_30-scripts-postpartum-visitor/kindle-upload.md`
   - This file has every field pre-written.

2. **Open KDP → Bookshelf → Kindle eBook → Create new title.**

3. **Kindle eBook Details page:**
   - Language: English (US)
   - Book Title: copy from upload pack
   - Subtitle: copy from upload pack
   - Series: `Soothemade · Book N` (use the per-book series number)
   - Author: Soothemade (primary author)
   - Description: copy the description block (KDP accepts basic HTML; the
     plain text in the pack works as-is)
   - Publishing Rights: "I own the copyright..."
   - Keywords: 7 phrases from the pack, one per field
   - Categories: pick the 3 primary categories listed
   - Save and Continue

4. **Kindle eBook Content page:**
   - Upload `book.epub` from the book's folder
   - Upload `cover-kdp.jpg` from the book's folder
   - Leave ISBN blank (KDP issues a free ASIN)
   - DRM: No
   - Save and Continue

5. **Kindle eBook Pricing page:**
   - KDP Select enrollment: Yes (90 days)
   - Royalty plan: 70%
   - List price: $4.99 USD
   - Territory pricing: see the grid in the upload pack
   - Book Lending: Yes (auto-enabled)
   - Publish

6. **After hitting Publish:**
   - KDP says "In review" — typically 24-72 hours
   - **Update `kdp/launch-tracker.csv`:** set `kdp_status` to `in_review`,
     paste the ASIN (visible on the book page), set the publication date.

---

## Phase 4 · After books go live

### Author Central (one-time, ~15 minutes)

After B01 is live:

1. Go to **https://authorcentral.amazon.com**
2. Claim "Soothemade" as the author
3. Paste the bio from `kdp/author-central-bio.md`
4. Upload an author photo
5. For each subsequent book that goes live: Author Central → Books → Add

### Free promo scheduling

KDP Select gives 5 free days per book per 90-day term. The schedule in
`kdp/COMMON-FIELDS.md` sequences them so each book gets attention without
cannibalizing the others.

For each free promo:

1. KDP → Bookshelf → click book → Promote and Advertise
2. Run a Free Book Promotion → pick 5 consecutive days
3. Save
4. On day 1 of the free promo: post the Reddit drafts from
   `kdp/reddit-launch-posts.md` (one per relevant subreddit)
5. On day 1: send the ARC outreach emails from `kdp/arc-outreach-template.md`
   to any contacts you haven't already given a copy to
6. **Update `kdp/launch-tracker.csv`** — log the free promo dates

### ARC outreach

`kdp/arc-outreach-template.md` has the email templates and tier list.

Target: ~30 outreaches per book over the first 30 days. Expect ~5-8 reviews
per book from this.

### Pinterest

`kdp/pinterest-pin-briefs.md` has 15 pin briefs across the 3 hero books
(B01, B07, B11).

Setup steps:
1. Pinterest Business account (https://business.pinterest.com)
2. Verify your domain `notes.soothemade.com`
3. Create the 3 boards listed in the pin briefs file
4. Generate the 15 base pins in Canva (~3-5 hours of Canva work)
5. Schedule via Tailwind (~$13/month) — 10 pins/day for 60 days

---

## Phase 5 · Day-30 / Day-60 / Day-90 checkpoints

### Day 30 — Read the data

In KDP dashboard, by book:
- Sales (paid copies × 70% × $4.99 = royalty)
- KU page-reads × $0.004 = page-read royalty
- Review count + average star rating
- Bestseller rank in each category

**If combined royalty per book > $50/month:** the book has legs. Keep promoting.
**If combined royalty per book < $10/month:** the problem is sample chapter,
cover, or title — not the book content. Fix and republish.

### Day 60 — Pinterest check

By now, if Pinterest is working, you should see:
- One pin with > 1000 impressions (the breakout candidate)
- Total monthly impressions across the account > 10,000
- Click-through to Amazon > 100/month

If yes: double down on the breakout pin (make 10 variants).
If no: pin design may be the issue. Re-check against the briefs.

### Day 90 — KU exclusivity decision

KDP Select auto-renews at day 90 unless you opt out. By that point:

**Per-book renewal logic:**
- Did the book earn > $100 in 90 days combined? **Renew exclusivity.** KU is
  paying enough that giving up Kobo/Apple/Google distribution makes sense.
- Did the book earn < $30? **Drop exclusivity.** Use
  `kdp/draft2digital-metadata.csv` to list on Draft2Digital, which distributes
  to Kobo, Apple Books, Google Play, Barnes & Noble. Wider distribution
  > KU exclusivity at that revenue level.
- $30-100: judgment call. Lean toward dropping if a specific channel (e.g.
  Apple Books) is requested by your audience.

---

## What you do NOT have to do

- ❌ Build a sales API integration. KDP has one, but the work isn't worth it
   at this scale. Read the dashboard manually monthly.
- ❌ Manually re-validate covers / epubs. `scripts/kindle_verify.py` does it.
- ❌ Re-write descriptions for each platform. The Draft2Digital CSV is already
   formatted for the post-KU distribution.
- ❌ Pay for review services or "Kindle bestseller" programs. They violate
   Amazon TOS and get accounts banned.
- ❌ Respond to every review. Replying to negative reviews looks defensive.
   Let the work speak.

---

## File index for this work

In repo:

```
kdp/
├── COMMON-FIELDS.md            ← Reference doc, all 12 books share these
├── author-central-bio.md       ← Author Central setup
├── launch-tracker.csv          ← Update as books go live
├── arc-outreach-template.md    ← Email templates
├── reddit-launch-posts.md      ← Subreddit-specific drafts
├── pinterest-pin-briefs.md     ← 15 pin briefs for B01/B07/B11
└── draft2digital-metadata.csv  ← Post-KU multi-platform sheet

ebooks/B[01-12]_*/
├── book.epub                   ← Upload to KDP
├── book.pdf                    ← Backup / alternate distribution
├── cover.png                   ← Source cover
├── cover-kdp.jpg               ← Upload to KDP (preferred)
├── kindle-upload.md            ← Per-book KDP form fields
└── metadata.yaml               ← Source (used by render_ebook.py)

scripts/
├── kindle_verify.py            ← Pre-flight compliance check
└── render_ebook.py             ← Source render (epub + pdf + cover)
```

---

## When you get stuck

Common KDP issues:

| Issue | Fix |
|---|---|
| "Cover doesn't meet specifications" | Re-run `scripts/kindle_verify.py`. If clean, try uploading `cover.png` instead of `cover-kdp.jpg` |
| "ePub failed validation" | Run `scripts/kindle_verify.py --book BXX`. Check the .opf section. Re-render via `scripts/render_ebook.py` if needed. |
| "Tax form rejected" | Often a name mismatch between Amazon account and tax form. Update one to match. |
| "Book is taking > 72 hours to review" | First book on a new account is sometimes 5-7 days. Be patient. After that, 24-48 hours is normal. |
| "Reviews aren't appearing" | Amazon delays review display 1-3 days after submission. Reviews from KU borrowers count after the borrower has read enough pages. |

Anything else: KDP Help (in the dashboard top-right) is responsive within ~6
hours for written tickets.

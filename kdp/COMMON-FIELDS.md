# KDP Common Fields

The fields below are identical across all 12 books. The per-book
`kindle-upload.md` files reference this document for sections 4-7.

## 4 · Kindle eBook Content

- **Manuscript:** Upload `book.epub` from the book's folder.
- **Cover:** Upload `cover-kdp.jpg` (preferred) or `cover.png` (also accepted).
- **Kindle eBook ISBN:** Leave blank. KDP issues a free ASIN.
- **Digital Rights Management (DRM):** **No.** Do not enable DRM.
  - DRM does not stop pirates and creates friction for legitimate buyers
    (cannot move file to non-Kindle devices, cannot re-download after
    Amazon account changes). Industry consensus among indie publishers is
    to opt out.

## 5 · Kindle eBook Pricing

- **KDP Select / Kindle Unlimited:** **Yes** (90-day exclusive).
  - Enables Kindle Unlimited (page-read royalties, ~$0.004 per page)
  - Enables 5 free promo days per 90-day term
  - Enables Kindle Countdown Deals (price drops during promo)
  - Locks the book out of Kobo / Apple Books / Google Play for 90 days
  - Can be turned off after 90 days if it underperforms
- **Royalty plan:** **70%**
  - Requires $2.99 ≤ list price ≤ $9.99
  - Requires Book Lending = Yes (auto-enabled)
  - Delivery fee applies (~$0.06 per book for our file sizes, negligible)
- **Primary marketplace:** Amazon.com (US)

### List price + suggested territory pricing

| Marketplace | Price | Notes |
|---|---|---|
| Amazon.com (US) | $4.99 | Primary |
| Amazon.co.uk (UK) | £3.99 | |
| Amazon.ca (Canada) | $6.49 CAD | |
| Amazon.com.au (Australia) | $7.49 AUD | |
| Amazon.de (Germany) | €4.99 | Same € for FR/ES/IT/NL |
| Amazon.fr (France) | €4.99 | |
| Amazon.es (Spain) | €4.99 | |
| Amazon.it (Italy) | €4.99 | |
| Amazon.nl (Netherlands) | €4.99 | |
| Amazon.co.jp (Japan) | ¥499 | |
| Amazon.in (India) | ₹299 | Purchasing-power adjusted |
| Amazon.com.mx (Mexico) | $99 MXN | |
| Amazon.com.br (Brazil) | R$24.99 | |

- **Book Lending:** Yes (auto-enabled with 70% royalty — leave on)
- **Matchbook:** Deprecated, skip.

## 6 · Launch sequence (per book)

1. **Days 1-5:** Free promo via KDP Select. Promote in r/Mommit, r/BabyBumps,
   r/Daddit, postpartum doula Facebook groups, your personal network. Target
   500-2000 downloads, 15-25 reviews.
2. **Day 6 onward:** Raise to $4.99. Early reviewers from the free run continue
   to leave reviews, which compound Kindle search rank.
3. **Day 30:** Check KU page-reads + paid sales in KDP dashboard. If combined
   royalty > $50, the book has legs. If under $10, sample chapter or cover
   needs work — not the book itself.
4. **Day 90:** KDP Select auto-renews unless you opt out. Decide based on
   30-day data:
   - **KU is paying:** Renew exclusivity.
   - **KU is not paying:** Drop exclusivity, list on Draft2Digital for
     Kobo / Apple Books / Google Play distribution (see
     `kdp/draft2digital-metadata.csv`).

## 7 · Author Central setup (do once, applies to all 12 books)

After your first book is live (typically B01):

1. Sign in at **authorcentral.amazon.com**
2. Claim "Soothemade" as the author name
3. Paste the bio from `kdp/author-central-bio.md`
4. Upload an author photo or the Soothemade brand mark
5. As each subsequent book goes live, link it to the Soothemade author profile
   (Author Central → Books → Add)

## Free-promo scheduling

KDP Select gives 5 free days per book per 90-day term. With 12 books, you have
60 free-promo days available per 90-day cycle. Do not burn them all at once —
sequence so each book gets attention.

**Recommended schedule** (assumes you launch all 12 books in week 1):

| Week | Free promo book | Notes |
|---|---|---|
| 1-2 | B01 (5 days) | Launch hero — postpartum visitor |
| 3 | B10 (5 days) | High search-volume — newborn survival |
| 4 | B07 (5 days) | Pinterest-shareable — slow motherhood |
| 5 | B11 (5 days) | Long shelf-life — eldercare |
| 6 | B04 (5 days) | Toddler audience |
| 7 | B05 (5 days) | Pregnancy safety |
| 8 | B06 (5 days) | Birth anxiety |
| 9 | B08 (5 days) | Partner postpartum |
| 10 | B09 (5 days) | Partner pregnancy |
| 11 | B02 (5 days) | Asking for help |
| 12 | B12 (5 days) | Long caregiving |
| 13 | B03 (5 days) | How to read your baby |

Don't run two free promos in the same week — they compete for the same
reader attention and dilute downloads.

## Account-level checklist (do once before any upload)

- [ ] Create / sign in to Amazon KDP at kdp.amazon.com
- [ ] Complete tax interview (W-9 for US, W-8BEN for international)
- [ ] Set up bank account for royalty payments (monthly direct deposit ~60
      days after the month closes)
- [ ] Verify identity if KDP requests (usually within 24 hours)
- [ ] Add a publisher name in the account — "Soothemade"

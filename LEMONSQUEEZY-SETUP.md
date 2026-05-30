# Lemon Squeezy Setup — selling from India to US buyers

Lemon Squeezy (LS) is a **Merchant of Record**: it accepts the buyer's card,
charges US sales tax / EU VAT for you, hosts and delivers the PDF, emails the
receipt + download, and **pays you in India via PayPal**. You do **not** need a
registered company, a US entity, or an Indian payment gateway. No upfront cost —
LS takes ~5% + 50¢ only on a sale.

Because LS does the delivery and receipts, you do **not** need the Stripe setup
(that engine stays dormant in the code) and you don't need email wired — LS
handles all of it.

The site is already wired: set a product's `lemonSqueezyUrl` and its **Buy**
button goes live, opening LS checkout as an on-brand overlay (it stays visually
on soothemade.com via lemon.js, with a plain-link fallback).

---

## Step 1 · Create the account + store (~5 min)

1. Sign up at **https://app.lemonsqueezy.com/register** (free).
2. Create a **Store** named **Soothemade**.
3. **Settings → Payouts:** connect **PayPal** (the India-friendly option — PayPal
   still receives cross-border payments to Indian banks). Add your PAN/bank where
   prompted.
4. **Settings → Tax:** LS collects tax as the Merchant of Record — just confirm
   your details. As a non-US person you'll complete a **W-8BEN** in their flow so
   they don't over-withhold; LS walks you through it.

## Step 2 · Create your first products (start with the heroes)

You do **not** need all 69 live to make the first sale. List these 8 hero
products first, validate, then expand. For each: **Products → New Product →**
- **Type:** Digital / Single payment
- **Name + price:** from the table below
- **Upload file:** the PDF is in the repo's `pdfs/` folder (filename in the table)
- Publish, then open the product and copy its **Share / Buy URL**
  (looks like `https://soothemade.lemonsqueezy.com/buy/xxxxxxxx`)

| Code | Product name (suggested) | Price | File to upload |
|---|---|---|---|
| P09 | Postpartum Depression and Anxiety Journal | $16 | `pdfs/P09_ppd-anxiety-journal.pdf` |
| P52 | Fear of Childbirth Workbook | $16 | `pdfs/P52_birth-anxiety-workbook.pdf` |
| P23 | Postpartum Mom Rage Workbook | $14 | `pdfs/P23_mom-rage-workbook.pdf` |
| P02 | Postpartum Visitor Boundary Scripts | $9 | `pdfs/P02_saying-no-scripts.pdf` |
| P07 | Newborn Feeding and Diaper Log (First Six Weeks) | $15 | `pdfs/P07_newborn-survival-planner.pdf` |
| P27 | Hospital Bag Checklist | $9 | `pdfs/P27_hospital-bag-checklist.pdf` |
| P46 | Eldercare, the First 90 Days | $14 | `pdfs/P46_eldercare-first-90-days-planner.pdf` |
| P20 | Pregnancy Loss Journal and Keepsake | $14 | `pdfs/P20_pregnancy-loss-gentle-companion.pdf` |

*(For the full searchable product names + the other 47 products, see
`audit/etsy-titles.md` and `audit/title-rewrites.md`. Prices are in each
product's `web.md`.)*

## Step 3 · Drop the URLs into the site

For each product you created, open its `web.md` in `products/<code>_<slug>/` and
add the line (anywhere in the frontmatter):

```yaml
lemonSqueezyUrl: "https://soothemade.lemonsqueezy.com/buy/xxxxxxxx"
```

Commit + push. Cloudflare auto-deploys, and that product's **Buy · $X** button is
now live. (Products without a URL keep the "notify me" capture — no dead ends.)

## Step 4 · Test, then go live

1. LS has a **Test mode** toggle. In test mode, buy your own product with a test
   card (LS shows test card numbers at checkout).
2. Confirm: payment succeeds, you land back on the product, and LS emails the
   download link.
3. Switch off test mode → you're live. Do one real small purchase to confirm,
   then refund yourself from the LS dashboard.

---

## Notes

- **Fee:** ~5% + 50¢ per sale, taken automatically. No monthly, no listing fee.
- **Payouts:** LS pays out to PayPal on a schedule (typically every couple of
  weeks) once you clear their minimum.
- **Tax:** handled entirely by LS as Merchant of Record — the big reason this
  beats running your own gateway from India.
- **Delivery + receipts:** LS hosts the file and emails the buyer. You don't need
  the R2/token download flow or an email provider for LS sales.
- **Bundles + ebooks:** create them as LS products too (upload a merged PDF or a
  zip), then paste the URL into the bundle's `web.md`. The Buy button works the
  same way for any product with a `lemonSqueezyUrl`.
- **The Stripe engine** (`/api/checkout`, webhook, token download) stays in the
  code but is unused while LS is your store. If you ever incorporate abroad and
  want lower fees, it's there to switch on (`STRIPE-SETUP.md`).

## Want me to bulk-create all 69 in LS?

LS has an API. If you create a store + an API key and share the key, I can write
a script to create most products programmatically (name + price + file) instead
of you doing 69 by hand. The one catch is file upload via their API can be
finicky, so the hero-first manual path above is the fastest way to start selling
*today* — the bulk script is a nice-to-have for the long tail.

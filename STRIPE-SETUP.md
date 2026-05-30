# Stripe Setup — selling on notes.soothemade.com

The checkout engine is built and deployed. It needs **two secret keys and one
webhook** to go live. No monthly fee, no listing fee — Stripe takes ~2.9% + 30¢
only when a sale clears. Total setup time: ~20 minutes.

## How it works (so the steps make sense)

1. Buyer clicks **Buy · $X** on a product page → `POST /api/checkout` creates a
   Stripe Checkout Session (price + title pulled live from the product) → buyer is
   redirected to Stripe's hosted checkout.
2. Buyer pays → Stripe calls **`/api/webhooks/stripe`** → we write an `orders` row
   and a 30-day `download_tokens` row in D1.
3. Buyer lands on **`/shop/success`** → sees a **Download** button per item
   (`/files/dl/<token>`), which streams the PDF from R2.

Only the **55 single printables (P-codes)** are sellable today — they have PDFs in
R2. Bundles (K-codes) and ebooks keep the "notify me" capture until their files
are uploaded (see the last section).

---

## Step 0 · Make sure the database is migrated (one-time)

The `orders` + `download_tokens` tables must exist on the live D1. If you set up
the data layer already they do; to be safe:

```
cd site
npx wrangler d1 migrations apply soothemade-notes --remote
```

## Step 1 · Create a Stripe account

- Sign up at **https://dashboard.stripe.com/register** (free).
- Stay in **Test mode** (toggle, top-right) for now.

## Step 2 · Get your test keys

- Dashboard → **Developers → API keys**.
- Copy the **Secret key** (`sk_test_...`). (You do not need the publishable key —
  this integration uses hosted checkout.)

## Step 3 · Set the secret on the Worker

Because the site auto-deploys from Git, set secrets in the **Cloudflare
dashboard** (most reliable with Git-integration builds):

- Cloudflare dashboard → **Workers & Pages → soothemade-notes → Settings →
  Variables and Secrets → Add**.
- Add a **Secret** named `STRIPE_SECRET_KEY`, value `sk_test_...`.

*(CLI alternative: `cd site && npx wrangler secret put STRIPE_SECRET_KEY`, paste
the value when prompted.)*

## Step 4 · Create the webhook

- Stripe dashboard → **Developers → Webhooks → Add endpoint**.
- Endpoint URL: `https://notes.soothemade.com/api/webhooks/stripe`
- Events to send: **`checkout.session.completed`** (just that one).
- Save, then click the endpoint and **reveal the Signing secret** (`whsec_...`).
- Add it as a second Cloudflare secret named **`STRIPE_WEBHOOK_SECRET`**.

## Step 5 · Test the whole flow

Secrets take effect on the running Worker within a minute (no redeploy needed).

1. Open any single product, e.g. `https://notes.soothemade.com/shop/saying-no-scripts`.
2. Click **Buy**. You should land on Stripe Checkout.
3. Pay with the test card **`4242 4242 4242 4242`**, any future expiry, any CVC,
   any ZIP.
4. You should land on the **success page** with a **Download** button, and the PDF
   should download.
5. Check **Stripe dashboard → Payments** (the test charge) and **D1** (a new
   `orders` row) to confirm fulfillment fired.

If the success page says "preparing your downloads" and never resolves, the
webhook secret is wrong or the event isn't subscribed — re-check Step 4.

## Step 6 · Go live

When the test flow works end to end:

1. Stripe dashboard → toggle to **Live mode**.
2. **Developers → API keys** → copy the **live** secret key (`sk_live_...`).
   Update the `STRIPE_SECRET_KEY` Cloudflare secret with it.
3. Create the **webhook again in Live mode** (same URL + event), copy the new live
   `whsec_...`, update `STRIPE_WEBHOOK_SECRET`.
4. Stripe dashboard → **Settings → Payouts** → add your bank account and complete
   the identity/business details so Stripe can pay you out.
5. Do one real $1-ish test purchase on a cheap product to confirm live mode, then
   refund yourself from the Stripe dashboard.

---

## Two things worth doing soon (not blockers)

### Email receipts
Right now the buyer gets their downloads on the **success page** (links valid 30
days, re-downloadable), but there is **no emailed receipt** yet. Stripe can send a
basic payment receipt on its own (Dashboard → **Settings → Customer emails →
Successful payments** → on). For a branded receipt *with the download links*, wire
an email provider (Resend or Postmark, both free to start) into the webhook — a
~30-line follow-up. Until then, tell buyers to save the success page.

### Sales tax
With direct Stripe, **you are the merchant of record**, so sales tax/VAT is your
responsibility. At low volume this is usually a non-issue, but when you're ready,
enable **Stripe Tax** (Dashboard → **Tax**) — it auto-calculates and collects at
checkout. (This is the one thing Gumroad/Lemon Squeezy would have handled for you
in exchange for their higher cut.)

---

## Selling bundles + ebooks later

Bundles (K01–K14) and ebooks aren't sellable via Stripe yet because there's no
file to deliver. To enable a bundle:

1. Build a single deliverable for it — either a merged PDF or a `.zip` of its
   constituent PDFs.
2. Upload it to R2 under the key `products/<CODE>.pdf` (e.g. `products/K03.pdf`):
   `npx wrangler r2 object put soothemade-notes-files/products/K03.pdf --file=path/to/k03.pdf`
3. In `site/src/pages/shop/[slug].astro`, widen the `deliverable` test from
   `/^P\d{2,3}$/` to also accept `K`/`B` codes (or list the ready codes).

The checkout + fulfillment already handle any code generically — it's only the
file and the one-line gate that need updating.

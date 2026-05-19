# Manual Setup Checklist — Owner Tasks in Parallel

These are things only you can do (account creation, ID verification, payouts, DNS). Total time: ~2.5 hrs across the 10 days, do in any order.

## Critical path (do first, blocks publishing later)

### 1. Etsy seller account (~30 min, plus 1–3 day ID-verify wait)

- Go to https://www.etsy.com/sell
- Sign up. Choose shop region (US recommended for largest buyer pool).
- Shop name: leave as auto-generated for now (you can change once). We'll lock the final name after persona decision. **If forced to pick:** use 3 short words you don't hate; you can rename later. Avoid `baby` / `mama` (oversaturated).
- Currency: USD. Language: English.
- Pick a generic shop banner placeholder (we'll replace with branded one after persona).
- Add your bank account for payouts.
- Submit ID verification (driver's license or passport). Etsy may take 1–3 days here.
- **DO NOT publish any listings yet.** We'll publish on owner's cadence after Day 10 handoff.

### 2. Gumroad account (~10 min)

- Go to https://gumroad.com/signup
- Create account.
- Add payout method (Stripe → bank, or PayPal).
- Verify email.
- Note: Gumroad's free tier takes 10% per sale — fine for now.

### 3. Pinterest Business account (~15 min, 1–3 day API-app approval)

- Go to https://business.pinterest.com/
- Convert your existing personal account OR create a fresh one (recommended fresh — separate from personal brand).
- Verify your domain (will be `shop.varunvashisht.com`).
- Apply for Pinterest API access via https://developers.pinterest.com/ (request a Trial Access Token for our app — say it's for content scheduling).
- This approval can take 1–3 days. Apply early.

### 4. ConvertKit (~5 min)

- Sign up at https://convertkit.com/ (free tier: 10K subscribers).
- Verify email.
- Create one form: "Postpartum Reset Audio (Lead Magnet)" — we'll wire it up later.

## DNS (for the blog)

### 5. Point `shop.varunvashisht.com` to GitHub Pages (~5 min, 1 hr DNS propagation)

When the GitHub Pages site is up:

- In your domain registrar's DNS panel (wherever `varunvashisht.com` is managed):
  - Add `CNAME` record: `shop` → `<github-username>.github.io`
  - Or A records pointing `shop.varunvashisht.com` to GitHub Pages IPs:
    - 185.199.108.153
    - 185.199.109.153
    - 185.199.110.153
    - 185.199.111.153
- Wait ~1 hour for DNS to propagate.

(I'll prompt with exact records when the Pages site is published.)

## Decisions you can make any time

### 6. Brand persona (look at `brand/persona.md` when committed)

Pick 1 of 3 options I'll draft. You can change voice tone later if it doesn't feel right.

### 7. Whether to buy a separate brand `.com`

Defer until you've seen the persona + Wave-1 products published. Don't spend $12 unless you've committed to the brand.

## Stuff you do NOT need to do

- ❌ Buy Etsy Plus subscription
- ❌ Buy Canva Pro (you have 1 month already — that's enough)
- ❌ Buy eRank / Sale Samurai / Marmalead
- ❌ Set up paid Etsy ads
- ❌ Create social-media accounts on TikTok, Instagram, etc. (not part of our channel mix)
- ❌ Buy stock photos (free tier sources cover us)
- ❌ Buy ElevenLabs paid (defer until first sale lands)
- ❌ Set up Shopify (Etsy + Gumroad cover us)
- ❌ Photograph anything (we generate mockups digitally)

## When you've done each, mark it here

- [ ] Etsy account created
- [ ] Etsy ID verified
- [ ] Etsy bank payouts confirmed
- [ ] Gumroad account created
- [ ] Gumroad payouts confirmed
- [ ] Pinterest business account created
- [ ] Pinterest domain verified
- [ ] Pinterest API trial token requested
- [ ] ConvertKit account created
- [ ] DNS records added (when prompted)
- [ ] Persona picked from `brand/persona.md`

## Estimated total time

| Task | Active time |
|---|---|
| Etsy | 30 min |
| Gumroad | 10 min |
| Pinterest | 15 min |
| ConvertKit | 5 min |
| DNS | 5 min |
| Persona decision | 15 min |
| **Total** | **~80 min active**, plus 2–3 day waits on Etsy + Pinterest approvals |

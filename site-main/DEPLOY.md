# Deploy soothemade.com

The umbrella site is a separate Cloudflare Worker from the Notes
subsite. It has no data-layer bindings — just SSR + assets. First
deploy ships to a free `*.workers.dev` URL; the apex domain
(`soothemade.com`) is a second step.

Verified before this guide:
- `npm install` ✅
- `npm run build` ✅

## 1. First deploy — get a live URL

You need a Cloudflare account at <https://dash.cloudflare.com>. If the
Notes site is already deployed, you already have one.

```powershell
# From the project:
cd C:\Users\varun\Documents\Soothemade\site-main

# Authorize wrangler against your Cloudflare account (one time only).
# Skip if you've already logged in for the Notes site.
npx wrangler login

# Build the site and deploy.
npm run deploy
```

Successful output ends with something like:

```
Deployed soothemade-main triggers (1.23 sec)
  https://soothemade-main.<your-account-subdomain>.workers.dev
```

Open that URL — site is live. SSL is automatic.

## 2. Custom domain — `soothemade.com` + `www.soothemade.com`

### 2a. Make sure `soothemade.com` is on Cloudflare nameservers

This is already done if the Notes site is live (Notes uses
`notes.soothemade.com`, which requires CF-hosted DNS for the root
domain). If not — follow §2a of `../site/DEPLOY.md`.

### 2b. Attach the custom domains to the worker

**Cloudflare UI (recommended):**

1. Cloudflare dashboard → **Workers & Pages** → `soothemade-main`
2. **Settings** → **Domains & Routes** → **Add** → **Custom domain**
3. Add `soothemade.com` → **Add**
4. Add `www.soothemade.com` → **Add**

Cloudflare provisions the apex DNS record + SSL automatically (~30s
each). The `www` subdomain will mirror the apex.

**Or via `wrangler.toml`:**

Uncomment the `routes` block at the bottom of `wrangler.toml` and
re-deploy. The Notes site uses the UI method; either works.

## Iterating after deploy

```powershell
npm run deploy
```

Roughly 10 seconds end-to-end. Workers edge propagates atomically.

### Watch logs in production

```powershell
npx wrangler tail soothemade-main
```

### Roll back

```powershell
npx wrangler deployments list
npx wrangler rollback <deployment-id>
```

## Connect GitHub for auto-deploy on push (optional, later)

Same flow as Notes (`../site/DEPLOY.md` §3), with these differences:

- **Worker name:** `soothemade-main`
- **Build command:** `cd site-main && npm install && npm run build`
- **Deploy command:** `cd site-main && npx wrangler deploy`

## Why no data layer?

The umbrella site is read-only. It does not sell, store newsletter
subscribers, or run search. The newsletter form POSTs to the Notes
worker's `/api/subscribe` endpoint with `source=umbrella` so all
addresses land in a single D1 table. When/if the umbrella outgrows
that arrangement, we add D1 here.

## Troubleshooting

**`Error: Authentication required`** — `npx wrangler login` again.

**The apex domain still hits the old page** — DNS cache. Try incognito
or wait 5 minutes. Cloudflare's edge updates in seconds; resolver
caches take longer.

**Newsletter form 404s** — the form posts to
`https://notes.soothemade.com/api/subscribe`. If you change that, edit
`src/components/Newsletter.astro`.

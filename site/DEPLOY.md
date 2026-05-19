# Deploy notes.soothemade.com

First deploy ships the site to a free `*.workers.dev` URL. The custom domain (`notes.soothemade.com`) is a second step that depends on Cloudflare-hosted DNS for `soothemade.com`.

Verified before this guide:
- `npm install` ✅
- `npm run build` ✅
- `npx wrangler deploy --dry-run` ✅ (925 KiB / 198 KiB gzipped)

## 1. First deploy — get a live URL

You need a free Cloudflare account at <https://dash.cloudflare.com>. Sign up there first if you don't have one.

```powershell
# In PowerShell, from the project:
cd C:\Users\varun\Documents\Soothemade\site

# Authorize wrangler against your Cloudflare account (one time only).
# Opens a browser tab; click "Allow".
npx wrangler login

# Build the site and deploy.
npm run deploy
```

Successful output ends with something like:

```
Deployed soothemade-notes triggers (1.23 sec)
  https://soothemade-notes.<your-account-subdomain>.workers.dev
```

Open that URL — site is live. SSL is automatic.

## 2. Custom domain — `notes.soothemade.com`

### 2a. Make sure `soothemade.com` is on Cloudflare nameservers

In the Cloudflare dashboard:

1. **Add a Site** → enter `soothemade.com` → Free plan → continue
2. Cloudflare gives you two nameservers like `ada.ns.cloudflare.com` + `kirk.ns.cloudflare.com`
3. Update the nameservers at your domain registrar (GoDaddy / Namecheap / wherever you bought the domain)
4. Wait for propagation (usually 10 min – 2 hours)

You only do this once for the whole domain. After this, every subdomain (notes, kitchen, studio, …) works through the same Cloudflare account.

### 2b. Attach the custom domain to the worker

**Option A — Cloudflare UI (recommended for first time):**

1. Cloudflare dashboard → **Workers & Pages** → `soothemade-notes`
2. **Settings** → **Domains & Routes** → **Add** → **Custom domain**
3. Type `notes.soothemade.com` → **Add**
4. Cloudflare creates the DNS record + provisions SSL automatically. Takes ~30 seconds.

**Option B — wrangler:**

Uncomment the `routes` block in `wrangler.toml`:

```toml
routes = [
  { pattern = "notes.soothemade.com", custom_domain = true }
]
```

Then re-deploy:

```powershell
npm run deploy
```

After either option, `https://notes.soothemade.com` resolves to the worker. Test in incognito if your browser cached the workers.dev URL.

## 3. The umbrella `soothemade.com`

When ready, the master umbrella site (a 1-page intro that links to sub-lines) becomes a separate worker — same theme codebase, different config. See `brand/architecture.md` for the model. For now, point `soothemade.com` at a placeholder or redirect to `notes.soothemade.com`.

## Iterating after deploy

Any time you push changes:

```powershell
npm run deploy
```

That's literally it — `astro build && wrangler deploy`. Each deploy takes ~10 seconds and is instant (no cache invalidation needed; Workers edge propagates atomically).

### Watch logs in production

```powershell
npx wrangler tail soothemade-notes
```

Streams the worker's `console.log` from every request, live.

### Roll back

Workers keep prior deployments. To roll back without re-pushing code:

```powershell
npx wrangler deployments list
npx wrangler rollback <deployment-id>
```

## Connect GitHub for auto-deploy on push (optional, Phase 2)

Manual `npm run deploy` is fine for now. When you want git-driven deploys:

1. CF dashboard → **Workers & Pages** → **Create** → **Connect to Git** → select `varunvashisht1/Soothemade`
2. **Production branch:** `main`
3. **Build command:** `cd site && npm install && npm run build`
4. **Deploy command:** `cd site && npx wrangler deploy`
5. **Root directory:** leave blank (build commands set the cwd)

After connecting, every push to `main` ships a new deploy automatically.

## Troubleshooting

**`Error: Authentication required`** — run `npx wrangler login` again.

**`Error: ENOENT package.json`** — you're in the wrong directory. `cd` into the `site/` folder.

**The site loads but `/admin` is blank** — Decap CMS auth needs a GitHub OAuth proxy on Cloudflare. That's a follow-up milestone. The CMS HTML is served correctly; clicking "Log in with GitHub" will fail until the proxy is up.

**Build warning: `Invalid binding 'SESSION'`** — harmless until we actually call `Astro.session` in code. Ignore for now; we'll wire up KV in the email-capture milestone.

**Mobile Chrome shows the site in dark mode anyway** — that's expected. The site IS dark. The browser's auto-dark-inversion will leave it alone.

## What to expect after first live deploy

- `https://soothemade-notes.<subdomain>.workers.dev` — works immediately
- Free tier: 100k requests/day. The site is well under this until significant Pinterest traffic kicks in.
- Web Analytics auto-enabled — see CF dashboard for traffic.
- `/admin/` loads (Decap shell) but can't authenticate until the OAuth proxy is set up.
- Newsletter form will 404 on submit until the `/api/subscribe` endpoint exists.
- All product detail and shop list pages will 404 until the content-collections milestone.

The first deploy is mostly the homepage. That's intentional — get the URL live, share it, then layer features in.

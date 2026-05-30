import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const prerender = true;

const SITE = 'https://notes.soothemade.com';

// Static, indexable pages (no /admin, no /api, no /cart).
const STATIC_PATHS = [
  '',
  'shop',
  'about',
  'contact',
  'policy',
  'press',
  'freebies',
  'wholesale',
  'journal',
];

export const GET: APIRoute = async () => {
  const products = await getCollection('products');
  const posts = await getCollection('journal');

  const urls = [
    ...STATIC_PATHS.map((p) => `${SITE}/${p}`),
    ...products.map((p) => `${SITE}/shop/${p.id}`),
    ...posts.map((p) => `${SITE}/journal/${p.id}`),
  ];

  const body =
    `<?xml version="1.0" encoding="UTF-8"?>\n` +
    `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
    urls.map((u) => `  <url><loc>${u}</loc></url>`).join('\n') +
    `\n</urlset>\n`;

  return new Response(body, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};

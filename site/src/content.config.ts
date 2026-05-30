/**
 * Astro Content Collections.
 *
 * Source of truth lives OUTSIDE the site/ folder, in the repo's
 * top-level products/ and content/ directories — so the markdown
 * is shared between this site and the PDF render pipeline.
 *
 * - products: `../products/<slug>/web.md`
 * - journal:  `../content/B*.md`
 */

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const products = defineCollection({
  loader: glob({
    pattern: '*/web.md',
    base: '../products',
    // Drop the "P##_" directory prefix and the "/web.md" suffix.
    // products/P09_ppd-anxiety-journal/web.md  ->  ppd-anxiety-journal
    generateId: ({ entry }) =>
      entry.replace(/\/web\.md$/, '').replace(/^[A-Z]\d+_/, ''),
  }),
  schema: z.object({
    title: z.string(),
    code: z.string(),

    price: z.number(),
    format: z.string().default('PDF'),
    specs: z.string(),

    category: z.enum([
      'pregnancy',
      'postpartum',
      'early-years',
      'partner',
      'recovery',
      'mental-health',
      'family',
    ]),
    buyer: z.string().optional(),

    heroLabel: z.string(),
    tagline: z.string(),
    glyph: z.enum([
      'circle', 'jar', 'square', 'partner',
      'house', 'cup', 'heart', 'twins', 'card',
    ]),

    publishedAt: z.date(),
    featured: z.boolean().default(false),
    featuredOrder: z.number().optional(),
    ymyl: z.boolean().default(false),

    summary: z.string(),
    badge: z.string().optional(),

    etsyUrl: z.string().url().optional(),
    gumroadUrl: z.string().url().optional(),
    lemonSqueezyUrl: z.string().url().optional(),

    crossSell: z.array(z.string()).optional(),
  }),
});

const journal = defineCollection({
  loader: glob({
    pattern: 'B*.md',
    base: '../content',
    // Drop the "B##_" prefix and ".md" suffix.
    // content/B01_sensory-play-by-age.md  ->  sensory-play-by-age
    generateId: ({ entry }) =>
      entry.replace(/\.md$/, '').replace(/^[A-Z]\d+_/, ''),
  }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    author: z.string().default('Maya'),
    categories: z.array(z.string()).default([]),
    description: z.string(),
    readTime: z.string().optional(),
    featured: z.boolean().default(false),
    relatedProducts: z.array(z.string()).optional(),
  }),
});

export const collections = { products, journal };

/**
 * Astro Content Collections.
 *
 * The umbrella site has its own journal — separate from Notes.
 * Notes' journal stays on notes.soothemade.com and uses its own voice
 * (parenthood-specific). The umbrella journal is broader: slowness,
 * pace, the unphotographed life.
 */

import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const journal = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/journal',
  }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    author: z.string().default('Soothemade'),
    description: z.string(),
    readTime: z.string().optional(),
    category: z.string().default('letter'),
    featured: z.boolean().default(false),
  }),
});

export const collections = { journal };

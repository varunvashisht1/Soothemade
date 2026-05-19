/**
 * Featured-on-homepage product summaries.
 *
 * This is a temporary in-code list — in the next milestone it becomes
 * an Astro Content Collection that reads the source-of-truth markdown
 * at ../../products/<P##>/content.md.
 */

export interface FeaturedProduct {
  slug: string;
  code: string;
  label: string;
  meta: string;
  tagline: string;
  price: string;
  glyph:
    | 'circle' | 'jar' | 'square' | 'partner'
    | 'house' | 'cup' | 'heart' | 'twins' | 'card';
}

export const featured: FeaturedProduct[] = [
  {
    slug: 'sensory-play-cards',
    code: 'P01',
    label: 'Sensory Play\nCard Deck',
    meta: '80 cards · 0–3 yrs',
    tagline: 'For the new senses',
    price: '$24',
    glyph: 'circle',
  },
  {
    slug: 'saying-no-scripts',
    code: 'P02',
    label: '"Saying No"\nScript Pack',
    meta: '30 scripts · postpartum',
    tagline: 'For the doorbell',
    price: '$7',
    glyph: 'jar',
  },
  {
    slug: 'slow-motherhood-planner',
    code: 'P03',
    label: 'Slow Motherhood\nPlanner',
    meta: '36 pages · undated',
    tagline: 'For the tired weeks',
    price: '$12',
    glyph: 'square',
  },
  {
    slug: 'partner-postpartum-playbook',
    code: 'P04',
    label: "Partner's\nPlaybook",
    meta: '24 pages · for partner',
    tagline: 'For the other parent',
    price: '$9',
    glyph: 'partner',
  },
  {
    slug: 'screen-free-challenge',
    code: 'P05',
    label: 'Screen-Free\nChallenge',
    meta: '30 cards · 3–10 yrs',
    tagline: 'For the quiet month',
    price: '$9',
    glyph: 'house',
  },
  {
    slug: 'csection-recovery-planner',
    code: 'P06',
    label: 'C-Section\nRecovery',
    meta: '36 pages · 5 phases',
    tagline: 'For the surgical week',
    price: '$14',
    glyph: 'cup',
  },
  {
    slug: 'ppd-anxiety-journal',
    code: 'P09',
    label: 'Postpartum\nMind Journal',
    meta: '60 pages · noticing',
    tagline: 'For the off days',
    price: '$14',
    glyph: 'heart',
  },
  {
    slug: 'twin-pregnancy-planner',
    code: 'P10',
    label: 'Twin Pregnancy\nPlanner',
    meta: '60 pages · 6–40 weeks',
    tagline: 'For the two of them',
    price: '$16',
    glyph: 'twins',
  },
];

export const featuredJournalPosts = [
  {
    href: '/journal/sensory-play-by-age',
    category: 'Sensory play',
    readTime: '12 min',
    title: 'The complete sensory play guide, by age.',
    blurb:
      "Most lists are 100-item smorgasbords. This one is sorted by what the baby can actually do today, and uses stuff in your kitchen drawer.",
  },
  {
    href: '/journal/postpartum-visitor-scripts',
    category: 'Postpartum',
    readTime: '8 min',
    title: 'The doorbell, the visitors, and the script library.',
    blurb:
      "The hardest part of postpartum isn't the baby. It's the people who keep arriving — and the version of yourself who keeps saying \"of course, come in.\"",
  },
  {
    href: '/journal/three-list-slots',
    category: 'Slow motherhood',
    readTime: '6 min',
    title: 'Three list slots a day, and why ten was always too many.',
    blurb:
      "I bought four productivity planners between my first kid and my second. I used zero of them past mid-March. Here's why, and what I made instead.",
  },
];

export const homeCategories = [
  { href: '/shop?cat=pregnancy', name: 'For pregnancy', count: '04 items', glyph: 'cross' as const },
  { href: '/shop?cat=postpartum', name: 'For postpartum', count: '07 items', glyph: 'leaf' as const },
  { href: '/shop?cat=years-after', name: 'For the years after', count: '06 items', glyph: 'book' as const },
  { href: '/shop?cat=partner', name: 'For the partner', count: '02 items', glyph: 'partner' as const },
];

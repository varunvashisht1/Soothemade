/**
 * Website cover image resolver — used by homepage, shop catalog, product
 * detail hero, and cross-sell cards. Single source of truth so adding a
 * new shipped product is a one-line change.
 *
 * Shipped products have a Canva-generated lifestyle JPG at
 * /products/<CODE>.jpg (sage palette, no text overlay — ProductCard
 * h3/meta-row provides the label).
 *
 * Unshipped products (no JPG yet) return undefined, and ProductCard
 * falls back to the jar-glyph design.
 */

// P06 removed 2026-05-20 — thumbnail flagged as odd, falling back to jar glyph
// until a clean replacement is rendered.
// P33-P44 not yet listed — products ship in parallel but their thumbnails are
// pending; the jar glyph carries them until rendered.
const SHIPPED_CODES = new Set([
  'P01', 'P02', 'P03', 'P04', 'P05',        'P07',
  'P08', 'P09', 'P11', 'P12', 'P13', 'P14', 'P15',
  'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22',
  'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29',
  'P30', 'P31', 'P32',
]);

export function coverFor(code: string): string | undefined {
  return SHIPPED_CODES.has(code) ? `/products/${code}.jpg` : undefined;
}

/**
 * Minimalist "apothecary label" cover for products without a lifestyle
 * photo. Deliberately a different visual language from the umbrella site:
 * the umbrella uses faded BOTANICAL line-art on dark tiles; Notes uses
 * CELESTIAL/geometric ink marks (sun, moon, rings, dawn) on cream paper.
 * Celestial fits Notes thematically — the unphotographed hours: 3am,
 * dawn, the long night.
 *
 * Motif is chosen deterministically by product code so the catalog grid
 * has variety without per-product asset work. currentColor drives tint.
 */
const COVER_MOTIFS: Record<string, string> = {
  // full sun
  sun: `<circle cx="50" cy="50" r="15" fill="none" stroke="currentColor" stroke-width="2.4"/>
    <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
      <path d="M50 20V9"/><path d="M50 91V80"/><path d="M20 50H9"/><path d="M91 50H80"/>
      <path d="M28 28l-7-7"/><path d="M72 28l7-7"/><path d="M28 72l-7 7"/><path d="M72 72l7 7"/>
    </g>`,
  // crescent moon
  moon: `<path d="M61 15a35 35 0 1 0 0 70a27 27 0 1 1 0-70z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/>`,
  // concentric rings
  rings: `<g fill="none" stroke="currentColor" stroke-width="2.4">
      <circle cx="50" cy="50" r="9"/><circle cx="50" cy="50" r="19"/><circle cx="50" cy="50" r="29"/>
    </g>`,
  // rising sun over a horizon
  horizon: `<g stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round">
      <path d="M13 64H87"/>
      <path d="M34 64a16 16 0 0 1 32 0"/>
      <path d="M50 40V31"/><path d="M33 47l-6-6"/><path d="M67 47l6-6"/>
    </g>`,
  // dawn fan of rays
  fan: `<g stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round">
      <path d="M50 80V38"/><path d="M50 80L29 45"/><path d="M50 80L71 45"/>
      <path d="M50 80L16 60"/><path d="M50 80L84 60"/>
    </g>`,
  // arc of small stars
  dots: `<path d="M22 58Q50 28 78 58" fill="none" stroke="currentColor" stroke-width="1.4" stroke-dasharray="2 5" opacity="0.55"/>
    <g fill="currentColor">
      <circle cx="22" cy="58" r="3"/><circle cx="36" cy="44" r="3"/><circle cx="50" cy="38" r="3.6"/>
      <circle cx="64" cy="44" r="3"/><circle cx="78" cy="58" r="3"/>
    </g>`,
};

const MOTIF_KEYS = Object.keys(COVER_MOTIFS);

export interface CoverMotif {
  art: string;
  /** 'sage' | 'terracotta' — which brand accent tints the mark on cream. */
  tint: 'sage' | 'terracotta';
}

export function coverMotif(code: string): CoverMotif {
  const n = parseInt(String(code).replace(/\D/g, ''), 10) || 0;
  return {
    art: COVER_MOTIFS[MOTIF_KEYS[n % MOTIF_KEYS.length]],
    tint: n % 2 === 0 ? 'sage' : 'terracotta',
  };
}

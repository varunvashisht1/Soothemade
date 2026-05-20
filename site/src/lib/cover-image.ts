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

const SHIPPED_CODES = new Set([
  'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07',
  'P08', 'P09', 'P11', 'P12', 'P13', 'P14', 'P15',
  'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22',
  'P23', 'P24', 'P25', 'P26',
]);

export function coverFor(code: string): string | undefined {
  return SHIPPED_CODES.has(code) ? `/products/${code}.jpg` : undefined;
}

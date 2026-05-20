/**
 * Theme loader.
 *
 * Reads src/data/theme.json (CMS-editable) and produces the inline
 * <style> the layout injects to apply the chosen preset + any hybrid
 * token overrides.
 *
 * The umbrella site defaults to `daylight`. Notes' three dark themes
 * are also available for visual continuity if we ever want a darker
 * page.
 */

import themeData from '~/data/theme.json';

export type ThemePreset = 'daylight' | 'daylight' | 'charcoal' | 'mossy' | 'custom';

export interface ThemeOverrides {
  '--surface'?: string;
  '--surface-deep'?: string;
  '--surface-deepest'?: string;
  '--card'?: string;
  '--card-text'?: string;
  '--card-text-soft'?: string;
  '--ink'?: string;
  '--ink-soft'?: string;
  '--ink-faint'?: string;
  '--sage'?: string;
  '--sage-soft'?: string;
  '--accent'?: string;
  '--accent-soft'?: string;
  '--rule'?: string;
  '--rule-strong'?: string;
}

export interface ThemeConfig {
  preset: ThemePreset;
  overrides: ThemeOverrides;
}

const PRESET_DEFAULT: Exclude<ThemePreset, 'custom'> = 'daylight';

export function loadTheme(): ThemeConfig {
  return themeData as ThemeConfig;
}

/** The attribute the <html> tag should get, e.g. `data-theme="forest"`. */
export function themeAttr(t: ThemeConfig): string {
  return t.preset === 'custom' ? PRESET_DEFAULT : t.preset;
}

/** Inline style block to apply hybrid overrides on top of the preset. */
export function themeOverridesStyle(t: ThemeConfig): string {
  const entries = Object.entries(t.overrides).filter(
    ([, v]) => typeof v === 'string' && v.trim().length > 0,
  );
  if (entries.length === 0) return '';
  const decls = entries.map(([k, v]) => `${k}: ${v};`).join(' ');
  return `:root{${decls}}`;
}

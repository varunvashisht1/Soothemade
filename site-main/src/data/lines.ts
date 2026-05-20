/**
 * Sub-lines of Soothemade — the "rooms in the house."
 *
 * Notes is live. The rest are reserved per brand/architecture.md and
 * appear as quiet "in the workshop" placeholders. When one opens, flip
 * `status` to "live" and set the `href`.
 *
 * Voice rule for descriptions (from brand/umbrella-story.md):
 *   Concrete observations, not categories. Name a specific hour or
 *   object, not a market segment.
 */

export type LineStatus = 'live' | 'coming';

export interface Line {
  id: string;
  name: string;
  audience: string;
  /** One concrete sentence for the home page. */
  descShort: string;
  /** Two to three sentences for the /lines page. */
  descLong: string;
  href: string;
  status: LineStatus;
}

export const lines: Line[] = [
  {
    id: 'notes',
    name: 'Notes',
    audience: 'new parents',
    descShort:
      'Printables, planners, and cards for the 3 a.m. parts, the postpartum body, and the visitor doorbell.',
    descLong:
      'Printables, planners, journals, and card decks for the long, mostly-unphotographed first year of parenthood. Recovery weeks. Visitor scripts. The version of you no one is interviewing at four in the morning.',
    href: 'https://notes.soothemade.com',
    status: 'live',
  },
  {
    id: 'kitchen',
    name: 'Kitchen',
    audience: 'the home cook',
    descShort:
      'Recipe pages, freezer-meal plans, and the Tuesday-night fridge.',
    descLong:
      'For the Tuesday when there is nothing in the fridge and you are too tired to invent. Slow recipes, freezer-meal printables, pantry maps, grocery rhythms that survive a long week.',
    href: '',
    status: 'coming',
  },
  {
    id: 'studio',
    name: 'Studio',
    audience: 'solo work',
    descShort:
      'Templates and rhythms for one-person work — launch weeks, slow weeks, the calm catalog.',
    descLong:
      'For people building one small thing at a time. Launch checklists that do not yell. Quiet quarterly reviews. Templates that assume you are the whole team, and you are also a person.',
    href: '',
    status: 'coming',
  },
  {
    id: 'field',
    name: 'Field',
    audience: 'the long traveler',
    descShort:
      'Slow itineraries, road-trip pages, and guides for the parts of a trip that are not on a map.',
    descLong:
      'For people who travel like weather — slowly, off-itinerary, with time to read at a kitchen table that is not theirs. Walking notes, slow-train logs, road-trip pages for the days that go long on purpose.',
    href: '',
    status: 'coming',
  },
];

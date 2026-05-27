#!/usr/bin/env python3
"""Audit Soothemade content against the care contract in WRITING-RULES.md.

This is NOT a regex-only rule check. It is a care scorecard. Each product
gets six signals scored, plus catalog-level patterns are reported. Some
signals are mechanical, some flag candidates for a human read.

The bar is the one stated in WRITING-RULES.md: someone paid $14 in a tired
season and opens this between feeds. In the first page, can they feel that
a person made this, on purpose, for them?

Run from repo root:
    py scripts/audit_writing_rules.py
    py scripts/audit_writing_rules.py --product P09
    py scripts/audit_writing_rules.py --terse        # one line per product

Read-only. Never writes.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

# ── Signal 1: scene anchors ───────────────────────────────────────────────
# A real person was somewhere when they wrote this. Time / place / body /
# gesture. At least one of these in the first 60 lines of the opening note.
SCENE_TIME = re.compile(
    r"\b(\d{1,2}\s*(?:a\.?m\.?|p\.?m\.?|o'clock)|"
    r"morning|night|evening|afternoon|midnight|noon|"
    r"sunday|monday|tuesday|wednesday|thursday|friday|saturday|"
    r"dawn|dusk|midday|3\s*a\.?m\.?|hour|minute|second|"
    r"weeks?|months?|years?)\b",
    re.IGNORECASE,
)
SCENE_PLACE = re.compile(
    r"\b(parking lot|laundry|bathroom|kitchen|bedside|bedroom|hospital|"
    r"car|shower|microwave|nursery|grocery|store|park|gym|crib|cot|"
    r"window|kettle|stove|sink|table|porch|door|floor|hallway|couch|"
    r"sofa|bed|room|driveway|elevator|waiting room|garage|backyard|"
    r"garden|stairs|shelf|drawer|cabinet|hallway|counter|fridge|"
    r"sidewalk|chair|stoop|stairwell|nursery|crib-side)\b",
    re.IGNORECASE,
)
SCENE_BODY = re.compile(
    r"\b(cried|screamed|sobbed|knocked|shaking|crying|shook|gasped|"
    r"whispered|threw|held|reached|wept|tears|breathing|stomach|chest|"
    r"heart|hands|knee|leg|arm|face|eyes|skin|throat|lungs|gut|ache|"
    r"ached|cracked|trembling|trembled|pulse|hugged|flinched|froze|"
    r"sleeping|nursed|nursing|fed|feeding|labored|labour|laboured|"
    r"bled|bleeding|broke|broken|exhausted|kicked|panted|sweat|sweating)\b",
    re.IGNORECASE,
)
SCENE_OVERHEARD = re.compile(r"[\"'“”][^\"“”]{4,}[\"'“”]")

# ── Signal 2: signature ───────────────────────────────────────────────────
# Personal notes end with *With care, Maya* (Notes) or *with care, the
# studio* (umbrella). Old *Soothemade* signoff is the failure case.
SIGNATURE_MAYA = re.compile(r"\*With care, Maya\*", re.IGNORECASE)
SIGNATURE_STUDIO = re.compile(r"\*with care, the studio\*", re.IGNORECASE)
OLD_SIGNATURE = re.compile(r"^\*Soothemade\*$", re.MULTILINE)

# ── Signal 4: modesty / no over-promising ─────────────────────────────────
OVERPROMISE = re.compile(
    r"\b(transform(?:ed|ing)?|empowered?|breakthrough|radical|"
    r"level\s*up|next\s*level|crush(?:ed|ing)?\s+it|unlock(?:ed|ing)?|"
    r"you\s+deserve|game\s*chang(?:er|ing)|life[- ]chang(?:e|ed|ing))\b",
    re.IGNORECASE,
)
# "heal" as a promise verb is hard to detect mechanically. Heuristic:
# "heal your" / "we heal" / "heal in N" / "heal yourself" — but allow
# descriptive uses ("the body heals at its own pace").
HEAL_PROMISE = re.compile(
    r"\b(?:will\s+heal|heal\s+(?:your|yourself|you|in\s+\d))\b",
    re.IGNORECASE,
)

# ── Signal 5: hard things named (heuristic) ───────────────────────────────
# Euphemisms common in printables that Soothemade refuses.
# `big feelings` is NOT in this list — it is established genre vocabulary in
# gentle-parenting language for talking to toddlers, and it appears as a
# product name (P13 Toddler Big Feelings Cards). The Soothemade rule
# applies to BRAND euphemism for adult experiences, not to age-appropriate
# language for speaking to young children.
EUPHEMISMS = re.compile(
    r"\b(your\s+journey|the\s+journey|new\s+chapter|"
    r"unexpected\s+outcome|challenging\s+emotions|trying\s+season|"
    r"navigate\s+the|wellness\s+journey|self[- ]care\s+journey|"
    r"bumpy\s+road|silver\s+lining|blessing\s+in\s+disguise)\b",
    re.IGNORECASE,
)

# ── Section detection ─────────────────────────────────────────────────────
# Headers that introduce a personal note from the maker.
PERSONAL_NOTE_HEADERS = (
    "## a note from me",
    "## a note from the maker",
    "## a note before you start",
    "## a note before you print",
    "## a note before you open",
    "## read this first",
    "## before you open this",
    "## before you start",
)
TEMPLATE_H2 = re.compile(
    r"^## what\s+this\s+\w+\s+is,?\s+and\s+is\s+not\b",
    re.IGNORECASE | re.MULTILINE,
)


def find_personal_notes(text: str) -> list[tuple[int, int, str]]:
    """Return (start_line, end_line, body) for each personal-note section."""
    lines = text.split("\n")
    notes = []
    i = 0
    while i < len(lines):
        line = lines[i].strip().lower()
        if any(line.startswith(h) for h in PERSONAL_NOTE_HEADERS):
            start = i
            # Section ends at next H2 / H1 or a triple-dash divider.
            j = i + 1
            while j < len(lines):
                ln = lines[j].strip()
                if ln.startswith("## ") or ln.startswith("# ") or ln == "---":
                    break
                j += 1
            body = "\n".join(lines[i:j])
            notes.append((start + 1, j, body))
            i = j
        else:
            i += 1
    return notes


def first_paragraph_block(text: str) -> str:
    """Return the first ~60 lines after the title — the opening-matter block."""
    lines = text.split("\n")
    return "\n".join(lines[:80])


def disclaimer_blocks(text: str) -> list[str]:
    """Return each blockquote that looks like a YMYL disclaimer."""
    # Markdown blockquotes start with `> `.
    blocks = []
    current = []
    for line in text.split("\n"):
        if line.startswith(">"):
            current.append(line.lstrip("> ").strip())
        else:
            if current:
                blocks.append(" ".join(current).strip())
                current = []
    if current:
        blocks.append(" ".join(current).strip())
    # Keep only those that look like disclaimers (mention "not medical advice"
    # or "planning tool" or "not a diagnosis" or similar).
    sigs = ("not medical advice", "planning tool", "tracking tool", "not a diagnosis",
            "please consult", "please contact", "please call", "your provider",
            "obstetric provider", "pediatric provider", "this is a")
    return [b for b in blocks if any(s in b.lower() for s in sigs)]


# ── Per-product scorecard ─────────────────────────────────────────────────


def strip_non_voice_contexts(text: str) -> str:
    """Remove regions where flagged words are not the brand's voice.

    Strips:
    - fenced code blocks (``` ... ```) — these contain scripts, ASCII grids,
      fill-in-template fields, and read-aloud lines for young children.
      The brand's voice rules apply to the brand's prose, not to what it
      quotes parents saying to toddlers or to template field labels.
    - italic quoted blocks (*"..."*) — the brand quotes phrases it is
      critiquing ("they're crushing it", "have a drink, you deserve it").
      A flag inside a quote is the brand pointing at the bad phrase, not
      using it.
    """
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r'\*["“][^"”]+["”]\*', "", text)
    return text


def score_product(content_md: Path) -> dict:
    text = content_md.read_text(encoding="utf-8")
    voice_text = strip_non_voice_contexts(text)
    opening = first_paragraph_block(voice_text)
    notes = find_personal_notes(text)

    # Signal 1 — scene anchor
    scene_hits = {
        "time": SCENE_TIME.findall(opening),
        "place": SCENE_PLACE.findall(opening),
        "body": SCENE_BODY.findall(opening),
        "quote": SCENE_OVERHEARD.findall(opening),
    }
    scene_count = sum(1 for v in scene_hits.values() if v)
    scene_pass = scene_count >= 2  # at least two of the four marker types

    # Signal 2 — signature
    has_maya = bool(SIGNATURE_MAYA.search(text))
    has_old = bool(OLD_SIGNATURE.search(text))
    sig_pass = has_maya and not has_old

    # Signal 4 — modesty (scan only the brand's voice, not its quotes/scripts)
    overpromise_hits = OVERPROMISE.findall(voice_text)
    heal_hits = HEAL_PROMISE.findall(voice_text)
    modesty_pass = not overpromise_hits and not heal_hits

    # Signal 5 — hard things named (heuristic, voice-only)
    euphemism_hits = EUPHEMISMS.findall(voice_text)
    plain_pass = not euphemism_hits

    # Signal 6 — template form (catalog-wide, but flag per-product too)
    has_is_isnot = bool(TEMPLATE_H2.search(text))

    # Disclaimer text (Signal 3 is computed catalog-wide).
    disclaimers = disclaimer_blocks(text)

    return {
        "path": content_md,
        "code": content_md.parent.name.split("_", 1)[0],
        "notes_count": len(notes),
        "scene_hits": scene_hits,
        "scene_count": scene_count,
        "scene_pass": scene_pass,
        "has_maya": has_maya,
        "has_old_signature": has_old,
        "sig_pass": sig_pass,
        "overpromise_hits": overpromise_hits + heal_hits,
        "modesty_pass": modesty_pass,
        "euphemism_hits": euphemism_hits,
        "plain_pass": plain_pass,
        "has_is_isnot": has_is_isnot,
        "disclaimers": disclaimers,
    }


# ── Catalog-level signals ─────────────────────────────────────────────────


def disclaimer_reuse(scorecards: list[dict]) -> list[tuple[str, list[str]]]:
    """Cluster disclaimers by string similarity. Return groups where N>=4 share text."""
    # Flatten with provenance.
    items = []
    for s in scorecards:
        for d in s["disclaimers"]:
            items.append((s["code"], d))
    # Greedy cluster by similarity > 0.7.
    clusters: list[dict] = []
    for code, text in items:
        placed = False
        for cl in clusters:
            if difflib.SequenceMatcher(None, cl["repr"], text).ratio() > 0.7:
                cl["members"].append((code, text))
                placed = True
                break
        if not placed:
            clusters.append({"repr": text, "members": [(code, text)]})
    return [
        (cl["repr"], [m[0] for m in cl["members"]])
        for cl in clusters
        if len(cl["members"]) >= 4
    ]


def template_frequency(scorecards: list[dict]) -> tuple[int, int, float]:
    n_with = sum(1 for s in scorecards if s["has_is_isnot"])
    n_total = len(scorecards)
    return n_with, n_total, (n_with / n_total) if n_total else 0.0


# ── Output ────────────────────────────────────────────────────────────────


def print_scorecard(s: dict, terse: bool = False) -> None:
    code = s["code"]
    checks = [
        ("scene", s["scene_pass"]),
        ("signed", s["sig_pass"]),
        ("modest", s["modesty_pass"]),
        ("plain", s["plain_pass"]),
    ]
    pass_count = sum(1 for _, ok in checks if ok)
    badge = "[OK]" if pass_count == 4 else f"[{pass_count}/4]"
    if terse:
        flags = []
        if not s["scene_pass"]:
            flags.append("no-scene")
        if not s["sig_pass"]:
            flags.append("old-sig" if s["has_old_signature"] else "no-sig")
        if not s["modesty_pass"]:
            flags.append(f"overpromise:{','.join(set(s['overpromise_hits']))[:40]}")
        if not s["plain_pass"]:
            flags.append(f"euphemism:{','.join(set(s['euphemism_hits']))[:40]}")
        flags_s = " ".join(flags) if flags else "clean"
        print(f"  {badge} {code}  {flags_s}")
        return

    print(f"\n{badge} {code}  ({s['notes_count']} personal-note section(s))")
    # Signal 1
    if s["scene_pass"]:
        markers = ", ".join(
            f"{k}={len(v)}" for k, v in s["scene_hits"].items() if v
        )
        print(f"  scene anchor:        OK  ({markers})")
    else:
        present = [k for k, v in s["scene_hits"].items() if v]
        print(
            f"  scene anchor:        FAIL  needs >=2 marker types, has: "
            f"{present or 'none'}"
        )
    # Signal 2
    if s["sig_pass"]:
        print("  signature:           OK  (*With care, Maya*)")
    elif s["has_old_signature"]:
        print("  signature:           FAIL  old *Soothemade* signoff still present")
    else:
        print("  signature:           FAIL  no Maya signature found")
    # Signal 4
    if s["modesty_pass"]:
        print("  modest:              OK")
    else:
        print(
            f"  modest:              FAIL  hits: "
            f"{', '.join(set(s['overpromise_hits']))}"
        )
    # Signal 5
    if s["plain_pass"]:
        print("  hard things named:   OK")
    else:
        print(
            f"  hard things named:   REVIEW  euphemisms: "
            f"{', '.join(set(s['euphemism_hits']))}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", help="audit a single product code (e.g. P09)")
    parser.add_argument("--terse", action="store_true", help="one line per product")
    args = parser.parse_args()

    targets = sorted((ROOT / "products").glob("P*_*/content.md"))
    if args.product:
        targets = [t for t in targets if t.parent.name.startswith(args.product + "_")]
        if not targets:
            print(f"No product matches {args.product}")
            return 1

    scorecards = [score_product(p) for p in targets]

    if not args.terse:
        print(f"── Soothemade care audit — {len(scorecards)} products ──\n")
        print(
            "Six care signals from WRITING-RULES.md. Signals 3 and 6 are "
            "catalog-level and reported at the end.\n"
        )

    for s in scorecards:
        print_scorecard(s, terse=args.terse)

    # Catalog-level Signal 3: disclaimer reuse
    reuse = disclaimer_reuse(scorecards)
    print(f"\n── Signal 3: disclaimer reuse ──")
    if not reuse:
        print("  No clusters of 4+ products sharing the same disclaimer text.")
    else:
        for repr_text, codes in reuse:
            print(f"  {len(codes)} products share this disclaimer:")
            print(f"    \"{repr_text[:110]}...\"")
            print(f"    products: {', '.join(sorted(codes))}")
            print("    These need voicing (see P09 model in WRITING-RULES.md).")

    # Catalog-level Signal 6: template uniformity
    n_with, n_total, ratio = template_frequency(scorecards)
    print(f"\n── Signal 6: form variety ──")
    print(
        f"  {n_with}/{n_total} products ({ratio:.0%}) open with the "
        f"'## What this [X] is, and is not' template H2."
    )
    if ratio > 0.5:
        print(
            "  > 50% of catalog uses the same opening framework. Vary the "
            "lower-stakes products into prose framing or permission-slip "
            "blocks (see P43 first-birthday for the model)."
        )
    else:
        print("  Below 50% threshold. Catalog has form variety.")

    # Final tally
    n_pass = sum(
        1 for s in scorecards
        if s["scene_pass"] and s["sig_pass"] and s["modesty_pass"] and s["plain_pass"]
    )
    print(f"\n── Summary ──")
    print(f"  {n_pass}/{len(scorecards)} products pass all four per-product signals.")
    print(
        f"  Catalog-level Signal 3 (disclaimers) and Signal 6 (form variety) "
        f"reported above."
    )
    if n_pass == len(scorecards) and not reuse and ratio <= 0.5:
        print("  ✓ Catalog passes the care contract.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

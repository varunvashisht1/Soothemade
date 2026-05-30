#!/usr/bin/env python3
"""
Coverage-complete brand-voice lint for the WHOLE Soothemade content surface.

Why this exists: earlier audits were each scoped to one area (product markdown,
or the Notes site structure), and the union of their scopes left a hole — the
hand-written site page copy in both Astro apps was never voice-checked, so
em-dashes lived on soothemade.com undetected. This lint closes that hole by
walking every content root and checking extracted PROSE (never code/CSS) against
the voice rules.

Roots checked:
  products/**.md  ebooks/**manuscript.md  content/**.md
  site/src/**.{astro,ts}  site-main/src/**.{astro,ts,md}

Prose extraction (so we never flag code):
  .md     -> body minus frontmatter and ``` fences
  .astro  -> text nodes between tags + known copy attributes, AFTER stripping
             frontmatter, <style>, and <script> blocks
  .ts     -> string literals that look like human copy (has a space, lowercase)

Read-only. Prints file:line + rule + snippet. Exit 1 if anything is found.

Usage:  python scripts/audit_voice.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- rules -----------------------------------------------------------------
AI_TELLS = [
    "delve", "leverage", "robust", "seamless", "moreover", "furthermore",
    "synergy", "embark", "unlock", "ecosystem", "dive deep", "at the heart of",
    "stands as", "in conclusion", "in summary", "it is important to note",
    "needless to say", "nice to know", "elevate your", "game changer",
    "game-changer", "transformative", "effortless",
]
FILLER = [
    "in order to", "due to the fact that", "going forward", "moving forward",
    "in terms of", "at the end of the day", "in a nutshell", "in essence",
    "at this point in time", "a large number of", "a significant amount of",
    "with regard to", "ultimately", "basically",
]
BUZZWORDS = ["comprehensive", "holistic"]  # 'robust' already in AI_TELLS
# Carve-outs (allowed per WRITING-RULES): actually, harness (physical noun).

# Confirmed-acceptable hits, keyed by (relpath, "label:term"). WRITING-RULES
# allows the LITERAL time-of-day use of "at the end of the day"; both of these
# are literal ("swelling ... at the end of the day", "write ... at the end of
# the day"), not the idiomatic "ultimately" filler. Reviewed 2026-05-30.
ALLOWLIST = {
    ("products/P08_pregnancy-week-by-week/content.md", "filler:at the end of the day"),
    ("products/P28_nicu-parent-planner/content.md", "filler:at the end of the day"),
}

WORD_RULES = (
    [("AI-tell", t) for t in AI_TELLS]
    + [("filler", t) for t in FILLER]
    + [("buzzword", t) for t in BUZZWORDS]
)
WORD_PATTERNS = [(label, term, re.compile(r"\b" + re.escape(term) + r"\b", re.I)) for label, term in WORD_RULES]

COPY_ATTRS = re.compile(
    r"\b(?:title|body|tagline|summary|label|quote|quoteAccent|tail|headlinePre|"
    r"headlineAccent|headlinePost|blurb|description|placeholder|name|detail|whenToUse)\s*=\s*[\"']([^\"']+)[\"']"
)
TEXT_NODE = re.compile(r">\s*([^<>{}]*?[A-Za-z]{2,}[^<>{}]*?)\s*<")
TS_STRING = re.compile(r"[\"'`]([^\"'`]{8,}?)[\"'`]")
FENCE = re.compile(r"^```")


def strip_blocks(text: str) -> str:
    text = re.sub(r"<style[\s\S]*?</style>", "", text, flags=re.I)
    text = re.sub(r"<script[\s\S]*?</script>", "", text, flags=re.I)
    # Astro frontmatter fence
    if text.lstrip().startswith("---"):
        text = re.sub(r"^---[\s\S]*?---", "", text.lstrip(), count=1)
    return text


def looks_like_copy(s: str) -> bool:
    s = s.strip()
    if " " not in s:
        return False
    if s.startswith(("/", "#", ".", "http", "@", "~", "{")):
        return False
    if "/" in s and " " not in s.split("/")[0]:
        return False
    return bool(re.search(r"[a-z]{3,}\s+[a-z]{2,}", s))


def prose_segments(path: Path):
    """Yield (line_no, text) prose segments for a file."""
    raw = path.read_text(encoding="utf-8", errors="ignore")
    suffix = path.suffix

    if suffix == ".md":
        body = raw
        if body.lstrip().startswith("---"):
            body = re.sub(r"^---[\s\S]*?---", "", body.lstrip(), count=1)
        in_fence = False
        for i, line in enumerate(body.split("\n"), 1):
            if FENCE.match(line.strip()):
                in_fence = not in_fence
                continue
            if not in_fence and line.strip():
                yield i, line
        return

    if suffix in (".astro",):
        cleaned = strip_blocks(raw)
        # report on cleaned text; line numbers approximate to the cleaned body
        for i, line in enumerate(cleaned.split("\n"), 1):
            for m in TEXT_NODE.finditer(line):
                yield i, m.group(1)
            for m in COPY_ATTRS.finditer(line):
                yield i, m.group(1)
        return

    if suffix in (".ts", ".mjs"):
        for i, line in enumerate(raw.split("\n"), 1):
            if line.strip().startswith(("import ", "//")):
                continue
            for m in TS_STRING.finditer(line):
                if looks_like_copy(m.group(1)):
                    yield i, m.group(1)
        return


def targets():
    out = []
    out += list((ROOT / "products").glob("P*_*/content.md"))
    out += list((ROOT / "products").glob("P*_*/web.md"))
    out += list((ROOT / "products").glob("K*_*/web.md"))
    out += list((ROOT / "ebooks").glob("B*_*/manuscript.md"))
    if (ROOT / "content").is_dir():
        out += list((ROOT / "content").glob("*.md"))
    for app in ("site", "site-main"):
        base = ROOT / app / "src"
        if base.is_dir():
            out += [p for p in base.rglob("*.astro")]
            out += [p for p in base.rglob("*.ts")]
            out += [p for p in base.rglob("*.md")]
    return sorted(set(out))


def main() -> int:
    findings = []
    for path in targets():
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        for line_no, text in prose_segments(path):
            if "—" in text:
                findings.append((rel, line_no, "em-dash", text.strip()[:90]))
            if ";" in re.sub(r"&#?\w+;", "", text):  # ignore HTML entities like &amp;
                findings.append((rel, line_no, "semicolon", text.strip()[:90]))
            for label, term, pat in WORD_PATTERNS:
                if pat.search(text):
                    findings.append((rel, line_no, f"{label}:{term}", text.strip()[:90]))

    skipped = [f for f in findings if (f[0], f[2]) in ALLOWLIST]
    findings = [f for f in findings if (f[0], f[2]) not in ALLOWLIST]

    if not findings:
        extra = f" ({len(skipped)} documented carve-out(s) allowlisted)" if skipped else ""
        print(f"CLEAN — no voice violations across products, ebooks, content, and both site apps.{extra}")
        return 0

    by_file: dict = {}
    for rel, ln, rule, snip in findings:
        by_file.setdefault(str(rel), []).append((ln, rule, snip))
    for f in sorted(by_file):
        print(f"\n{f}")
        for ln, rule, snip in by_file[f]:
            print(f"  L{ln}  [{rule}]  {snip}")
    print(f"\n{len(findings)} violation(s) across {len(by_file)} file(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())

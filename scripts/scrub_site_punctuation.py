#!/usr/bin/env python3
"""
Scrub em-dashes (an AI-tell + a hard brand-rule violation) from the two Astro
site apps' source. Mirrors scripts/scrub_ai_punctuation.py but:

  - Targets site-main/src and site/src (.astro, .ts, .md, .css).
  - Touches ONLY em-dashes (U+2014). It NEVER touches semicolons, because those
    are load-bearing in JS/CSS — that is why the product scrubber must not run
    here.
  - Leaves en-dashes (U+2013) alone — they are correct for number ranges like
    "0-3 yrs" / "ages 3-10".

Per line, in order:
  1. decorative eyebrow frame  ">— LABEL —<"  -> ">LABEL<"   (strip framing dashes)
  2. leading dash              "^<ws>— "       -> "^<ws>"     (signatures/labels)
  3. prose interrupter         " — "           -> ", "
  4. catch-all                 "—"             -> ","

Usage:
    python scripts/scrub_site_punctuation.py            # apply
    python scripts/scrub_site_punctuation.py --dry-run  # report only
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIRS = [ROOT / "site-main" / "src", ROOT / "site" / "src"]
EXTS = {".astro", ".ts", ".md", ".css", ".mjs"}

EYEBROW_OPEN = re.compile(r">(\s*)—\s+")        # tag-framed label:  >— X —<
EYEBROW_CLOSE = re.compile(r"\s+—(\s*)<")
QUOTE_OPEN = re.compile(r"(['\"])—\s+")          # quoted label:  "— X —"  /  '— X —'
QUOTE_CLOSE = re.compile(r"\s+—(['\"])")
LEADING = re.compile(r"^(\s*)—\s+")              # line-leading signature: — Maya


def scrub_line(line: str) -> str:
    # Strip decorative framing dashes first (tag- or quote-framed labels), so
    # "— X —" becomes "X" rather than ", X ,".
    line = EYEBROW_OPEN.sub(r">\1", line)
    line = EYEBROW_CLOSE.sub(r"\1<", line)
    line = QUOTE_OPEN.sub(r"\1", line)
    line = QUOTE_CLOSE.sub(r"\1", line)
    line = LEADING.sub(r"\1", line)
    # Remaining em-dashes are prose: interrupter -> comma.
    line = line.replace(" — ", ", ")
    line = line.replace("—", ",")
    return line


def scrub_file(path: Path, dry: bool) -> int:
    original = path.read_text(encoding="utf-8")
    if "—" not in original:
        return 0
    new_text = "\n".join(scrub_line(ln) for ln in original.split("\n"))
    n = original.count("—") - new_text.count("—")
    if not dry and new_text != original:
        path.write_text(new_text, encoding="utf-8")
    return n


def main() -> None:
    dry = "--dry-run" in sys.argv
    total = 0
    files = 0
    for base in SRC_DIRS:
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.suffix in EXTS and path.is_file():
                n = scrub_file(path, dry)
                if n:
                    print(f"{path.relative_to(ROOT)}: {n} em-dash{'es' if n != 1 else ''}")
                    total += n
                    files += 1
    verb = "would remove" if dry else "removed"
    print(f"\n{verb} {total} em-dashes across {files} files")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Scrub AI-tell punctuation (em dashes, semicolons) from product content.md files.

Replacements applied per line:
  - Line-leading "— "  -> ""   (signatures like "— Soothemade" become "Soothemade")
  - " — "              -> ", " (inline em-dash interrupters become commas)
  - "—"                -> ","  (any remaining em dashes become commas)
  - "; "               -> ". " (semicolon-space becomes period-space)
  - ";"                -> "."  (catch-all semicolons become periods)

Usage:
    python scripts/scrub_ai_punctuation.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = sorted(
    list((ROOT / "products").glob("P*_*/content.md"))
    + list((ROOT / "products").glob("P*_*/web.md"))
    + list((ROOT / "ebooks").glob("B*_*/manuscript.md"))
)


def scrub_line(line: str) -> str:
    if line.startswith("— "):
        line = line[2:]
    line = line.replace(" — ", ", ")
    line = line.replace("—", ",")
    line = line.replace("; ", ". ")
    line = line.replace(";", ".")
    return line


def scrub_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    new_lines = [scrub_line(line) for line in original.split("\n")]
    new_text = "\n".join(new_lines)
    if new_text == original:
        return 0
    path.write_text(new_text, encoding="utf-8")
    # Count replacements made (sum across both characters)
    return (original.count("—") - new_text.count("—")) + (
        original.count(";") - new_text.count(";")
    )


def main() -> None:
    total = 0
    for path in TARGETS:
        n = scrub_file(path)
        rel = path.relative_to(ROOT)
        if n:
            print(f"{rel}: {n} replacements")
            total += n
        else:
            print(f"{rel}: clean (no changes)")
    print(f"\nTotal: {total} replacements across {len(TARGETS)} files")


if __name__ == "__main__":
    main()

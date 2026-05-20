#!/usr/bin/env python3
"""
Render a single product's cover with multiple --accent colors so they can be
compared side-by-side. Useful when picking the brand accent direction.

The script temporarily edits scripts/templates/product.css to swap the
--accent hex, renders to a preview PDF (does NOT touch the canonical
product.pdf), converts page 1 to PNG, and restores the CSS at the end.

Usage:
    python scripts/color_preview.py
        Defaults to P03 + the 4 candidate colors (sage, umber, clay, plum).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "scripts" / "templates" / "product.css"
PRODUCT_DIR = ROOT / "products" / "P03_slow-motherhood-planner"

# Candidate accent colors. forest #3B6B5A is the current setting in product.css
# (already rendered as p03_forest_v2-01.png), so it's not re-rendered here.
COLORS = {
    "sage":  "#8C9B7A",   # B - Sage-only (existing brand palette color)
    "umber": "#6D4C2D",   # C - Dusty umber (rich warm brown)
    "clay":  "#9C5544",   # D - Muted clay (less orangey terracotta)
    "plum":  "#735060",   # E - Plum / maroon
}


def main() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    from render import render_one  # noqa: E402

    original_css = CSS.read_text(encoding="utf-8")
    accent_pattern = re.compile(r"(--accent:\s+)#[0-9A-Fa-f]+")

    try:
        for name, hex_val in COLORS.items():
            modified = accent_pattern.sub(rf"\1{hex_val}", original_css, count=1)
            CSS.write_text(modified, encoding="utf-8")

            pdf_out = ROOT / f"p03_{name}_preview.pdf"
            render_one(PRODUCT_DIR, output=pdf_out)

            png_prefix = ROOT / f"p03_{name}"
            subprocess.run(
                [
                    "pdftoppm", "-r", "130", "-png",
                    "-f", "1", "-l", "1",
                    str(pdf_out), str(png_prefix),
                ],
                check=True,
            )
            print(f"  {name:<6} {hex_val}  ->  p03_{name}-01.png")
    finally:
        CSS.write_text(original_css, encoding="utf-8")
        print("CSS restored to original.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Render product content.md → product.pdf via WeasyPrint.

Usage:
    python scripts/render.py products/P02_saying-no-scripts/
    python scripts/render.py --all                # render every product
    python scripts/render.py --size A4            # default is US Letter

Requires:
    pip install weasyprint markdown jinja2

This script reads `content.md`, applies the brand stylesheet, and writes
`product.pdf` into the product's folder. It also writes `product_a4.pdf`
when `--size both` is passed.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import markdown
    from jinja2 import Template
    from weasyprint import HTML, CSS
except ImportError as e:
    sys.exit(
        f"Missing dependency: {e}\n"
        "Install with: pip install weasyprint markdown jinja2"
    )

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "scripts" / "templates" / "product.html.j2"
STYLESHEET_PATH = ROOT / "scripts" / "templates" / "product.css"


def render_one(product_dir: Path, size: str = "letter") -> Path:
    """Render content.md in `product_dir` to product.pdf. Returns output path."""
    content_md = product_dir / "content.md"
    if not content_md.exists():
        raise FileNotFoundError(f"No content.md in {product_dir}")

    md_text = content_md.read_text(encoding="utf-8")

    # Convert markdown to HTML.
    body_html = markdown.markdown(
        md_text,
        extensions=["extra", "smarty", "sane_lists", "toc"],
        output_format="html5",
    )

    # Wrap in our brand template.
    template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    template = Template(template_text)
    page_size = "A4" if size == "a4" else "Letter"
    html_doc = template.render(body=body_html, page_size=page_size)

    # Output path.
    suffix = "" if size == "letter" else f"_{size}"
    output = product_dir / f"product{suffix}.pdf"

    # Render to PDF with our stylesheet applied.
    css = CSS(filename=str(STYLESHEET_PATH))
    HTML(string=html_doc, base_url=str(ROOT)).write_pdf(
        target=str(output), stylesheets=[css]
    )

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "product_dir",
        nargs="?",
        help="Path to a product folder (containing content.md)",
    )
    parser.add_argument(
        "--all", action="store_true", help="Render every product in products/"
    )
    parser.add_argument(
        "--size",
        choices=["letter", "a4", "both"],
        default="letter",
        help="Page size (default: letter)",
    )
    args = parser.parse_args()

    sizes = ["letter", "a4"] if args.size == "both" else [args.size]

    if args.all:
        targets = sorted((ROOT / "products").glob("P*_*"))
    elif args.product_dir:
        targets = [Path(args.product_dir).resolve()]
    else:
        parser.error("Pass a product directory or --all")

    for target in targets:
        if not target.is_dir():
            print(f"skip (not a directory): {target}")
            continue
        print(f"rendering {target.name}...", end=" ", flush=True)
        for size in sizes:
            try:
                out = render_one(target, size=size)
                print(f"→ {out.relative_to(ROOT)}", end=" ")
            except FileNotFoundError as e:
                print(f"\n  {e}")
                break
        print()


if __name__ == "__main__":
    main()

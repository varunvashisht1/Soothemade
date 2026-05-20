#!/usr/bin/env python3
"""
Render product content.md → product.pdf via WeasyPrint.

Usage:
    python scripts/render.py products/P02_saying-no-scripts/
    python scripts/render.py --all                # render every product
    python scripts/render.py --size A4            # default is US Letter
    python scripts/render.py --size both          # both letter + a4

When a sibling web.md exists, its frontmatter drives the cover page
(title, code, specs, summary). The first H1 of content.md is dropped
to avoid duplication; the body content starts on its own page after
the cover. A back-cover colophon is appended automatically.

Requires:
    pip install weasyprint markdown jinja2 python-frontmatter
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import frontmatter
    import markdown
    from jinja2 import Template
    from weasyprint import HTML, CSS
except ImportError as e:
    sys.exit(
        f"Missing dependency: {e}\n"
        "Install with: pip install weasyprint markdown jinja2 python-frontmatter"
    )

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "scripts" / "templates" / "product.html.j2"
STYLESHEET_PATH = ROOT / "scripts" / "templates" / "product.css"
PDFS_DIR = ROOT / "pdfs"  # Flat folder mirror, one PDF per product, named by slug


def load_meta(product_dir: Path) -> dict | None:
    """Return product metadata from sibling web.md, or None."""
    web_md = product_dir / "web.md"
    if not web_md.exists():
        return None
    return dict(frontmatter.load(web_md).metadata)


def strip_first_h1(body_html: str) -> tuple[str, str]:
    """Strip the first <h1>...</h1> from body_html and return (h1_text, rest)."""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body_html, flags=re.DOTALL | re.IGNORECASE)
    if not m:
        return "", body_html
    title = m.group(1).strip()
    rest = body_html[: m.start()] + body_html[m.end():]
    return title, rest


def strip_leading_italic_para(body_html: str) -> tuple[str, str]:
    """Pull off the first <p><em>...</em></p> (the subtitle) if present."""
    m = re.search(
        r"^\s*<p[^>]*>\s*<em>(.*?)</em>\s*</p>\s*",
        body_html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return "", body_html
    return m.group(1).strip(), body_html[m.end():]


def render_one(product_dir: Path, size: str = "letter", output: Path | None = None) -> Path:
    """Render content.md in `product_dir` to PDF. Returns output path.

    If `output` is None, writes to `product_dir/product.pdf` (or
    `product_dir/product_<size>.pdf` for non-letter). If `output` is given,
    writes there directly — useful when the canonical product.pdf is locked
    by a viewer and you want to preview without overwriting it.
    """
    content_md = product_dir / "content.md"
    if not content_md.exists():
        raise FileNotFoundError(f"No content.md in {product_dir}")

    md_text = content_md.read_text(encoding="utf-8")

    body_html = markdown.markdown(
        md_text,
        extensions=["extra", "smarty", "sane_lists", "toc"],
        output_format="html5",
    )

    meta = load_meta(product_dir) or {}

    # Cover content. Prefer web.md metadata; fall back to content.md's H1+subtitle.
    h1_text, body_html = strip_first_h1(body_html)
    subtitle_text, body_html = strip_leading_italic_para(body_html)

    cover = {
        "title": meta.get("title") or h1_text or product_dir.name,
        "code": meta.get("code") or "",
        "specs": meta.get("specs") or "",
        "subtitle": meta.get("summary") or subtitle_text or "",
        "tagline": meta.get("tagline") or "",
        "ymyl": bool(meta.get("ymyl")),
    }

    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    page_size = "A4" if size == "a4" else "Letter"
    html_doc = template.render(
        body=body_html,
        cover=cover,
        page_size=page_size,
    )

    if output is None:
        suffix = "" if size == "letter" else f"_{size}"
        output = product_dir / f"product{suffix}.pdf"

    css = CSS(filename=str(STYLESHEET_PATH))
    HTML(string=html_doc, base_url=str(ROOT)).write_pdf(
        target=str(output), stylesheets=[css]
    )

    # Mirror to flat pdfs/ folder, named by product directory (e.g.
    # P07_newborn-survival-planner.pdf). Only for canonical letter-size
    # renders to the default path, not for --output overrides or A4 variants.
    is_canonical = (
        output == product_dir / "product.pdf" and size == "letter"
    )
    if is_canonical:
        PDFS_DIR.mkdir(exist_ok=True)
        mirror = PDFS_DIR / f"{product_dir.name}.pdf"
        mirror.write_bytes(output.read_bytes())

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("product_dir", nargs="?")
    parser.add_argument("--all", action="store_true", help="Render every product")
    parser.add_argument(
        "--size", choices=["letter", "a4", "both"], default="letter"
    )
    parser.add_argument(
        "--output",
        help="Override output path (single-product mode only). Useful when the "
        "canonical product.pdf is locked by a viewer.",
    )
    args = parser.parse_args()

    sizes = ["letter", "a4"] if args.size == "both" else [args.size]

    if args.all:
        targets = sorted((ROOT / "products").glob("P*_*"))
    elif args.product_dir:
        targets = [Path(args.product_dir).resolve()]
    else:
        parser.error("Pass a product directory or --all")

    override_output = Path(args.output).resolve() if args.output else None
    if override_output and (args.all or len(targets) > 1):
        parser.error("--output only valid for a single product")

    for target in targets:
        if not target.is_dir():
            print(f"skip (not a directory): {target}")
            continue
        print(f"rendering {target.name}...", end=" ", flush=True)
        for size in sizes:
            try:
                out = render_one(target, size=size, output=override_output)
                print(f"→ {out}", end=" ")
            except FileNotFoundError as e:
                print(f"\n  {e}")
                break
        print()


if __name__ == "__main__":
    main()

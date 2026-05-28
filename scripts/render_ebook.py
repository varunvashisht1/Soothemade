#!/usr/bin/env python3
"""
Render a Soothemade Press ebook from a B-folder.

For a folder `ebooks/Bnn_<slug>/`, produces:
  cover.png       (1600 x 2560, rendered from cover.html via WeasyPrint)
  book.epub       (Pandoc-generated, with cover embedded)

Usage (intended to run inside the `soothemade-ebook` Docker image):

    docker run --rm -v /c/Users/varun/Documents/GitHub/Soothemade:/work \\
        soothemade-ebook python scripts/render_ebook.py \\
        ebooks/B01_30-scripts-postpartum-visitor/

Outside Docker, requires: weasyprint, poppler-utils (pdftoppm), pandoc.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def render_cover(book_dir: Path) -> Path:
    """Render cover.html to cover.png at 1600x2560."""
    cover_html = book_dir / "cover.html"
    cover_pdf = book_dir / "cover.pdf"
    cover_png = book_dir / "cover.png"

    if not cover_html.exists():
        sys.exit(f"Missing {cover_html}")

    print(f"Rendering cover: {cover_html.name} -> {cover_png.name}")

    # WeasyPrint: HTML -> PDF
    from weasyprint import HTML

    HTML(str(cover_html)).write_pdf(str(cover_pdf))

    # pdftoppm: PDF -> PNG at 96 dpi (matches the @page size in CSS pixels)
    # We render to a stem and pdftoppm appends "-1" for the single page.
    stem = book_dir / "cover_tmp"
    subprocess.run(
        ["pdftoppm", "-r", "96", "-png", "-f", "1", "-l", "1", str(cover_pdf), str(stem)],
        check=True,
    )
    # pdftoppm naming: "cover_tmp-1.png" (or "cover_tmp-01.png" depending on page count)
    candidates = sorted(book_dir.glob("cover_tmp-*.png"))
    if not candidates:
        sys.exit("pdftoppm produced no output")
    candidates[0].rename(cover_png)

    # Clean up intermediate
    cover_pdf.unlink(missing_ok=True)

    return cover_png


def render_epub(book_dir: Path) -> Path:
    """Run Pandoc to convert manuscript.md + metadata.yaml -> book.epub."""
    manuscript = book_dir / "manuscript.md"
    metadata = book_dir / "metadata.yaml"
    book_epub = book_dir / "book.epub"
    epub_css = book_dir / "epub.css"

    if not manuscript.exists():
        sys.exit(f"Missing {manuscript}")
    if not metadata.exists():
        sys.exit(f"Missing {metadata}")

    print(f"Rendering ebook: {manuscript.name} -> {book_epub.name}")

    # Run pandoc from inside the book dir so relative paths in metadata
    # (e.g. css: epub.css, cover-image: cover.png) resolve correctly.
    cmd = [
        "pandoc",
        "manuscript.md",
        "--metadata-file", "metadata.yaml",
        "--from", "markdown+yaml_metadata_block+pipe_tables+raw_html",
        "--to", "epub3",
        "--standalone",
        "--toc",
        "--toc-depth=1",
        "--output", "book.epub",
    ]
    if epub_css.exists():
        cmd.extend(["--css", "epub.css"])
    cover_png = book_dir / "cover.png"
    if cover_png.exists():
        cmd.extend(["--epub-cover-image", "cover.png"])

    subprocess.run(cmd, check=True, cwd=str(book_dir))

    return book_epub


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book_dir", type=Path, help="Path like ebooks/Bnn_<slug>/")
    parser.add_argument("--skip-cover", action="store_true", help="Skip cover rendering (use existing cover.png)")
    args = parser.parse_args()

    book_dir = args.book_dir.resolve() if args.book_dir.is_absolute() else (ROOT / args.book_dir).resolve()
    if not book_dir.exists():
        sys.exit(f"Not a directory: {book_dir}")

    if not args.skip_cover:
        cover = render_cover(book_dir)
        size = cover.stat().st_size
        print(f"  cover: {cover.name} ({size:,} bytes)")

    epub = render_epub(book_dir)
    size = epub.stat().st_size
    print(f"  ebook: {epub.name} ({size:,} bytes)")
    print("Done.")


if __name__ == "__main__":
    main()

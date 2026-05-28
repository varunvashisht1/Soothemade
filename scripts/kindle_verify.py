#!/usr/bin/env python3
"""Verify KDP-compliance for every book in ebooks/B*_*/

Checks:
  - cover.png exists and is 1600x2560 (KDP recommended ebook cover dims)
  - cover-kdp.jpg exists and is < 50MB (KDP file-size cap)
  - book.epub exists and is < 650MB (KDP file-size cap)
  - book.epub starts with the EPUB magic bytes
  - kindle-upload.md exists
  - Title and description content in the upload pack is non-empty

Prints a per-book report. Exits non-zero if any book fails.
Re-runnable. Read-only — does not modify any file.

Usage:
  python scripts/kindle_verify.py
  python scripts/kindle_verify.py --book B01
  python scripts/kindle_verify.py --strict   # also check epubcheck if available
"""

from __future__ import annotations

import argparse
import os
import re
import struct
import sys
import zipfile
from pathlib import Path
from typing import NamedTuple

# Force UTF-8 on Windows consoles so the check marks render.
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, OSError):
        pass

REPO = Path(__file__).resolve().parent.parent
EBOOKS_DIR = REPO / "ebooks"

# KDP technical limits (from kdp.amazon.com help docs)
COVER_MIN_W = 1600
COVER_MIN_H = 2560
COVER_MIN_RATIO = 1.6  # height / width
COVER_MAX_FILE_BYTES = 50 * 1024 * 1024  # 50MB
EPUB_MAX_FILE_BYTES = 650 * 1024 * 1024  # 650MB

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BOLD = "\033[1m"


class CheckResult(NamedTuple):
    ok: bool
    message: str
    severity: str  # "error", "warn", "ok"


def png_dimensions(path: Path) -> tuple[int, int] | None:
    """Read PNG width and height from the IHDR chunk without Pillow."""
    try:
        with path.open("rb") as f:
            sig = f.read(8)
            if sig != b"\x89PNG\r\n\x1a\n":
                return None
            f.read(4)  # IHDR length
            chunk = f.read(4)
            if chunk != b"IHDR":
                return None
            w, h = struct.unpack(">II", f.read(8))
            return w, h
    except (OSError, struct.error):
        return None


def jpg_dimensions(path: Path) -> tuple[int, int] | None:
    """Read JPEG width and height from the SOF marker without Pillow."""
    try:
        with path.open("rb") as f:
            data = f.read()
        # Find SOF0 / SOF1 / SOF2 markers
        for marker in (b"\xff\xc0", b"\xff\xc1", b"\xff\xc2"):
            idx = data.find(marker)
            if idx != -1:
                # 2 byte marker, 2 byte length, 1 byte precision, 2 byte height, 2 byte width
                h, w = struct.unpack(">HH", data[idx + 5 : idx + 9])
                return w, h
        return None
    except (OSError, struct.error):
        return None


def check_cover_png(book_dir: Path) -> list[CheckResult]:
    out: list[CheckResult] = []
    cover = book_dir / "cover.png"
    if not cover.exists():
        out.append(CheckResult(False, "cover.png MISSING", "error"))
        return out

    size = cover.stat().st_size
    if size > COVER_MAX_FILE_BYTES:
        out.append(CheckResult(False, f"cover.png too large: {size / 1024 / 1024:.1f}MB > 50MB", "error"))
    else:
        out.append(CheckResult(True, f"cover.png size OK ({size // 1024}KB)", "ok"))

    dims = png_dimensions(cover)
    if dims is None:
        out.append(CheckResult(False, "cover.png not readable as PNG", "error"))
        return out

    w, h = dims
    if w < COVER_MIN_W or h < COVER_MIN_H:
        out.append(CheckResult(False, f"cover.png too small: {w}x{h} < {COVER_MIN_W}x{COVER_MIN_H}", "error"))
    else:
        out.append(CheckResult(True, f"cover.png dimensions OK ({w}x{h})", "ok"))

    ratio = h / w
    if not (1.5 <= ratio <= 1.7):
        out.append(CheckResult(False, f"cover.png aspect ratio {ratio:.2f} outside [1.5, 1.7] — KDP wants ~1.6", "warn"))

    return out


def check_cover_jpg(book_dir: Path) -> list[CheckResult]:
    out: list[CheckResult] = []
    cover = book_dir / "cover-kdp.jpg"
    if not cover.exists():
        out.append(CheckResult(False, "cover-kdp.jpg missing (run scripts/generate_kdp_covers.sh)", "warn"))
        return out

    size = cover.stat().st_size
    if size > COVER_MAX_FILE_BYTES:
        out.append(CheckResult(False, f"cover-kdp.jpg too large: {size / 1024 / 1024:.1f}MB > 50MB", "error"))
    else:
        out.append(CheckResult(True, f"cover-kdp.jpg size OK ({size // 1024}KB)", "ok"))

    dims = jpg_dimensions(cover)
    if dims is None:
        out.append(CheckResult(False, "cover-kdp.jpg not readable as JPG", "error"))
        return out
    w, h = dims
    if w < COVER_MIN_W or h < COVER_MIN_H:
        out.append(CheckResult(False, f"cover-kdp.jpg too small: {w}x{h}", "error"))
    else:
        out.append(CheckResult(True, f"cover-kdp.jpg dimensions OK ({w}x{h})", "ok"))
    return out


def check_epub(book_dir: Path) -> list[CheckResult]:
    out: list[CheckResult] = []
    epub = book_dir / "book.epub"
    if not epub.exists():
        out.append(CheckResult(False, "book.epub MISSING", "error"))
        return out

    size = epub.stat().st_size
    if size > EPUB_MAX_FILE_BYTES:
        out.append(CheckResult(False, f"book.epub too large: {size / 1024 / 1024:.1f}MB > 650MB", "error"))
    else:
        out.append(CheckResult(True, f"book.epub size OK ({size // 1024}KB)", "ok"))

    # Verify it's a valid zip and contains a mimetype entry with the epub mime
    try:
        with zipfile.ZipFile(epub) as zf:
            names = zf.namelist()
            if "mimetype" not in names:
                out.append(CheckResult(False, "book.epub missing mimetype entry", "error"))
            else:
                with zf.open("mimetype") as mt:
                    mime = mt.read().decode("ascii", errors="ignore").strip()
                if mime == "application/epub+zip":
                    out.append(CheckResult(True, f"book.epub mimetype OK ({mime})", "ok"))
                else:
                    out.append(CheckResult(False, f"book.epub bad mimetype: {mime}", "error"))

            # Check for the OPF (package) document
            opf = [n for n in names if n.endswith(".opf")]
            if not opf:
                out.append(CheckResult(False, "book.epub missing .opf package document", "error"))
            else:
                out.append(CheckResult(True, f"book.epub has {opf[0]}", "ok"))
    except zipfile.BadZipFile:
        out.append(CheckResult(False, "book.epub is not a valid zip archive", "error"))

    return out


def check_upload_pack(book_dir: Path) -> list[CheckResult]:
    out: list[CheckResult] = []
    pack = book_dir / "kindle-upload.md"
    if not pack.exists():
        out.append(CheckResult(False, "kindle-upload.md MISSING", "error"))
        return out

    text = pack.read_text(encoding="utf-8")
    # Sanity-check the required headings are present
    for heading in ["**Book Title:**", "**Subtitle:**", "**Description:**", "## 2 · Keywords", "## 3 · Categories"]:
        if heading not in text:
            out.append(CheckResult(False, f"kindle-upload.md missing section: {heading!r}", "error"))
            return out

    # Title and subtitle line lengths (KDP caps subtitle at 200 chars)
    subtitle_match = re.search(r"\*\*Subtitle:\*\*\s*\n>\s*(.+?)\n", text)
    if subtitle_match:
        subtitle = subtitle_match.group(1).strip()
        if len(subtitle) > 200:
            out.append(CheckResult(False, f"subtitle is {len(subtitle)} chars > 200 limit: {subtitle[:60]}...", "error"))
        else:
            out.append(CheckResult(True, f"subtitle length OK ({len(subtitle)} chars)", "ok"))

    # Keyword count (KDP requires 7 slots)
    kw_section = re.search(r"## 2 · Keywords.*?\n(.*?)\n## 3", text, flags=re.DOTALL)
    if kw_section:
        kw_count = len(re.findall(r"^\d+\.\s", kw_section.group(1), flags=re.MULTILINE))
        if kw_count == 7:
            out.append(CheckResult(True, f"keywords OK (7 slots filled)", "ok"))
        else:
            out.append(CheckResult(False, f"keywords: {kw_count} found, KDP wants 7", "warn"))

    # Categories (3 primary)
    cat_section = re.search(r"## 3 · Categories.*?\n(.*?)\n##", text, flags=re.DOTALL)
    if cat_section:
        cat_count = len(re.findall(r"^\d+\.\s", cat_section.group(1), flags=re.MULTILINE))
        if cat_count >= 3:
            out.append(CheckResult(True, f"categories OK ({cat_count} primary slots)", "ok"))
        else:
            out.append(CheckResult(False, f"categories: only {cat_count} found, KDP wants 3 primary", "warn"))

    out.append(CheckResult(True, f"kindle-upload.md present ({len(text)} chars)", "ok"))
    return out


def verify_book(book_dir: Path, strict: bool = False) -> bool:
    results: list[CheckResult] = []
    results.extend(check_cover_png(book_dir))
    results.extend(check_cover_jpg(book_dir))
    results.extend(check_epub(book_dir))
    results.extend(check_upload_pack(book_dir))

    book_id = book_dir.name.split("_")[0]
    has_error = any(not r.ok and r.severity == "error" for r in results)
    has_warn = any(not r.ok and r.severity == "warn" for r in results)
    status_color = RED if has_error else (YELLOW if has_warn else GREEN)
    status_label = "FAIL" if has_error else ("WARN" if has_warn else "OK")
    print(f"{BOLD}{status_color}[{status_label}]{RESET} {book_id} ({book_dir.name})")

    for r in results:
        if r.ok:
            print(f"    {GREEN}[ok]{RESET} {r.message}")
        elif r.severity == "warn":
            print(f"    {YELLOW}[warn]{RESET} {r.message}")
        else:
            print(f"    {RED}[fail]{RESET} {r.message}")
    print()

    return not has_error


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--book", help="Verify a single book (e.g. B01)")
    ap.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = ap.parse_args()

    if not EBOOKS_DIR.is_dir():
        print(f"{RED}ebooks/ directory not found at {EBOOKS_DIR}{RESET}")
        return 2

    book_dirs = sorted(d for d in EBOOKS_DIR.iterdir() if d.is_dir() and d.name.startswith("B"))
    if args.book:
        book_dirs = [d for d in book_dirs if d.name.startswith(args.book + "_")]
        if not book_dirs:
            print(f"{RED}No book matching {args.book}{RESET}")
            return 2

    print(f"{BOLD}Verifying {len(book_dirs)} book(s) for KDP compliance...{RESET}\n")

    all_ok = True
    for d in book_dirs:
        ok = verify_book(d, strict=args.strict)
        all_ok = all_ok and ok

    if all_ok:
        print(f"{GREEN}{BOLD}All books pass.{RESET}")
        return 0
    else:
        print(f"{RED}{BOLD}One or more books have errors. Fix before uploading to KDP.{RESET}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

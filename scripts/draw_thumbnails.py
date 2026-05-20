"""
Hand-composed product thumbnails using Pillow primitives.

Why this exists: the Canva `generate-design` recipe documented in
publishing/thumbnail-batch-brief.md drifted (with brand_kit_id it produces
typography cards; without it, multi-photo collages). Rather than fight the
tool, we draw the same compositional vocabulary directly — sage linen surface,
top-down still life, cream booklet/cards/journal centred, accent objects from
the brand vocabulary (eucalyptus sprig, mug, folded cloth, pen).

Output for each product code:
  marketing/mockups/raw/Pnn_final.png   1080x1350 raw (preserved for Pinterest)
  site/public/products/Pnn.jpg          800x1000  q85 (consumed by the site)

Run: py scripts/draw_thumbnails.py P33
     py scripts/draw_thumbnails.py P33 P34 P35 P36 P37 P38
     py scripts/draw_thumbnails.py --all
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# ---------------------------------------------------------------------------
# Palette — cool sage + warm cream, matching site --card #f1ead4 and brand sage
# ---------------------------------------------------------------------------

LINEN          = (188, 199, 163)   # base sage linen
LINEN_LIGHT    = (200, 211, 174)   # subtle highlight tile
LINEN_DARK     = (174, 185, 149)   # subtle shadow tile
CARD_CREAM     = (241, 234, 212)   # softcover cream (matches site --card)
CARD_CREAM_EDGE= (216, 208, 184)   # cream edge / spine shadow
CLOTH_SAGE     = (154, 168, 136)   # folded muslin, darker than linen
CLOTH_FOLD     = (138, 152, 121)   # fold line
SAGE_DEEP      = (125, 142, 106)   # eucalyptus stem + leaf
SAGE_LEAF      = (140, 158, 122)   # leaf body
SAGE_LEAF_HI   = (165, 182, 145)   # leaf highlight
MUG_CREAM      = (237, 228, 207)   # ceramic body
MUG_RIM        = (220, 211, 188)   # inner rim
MUG_TEA        = (152, 130, 96)    # tea liquid (cool brown)
PEN_BODY       = (76, 68, 54)      # dark umber
PEN_CLIP       = (140, 155, 122)   # sage clip
DISH_CREAM     = (228, 219, 196)   # small saucer
INK_FAINT      = (90, 104, 69)     # for subtle marks


# ---------------------------------------------------------------------------
# Canvas — render at 2x then downsample for antialiased edges
# ---------------------------------------------------------------------------

RENDER_W, RENDER_H = 2160, 2700      # 2x target
RAW_W, RAW_H       = 1080, 1350      # preserved
SITE_W, SITE_H     = 800,  1000      # site jpg

REPO_ROOT = Path(__file__).resolve().parent.parent


def new_canvas() -> Image.Image:
    return Image.new("RGB", (RENDER_W, RENDER_H), LINEN)


# ---------------------------------------------------------------------------
# Surface — linen background with subtle organic noise (no gradients)
# ---------------------------------------------------------------------------

def draw_linen(im: Image.Image, rng: random.Random) -> None:
    """Paint a sage linen surface: base colour + per-tile colour jitter + grain."""
    base = Image.new("RGB", im.size, LINEN)
    im.paste(base)

    # Subtle horizontal "warp" stripes — barely perceptible weave hint
    d = ImageDraw.Draw(im)
    for y in range(0, im.size[1], 6):
        shade = LINEN_DARK if (y // 6) % 2 == 0 else LINEN_LIGHT
        # very low-contrast 1px line
        for x in range(0, im.size[0], 1):
            if rng.random() < 0.18:
                r, g, b = im.getpixel((x, y))
                tr, tg, tb = shade
                # blend 8% toward shade
                im.putpixel((x, y), (
                    int(r * 0.92 + tr * 0.08),
                    int(g * 0.92 + tg * 0.08),
                    int(b * 0.92 + tb * 0.08),
                ))

    # Tiny fibre flecks
    for _ in range(4200):
        x = rng.randint(0, im.size[0] - 1)
        y = rng.randint(0, im.size[1] - 1)
        v = rng.choice((LINEN_LIGHT, LINEN_DARK))
        d.point((x, y), fill=v)

    # Cluster a few darker "shadowed" patches for organic feel
    for _ in range(28):
        cx = rng.randint(50, im.size[0] - 50)
        cy = rng.randint(50, im.size[1] - 50)
        r = rng.randint(40, 90)
        for _ in range(rng.randint(40, 90)):
            ox = rng.randint(-r, r)
            oy = rng.randint(-r, r)
            if ox * ox + oy * oy <= r * r:
                d.point((cx + ox, cy + oy), fill=LINEN_DARK)


# ---------------------------------------------------------------------------
# Objects — drawn into a separate transparent layer so we can rotate / blur
#           individual pieces and composite cleanly onto the linen.
# ---------------------------------------------------------------------------

def _rotate_alpha(layer: Image.Image, angle: float) -> Image.Image:
    return layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)


def _paste_layer(canvas: Image.Image, layer: Image.Image, pos: tuple[int, int]) -> None:
    canvas.paste(layer, pos, layer)


def make_booklet(
    w: int, h: int, cover: tuple[int, int, int] = CARD_CREAM,
    edge: tuple[int, int, int] = CARD_CREAM_EDGE,
    spine_side: str = "left",
) -> Image.Image:
    """A closed softcover booklet, top-down. Plain cream cover, no text."""
    pad = 20
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0 = pad, pad
    x1, y1 = pad + w, pad + h

    # subtle paper edge — slightly darker rectangle 4px wider/taller behind the cover
    d.rectangle((x0 - 4, y0 - 4, x1 + 4, y1 + 4), fill=edge)
    # cover
    d.rectangle((x0, y0, x1, y1), fill=cover)
    # spine line — a thin darker band along one side suggesting binding
    if spine_side == "left":
        d.rectangle((x0, y0, x0 + 10, y1), fill=edge)
    else:
        d.rectangle((x1 - 10, y0, x1, y1), fill=edge)
    # interior shadow rim 3px in from edges, very subtle
    d.rectangle((x0 + 3, y0 + 3, x1 - 3, y1 - 3), outline=edge, width=1)

    # debossed quarter-fold suggestion: faint horizontal hairline in middle, very low contrast
    mid_y = (y0 + y1) // 2
    d.line((x0 + 30, mid_y, x1 - 30, mid_y),
           fill=(edge[0] - 6, edge[1] - 6, edge[2] - 6), width=1)
    return layer


def make_card_fan(
    n: int, card_w: int, card_h: int, rng: random.Random,
) -> Image.Image:
    """A loose fan of n cream cards spread on the surface."""
    pad = card_w
    layer = Image.new("RGBA", (card_w * 3, card_h * 2 + pad), (0, 0, 0, 0))
    cx, cy = layer.size[0] // 2, layer.size[1] - card_h // 2 - 20

    for i in range(n):
        angle = -22 + i * (44 / max(1, n - 1)) + rng.uniform(-2, 2)
        card = make_card(card_w, card_h)
        rc = _rotate_alpha(card, angle)
        px = cx - rc.size[0] // 2 + int(math.sin(math.radians(angle)) * 30)
        py = cy - rc.size[1] // 2 - 10
        layer.paste(rc, (px, py), rc)
    return layer


def make_card(w: int, h: int) -> Image.Image:
    pad = 12
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = pad, pad, pad + w, pad + h
    # edge shadow
    d.rounded_rectangle((x0 - 2, y0 - 2, x1 + 2, y1 + 2), radius=10, fill=CARD_CREAM_EDGE)
    # face
    d.rounded_rectangle((x0, y0, x1, y1), radius=10, fill=CARD_CREAM)
    # inner hairline
    d.rounded_rectangle((x0 + 4, y0 + 4, x1 - 4, y1 - 4), radius=7,
                        outline=CARD_CREAM_EDGE, width=1)
    # subtle horizontal rule near top suggests "title area" without text
    d.line((x0 + 16, y0 + 28, x1 - 16, y0 + 28), fill=CARD_CREAM_EDGE, width=1)
    return layer


def make_mug(diameter: int) -> Image.Image:
    """Top-down mug — outer ring + inner cup with tea liquid."""
    pad = 24
    s = diameter + pad * 2
    layer = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = diameter // 2
    cx, cy = s // 2, s // 2
    # subtle edge shadow ring
    d.ellipse((cx - r - 5, cy - r - 5, cx + r + 5, cy + r + 5), fill=(170, 178, 154))
    # ceramic body
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=MUG_CREAM)
    # inner wall
    iw = int(r * 0.86)
    d.ellipse((cx - iw, cy - iw, cx + iw, cy + iw), fill=MUG_RIM)
    # tea liquid
    tw = int(r * 0.78)
    d.ellipse((cx - tw, cy - tw, cx + tw, cy + tw), fill=MUG_TEA)
    # faint highlight crescent on tea
    hw = int(r * 0.6)
    hx, hy = cx - int(r * 0.18), cy - int(r * 0.22)
    d.ellipse((hx - hw // 2, hy - hw // 2 - 4, hx + hw // 2, hy + hw // 2 - 4),
              fill=(168, 146, 110))
    return layer


def make_dish(diameter: int) -> Image.Image:
    pad = 16
    s = diameter + pad * 2
    layer = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = diameter // 2
    cx, cy = s // 2, s // 2
    d.ellipse((cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4), fill=(170, 178, 154))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=DISH_CREAM)
    ir = int(r * 0.72)
    d.ellipse((cx - ir, cy - ir, cx + ir, cy + ir), outline=CARD_CREAM_EDGE, width=2)
    return layer


def make_folded_cloth(w: int, h: int) -> Image.Image:
    pad = 18
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = pad, pad, pad + w, pad + h
    # under-shadow strip — slightly shifted darker rect for "fold thickness"
    d.rectangle((x0 + 6, y1 - 10, x1 + 6, y1 + 6), fill=CLOTH_FOLD)
    # cloth body
    d.rectangle((x0, y0, x1, y1), fill=CLOTH_SAGE)
    # fold lines — three parallel hairlines
    for frac in (0.32, 0.55, 0.78):
        ly = int(y0 + (y1 - y0) * frac)
        d.line((x0 + 12, ly, x1 - 12, ly), fill=CLOTH_FOLD, width=2)
    # corner crease
    d.line((x0, y0, x0 + 26, y0 + 26), fill=CLOTH_FOLD, width=2)
    return layer


def make_pen(length: int, thickness: int = 18) -> Image.Image:
    pad = 14
    w = length + pad * 2
    h = thickness + pad * 2
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0 = pad, pad
    x1, y1 = pad + length, pad + thickness
    # body
    d.rounded_rectangle((x0, y0, x1, y1), radius=thickness // 2, fill=PEN_BODY)
    # tip cone (right end)
    d.polygon([
        (x1 - thickness // 2, y0),
        (x1 + thickness, y0 + thickness // 2),
        (x1 - thickness // 2, y1),
    ], fill=PEN_BODY)
    # clip — a sage band near the cap
    clip_x = x0 + int(length * 0.18)
    d.rectangle((clip_x, y0 - 4, clip_x + int(length * 0.06), y1 + 4), fill=PEN_CLIP)
    return layer


def make_eucalyptus_sprig(stem_len: int, n_leaves: int = 6) -> Image.Image:
    """A small eucalyptus branch using the brand-sprig vocabulary, scaled up
    with multiple leaves alternating along the stem."""
    pad = 80
    layer = Image.new("RGBA", (stem_len + pad * 2, stem_len + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # stem — a soft curve drawn as many small segments
    cx0, cy0 = pad + 40, layer.size[1] - pad
    cx1, cy1 = pad + stem_len // 2 + 8, pad
    pts = []
    steps = 60
    for i in range(steps + 1):
        t = i / steps
        # quadratic-ish bend to mimic the brand sprig path
        bx = (1 - t) ** 2 * cx0 + 2 * (1 - t) * t * (cx0 + 30) + t ** 2 * cx1
        by = (1 - t) ** 2 * cy0 + 2 * (1 - t) * t * (cy0 - stem_len * 0.55) + t ** 2 * cy1
        pts.append((bx, by))
    for (a, b) in zip(pts, pts[1:]):
        d.line([a, b], fill=SAGE_DEEP, width=4)
    # leaves along the stem, alternating sides — sized largest mid-stem
    for i, (px, py) in enumerate(pts[5:-5:max(1, (steps - 10) // n_leaves)]):
        side = 1 if i % 2 == 0 else -1
        # leaf direction roughly perpendicular to stem segment
        if i + 5 < len(pts) - 1:
            sx, sy = pts[i * max(1, (steps - 10) // n_leaves) + 5]
            ex, ey = pts[i * max(1, (steps - 10) // n_leaves) + 6]
            dx, dy = ex - sx, ey - sy
        else:
            dx, dy = 0, -1
        ang = math.degrees(math.atan2(dy, dx)) + 90 * side
        size_frac = 1.0 - abs(i / max(1, n_leaves) - 0.5) * 0.8  # bigger in middle
        leaf_w = int(80 * size_frac)
        leaf_h = int(28 * size_frac)
        leaf = Image.new("RGBA", (leaf_w * 2, leaf_h * 2), (0, 0, 0, 0))
        ld = ImageDraw.Draw(leaf)
        ld.ellipse((leaf_w // 2, leaf_h // 2, leaf_w // 2 + leaf_w, leaf_h // 2 + leaf_h),
                   fill=SAGE_LEAF)
        # highlight crescent on one side
        ld.ellipse((leaf_w // 2 + 6, leaf_h // 2 + 4,
                    leaf_w // 2 + leaf_w - 10, leaf_h // 2 + leaf_h - 6),
                   fill=SAGE_LEAF_HI)
        rleaf = _rotate_alpha(leaf, ang)
        layer.paste(rleaf, (int(px) - rleaf.size[0] // 2, int(py) - rleaf.size[1] // 2), rleaf)
    return layer


def make_wooden_spoon(length: int) -> Image.Image:
    """A simple wooden spoon, top-down. Used for the cookbook product."""
    pad = 30
    w = length + pad * 2
    h = int(length * 0.32) + pad * 2
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # handle
    hx0 = pad
    hx1 = pad + int(length * 0.7)
    hy = h // 2
    d.rounded_rectangle((hx0, hy - 8, hx1, hy + 8), radius=8, fill=(160, 132, 90))
    # bowl
    bowl_r = int(length * 0.18)
    bcx = pad + length - bowl_r
    d.ellipse((bcx - bowl_r, hy - bowl_r, bcx + bowl_r, hy + bowl_r), fill=(178, 148, 100))
    d.ellipse((bcx - bowl_r + 6, hy - bowl_r + 6, bcx + bowl_r - 6, hy + bowl_r - 6),
              fill=(150, 122, 80))
    return layer


# ---------------------------------------------------------------------------
# Per-product compositions
# ---------------------------------------------------------------------------

def compose_p33(rng: random.Random) -> Image.Image:
    """P33 Twin Pregnancy Week-by-Week Planner.
       Centre: a cream softcover planner, slightly off-axis.
       Around: folded sage cloth (low-left), small mug (mid-right),
               eucalyptus sprig (top-right diagonal), slim pen across booklet."""
    im = new_canvas()
    rng_local = random.Random(33)
    draw_linen(im, rng_local)

    # Booklet — slightly left-of-centre, rotated CCW
    booklet = make_booklet(880, 1180, spine_side="left")
    rot = _rotate_alpha(booklet, -3.2)
    px = RENDER_W // 2 - rot.size[0] // 2 - 90
    py = RENDER_H // 2 - rot.size[1] // 2 + 40
    _paste_layer(im, rot, (px, py))

    # Folded cloth — low-left corner peeking under the booklet
    cloth = make_folded_cloth(580, 380)
    cloth_r = _rotate_alpha(cloth, 6.5)
    _paste_layer(im, cloth_r, (90, RENDER_H - cloth_r.size[1] - 130))

    # Mug — mid-right
    mug = make_mug(320)
    _paste_layer(im, mug, (RENDER_W - 540, int(RENDER_H * 0.46)))

    # Eucalyptus — top-right diagonal
    sprig = make_eucalyptus_sprig(720, n_leaves=8)
    sprig_r = _rotate_alpha(sprig, 18)
    _paste_layer(im, sprig_r,
                 (RENDER_W - sprig_r.size[0] + 60, -120))

    # Pen — diagonal across lower portion of booklet
    pen = make_pen(620, thickness=26)
    pen_r = _rotate_alpha(pen, -28)
    _paste_layer(im, pen_r, (RENDER_W // 2 - 140, RENDER_H - 720))

    return im


# Registry — extend when adding new products
COMPOSITIONS = {
    "P33": compose_p33,
}


# ---------------------------------------------------------------------------
# Pipeline — render → downsample → grain pass → write raw + site jpg
# ---------------------------------------------------------------------------

def finalize(im: Image.Image, rng: random.Random) -> Image.Image:
    """Downsample to RAW size with high-quality filter, then add a light film grain."""
    raw = im.resize((RAW_W, RAW_H), Image.Resampling.LANCZOS)
    # slight global softening — kills any pixel-sharp edges that read as digital
    raw = raw.filter(ImageFilter.GaussianBlur(radius=0.6))
    # film grain — tiny random pixel jitter, 6% of pixels
    px = raw.load()
    for _ in range(int(RAW_W * RAW_H * 0.06)):
        x = rng.randint(0, RAW_W - 1)
        y = rng.randint(0, RAW_H - 1)
        r, g, b = px[x, y]
        j = rng.randint(-6, 6)
        px[x, y] = (
            max(0, min(255, r + j)),
            max(0, min(255, g + j)),
            max(0, min(255, b + j)),
        )
    return raw


def render(code: str) -> dict:
    if code not in COMPOSITIONS:
        raise SystemExit(f"No composition registered for {code}")
    rng = random.Random(int(code[1:]) * 977 + 13)
    big = COMPOSITIONS[code](rng)
    raw = finalize(big, rng)

    raw_path = REPO_ROOT / "marketing" / "mockups" / "raw" / f"{code}_final.png"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw.save(raw_path, "PNG", optimize=True)

    site = raw.resize((SITE_W, SITE_H), Image.Resampling.LANCZOS)
    site_path = REPO_ROOT / "site" / "public" / "products" / f"{code}.jpg"
    site_path.parent.mkdir(parents=True, exist_ok=True)
    site.save(site_path, "JPEG", quality=85, optimize=True)

    return {
        "code": code,
        "raw": raw_path,
        "site": site_path,
        "raw_bytes": raw_path.stat().st_size,
        "site_bytes": site_path.stat().st_size,
    }


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args == ["--all"]:
        codes = list(COMPOSITIONS.keys())
    else:
        codes = args
    for code in codes:
        result = render(code)
        print(f"{result['code']:>4}  raw {result['raw_bytes']:>7} B  "
              f"site {result['site_bytes']:>6} B  -> {result['site']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

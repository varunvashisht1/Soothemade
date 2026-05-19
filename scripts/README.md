# Scripts

Production scripts. Most work on Pro plan with no Claude usage.

## `render.py` — content.md → product.pdf

Renders any product's `content.md` to a polished, branded PDF via WeasyPrint.

### Setup (one-time)

```bash
pip install weasyprint markdown jinja2
```

Note: WeasyPrint also needs system libraries on Linux:
```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0
```

On macOS:
```bash
brew install pango
```

### Usage

Render one product:
```bash
python scripts/render.py products/P02_saying-no-scripts/
```

Render every product:
```bash
python scripts/render.py --all
```

Both US Letter and A4 versions:
```bash
python scripts/render.py --all --size both
```

### What it does

1. Reads `content.md` in the product folder
2. Converts markdown → HTML
3. Applies the brand stylesheet (`scripts/templates/product.css`)
4. Renders to `product.pdf` in the same folder

### Customizing per product

If a product needs a different layout (e.g., card decks with 4-up grids), drop a `source/interior.css` in the product folder. The renderer will use it if present.

(Currently the script uses one global CSS. Per-product CSS override is a TODO for Day 7.)

## Future scripts (placeholders)

- `pin_export.py` — render Pinterest pin variants from a YAML spec (Day 9 toolkit task)
- `etsy_listing_check.py` — validate Etsy listing constraints (title length, tag count) (Day 10 toolkit task)
- `inventory_sync.py` — sync `STATUS.md` published-state with Etsy/Gumroad

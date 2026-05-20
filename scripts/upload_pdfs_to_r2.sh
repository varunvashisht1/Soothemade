#!/usr/bin/env bash
# Upload every PDF in pdfs/ to R2 bucket soothemade-notes-files
# under the key products/<code>.pdf.
#
# Re-run any time content changes; R2 puts overwrite by key.
#
# Requires: wrangler logged in (npx wrangler whoami).

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUCKET="soothemade-notes-files"

cd "$REPO/site"

count=0
for pdf in "$REPO"/pdfs/P*.pdf; do
  base="$(basename "$pdf")"
  code="${base%%_*}"                 # P01_foo-bar.pdf -> P01
  key="products/${code}.pdf"
  echo "→ $code  ($(du -h "$pdf" | cut -f1))"
  npx wrangler r2 object put "${BUCKET}/${key}" \
    --file "$pdf" \
    --content-type "application/pdf"
  count=$((count + 1))
done

echo "Done. Uploaded $count PDFs to r2://${BUCKET}/products/"

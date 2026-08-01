#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

required=(
  AI_PROVENANCE.md
  PROVENANCE_TIERS.yaml
  tex/ubtprovenance.sty
  tools/apply_provenance_headers.py
  tools/verify_pdf_provenance.py
  tests/test_provenance_headers.py
)
for path in "${required[@]}"; do
  [[ -e "$path" ]] || { echo "Missing required overlay file: $path" >&2; exit 2; }
done

# Runtime debris must not enter release inventories.
find . -type d \( -name __pycache__ -o -name .pytest_cache \) -prune -exec rm -rf {} +
find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete

python3 tools/apply_provenance_headers.py --apply
python3 tools/apply_provenance_headers.py --check
python3 tools/apply_provenance_headers.py --report \
  > PROVENANCE_INVENTORY_2026-08-01.txt

# Generated wiki output must be a fixed point.
python3 tools/generate_wiki.py
before="$(find wiki -maxdepth 1 -type f -name '*.md' -print0 | sort -z | xargs -0 sha256sum)"
python3 tools/generate_wiki.py
after="$(find wiki -maxdepth 1 -type f -name '*.md' -print0 | sort -z | xargs -0 sha256sum)"
[[ "$before" == "$after" ]] || { echo 'Wiki provenance generation is not idempotent.' >&2; exit 3; }

python3 tools/verify_pdf_provenance.py --require-all
python3 tools/regenerate_sha256sums.py
sha256sum -c SHA256SUMS.txt

python3 -m pytest -q \
  tests/test_provenance_headers.py \
  tests/test_sha256sums_integrity.py \
  tests/test_no_hardcoded_constants.py \
  tests/test_gr_closure_regressions.py \
  -k 'not test_tier_map_is_signed_off'

echo
echo 'Overlay checks passed.'
echo 'AUTHOR ACTION: review every A-tier path, then fill signed_off_by,'
echo 'signed_off_date, and attested_as_of in PROVENANCE_TIERS.yaml.'
echo 'After signing, rerun tests/test_provenance_headers.py and regenerate SHA256SUMS.txt.'

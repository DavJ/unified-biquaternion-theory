#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 tools/verify_sha256sums.py \
  --file OVERLAY_MANIFEST_GR_THETA_HESSIAN_STATIC_2026-08-01.sha256 \
  --quiet

python3 tools/apply_provenance_headers.py --check
python3 tools/verify_theta_hessian_principal_symbol.py

# Inventory and integrity anchors must be refreshed before tests that assert them.
python3 tools/apply_provenance_headers.py --report \
  > PROVENANCE_INVENTORY_2026-08-01.txt
python3 tools/regenerate_sha256sums.py

python3 -m pytest -q \
  tests/test_theta_hessian_principal_symbol.py \
  tests/test_dcomposite_linearized.py \
  tests/test_gr_endgame_completion.py \
  tests/test_provenance_headers.py \
  tests/test_provenance_release_workflow.py \
  tests/test_sha256sums_integrity.py
python3 tools/verify_pdf_provenance.py --require-all

# Re-anchor after all checks so the committed integrity file matches the final tree.
python3 tools/apply_provenance_headers.py --report \
  > PROVENANCE_INVENTORY_2026-08-01.txt
python3 tools/regenerate_sha256sums.py
python3 tools/verify_sha256sums.py --quiet

printf '\nTheta-Hessian principal-symbol decision and provenance checks passed.\n'

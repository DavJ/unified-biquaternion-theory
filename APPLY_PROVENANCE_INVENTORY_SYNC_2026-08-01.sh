#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 tools/verify_sha256sums.py \
  --file OVERLAY_MANIFEST_PROVENANCE_INVENTORY_SYNC_2026-08-01.sha256 \
  --quiet

python3 tools/apply_provenance_headers.py --check
python3 tools/apply_provenance_headers.py --report \
  > PROVENANCE_INVENTORY_2026-08-01.txt
python3 tools/regenerate_sha256sums.py
python3 -m pytest -q \
  tests/test_provenance_headers.py \
  tests/test_provenance_release_workflow.py \
  tests/test_sha256sums_integrity.py
python3 tools/verify_sha256sums.py --quiet

printf '\nProvenance inventory is synchronized with the current tree.\n'

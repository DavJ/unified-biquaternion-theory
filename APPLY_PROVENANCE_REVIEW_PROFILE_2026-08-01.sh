#!/usr/bin/env bash
set -euo pipefail
exec </dev/null
export PYTHONUNBUFFERED=1
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 tools/verify_sha256sums.py \
  --file OVERLAY_MANIFEST_PROVENANCE_REVIEW_PROFILE_2026-08-01.sha256
python3 tools/apply_provenance_headers.py --check
python3 tools/apply_provenance_headers.py --report > PROVENANCE_INVENTORY_2026-08-01.txt
python3 tools/verify_provenance_review.py
python3 tools/verify_sha256sums.py --quiet

echo
echo "Orthogonal provenance review profiles are installed and synchronized."
echo "Run bash VERIFY_PROVENANCE_REVIEW_PROFILE_2026-08-01.sh for the full test/PDF audit."

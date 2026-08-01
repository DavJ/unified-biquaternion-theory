#!/usr/bin/env bash
set -euo pipefail
exec </dev/null
export PYTHONUNBUFFERED=1
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 -m pytest -q \
  tests/test_provenance_review.py \
  tests/test_provenance_headers.py \
  tests/test_provenance_release_workflow.py \
  tests/test_theta_hessian_principal_symbol.py
python3 tools/verify_pdf_provenance.py --require-all
python3 tools/verify_sha256sums.py --quiet

echo
echo "Review-profile tests, curated PDF audit and integrity checks passed."

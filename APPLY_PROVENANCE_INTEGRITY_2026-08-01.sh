#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

required=(
  tests/test_no_hardcoded_constants.py
  tests/test_sha256sums_integrity.py
  tools/forensic_fingerprint/layer2/predictors.py
  tools/regenerate_sha256sums.py
  data/reference_constants/codata_reference.json
  DATA/reference_constants/codata_reference.json
  SHA256SUMS.txt
)
for path in "${required[@]}"; do
  [[ -f "$path" ]] || { echo "Missing overlay payload: $path" >&2; exit 1; }
done

cmp --silent data/reference_constants/codata_reference.json DATA/reference_constants/codata_reference.json || {
  echo "CODATA reference mirrors differ" >&2
  exit 1
}

python3 -m pytest -q \
  tests/test_no_hardcoded_constants.py \
  tests/test_layer2_predictors_placeholder_vs_ubt.py \
  tests/test_sha256sums_integrity.py

sha256sum -c SHA256SUMS.txt

echo "CODATA provenance guard and SHA256 integrity hardening applied and verified."

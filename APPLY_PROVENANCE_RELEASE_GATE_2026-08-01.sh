#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

required=(
  PROVENANCE_TIERS.yaml
  tools/apply_provenance_headers.py
  tools/regenerate_sha256sums.py
  tools/verify_sha256sums.py
  tests/test_provenance_headers.py
  tests/test_provenance_release_workflow.py
  .github/workflows/latex_build.yml
)
for path in "${required[@]}"; do
  [[ -e "$path" ]] || { echo "Missing required release-gate file: $path" >&2; exit 2; }
done

# The overlay archive carries its own non-self-referential integrity manifest.
if [[ -f OVERLAY_MANIFEST_PROVENANCE_RELEASE_GATE_2026-08-01.sha256 ]]; then
  python3 tools/verify_sha256sums.py \
    --file OVERLAY_MANIFEST_PROVENANCE_RELEASE_GATE_2026-08-01.sha256 \
    --quiet
fi

python3 tools/apply_provenance_headers.py --apply
python3 tools/apply_provenance_headers.py --check
python3 tools/apply_provenance_headers.py --report \
  > PROVENANCE_INVENTORY_2026-08-01.txt

# Regenerate before testing because the human signature legitimately changed
# PROVENANCE_TIERS.yaml after the original provenance overlay was built.
python3 tools/regenerate_sha256sums.py

python3 -m pytest -q \
  tests/test_provenance_release_workflow.py \
  tests/test_provenance_headers.py \
  tests/test_sha256sums_integrity.py

python3 tools/verify_sha256sums.py --quiet

printf '\nSigned provenance release gate and portable checksum checks passed.\n'

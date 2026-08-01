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
  tools/verify_sha256sums.py
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

# Generated wiki output must be a fixed point. Use Python rather than the
# GNU-only sha256sum command so the check works unchanged on macOS.
wiki_digest() {
  python3 - <<'PY'
from hashlib import sha256
from pathlib import Path

digest = sha256()
for path in sorted(Path("wiki").glob("*.md")):
    rel = path.as_posix().encode("utf-8")
    data = path.read_bytes()
    digest.update(len(rel).to_bytes(4, "big"))
    digest.update(rel)
    digest.update(len(data).to_bytes(8, "big"))
    digest.update(data)
print(digest.hexdigest())
PY
}
python3 tools/generate_wiki.py
before="$(wiki_digest)"
python3 tools/generate_wiki.py
after="$(wiki_digest)"
[[ "$before" == "$after" ]] || { echo 'Wiki provenance generation is not idempotent.' >&2; exit 3; }

python3 tools/verify_pdf_provenance.py --require-all
python3 tools/regenerate_sha256sums.py
python3 tools/verify_sha256sums.py --quiet

python3 -m pytest -q \
  tests/test_provenance_headers.py \
  tests/test_sha256sums_integrity.py \
  tests/test_no_hardcoded_constants.py \
  tests/test_gr_closure_regressions.py

echo
echo 'Overlay checks passed.'
echo 'Human A-tier attestation and provenance checks passed.'

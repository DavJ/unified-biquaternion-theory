#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Remove ignored runtime debris that can leak into hand-made repository ZIPs.
find "$ROOT" -type d -name '__pycache__' -prune -exec rm -rf {} +
find "$ROOT" -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
rm -rf -- "$ROOT/.pytest_cache"
rm -f -- \
  "$ROOT/data/alpha_two_loop_grid.csv" \
  "$ROOT/reports/audit_computed_not_reference.json"

printf 'GR split-jet status synchronization and repository cache cleanup applied.\n'
printf 'Recommended validation:\n'
printf '  python3 -m pytest -q tests/test_gr_status_consistency.py tests/test_gr_endgame_completion.py tests/test_publication_canonical_status.py\n'
printf '  cd papers && latexmk -pdf -interaction=nonstopmode -halt-on-error UBT_GR_Submission.tex\n'

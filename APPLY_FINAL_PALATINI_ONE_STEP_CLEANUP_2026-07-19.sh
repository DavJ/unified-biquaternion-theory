#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

correct_tex="canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex"
correct_pdf="docs/pdfs/gap_10t_palatini_torsion_dynamics.pdf"
old_tex="canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex"
old_pdf="docs/pdfs/gap_10t_paladini_torsion_dynamics.pdf"

[[ -f "$correct_tex" ]] || { echo "ERROR: missing $correct_tex" >&2; exit 1; }
[[ -f "$correct_pdf" ]] || { echo "ERROR: missing $correct_pdf" >&2; exit 1; }

rm -f -- "$old_tex" "$old_pdf"

[[ ! -e "$old_tex" ]] || { echo "ERROR: failed to remove $old_tex" >&2; exit 1; }
[[ ! -e "$old_pdf" ]] || { echo "ERROR: failed to remove $old_pdf" >&2; exit 1; }

python3 -m pytest -q \
  tests/test_release_polish_palatini_refs.py \
  tests/test_theta_fit_tau.py \
  tests/test_planck_validation_mapping.py

echo "Final Palatini cleanup applied successfully."

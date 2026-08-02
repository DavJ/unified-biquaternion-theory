#!/usr/bin/env bash
set -euo pipefail
exec </dev/null
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
src = Path('docs/textbook/indices_torsion_anticommutator_rot_student_paper_cs.tex').read_text()
body = Path('docs/textbook/student_papers/indices_torsion_anticommutator_rot_cs.tex').read_text()
assert 'tier: C_working' in src
assert 'AI-generated educational draft' in src
assert r'\UBTTier{C}' in src
for token in [
    r'Gamma^\rho{}_{\mu\nu}',
    r'T^\rho{}_{\mu\nu}',
    r'\operatorname{rot}',
    r'\gamma_{\mu\nu}',
    r'\Sigma_{\mu\nu}',
]:
    assert token in body, token
print('Static content and Tier-C checks passed.')
PY

python3 tools/apply_provenance_headers.py --check

if command -v latexmk >/dev/null 2>&1; then
  (
    cd docs/textbook
    TEXINPUTS=../../tex: latexmk -pdf -halt-on-error -interaction=nonstopmode \
      indices_torsion_anticommutator_rot_student_paper_cs.tex >/tmp/ubt_student_indices_build.log 2>&1
  )
fi

if command -v pdfinfo >/dev/null 2>&1; then
  INFO="$(pdfinfo docs/pdfs/UBT_Studentske_texty_Indexy_torze_antikomutator_rot_2026-08-02.pdf)"
  grep -q 'Pages:.*9' <<<"$INFO"
  grep -q 'provenance tier C' <<<"$INFO"
fi

echo "Student paper source, build, PDF metadata and provenance checks passed."

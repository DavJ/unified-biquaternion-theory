#!/usr/bin/env bash
set -euo pipefail
exec </dev/null
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

sha256sum -c OVERLAY_MANIFEST_STUDENT_INDICES_TORSION_ROT_2026-08-02.sha256 >/dev/null

python3 - <<'PY'
from pathlib import Path
required = [
    Path('docs/textbook/indices_torsion_anticommutator_rot_student_paper_cs.tex'),
    Path('docs/textbook/student_papers/indices_torsion_anticommutator_rot_cs.tex'),
    Path('docs/pdfs/UBT_Studentske_texty_Indexy_torze_antikomutator_rot_2026-08-02.pdf'),
    Path('PATCH_NOTES_STUDENT_INDICES_TORSION_ANTICOMMUTATOR_ROT_2026-08-02.md'),
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing overlay files: ' + ', '.join(missing))
print('Student-paper overlay files are present.')
PY

python3 tools/apply_provenance_headers.py --check
bash VERIFY_STUDENT_INDICES_TORSION_ROT_2026-08-02.sh

echo
echo "Student paper installed under docs/textbook and docs/pdfs."

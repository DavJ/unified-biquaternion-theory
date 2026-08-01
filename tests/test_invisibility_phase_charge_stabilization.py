from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "speculative_extensions/invisibility/PHASE_CHARGE_FINITE_SCALE_STABILIZATION.md"


def test_phase_charge_verifier() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools/verify_invisibility_phase_charge_stabilization.py")],
        cwd=ROOT,
        check=True,
    )


def test_status_remains_reduced_and_noncanonical() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "EXACT REDUCED-MODEL THEOREM" in text
    assert "NONCANONICAL DYNAMICAL CANDIDATE" in text
    assert "not yet a completed machine" in text
    assert "zero-scattering" in text


def test_core_stabilisation_formulas_are_recorded() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "Q_\\alpha" in text
    assert "E_Q(\\chi)" in text
    assert "\\chi_*^6" in text
    assert "12\\sigma a_W" in text
    assert "\\chi=\\zeta R" in text

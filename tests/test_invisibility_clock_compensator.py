from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "speculative_extensions/invisibility/CLOCK_COMPENSATED_SUPPORT_GRAM.md"


def test_clock_compensator_verifier() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools/verify_invisibility_clock_compensator.py")],
        cwd=ROOT,
        check=True,
    )


def test_status_is_conditional_and_noncanonical() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "EXACT CONDITIONAL KINEMATIC THEOREM" in text
    assert "MODEL-SPECIFIC CLOCK MODE" in text
    assert "not a canonical promotion" in text
    assert "zero exterior scattering" in text


def test_core_formulas_are_recorded() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "\\mathcal N_\\Theta" in text
    assert "\\mathsf h^{\\rm clk}_{\\mu\\nu}" in text
    assert "T_\\Theta" in text
    assert "\\widehat h_{\\mu\\nu}" in text
    assert "S_{\\rm supp}^{\\rm clk}" in text

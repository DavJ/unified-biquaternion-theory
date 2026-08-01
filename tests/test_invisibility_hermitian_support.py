from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "speculative_extensions/invisibility/HERMITIAN_SUPPORT_GRAM_ROUTE.md"


def test_hermitian_support_verifier() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools/verify_invisibility_hermitian_support.py")],
        check=True,
        cwd=ROOT,
    )


def test_support_route_keeps_claim_status_honest() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "EXACT KINEMATIC RESULT / NON-CANONICAL ACTION ROUTE" in text
    assert "not declared to be the physical spacetime metric" in text
    assert "Lorentz/gauge-covariant promotion" in text
    assert "not the dynamical or invisibility closure" in text


def test_support_route_records_both_area_channels() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "dA_\\gamma=0" in text
    assert "dA_{\\mathsf h}>0" in text
    assert "det\\gamma\\big|_{R_1}=0" in text
    assert "det\\mathsf h\\big|_{R_1}>0" in text

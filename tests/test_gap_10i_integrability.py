# © 2026 Ing. David Jaroš — MIT license for code.
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_gap_10i_verifier_passes():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_gap_10i_integrability.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "ALL CHECKS PASSED" in proc.stdout
    assert "Minkowski metric" in proc.stdout
    assert "two-sided derivative" in proc.stdout


def test_gap_10i_status_is_split_honestly():
    status = (ROOT / "STATUS_OF_UBT.md").read_text(encoding="utf-8")
    claims = (ROOT / "CLAIMS.yaml").read_text(encoding="utf-8")
    paper = (ROOT / "papers" / "UBT_GR_Submission.tex").read_text(encoding="utf-8")
    for text in (status, claims, paper):
        assert "GAP-10I-SR" in text
        assert "GAP-10I-1S" in text
        assert "GAP-10I-CURVED" in text
    assert "CLOSED" in status
    assert "NO-GO" in status
    assert "two-sided" in status.lower()


def test_student_material_contains_implicit_and_transcendental_distinction():
    cz = (ROOT / "docs" / "czech" / "UBT_KOVARIANTNI_GEOMETRIE_PRO_STUDENTY_CZ.md").read_text(encoding="utf-8")
    chapter = (ROOT / "docs" / "textbook" / "chapters" / "04_covariant_tetrad_geometry.tex").read_text(encoding="utf-8")
    for text in (cz, chapter):
        low = text.lower()
        assert "implicit" in low
        assert "transcendent" in low
        assert "kontorz" in low or "contors" in low
        assert "two-sided" in low or "oboustrann" in low
        assert "christoff" in low


def test_canonical_theta_field_uses_two_sided_curved_candidate():
    paths = [
        ROOT / "canonical" / "fields" / "theta_field.tex",
        ROOT / "canonical" / "THEORY" / "math" / "fields" / "theta_field.tex",
    ]
    for path in paths:
        text = path.read_text(encoding="utf-8")
        assert r"D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu" in text
        assert "origin or unique elimination" not in text.lower()
        assert "curvature-intertwiner" in text.lower()


def test_what_is_proved_does_not_restore_superseded_gr_metric_or_lapse_claims():
    text = (ROOT / "WHAT_IS_PROVED.md").read_text(encoding="utf-8")
    assert "GAP-B-MASTER" in text
    assert "Temporal Schwarzschild lapse" in text
    assert "former phase/Maxwell wording is withdrawn" in text
    assert "g_{\\mu\\nu} = \\mathrm{Re}[\\mathrm{Tr}" not in text
    assert "Temporal component $g_{tt} = -\\Phi^2$ from complex-time" not in text

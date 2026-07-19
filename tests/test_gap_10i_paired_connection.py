# © 2026 Ing. David Jaroš — MIT license for code.
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_gap_10i_paired_connection_verifier_passes():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_gap_10i_paired_connection.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "ALL CHECKS PASSED" in proc.stdout
    assert "one Omega remains" in proc.stdout
    assert "Schwarzschild" in proc.stdout


def test_pairing_audit_has_honest_status():
    text = (ROOT / "canonical" / "gr_closure" / "gap_10i_paired_connection_audit.tex").read_text(
        encoding="utf-8"
    )
    assert "GAP-10I-PAIR-KIN: CLOSED" in text
    assert "GAP-10I-PAIR-GR: CLOSED AS A TORSION-FREE NO-GO" in text
    assert "GAP-10I-TORSION-LOCAL: CLOSED LOCALLY" in text
    assert "GAP-10D: NOT CLOSED BY THIS REDUCTION" in text
    assert r"B_\mu=-\Omega_\mu^\ddagger" in text


def test_pairing_audit_is_published_and_canonical_ledgers_are_updated():
    mapping = (ROOT / ".github" / "latex_publish_map.tsv").read_text(encoding="utf-8")
    assert "gap_10i_paired_connection_audit.pdf" in mapping
    for rel in (
        "CLAIMS.yaml",
        "STATUS_OF_UBT.md",
        "WHAT_IS_PROVED.md",
        "canonical/AXIOMS.md",
        "papers/UBT_GR_Submission.tex",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "GAP-10I-PAIR-KIN" in text
        assert "GAP-10I-PAIR-GR" in text

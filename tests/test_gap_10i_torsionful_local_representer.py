# © 2026 Ing. David Jaroš — MIT license for code.
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_torsionful_local_representer_verifier_passes():
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "verify_gap_10i_torsionful_local_representer.py"),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "ALL CHECKS PASSED" in proc.stdout
    assert "Schwarzschild exterior" in proc.stdout
    assert "NOT TESTED" in proc.stdout


def test_torsionful_audit_has_honest_split_status():
    text = (
        ROOT
        / "canonical"
        / "gr_closure"
        / "gap_10i_torsionful_local_representer.tex"
    ).read_text(encoding="utf-8")
    assert "GAP-10I-TORSION-LOCAL: CLOSED LOCALLY" in text
    assert "GAP-10I-PAIR-GR: CLOSED AS A TORSION-FREE NO-GO" in text
    assert "LOCAL KINEMATICS CLOSED; DYNAMICS/GLOBAL PART NARROWED" in text
    assert "GAP-10D and GAP-U2" in text
    assert r"K_{\nu\mu\rho}" in text


def test_status_surfaces_include_torsionful_local_subclosure():
    for rel in (
        "AGENTS.md",
        ".github/copilot-instructions.md",
        "CLAIMS.yaml",
        "STATUS_OF_UBT.md",
        "WHAT_IS_PROVED.md",
        "DERIVATION_INDEX.md",
        "canonical/AXIOMS.md",
        "canonical/CANONICAL_DEFINITIONS.md",
        "papers/UBT_GR_Submission.tex",
        "docs/czech/UBT_KOVARIANTNI_GEOMETRIE_PRO_STUDENTY_CZ.md",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "GAP-10I-TORSION-LOCAL" in text, rel


def test_pairing_no_go_is_explicitly_torsion_free_in_key_surfaces():
    for rel in (
        "AGENTS.md",
        ".github/copilot-instructions.md",
        "STATUS_OF_UBT.md",
        "WHAT_IS_PROVED.md",
        "canonical/AXIOMS.md",
        "papers/UBT_GR_Submission.tex",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "torsion-free" in text.lower(), rel
        assert "GAP-10I-PAIR-GR" in text, rel

# © 2026 Ing. David Jaroš — MIT license for code.
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_gap_10omega_verifier_passes():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_gap_10omega_connection.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "ALL CHECKS PASSED" in proc.stdout
    assert "rank 24/24" in proc.stdout


def test_gap_10omega_status_is_split_honestly():
    status = (ROOT / "STATUS_OF_UBT.md").read_text(encoding="utf-8")
    claims = (ROOT / "CLAIMS.yaml").read_text(encoding="utf-8")
    paper = (ROOT / "papers" / "UBT_GR_Submission.tex").read_text(encoding="utf-8")
    for text in (status, claims, paper):
        assert (
            "GAP-10Ω-KIN" in text
            or "GAP-10Omega-KIN" in text
            or "GAP-10$\\Omega$-KIN" in text
        )
        assert (
            "GAP-10Ω-GR" in text
            or "GAP-10Omega-GR" in text
            or "GAP-10$\\Omega$-GR" in text
        )
        assert "GAP-10T-DYN" in text
    assert "CLOSED" in status
    assert "contorsion" in status.lower()
    assert "GAP-10Ω-FULL" not in status
    assert "GAP-10Omega-FULL" not in claims


def test_agent_instructions_lock_tetrad_route():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    copilot = (ROOT / ".github" / "copilot-instructions.md").read_text(encoding="utf-8")
    for text in (agents, copilot):
        assert "E_μ" in text or "E_\\mu" in text
        assert "anticommutator" in text.lower()
        assert "fiber" in text.lower()
        assert "projection" in text.lower()
        assert "torsion" in text.lower()
        assert "two-sided" in text.lower()
        assert "GAP-10I-1S" in text

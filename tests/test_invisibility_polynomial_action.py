from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_polynomial_action_exactness_verifier() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_invisibility_polynomial_action.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "exact nonzero four-form" in result.stdout
    assert "has no bulk selection equation" in result.stdout
    assert "nonconstant central weighting" in result.stdout


def test_action_audit_keeps_physical_claim_open() -> None:
    note = (
        ROOT
        / "speculative_extensions"
        / "invisibility"
        / "POLYNOMIAL_ACTION_REGULARITY_AUDIT.md"
    ).read_text()
    assert "EXACT STRUCTURAL RESULT" in note
    assert "pure boundary term" in note
    assert "does not select the shell" in note
    assert "No particular `Xi` is promoted here" in note
    assert "finite-action on-shell shell" in note


def test_main_shell_status_points_to_action_audit() -> None:
    shell = (
        ROOT
        / "speculative_extensions"
        / "invisibility"
        / "SPHERICAL_TANGENTIAL_NULL_SHELL.md"
    ).read_text()
    assert "POLYNOMIAL_ACTION_REGULARITY_AUDIT.md" in shell
    assert "topological" in shell
    assert "non-topological action" in shell

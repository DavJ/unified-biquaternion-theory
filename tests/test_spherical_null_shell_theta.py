from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_whitney_spherical_null_shell_symbolic_verifier() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_spherical_null_shell_theta.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Whitney angular potential is globally integrable" in result.stdout
    assert "central angular metric is exactly null" in result.stdout
    assert "area form is pointwise nonzero" in result.stdout
    assert "matches flat spherical exterior" in result.stdout


def test_whitney_construction_claim_status_is_honest() -> None:
    note = (
        ROOT
        / "speculative_extensions"
        / "invisibility"
        / "WHITNEY_SPHERICAL_NULL_SHELL_THETA.md"
    ).read_text()
    assert "EXACT OFF-SHELL KINEMATIC CONSTRUCTION" in note
    assert "not on shell" in note
    assert "not yet an invisibility machine" in note
    assert "\\gamma^W_{\\theta\\theta}" in note
    assert "\\mathcal B_{S^2}\\big|_{R_1}" in note
    assert "exactly flat" in note


def test_spherical_shell_points_to_closed_integrability_step() -> None:
    shell = (
        ROOT
        / "speculative_extensions"
        / "invisibility"
        / "SPHERICAL_TANGENTIAL_NULL_SHELL.md"
    ).read_text()
    assert "WHITNEY_SPHERICAL_NULL_SHELL_THETA.md" in shell
    assert "off-shell kinematic construction is now explicit" in shell
    assert "action, stability, and zero-scattering" in shell

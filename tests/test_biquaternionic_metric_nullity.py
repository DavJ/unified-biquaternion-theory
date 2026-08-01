from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_biquaternionic_metric_nullity_verifier() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "verify_biquaternionic_metric_nullity.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "explicit gamma=0, Sigma!=0 algebraic witness" in result.stdout
    assert "pointwise metric-null rank is bounded by two" in result.stdout
    assert "four independent psi profiles give gamma_profile=0" in result.stdout


def test_invisibility_track_is_explicitly_noncanonical() -> None:
    readme = (ROOT / "speculative_extensions" / "invisibility" / "README.md").read_text()
    program = (
        ROOT
        / "speculative_extensions"
        / "invisibility"
        / "BIQUATERNIONIC_METRIC_NULLITY_PROGRAM.md"
    ).read_text()
    assert "SPECULATIVE / NON-CANONICAL" in readme
    assert "NOT CANONICAL, NOT AN ENGINEERING CLAIM" in program
    assert "gamma_{\\mu\\nu}=0" in program
    assert "Sigma_{\\mu\\nu}\\neq0" in program


def test_spherical_tangential_null_shell_is_recorded_as_speculative() -> None:
    shell = (
        ROOT
        / "speculative_extensions"
        / "invisibility"
        / "SPHERICAL_TANGENTIAL_NULL_SHELL.md"
    ).read_text()
    assert "SPECULATIVE / NON-CANONICAL" in shell
    assert "\\gamma_{AB}\\big|_{r=R_1}=0" in shell
    assert "\\mathcal B_{S^2}\\big|_{r=R_1}\\ne0" in shell
    assert "zero exterior scattering" in shell
    assert "not an on-shell UBT solution" in shell

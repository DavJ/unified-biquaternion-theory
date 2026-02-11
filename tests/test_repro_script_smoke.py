"""
Smoke tests for CMB verdict reproducibility script.

These tests validate the script's CLI and dry-run mode without requiring actual data.

License: MIT
"""

import subprocess
import sys
from pathlib import Path

import pytest


# Find repo root
def find_repo_root():
    """Find repository root from this test file."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / 'pytest.ini').exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not find repo root")


REPO_ROOT = find_repo_root()
SCRIPT = REPO_ROOT / 'scripts' / 'repro_cmb_verdict.py'


def test_script_exists():
    """Test that the reproducibility script exists."""
    assert SCRIPT.exists(), f"Script not found: {SCRIPT}"


def test_script_executable():
    """Test that the script is executable."""
    assert SCRIPT.stat().st_mode & 0o111, f"Script not executable: {SCRIPT}"


def test_help_message():
    """Test that --help works."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, "Help command failed"
    assert 'CMB verdict reproduction' in result.stdout
    assert '--mode' in result.stdout
    assert '--dry-run' in result.stdout


def test_dry_run_theory_mode():
    """Test dry-run in theory mode."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--mode', 'theory', '--dry-run'],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode == 0, f"Dry-run failed: {result.stderr}"
    assert 'DRY RUN' in result.stdout
    assert 'STEP 1: Download CMB datasets' in result.stdout
    assert 'STEP 2: Sanity check' in result.stdout
    assert 'STEP 3: Generate SHA-256 manifests' in result.stdout
    assert 'STEP 4: Validate manifests' in result.stdout
    assert 'STEP 5: Run CMB comb pipeline' in result.stdout
    assert 'STEP 6: Locate latest run' in result.stdout


def test_dry_run_obs_as_model_mode():
    """Test dry-run in obs-as-model mode."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--mode', 'obs-as-model', '--dry-run'],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode == 0, f"Dry-run failed: {result.stderr}"
    assert 'obs-as-model' in result.stdout
    assert 'DRY RUN' in result.stdout


def test_dry_run_with_custom_paths():
    """Test dry-run with custom path arguments."""
    result = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            '--planck-obs', 'custom/planck.txt',
            '--wmap-obs', 'custom/wmap.txt',
            '--dry-run'
        ],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode == 0, f"Dry-run failed: {result.stderr}"
    assert 'custom/planck.txt' in result.stdout
    assert 'custom/wmap.txt' in result.stdout


def test_dry_run_no_download():
    """Test dry-run with --no-download flag."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--no-download', '--dry-run'],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode == 0, f"Dry-run failed: {result.stderr}"
    assert 'Skipping download step' in result.stdout


def test_dry_run_custom_pipeline_params():
    """Test dry-run with custom pipeline parameters."""
    result = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            '--ell-min-planck', '50',
            '--ell-max-planck', '1000',
            '--variant', 'A',
            '--mc-samples', '5000',
            '--seed', '123',
            '--dry-run'
        ],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode == 0, f"Dry-run failed: {result.stderr}"
    assert '--ell_min_planck 50' in result.stdout
    assert '--ell_max_planck 1000' in result.stdout
    assert '--variant A' in result.stdout
    assert '--mc_samples 5000' in result.stdout
    assert '--seed 123' in result.stdout


def test_repo_root_detection():
    """Test that repo root detection works."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--dry-run'],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode == 0
    assert 'Repository root:' in result.stdout
    # Should contain the actual repo path
    assert str(REPO_ROOT) in result.stdout


def test_invalid_mode():
    """Test that invalid mode is rejected."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), '--mode', 'invalid'],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT
    )
    assert result.returncode != 0, "Should reject invalid mode"
    assert 'invalid choice' in result.stderr.lower()


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

#!/usr/bin/env python3
# tests/test_runner_integration.py
# SPDX-License-Identifier: MIT
"""
Test: Integration test for run_real_data_cmb_comb.py
=====================================================

Tests that verify the runner correctly handles:
1. Manifest validation with file matching
2. Rejection of invalid model files
3. Graceful handling of missing model files
"""
import json
import sys
import tempfile
import subprocess
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]

# Add tools to path for hash generation
sys.path.insert(0, str(repo_root / 'tools' / 'data_provenance'))
import hash_dataset


def test_runner_rejects_mismatched_manifest():
    """
    Test that runner rejects manifest that doesn't contain the exact files being used.
    """
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create minimal valid spectrum files (>50 rows to pass validation)
        obs_file = tmpdir / "obs_spectrum.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):  # 100 rows
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        model_file = tmpdir / "model_spectrum.txt"
        with open(model_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                f.write(f"{i} {950 + i*10} {50} {50}\n")
        
        # Create another file not used in the run
        other_file = tmpdir / "other_spectrum.txt"
        with open(other_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                f.write(f"{i} {900 + i*10} {50} {50}\n")
        
        # Create manifest with only obs_file and other_file (missing model_file)
        manifest = hash_dataset.hash_dataset([str(obs_file), str(other_file)])
        manifest_file = tmpdir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        # Try to run with manifest that doesn't include model_file
        runner_script = repo_root / 'forensic_fingerprint' / 'run_real_data_cmb_comb.py'
        
        cmd = [
            sys.executable, str(runner_script),
            '--planck_obs', str(obs_file),
            '--planck_model', str(model_file),
            '--planck_manifest', str(manifest_file),
            '--mc_samples', '10',  # Very small for speed
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Should fail with error about missing file in manifest
        assert result.returncode != 0, "Runner should fail when manifest doesn't contain model file"
        assert 'model_spectrum.txt' in result.stdout or 'model_spectrum.txt' in result.stderr, \
            f"Error should mention missing file. stdout: {result.stdout}, stderr: {result.stderr}"
        
        print("✓ Runner correctly rejects manifest missing required files")


def test_runner_rejects_likelihood_file():
    """
    Test that runner rejects parameter/likelihood files as model input.
    
    This test verifies content-based rejection (not filename-based).
    """
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create valid observation file
        obs_file = tmpdir / "obs_spectrum.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        # Create invalid "model" file (likelihood/parameter file)
        # The file contains -log(Like) in the actual data, not just header
        invalid_model = tmpdir / "likelihood_params.txt"
        with open(invalid_model, 'w') as f:
            f.write("# L  -log(Like)  Chi2\n")
            # Put -log(Like) in the actual data content
            f.write("2  -log(Like)=1234.56  100.0\n")
            for i in range(30, 130):
                f.write(f"{i} {1234.56 + i*0.1} {100.0}\n")
        
        runner_script = repo_root / 'forensic_fingerprint' / 'run_real_data_cmb_comb.py'
        
        cmd = [
            sys.executable, str(runner_script),
            '--planck_obs', str(obs_file),
            '--planck_model', str(invalid_model),
            '--mc_samples', '10',
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Should fail with error about invalid model file (content-based check)
        assert result.returncode != 0, "Runner should reject likelihood/parameter file as model"
        assert '-log(like)' in result.stdout.lower() or 'loglike' in result.stdout.lower() or \
               '-log(like)' in result.stderr.lower() or 'loglike' in result.stderr.lower(), \
            f"Error should mention likelihood content. stdout: {result.stdout}, stderr: {result.stderr}"
        
        print("✓ Runner correctly rejects likelihood/parameter file as model")


def test_runner_accepts_valid_setup():
    """
    Test that runner accepts valid observation file with matching manifest.
    
    Note: This test might take a few seconds due to actual analysis.
    """
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create valid spectrum file
        obs_file = tmpdir / "valid_spectrum.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):  # 100 multipoles
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        # Create manifest with the observation file
        manifest = hash_dataset.hash_dataset([str(obs_file)])
        manifest_file = tmpdir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        # Create output directory
        output_dir = tmpdir / "output"
        
        runner_script = repo_root / 'forensic_fingerprint' / 'run_real_data_cmb_comb.py'
        
        cmd = [
            sys.executable, str(runner_script),
            '--planck_obs', str(obs_file),
            '--planck_manifest', str(manifest_file),
            '--mc_samples', '10',  # Very small for speed
            '--output_dir', str(output_dir),
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        # Should succeed
        if result.returncode != 0:
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            assert False, f"Runner should succeed with valid setup. Return code: {result.returncode}"
        
        # Check output files were created
        assert (output_dir / 'planck_results.json').exists(), "Results JSON should be created"
        assert (output_dir / 'combined_verdict.md').exists(), "Verdict report should be created"
        
        print("✓ Runner successfully processes valid setup with matching manifest")


if __name__ == "__main__":
    print("Testing Runner Integration")
    print("=" * 80)
    
    test_runner_rejects_mismatched_manifest()
    test_runner_rejects_likelihood_file()
    test_runner_accepts_valid_setup()
    
    print("=" * 80)
    print("✓ All runner integration tests passed!")

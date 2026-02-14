#!/usr/bin/env python3
"""
Tests for Layer2 Rigidity Experiment Runner
============================================

Tests the multi-scale stability experiment tool.

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

import json
import subprocess
import sys
from pathlib import Path
import tempfile

# Add repository root to path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))


def test_rigidity_experiment_help():
    """Test that the rigidity experiment tool shows help."""
    result = subprocess.run(
        ['python3', 'forensic_fingerprint/tools/layer2_rigidity_experiment.py', '--help'],
        cwd=repo_root,
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"Help command failed: {result.stderr}"
    assert "Layer 2 Rigidity Experiment" in result.stdout
    assert "--samples" in result.stdout
    assert "--mapping" in result.stdout
    assert "--seed" in result.stdout
    assert "--space" in result.stdout


def test_rigidity_experiment_dry_run():
    """Test that the rigidity experiment runs successfully with minimal samples."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            [
                'python3', 'forensic_fingerprint/tools/layer2_rigidity_experiment.py',
                '--samples', '5',
                '--mapping', 'placeholder',
                '--seed', '999',
                '--space', 'debug',
                '--outdir', tmpdir
            ],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Check command succeeded
        assert result.returncode == 0, f"Experiment failed: {result.stderr}"
        
        # Check output contains expected patterns
        assert "Layer 2 Rigidity Experiment" in result.stdout
        assert "EXPERIMENT COMPLETE" in result.stdout
        assert "Verdict:" in result.stdout
        
        # Check files were created
        exp_dirs = list(Path(tmpdir).glob("rigidity_experiment_*"))
        assert len(exp_dirs) == 1, f"Expected 1 experiment dir, found {len(exp_dirs)}"
        
        exp_dir = exp_dirs[0]
        
        # Check main output files exist
        assert (exp_dir / "VERDICT.md").exists(), "VERDICT.md not created"
        assert (exp_dir / "stability_metrics.json").exists(), "stability_metrics.json not created"
        
        # Check scale directories exist
        assert (exp_dir / "scale_0.8").exists(), "scale_0.8 directory not created"
        assert (exp_dir / "scale_1.0").exists(), "scale_1.0 directory not created"
        assert (exp_dir / "scale_1.2").exists(), "scale_1.2 directory not created"
        
        # Check each scale has expected files
        for scale in ["0.8", "1.0", "1.2"]:
            scale_dir = exp_dir / f"scale_{scale}"
            assert (scale_dir / "configurations.csv").exists(), f"scale_{scale}/configurations.csv missing"
            assert (scale_dir / "summary.json").exists(), f"scale_{scale}/summary.json missing"
            assert (scale_dir / "results.txt").exists(), f"scale_{scale}/results.txt missing"


def test_rigidity_experiment_verdict_content():
    """Test that VERDICT.md has expected content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            [
                'python3', 'forensic_fingerprint/tools/layer2_rigidity_experiment.py',
                '--samples', '5',
                '--mapping', 'placeholder',
                '--seed', '999',
                '--space', 'debug',
                '--outdir', tmpdir
            ],
            cwd=repo_root,
            capture_output=True,
            timeout=60
        )
        
        exp_dir = list(Path(tmpdir).glob("rigidity_experiment_*"))[0]
        verdict_path = exp_dir / "VERDICT.md"
        
        with open(verdict_path, 'r') as f:
            verdict_content = f.read()
        
        # Check key sections are present
        assert "# Layer 2 Rigidity Experiment" in verdict_content
        assert "## Experiment Configuration" in verdict_content
        assert "## Results by Scale" in verdict_content
        assert "## Stability Metrics" in verdict_content
        assert "## Robustness Verdict" in verdict_content
        assert "## Interpretation" in verdict_content
        
        # Check scales are present in table
        assert "0.8" in verdict_content
        assert "1.0" in verdict_content
        assert "1.2" in verdict_content
        
        # Check verdict is present (STABLE or UNSTABLE)
        assert "STABLE" in verdict_content or "UNSTABLE" in verdict_content
        
        # Check placeholder warning is present
        assert "PLACEHOLDER" in verdict_content


def test_rigidity_experiment_stability_metrics():
    """Test that stability_metrics.json has correct structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            [
                'python3', 'forensic_fingerprint/tools/layer2_rigidity_experiment.py',
                '--samples', '5',
                '--mapping', 'placeholder',
                '--seed', '999',
                '--space', 'debug',
                '--outdir', tmpdir
            ],
            cwd=repo_root,
            capture_output=True,
            timeout=60
        )
        
        exp_dir = list(Path(tmpdir).glob("rigidity_experiment_*"))[0]
        metrics_path = exp_dir / "stability_metrics.json"
        
        with open(metrics_path, 'r') as f:
            metrics = json.load(f)
        
        # Check required fields are present
        assert 'max_delta' in metrics
        assert 'ratio_hit_rate' in metrics
        assert 'verdict' in metrics
        assert 'baseline_rarity_bits' in metrics
        assert 'scales' in metrics
        assert 'hit_rates' in metrics
        assert 'rarity_bits' in metrics
        
        # Check scales list
        assert metrics['scales'] == [0.8, 1.0, 1.2]
        
        # Check verdict is valid
        assert metrics['verdict'] in ['STABLE', 'UNSTABLE']
        
        # Check hit_rates and rarity_bits are lists of correct length
        assert len(metrics['hit_rates']) == 3
        assert len(metrics['rarity_bits']) == 3


def test_rigidity_experiment_reproducibility():
    """Test that the same seed produces identical results."""
    with tempfile.TemporaryDirectory() as tmpdir1:
        # First run with seed 333
        result1 = subprocess.run(
            [
                'python3', 'forensic_fingerprint/tools/layer2_rigidity_experiment.py',
                '--samples', '5',
                '--mapping', 'placeholder',
                '--seed', '333',
                '--space', 'debug',
                '--outdir', tmpdir1
            ],
            cwd=repo_root,
            capture_output=True,
            timeout=60
        )
        
        assert result1.returncode == 0
        
        # Get experiment directory
        exp_dirs1 = list(Path(tmpdir1).glob("rigidity_experiment_*"))
        assert len(exp_dirs1) == 1
        
        # Load stability metrics
        with open(exp_dirs1[0] / "stability_metrics.json", 'r') as f:
            metrics1 = json.load(f)
    
    with tempfile.TemporaryDirectory() as tmpdir2:
        # Second run with same seed 333
        result2 = subprocess.run(
            [
                'python3', 'forensic_fingerprint/tools/layer2_rigidity_experiment.py',
                '--samples', '5',
                '--mapping', 'placeholder',
                '--seed', '333',
                '--space', 'debug',
                '--outdir', tmpdir2
            ],
            cwd=repo_root,
            capture_output=True,
            timeout=60
        )
        
        assert result2.returncode == 0
        
        # Get experiment directory
        exp_dirs2 = list(Path(tmpdir2).glob("rigidity_experiment_*"))
        assert len(exp_dirs2) == 1
        
        # Load stability metrics
        with open(exp_dirs2[0] / "stability_metrics.json", 'r') as f:
            metrics2 = json.load(f)
        
        # With the same seed, results should be identical
        assert metrics1['hit_rates'] == metrics2['hit_rates'], \
            "Same seed should produce identical hit rates"
        assert metrics1['verdict'] == metrics2['verdict'], \
            "Same seed should produce identical verdict"
        
        # Check that hit_rates and rarity_bits match (accounting for None values)
        for i in range(3):
            assert metrics1['hit_rates'][i] == metrics2['hit_rates'][i], \
                f"Hit rate at index {i} should be identical"
            
            # Handle None values for rarity_bits (inf/nan)
            if metrics1['rarity_bits'][i] is None:
                assert metrics2['rarity_bits'][i] is None, \
                    f"Rarity bits at index {i} should both be None"
            else:
                assert abs(metrics1['rarity_bits'][i] - metrics2['rarity_bits'][i]) < 1e-6, \
                    f"Rarity bits at index {i} should be identical"


if __name__ == '__main__':
    # Run tests
    print("Running test_rigidity_experiment_help...")
    test_rigidity_experiment_help()
    print("✓ PASSED")
    
    print("\nRunning test_rigidity_experiment_dry_run...")
    test_rigidity_experiment_dry_run()
    print("✓ PASSED")
    
    print("\nRunning test_rigidity_experiment_verdict_content...")
    test_rigidity_experiment_verdict_content()
    print("✓ PASSED")
    
    print("\nRunning test_rigidity_experiment_stability_metrics...")
    test_rigidity_experiment_stability_metrics()
    print("✓ PASSED")
    
    print("\nRunning test_rigidity_experiment_reproducibility...")
    test_rigidity_experiment_reproducibility()
    print("✓ PASSED")
    
    print("\n" + "=" * 60)
    print("All tests passed!")
    print("=" * 60)

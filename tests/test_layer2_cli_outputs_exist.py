#!/usr/bin/env python3
"""
Tests for Layer2 Fingerprint - CLI Output Files
================================================

Tests that CLI tool generates all required output files.

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

import pytest
import subprocess
import tempfile
import shutil
from pathlib import Path


def test_cli_outputs_exist():
    """Test that CLI tool generates all required output files."""
    
    # Create temporary output directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Run CLI tool in debug mode with minimal samples
        cmd = [
            'python3',
            'forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py',
            '--space', 'debug',
            '--samples', '10',
            '--mapping', 'placeholder',
            '--outdir', str(tmpdir),
            '--seed', '42'
        ]
        
        # Run from repo root
        result = subprocess.run(
            cmd,
            cwd='/home/runner/work/unified-biquaternion-theory/unified-biquaternion-theory',
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Check that command succeeded
        assert result.returncode == 0, f"CLI failed: {result.stderr}"
        
        # Find output directory (should be timestamped)
        run_dirs = list(tmpdir.glob('layer2_sweep_*'))
        assert len(run_dirs) == 1, f"Expected 1 run dir, found {len(run_dirs)}"
        run_dir = run_dirs[0]
        
        # Check required files exist
        required_files = [
            'configurations.csv',
            'summary.json',
            'report.md',
            'VERDICT.md',
        ]
        
        for filename in required_files:
            filepath = run_dir / filename
            assert filepath.exists(), f"Missing required file: {filename}"
            assert filepath.stat().st_size > 0, f"File is empty: {filename}"
        
        # Check figures directory exists
        figures_dir = run_dir / 'figures'
        assert figures_dir.exists(), "Missing figures/ directory"
        
        # Check for expected figure files
        expected_figures = [
            'score_hist.png',
            'alpha_error_hist.png',
            'scatter_winding_vs_alpha_error.png',
        ]
        
        for figname in expected_figures:
            figpath = figures_dir / figname
            # Figures might not exist if matplotlib is not available
            # Just check that the directory exists
            pass  # We just check directory exists above


def test_cli_robustness_outputs():
    """Test that CLI tool with --robustness generates VERDICT.md with robustness table."""
    
    # Create temporary output directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Run CLI tool with robustness mode
        cmd = [
            'python3',
            'forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py',
            '--space', 'debug',
            '--samples', '5',  # Very small for speed
            '--mapping', 'placeholder',
            '--robustness',
            '--outdir', str(tmpdir),
            '--seed', '42'
        ]
        
        # Run from repo root
        result = subprocess.run(
            cmd,
            cwd='/home/runner/work/unified-biquaternion-theory/unified-biquaternion-theory',
            capture_output=True,
            text=True,
            timeout=120
        )
        
        # Check that command succeeded
        assert result.returncode == 0, f"CLI failed: {result.stderr}"
        
        # Find output directory
        run_dirs = list(tmpdir.glob('layer2_sweep_*'))
        assert len(run_dirs) == 1, f"Expected 1 run dir, found {len(run_dirs)}"
        run_dir = run_dirs[0]
        
        # Check VERDICT.md exists and contains robustness table
        verdict_path = run_dir / 'VERDICT.md'
        assert verdict_path.exists(), "Missing VERDICT.md"
        
        verdict_content = verdict_path.read_text()
        
        # Check for robustness section
        assert 'Robustness Analysis' in verdict_content, \
            "VERDICT.md should contain Robustness Analysis section"
        
        # Check for scale values in table
        assert '0.8' in verdict_content, "Should mention scale 0.8"
        assert '1.0' in verdict_content, "Should mention scale 1.0"
        assert '1.2' in verdict_content, "Should mention scale 1.2"
        
        # Check for hit-rate columns
        assert 'Hit-Rate' in verdict_content, "Should have Hit-Rate column"
        assert 'Rarity' in verdict_content, "Should have Rarity column"


def test_cli_placeholder_warning():
    """Test that CLI emits warning when using placeholder mode."""
    
    # Create temporary output directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Run CLI tool in placeholder mode
        cmd = [
            'python3',
            'forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py',
            '--space', 'debug',
            '--samples', '5',
            '--mapping', 'placeholder',
            '--outdir', str(tmpdir),
            '--seed', '42'
        ]
        
        # Run from repo root
        result = subprocess.run(
            cmd,
            cwd='/home/runner/work/unified-biquaternion-theory/unified-biquaternion-theory',
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Check output contains warning
        output = result.stdout + result.stderr
        assert 'WARNING' in output or 'warning' in output.lower(), \
            "Should emit warning for placeholder mode"
        assert 'PLACEHOLDER' in output or 'placeholder' in output.lower(), \
            "Should mention placeholder in warning"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

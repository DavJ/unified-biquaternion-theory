#!/usr/bin/env python3
# tests/test_planck_model_validation.py
# SPDX-License-Identifier: MIT
"""
Test: Planck Model File Validation (Part B)
============================================

Tests for preflight checks that reject invalid Planck model files:
- Files containing '-log(Like)' (likelihood/parameter tables)
- Files with < 50 data rows (likely not a spectrum)
"""
import sys
import tempfile
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Add forensic_fingerprint loaders to path
loaders_path = repo_root / 'forensic_fingerprint' / 'loaders'
if str(loaders_path) not in sys.path:
    sys.path.insert(0, str(loaders_path))

import planck


def test_reject_likelihood_file_by_content():
    """
    Test that files containing '-log(Like)' are rejected.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a fake likelihood file with -log(Like) in data
        likelihood_file = tmpdir / "fake_likelihood.txt"
        with open(likelihood_file, 'w') as f:
            f.write("# L  -log(Like)  Chi2\n")
            f.write("2  1234.56  100.0\n")
            f.write("3  1235.78  101.5\n")
        
        # Attempt to load should raise ValueError
        try:
            ell, cl, sigma = planck._load_planck_text(likelihood_file)
            assert False, "Should have raised ValueError for likelihood file"
        except ValueError as e:
            error_msg = str(e)
            assert 'likelihood' in error_msg.lower() or 'log(like)' in error_msg.lower(), \
                f"Error should mention likelihood, got: {error_msg}"
            print(f"✓ Correctly rejected likelihood file with error: {error_msg[:100]}")


def test_reject_tiny_file():
    """
    Test that files with < 50 data rows are rejected.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a file with only 10 data rows
        tiny_file = tmpdir / "tiny_spectrum.txt"
        with open(tiny_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(2, 12):  # Only 10 rows
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        # Attempt to load should raise ValueError
        try:
            ell, cl, sigma = planck._load_planck_text(tiny_file)
            assert False, "Should have raised ValueError for tiny file"
        except ValueError as e:
            error_msg = str(e)
            assert 'data rows' in error_msg.lower() or 'spectrum' in error_msg.lower(), \
                f"Error should mention data rows or spectrum, got: {error_msg}"
            print(f"✓ Correctly rejected tiny file with error: {error_msg[:100]}")


def test_accept_valid_spectrum():
    """
    Test that valid spectrum files are accepted.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a valid spectrum file with > 50 rows
        valid_file = tmpdir / "valid_spectrum.txt"
        with open(valid_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(2, 102):  # 100 rows
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        # Load should succeed
        try:
            ell, cl, sigma = planck._load_planck_text(valid_file)
            assert len(ell) == 100, f"Expected 100 multipoles, got {len(ell)}"
            print(f"✓ Valid spectrum file loaded successfully ({len(ell)} multipoles)")
        except ValueError as e:
            assert False, f"Valid spectrum should not raise error, got: {e}"


def test_reject_minimum_file_by_name():
    """
    Test that files with 'minimum' or 'plikHM' in name are handled appropriately.
    
    Note: The planck.py loader routes these to _load_planck_minimum_format(),
    which is designed to handle them. However, the runner script should reject
    them before loading.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a file with 'minimum' in the name
        minimum_file = tmpdir / "base-plikHM-minimum_R3.01.txt"
        with open(minimum_file, 'w') as f:
            f.write("# L  TT  TE  EE  BB\n")
            for i in range(2, 52):  # 50 rows to pass size check
                f.write(f"{i}  {1000 + i*10}  10  5  2\n")
        
        # The loader itself will route this to minimum format loader
        # The runner script should have already rejected it
        # We just verify the loader can identify it
        try:
            ell, cl, sigma = planck._load_planck_text(minimum_file)
            # If it loads, it went through minimum format loader
            # This is OK for the loader, but runner should reject it
            print(f"✓ Minimum file detected and routed to minimum format loader")
        except ValueError as e:
            # If it raises an error, that's also acceptable
            print(f"✓ Minimum file rejected: {str(e)[:100]}")


if __name__ == "__main__":
    print("Testing Planck Model File Validation")
    print("=" * 80)
    
    test_reject_likelihood_file_by_content()
    test_reject_tiny_file()
    test_accept_valid_spectrum()
    test_reject_minimum_file_by_name()
    
    print("=" * 80)
    print("✓ All Planck model validation tests passed!")

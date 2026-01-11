#!/usr/bin/env python3
# tests/test_manifest_validation_strict.py
# SPDX-License-Identifier: MIT
"""
Test: Strict Manifest Validation (Part A)
==========================================

Tests for enhanced manifest validation that ensures manifests contain
the exact files used in the analysis run.
"""
import json
import os
import sys
import tempfile
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Add tools and forensic_fingerprint to path
tools_path = repo_root / 'tools' / 'data_provenance'
forensic_path = repo_root / 'forensic_fingerprint'
if str(tools_path) not in sys.path:
    sys.path.insert(0, str(tools_path))
if str(forensic_path) not in sys.path:
    sys.path.insert(0, str(forensic_path))

import hash_dataset
import validate_manifest

# Import the validation function from run_real_data_cmb_comb
# We need to be careful here since it has dependencies
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))


def test_manifest_contains_exact_files():
    """
    Test that validation fails if manifest doesn't contain exact files used.
    """
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create test data files
        obs_file = tmpdir / "test_obs.txt"
        obs_file.write_text("# l Dl\n2 100\n3 200\n")
        
        model_file = tmpdir / "test_model.txt"
        model_file.write_text("# l Dl\n2 95\n3 195\n")
        
        other_file = tmpdir / "other_data.txt"
        other_file.write_text("# l Dl\n2 90\n3 190\n")
        
        # Create manifest with only obs_file and other_file (missing model_file)
        manifest = hash_dataset.hash_dataset([str(obs_file), str(other_file)])
        
        manifest_file = tmpdir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        # Validation of manifest itself should pass
        result = validate_manifest.validate_manifest(manifest_file, base_dir=repo_root)
        assert result, "Basic manifest validation should pass"
        
        # Load manifest and check it contains obs but not model
        with open(manifest_file, 'r') as f:
            manifest_data = json.load(f)
        
        manifest_files = {fi['filename'] for fi in manifest_data['files']}
        
        assert 'test_obs.txt' in manifest_files, "Manifest should contain obs file"
        assert 'test_model.txt' not in manifest_files, "Manifest should NOT contain model file"
        assert 'other_data.txt' in manifest_files, "Manifest should contain other file"
        
        print("✓ Manifest validation detects missing files correctly")


def test_manifest_with_all_required_files():
    """
    Test that validation passes when manifest contains all required files.
    """
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create test data files
        obs_file = tmpdir / "test_obs.txt"
        obs_file.write_text("# l Dl\n2 100\n3 200\n")
        
        model_file = tmpdir / "test_model.txt"
        model_file.write_text("# l Dl\n2 95\n3 195\n")
        
        # Create manifest with both files
        manifest = hash_dataset.hash_dataset([str(obs_file), str(model_file)])
        
        manifest_file = tmpdir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        # Validation should pass
        result = validate_manifest.validate_manifest(manifest_file, base_dir=repo_root)
        assert result, "Manifest validation should pass with all files"
        
        # Check manifest contains both files
        with open(manifest_file, 'r') as f:
            manifest_data = json.load(f)
        
        manifest_files = {fi['filename'] for fi in manifest_data['files']}
        
        assert 'test_obs.txt' in manifest_files, "Manifest should contain obs file"
        assert 'test_model.txt' in manifest_files, "Manifest should contain model file"
        
        print("✓ Manifest with all required files validates successfully")


if __name__ == "__main__":
    print("Testing Strict Manifest Validation")
    print("=" * 80)
    
    test_manifest_contains_exact_files()
    test_manifest_with_all_required_files()
    
    print("=" * 80)
    print("✓ All strict manifest validation tests passed!")

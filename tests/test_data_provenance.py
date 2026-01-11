#!/usr/bin/env python3
# tests/test_data_provenance.py
# SPDX-License-Identifier: MIT
"""
Test: Data Provenance Tools
============================

Tests for hash_dataset.py and validate_manifest.py to ensure:
1. Manifests store repo-relative paths
2. Validation works from different CWDs
3. Empty manifests fail validation
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

# Add tools to path
tools_path = repo_root / 'tools' / 'data_provenance'
if str(tools_path) not in sys.path:
    sys.path.insert(0, str(tools_path))

import hash_dataset
import validate_manifest


def test_hash_dataset_stores_repo_relative_paths():
    """
    Test that hash_dataset stores paths relative to repo root by default.
    """
    # Create a temporary file in the repo
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        test_file = tmpdir / "test_data.txt"
        test_file.write_text("test content for hashing\n")
        
        # Hash the file (should auto-discover repo root)
        manifest = hash_dataset.hash_dataset([str(test_file)])
        
        # Check manifest structure
        assert 'files' in manifest
        assert len(manifest['files']) == 1
        
        file_info = manifest['files'][0]
        assert file_info['filename'] == 'test_data.txt'
        
        # The path should be relative to repo root, not absolute
        stored_path = file_info['path']
        assert not Path(stored_path).is_absolute(), (
            f"Expected relative path, got absolute: {stored_path}"
        )
        
        # The stored path should start with the tmpdir name (relative to repo root)
        # e.g., "tmp_xyz/test_data.txt"
        assert tmpdir.name in stored_path, (
            f"Expected path to contain {tmpdir.name}, got: {stored_path}"
        )
        
        # Verify the path can be resolved from repo root
        resolved = repo_root / stored_path
        assert resolved.exists(), f"Stored path does not resolve: {resolved}"
        
        print(f"✓ Stored path is repo-relative: {stored_path}")


def test_hash_dataset_with_explicit_relative_to():
    """
    Test that hash_dataset respects --relative-to option.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        test_file = tmpdir / "test_data.txt"
        test_file.write_text("test content\n")
        
        # Hash with explicit relative_to
        manifest = hash_dataset.hash_dataset([str(test_file)], relative_to=tmpdir)
        
        file_info = manifest['files'][0]
        stored_path = file_info['path']
        
        # Should be just the filename when relative to tmpdir
        assert stored_path == 'test_data.txt', (
            f"Expected 'test_data.txt', got: {stored_path}"
        )
        
        print(f"✓ Explicit relative_to works: {stored_path}")


def test_hash_dataset_outside_repo():
    """
    Test that files outside repo root get absolute paths.
    """
    with tempfile.TemporaryDirectory(dir='/tmp') as tmpdir:
        tmpdir = Path(tmpdir)
        test_file = tmpdir / "outside_repo.txt"
        test_file.write_text("outside repo\n")
        
        # Hash the file
        manifest = hash_dataset.hash_dataset([str(test_file)])
        
        file_info = manifest['files'][0]
        stored_path = file_info['path']
        
        # Should be absolute since file is outside repo
        assert Path(stored_path).is_absolute(), (
            f"Expected absolute path for file outside repo, got: {stored_path}"
        )
        
        print(f"✓ Files outside repo get absolute paths: {stored_path}")


def test_validate_manifest_from_different_cwd():
    """
    Test that validate_manifest works when run from different CWDs.
    """
    # Create temporary test data in repo
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        test_file = tmpdir / "test_validation.txt"
        test_content = "validation test content\n"
        test_file.write_text(test_content)
        
        # Create manifest with repo-relative path
        manifest = hash_dataset.hash_dataset([str(test_file)])
        
        manifest_file = tmpdir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        # Save original CWD
        original_cwd = os.getcwd()
        
        try:
            # Test 1: Validate from repo root
            os.chdir(repo_root)
            result = validate_manifest.validate_manifest(manifest_file)
            assert result, "Validation failed from repo root"
            print("✓ Validation works from repo root")
            
            # Test 2: Validate from a different directory
            with tempfile.TemporaryDirectory() as other_dir:
                os.chdir(other_dir)
                result = validate_manifest.validate_manifest(manifest_file)
                assert result, "Validation failed from different CWD"
                print("✓ Validation works from different CWD")
            
            # Test 3: Validate with explicit base_dir
            os.chdir('/tmp')
            result = validate_manifest.validate_manifest(manifest_file, base_dir=repo_root)
            assert result, "Validation failed with explicit base_dir"
            print("✓ Validation works with explicit base_dir")
            
        finally:
            os.chdir(original_cwd)


def test_empty_manifest_fails():
    """
    Test that empty manifests fail validation with non-zero exit.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create empty manifest
        empty_manifest = {
            'generated': '2026-01-10T00:00:00',
            'tool': 'hash_dataset.py',
            'hash_algorithm': 'SHA-256',
            'files': []
        }
        
        manifest_file = tmpdir / "empty_manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(empty_manifest, f, indent=2)
        
        # Validate should fail
        result = validate_manifest.validate_manifest(manifest_file)
        assert result is False, "Empty manifest should fail validation"
        
        print("✓ Empty manifest fails validation")


def test_find_repo_root():
    """
    Test that find_repo_root correctly finds the repository root.
    """
    # Test from tools directory
    tools_dir = repo_root / 'tools' / 'data_provenance'
    found_root = hash_dataset.find_repo_root(tools_dir)
    assert found_root == repo_root, (
        f"Expected {repo_root}, got {found_root}"
    )
    
    # Test from repo root
    found_root = hash_dataset.find_repo_root(repo_root)
    assert found_root == repo_root
    
    print(f"✓ find_repo_root works correctly: {found_root}")


if __name__ == "__main__":
    print("Testing Data Provenance Tools")
    print("=" * 80)
    
    test_find_repo_root()
    test_hash_dataset_stores_repo_relative_paths()
    test_hash_dataset_with_explicit_relative_to()
    test_hash_dataset_outside_repo()
    test_validate_manifest_from_different_cwd()
    test_empty_manifest_fails()
    
    print("=" * 80)
    print("✓ All data provenance tests passed!")

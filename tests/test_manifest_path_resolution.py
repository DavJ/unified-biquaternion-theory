#!/usr/bin/env python3
"""
Test that manifest path resolution works from any working directory.

This test verifies the fix for the issue where run_real_data_cmb_comb.py
would fail with "MISSING" errors when executed from different directories.
"""

import sys
import tempfile
import json
import os
from pathlib import Path

# Add project root to path
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / 'tools' / 'data_provenance'))

import validate_manifest
import hash_dataset


def find_repo_root(start_path=None):
    """
    Find repository root by walking upward from start_path.
    
    This is a copy of the function from run_real_data_cmb_comb.py for testing.
    """
    if start_path is None:
        start_path = Path(__file__).resolve().parent
    else:
        start_path = Path(start_path).resolve()
    
    current = start_path
    # Prioritize .git as the most reliable marker
    markers = ['.git', 'pyproject.toml', 'pytest.ini']
    
    # Walk up directory tree
    while current != current.parent:
        # Check if any marker exists in current directory
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent
    
    # Check root directory too
    for marker in markers:
        if (current / marker).exists():
            return current
    
    raise FileNotFoundError(
        f"Could not find repository root. Searched from {start_path} upward. "
        f"Looking for markers: {', '.join(markers)}"
    )


def test_find_repo_root():
    """Test that find_repo_root works from various locations."""
    # Should find repo root from test directory
    root = find_repo_root(Path(__file__).parent)
    assert root.exists()
    assert (root / '.git').exists() or (root / 'pytest.ini').exists()
    
    # Should find repo root from a real nested subdirectory
    forensic_dir = repo_root / 'forensic_fingerprint'
    if forensic_dir.exists():
        root2 = find_repo_root(forensic_dir)
        assert root2 == root
    
    print("✓ find_repo_root() works correctly")


def test_manifest_validation_with_base_dir():
    """Test that validate_manifest works with base_dir parameter."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a test file in a subdirectory
        data_dir = tmpdir / 'data' / 'test'
        data_dir.mkdir(parents=True)
        
        test_file = data_dir / 'test_data.txt'
        test_content = b"Test data for manifest validation"
        test_file.write_bytes(test_content)
        
        # Create manifest in different directory
        manifest_dir = tmpdir / 'manifests'
        manifest_dir.mkdir()
        
        # Generate manifest with relative path
        manifest = hash_dataset.hash_dataset(
            [str(test_file)],
            relative_to=tmpdir
        )
        
        manifest_file = manifest_dir / 'test_manifest.json'
        manifest_file.write_text(json.dumps(manifest, indent=2))
        
        # Test validation with base_dir
        # This should work even though manifest is in different dir than data
        result = validate_manifest.validate_manifest(
            manifest_file,
            base_dir=tmpdir
        )
        
        assert result, "Manifest validation should succeed with base_dir"
        print("✓ validate_manifest() works with base_dir parameter")


def test_manifest_validation_from_different_cwd():
    """Test that validation works when CWD is different from repo root."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create test structure
        data_dir = tmpdir / 'data'
        data_dir.mkdir()
        
        test_file = data_dir / 'test.txt'
        test_file.write_text("test content")
        
        # Create manifest with path relative to tmpdir
        manifest = hash_dataset.hash_dataset(
            [str(test_file)],
            relative_to=tmpdir
        )
        
        manifest_file = tmpdir / 'manifest.json'
        manifest_file.write_text(json.dumps(manifest, indent=2))
        
        # Change to a different directory
        original_cwd = os.getcwd()
        try:
            # Create a different working directory
            other_dir = tmpdir / 'other'
            other_dir.mkdir()
            os.chdir(other_dir)
            
            # Validation should still work with base_dir
            result = validate_manifest.validate_manifest(
                manifest_file,
                base_dir=tmpdir
            )
            
            assert result, "Validation should work regardless of CWD when base_dir is provided"
            print("✓ Validation works from different CWD with base_dir")
            
        finally:
            os.chdir(original_cwd)


def test_hash_dataset_relative_to():
    """Test that hash_dataset stores relative paths correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create test files
        data_dir = tmpdir / 'data' / 'subdir'
        data_dir.mkdir(parents=True)
        
        test_file = data_dir / 'file.txt'
        test_file.write_text("content")
        
        # Generate manifest with --relative-to
        manifest = hash_dataset.hash_dataset(
            [str(test_file)],
            relative_to=tmpdir
        )
        
        # Check that path is stored relative to tmpdir
        assert len(manifest['files']) == 1
        stored_path = manifest['files'][0]['path']
        
        # Should be relative path, not absolute
        assert not Path(stored_path).is_absolute()
        # Use Path normalization for cross-platform compatibility
        expected_path = Path('data') / 'subdir' / 'file.txt'
        assert Path(stored_path) == expected_path
        
        print("✓ hash_dataset stores relative paths correctly with --relative-to")


def test_hash_dataset_outside_relative_to():
    """Test that hash_dataset handles files outside relative_to directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create file inside
        inside_dir = tmpdir / 'inside'
        inside_dir.mkdir()
        inside_file = inside_dir / 'inside.txt'
        inside_file.write_text("inside")
        
        # Create file outside tmpdir
        with tempfile.TemporaryDirectory() as outside_tmpdir:
            outside_file = Path(outside_tmpdir) / 'outside.txt'
            outside_file.write_text("outside")
            
            # Generate manifest
            manifest = hash_dataset.hash_dataset(
                [str(inside_file), str(outside_file)],
                relative_to=tmpdir
            )
            
            assert len(manifest['files']) == 2
            
            # Inside file should be relative
            inside_entry = [f for f in manifest['files'] if f['filename'] == 'inside.txt'][0]
            assert not Path(inside_entry['path']).is_absolute()
            
            # Outside file should be absolute
            outside_entry = [f for f in manifest['files'] if f['filename'] == 'outside.txt'][0]
            assert Path(outside_entry['path']).is_absolute()
            
            print("✓ hash_dataset handles files outside relative_to correctly")


def test_runner_integration_from_subdir():
    """
    Integration test: Simulate running runner from a temp subdirectory.
    
    This tests the complete workflow:
    1. Create test data files in a structure like data/test/
    2. Generate manifest with --relative-to
    3. Create a temp working directory
    4. Change to that directory
    5. Validate manifest using base_dir
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create fake repo structure
        fake_repo = tmpdir / 'fake_repo'
        fake_repo.mkdir()
        
        # Add a .git marker
        (fake_repo / '.git').mkdir()
        
        # Create data directory
        data_dir = fake_repo / 'data' / 'test'
        data_dir.mkdir(parents=True)
        
        # Create test data files
        obs_file = data_dir / 'spectrum.txt'
        obs_file.write_text("# ell Cl_TT sigma\n2 1000 50\n3 1100 55\n")
        
        model_file = data_dir / 'model.txt'
        model_file.write_text("# ell Cl_TT\n2 1000\n3 1100\n")
        
        # Create manifest directory
        manifest_dir = fake_repo / 'manifests'
        manifest_dir.mkdir()
        
        # Generate manifest with relative paths
        manifest = hash_dataset.hash_dataset(
            [str(obs_file), str(model_file)],
            relative_to=fake_repo
        )
        
        manifest_file = manifest_dir / 'test_manifest.json'
        manifest_file.write_text(json.dumps(manifest, indent=2))
        
        # Now test validation from a different working directory
        work_dir = fake_repo / 'subdir' / 'work'
        work_dir.mkdir(parents=True)
        
        original_cwd = os.getcwd()
        try:
            # Change to the subdirectory
            os.chdir(work_dir)
            
            # Validation should work by providing base_dir
            result = validate_manifest.validate_manifest(
                fake_repo / 'manifests' / 'test_manifest.json',
                base_dir=fake_repo
            )
            
            assert result, "Integration test: validation should succeed from subdirectory"
            print("✓ Runner integration test: validation works from nested subdirectory")
            
        finally:
            os.chdir(original_cwd)


if __name__ == '__main__':
    print("Testing manifest path resolution fixes...\n")
    
    test_find_repo_root()
    test_manifest_validation_with_base_dir()
    test_manifest_validation_from_different_cwd()
    test_hash_dataset_relative_to()
    test_hash_dataset_outside_relative_to()
    test_runner_integration_from_subdir()
    
    print("\n✓ All manifest path resolution tests passed!")

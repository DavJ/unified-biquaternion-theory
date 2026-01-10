#!/usr/bin/env python3
"""
Validate dataset files against pre-registered SHA-256 manifest.

This tool verifies that data files match their pre-registered hashes,
ensuring data provenance and preventing tampering.

Usage:
    python validate_manifest.py manifest.json

Exit codes:
    0 - All files validated successfully
    1 - Validation failed (hash mismatch or missing files)

License: MIT
"""

import sys
import hashlib
import json
from pathlib import Path


def compute_sha256(filepath):
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    
    return sha256.hexdigest()


def validate_manifest(manifest_path):
    """
    Validate files against manifest.
    
    Parameters
    ----------
    manifest_path : str or Path
        Path to manifest JSON file
    
    Returns
    -------
    bool
        True if all files validated, False otherwise
    """
    manifest_path = Path(manifest_path)
    
    if not manifest_path.exists():
        print(f"ERROR: Manifest not found: {manifest_path}", file=sys.stderr)
        return False
    
    # Load manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    print("=" * 80)
    print("Dataset Validation Report")
    print("=" * 80)
    print(f"Manifest: {manifest_path}")
    print(f"Generated: {manifest.get('generated', 'unknown')}")
    print(f"Hash algorithm: {manifest.get('hash_algorithm', 'unknown')}")
    print(f"Number of files: {len(manifest.get('files', []))}")
    print("")
    
    all_valid = True
    validated_count = 0
    
    for file_info in manifest.get('files', []):
        filename = file_info['filename']
        expected_hash = file_info['sha256']
        expected_size = file_info.get('size_bytes')
        file_path = file_info.get('path', filename)
        
        print(f"Validating: {filename}")
        
        # Check if file exists
        path = Path(file_path)
        if not path.exists():
            # Try relative to manifest directory
            path = manifest_path.parent / filename
        
        if not path.exists():
            print(f"  ✗ MISSING: File not found")
            all_valid = False
            continue
        
        # Check size if provided
        actual_size = path.stat().st_size
        if expected_size is not None and actual_size != expected_size:
            print(f"  ✗ SIZE MISMATCH: expected {expected_size} bytes, got {actual_size} bytes")
            all_valid = False
            continue
        
        # Compute and check hash
        print(f"  Computing hash...", end='')
        actual_hash = compute_sha256(path)
        
        if actual_hash == expected_hash:
            print(f" ✓ VALID")
            validated_count += 1
        else:
            print(f" ✗ HASH MISMATCH")
            print(f"    Expected: {expected_hash}")
            print(f"    Got:      {actual_hash}")
            all_valid = False
        
        print("")
    
    # Summary
    print("=" * 80)
    if all_valid:
        print(f"✓ SUCCESS: All {validated_count} file(s) validated")
        print("")
        print("Data provenance confirmed. Files match pre-registered hashes.")
    else:
        print(f"✗ FAILURE: Validation failed")
        print("")
        print("Some files missing or hashes don't match.")
        print("DO NOT use this data for analysis without resolving discrepancies.")
    print("=" * 80)
    
    return all_valid


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_manifest.py <manifest.json>", file=sys.stderr)
        print("", file=sys.stderr)
        print("Example:", file=sys.stderr)
        print("  python validate_manifest.py data/planck_2018/manifest.json", file=sys.stderr)
        sys.exit(1)
    
    manifest_path = sys.argv[1]
    
    success = validate_manifest(manifest_path)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

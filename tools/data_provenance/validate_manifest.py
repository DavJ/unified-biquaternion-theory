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

import argparse
import hashlib
import json
import sys
from pathlib import Path

from repo_utils import find_repo_root


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


def validate_manifest(manifest_path, base_dir=None):
    """
    Validate files against manifest.
    
    Parameters
    ----------
    manifest_path : str or Path
        Path to manifest JSON file
    base_dir : str or Path or None
        Base directory for resolving relative paths in manifest.
        If None, auto-discovers repo root.
    
    Returns
    -------
    bool
        True if all files validated, False otherwise
    """
    manifest_path = Path(manifest_path)
    
    if not manifest_path.exists():
        print(f"ERROR: Manifest not found: {manifest_path}", file=sys.stderr)
        return False
    
    # Load manifest first to check for empty manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    # Check for empty manifest (Part C)
    if not manifest.get('files'):
        print("=" * 80, file=sys.stderr)
        print("ERROR: Empty manifest", file=sys.stderr)
        print("=" * 80, file=sys.stderr)
        print(f"Manifest: {manifest_path}", file=sys.stderr)
        print(f"Number of files: 0", file=sys.stderr)
        print("", file=sys.stderr)
        print("Manifest contains no files to validate.", file=sys.stderr)
        print("This may indicate an error in manifest generation.", file=sys.stderr)
        print("=" * 80, file=sys.stderr)
        return False
    
    # Set base directory for resolving relative paths
    if base_dir is None:
        try:
            base_dir = find_repo_root()
            print(f"Auto-discovered repo root: {base_dir}", file=sys.stderr)
        except FileNotFoundError:
            # Fall back to manifest parent directory
            base_dir = manifest_path.parent
            print(f"WARNING: Could not find repo root, using manifest directory: {base_dir}", file=sys.stderr)
    else:
        base_dir = Path(base_dir)
    
    print("=" * 80)
    print("Dataset Validation Report")
    print("=" * 80)
    print(f"Manifest: {manifest_path}")
    print(f"Base directory: {base_dir}")
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
        
        # Resolve path with multiple strategies
        path = Path(file_path)
        
        # Strategy 1: If absolute path exists, use it
        if path.is_absolute() and path.exists():
            resolved_path = path
        # Strategy 2: Try relative to base_dir
        elif (base_dir / file_path).exists():
            resolved_path = base_dir / file_path
        # Strategy 3: Try filename only relative to base_dir
        elif (base_dir / filename).exists():
            resolved_path = base_dir / filename
        # Strategy 4: Try relative to manifest directory
        elif (manifest_path.parent / filename).exists():
            resolved_path = manifest_path.parent / filename
        # Strategy 5: Try path as-is relative to CWD
        elif path.exists():
            resolved_path = path
        else:
            # File not found with any strategy
            print(f"  ✗ MISSING: File not found")
            print(f"    Tried paths:")
            print(f"      - {path.absolute()} (absolute/CWD)")
            print(f"      - {base_dir / file_path} (base_dir + path)")
            print(f"      - {base_dir / filename} (base_dir + filename)")
            print(f"      - {manifest_path.parent / filename} (manifest_dir + filename)")
            all_valid = False
            continue
        
        # Check size if provided
        actual_size = resolved_path.stat().st_size
        if expected_size is not None and actual_size != expected_size:
            print(f"  ✗ SIZE MISMATCH: expected {expected_size} bytes, got {actual_size} bytes")
            print(f"    Resolved path: {resolved_path}")
            all_valid = False
            continue
        
        # Compute and check hash
        print(f"  Computing hash (resolved: {resolved_path})...", end='')
        actual_hash = compute_sha256(resolved_path)
        
        if actual_hash == expected_hash:
            print(f" ✓ VALID")
            validated_count += 1
        else:
            print(f" ✗ HASH MISMATCH")
            print(f"    Resolved path: {resolved_path}")
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
    parser = argparse.ArgumentParser(
        description="Validate dataset files against SHA-256 manifest",
        epilog="Example: python validate_manifest.py data/planck_2018/manifest.json --base-dir /path/to/repo\n"
               "         python validate_manifest.py manifest.json  # auto-discovers repo root"
    )
    parser.add_argument('manifest', help='Path to manifest JSON file')
    parser.add_argument('--base-dir', dest='base_dir',
                       help='Base directory for resolving relative paths (default: auto-discover repo root)')
    
    args = parser.parse_args()
    
    success = validate_manifest(args.manifest, base_dir=args.base_dir)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

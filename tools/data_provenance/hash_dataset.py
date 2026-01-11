#!/usr/bin/env python3
"""
Compute SHA-256 hashes of dataset files for provenance tracking.

This tool computes cryptographic hashes of data files to ensure
reproducibility and prevent tampering.

Usage:
    python hash_dataset.py file1.txt file2.fits > manifest.json
    python hash_dataset.py *.txt >> manifest.json

Output: JSON manifest with filename, size, and SHA-256 hash.

License: MIT
"""

import sys
import hashlib
import json
import argparse
from pathlib import Path
from datetime import datetime


def compute_sha256(filepath):
    """
    Compute SHA-256 hash of a file.
    
    Parameters
    ----------
    filepath : str or Path
        Path to file
    
    Returns
    -------
    str
        Hexadecimal SHA-256 hash
    """
    sha256 = hashlib.sha256()
    
    with open(filepath, 'rb') as f:
        # Read in chunks to handle large files
        while True:
            data = f.read(65536)  # 64 KB chunks
            if not data:
                break
            sha256.update(data)
    
    return sha256.hexdigest()


def hash_dataset(filepaths, relative_to=None):
    """
    Compute hashes for multiple files and return manifest.
    
    Parameters
    ----------
    filepaths : list of str or Path
        Paths to files
    relative_to : str or Path or None
        Base directory to compute relative paths from.
        If provided, stores paths relative to this directory (if files are inside it).
        Otherwise stores absolute paths.
    
    Returns
    -------
    dict
        Manifest with metadata and file hashes
    """
    manifest = {
        'generated': datetime.now().isoformat(),
        'tool': 'hash_dataset.py',
        'hash_algorithm': 'SHA-256',
        'files': []
    }
    
    # Convert relative_to to absolute path if provided
    if relative_to is not None:
        relative_to = Path(relative_to).resolve()
    
    for filepath in filepaths:
        path = Path(filepath).resolve()  # Convert to absolute path
        
        if not path.exists():
            print(f"WARNING: File not found: {filepath}", file=sys.stderr)
            continue
        
        if not path.is_file():
            print(f"WARNING: Not a file: {filepath}", file=sys.stderr)
            continue
        
        print(f"Hashing {path.name}...", file=sys.stderr)
        
        # Determine path to store in manifest
        if relative_to is not None:
            try:
                # Try to make path relative to relative_to
                stored_path = str(path.relative_to(relative_to))
            except ValueError:
                # Path is not relative to relative_to, use absolute
                stored_path = str(path)
        else:
            # Use absolute path
            stored_path = str(path)
        
        file_info = {
            'filename': path.name,
            'size_bytes': path.stat().st_size,
            'sha256': compute_sha256(path),
            'path': stored_path
        }
        
        manifest['files'].append(file_info)
    
    return manifest


def main():
    parser = argparse.ArgumentParser(
        description="Compute SHA-256 hashes of dataset files for provenance tracking",
        epilog="Examples:\n"
               "  python hash_dataset.py data.txt > manifest.json\n"
               "  python hash_dataset.py *.fits --relative-to /path/to/repo > manifest.json",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('files', nargs='+', help='Files to hash')
    parser.add_argument('--relative-to', help='Store paths relative to this directory (default: absolute paths)')
    
    args = parser.parse_args()
    
    manifest = hash_dataset(args.files, relative_to=args.relative_to)
    
    # Output JSON to stdout
    print(json.dumps(manifest, indent=2))
    
    # Summary to stderr
    print("", file=sys.stderr)
    print(f"Generated manifest for {len(manifest['files'])} file(s)", file=sys.stderr)
    if args.relative_to:
        print(f"Paths stored relative to: {args.relative_to}", file=sys.stderr)


if __name__ == '__main__':
    main()

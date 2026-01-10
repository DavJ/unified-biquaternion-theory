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


def hash_dataset(filepaths):
    """
    Compute hashes for multiple files and return manifest.
    
    Parameters
    ----------
    filepaths : list of str or Path
        Paths to files
    
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
    
    for filepath in filepaths:
        path = Path(filepath)
        
        if not path.exists():
            print(f"WARNING: File not found: {filepath}", file=sys.stderr)
            continue
        
        if not path.is_file():
            print(f"WARNING: Not a file: {filepath}", file=sys.stderr)
            continue
        
        print(f"Hashing {path.name}...", file=sys.stderr)
        
        file_info = {
            'filename': path.name,
            'size_bytes': path.stat().st_size,
            'sha256': compute_sha256(path),
            'path': str(path)
        }
        
        manifest['files'].append(file_info)
    
    return manifest


def main():
    if len(sys.argv) < 2:
        print("Usage: python hash_dataset.py <file1> [file2] ...", file=sys.stderr)
        print("", file=sys.stderr)
        print("Example:", file=sys.stderr)
        print("  python hash_dataset.py data.txt > manifest.json", file=sys.stderr)
        print("  python hash_dataset.py *.fits > manifest.json", file=sys.stderr)
        sys.exit(1)
    
    filepaths = sys.argv[1:]
    
    manifest = hash_dataset(filepaths)
    
    # Output JSON to stdout
    print(json.dumps(manifest, indent=2))
    
    # Summary to stderr
    print("", file=sys.stderr)
    print(f"Generated manifest for {len(manifest['files'])} file(s)", file=sys.stderr)


if __name__ == '__main__':
    main()

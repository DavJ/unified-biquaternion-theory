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

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path


def find_repo_root(start_path=None):
    """
    Find repository root by walking upward from start_path.
    
    Looks for markers like .git or pyproject.toml.
    
    Parameters
    ----------
    start_path : Path or None
        Starting directory (default: directory containing this file)
    
    Returns
    -------
    Path
        Repository root directory
    
    Raises
    ------
    FileNotFoundError
        If no repository markers found
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
        If None, auto-discovers repo root and uses it.
        If provided, stores paths relative to this directory (if files are inside it).
    
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
    
    # Auto-discover repo root if not provided
    if relative_to is None:
        try:
            relative_to = find_repo_root()
            print(f"Auto-discovered repo root: {relative_to}", file=sys.stderr)
        except FileNotFoundError:
            # Fall back to not using relative paths
            print("WARNING: Could not find repo root. Using absolute paths.", file=sys.stderr)
            relative_to = None
    
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
                print(f"WARNING: {path} is outside repo root, storing absolute path", file=sys.stderr)
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
               "  python hash_dataset.py *.fits --relative-to /path/to/repo > manifest.json\n"
               "  python hash_dataset.py data/*.txt > manifest.json  # auto-discovers repo root",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('files', nargs='+', help='Files to hash')
    parser.add_argument('--relative-to', 
                       help='Store paths relative to this directory (default: auto-discover repo root)')
    
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

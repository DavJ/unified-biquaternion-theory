"""
Repository Path Utilities for Tests

Provides consistent path resolution for tests after repository restructuring.

This module helps tests locate:
- forensic_fingerprint (via shim or explicit path)
- ubt_with_chronofactor content
- ubt_no_chronofactor content
- Repository root

Usage:
    from tests.utils_repo_paths import repo_root, forensic_root
    
    # Get repo root
    root = repo_root()
    
    # Get forensic_fingerprint root (via shim)
    ff_root = forensic_root()
    
    # Get explicit paths
    with_chrono = repo_root() / 'ubt_with_chronofactor'
    no_chrono = repo_root() / 'ubt_no_chronofactor'

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

from __future__ import annotations
from pathlib import Path
import sys


def repo_root() -> Path:
    """
    Get the repository root directory.
    
    Returns:
        Path to repository root
    """
    # This file is in tests/, so parent is repo root
    return Path(__file__).resolve().parent.parent


def forensic_root() -> Path:
    """
    Get the forensic_fingerprint root directory.
    
    Returns the shim directory at repo root, which delegates to
    ubt_with_chronofactor/forensic_fingerprint/.
    
    Returns:
        Path to forensic_fingerprint shim directory
    """
    return repo_root() / 'forensic_fingerprint'


def forensic_target_root() -> Path:
    """
    Get the actual forensic_fingerprint implementation directory.
    
    Returns:
        Path to ubt_with_chronofactor/forensic_fingerprint/
    """
    return repo_root() / 'ubt_with_chronofactor' / 'forensic_fingerprint'


def ubt_with_chronofactor_root() -> Path:
    """
    Get the chronofactor-based UBT formulation root.
    
    Returns:
        Path to ubt_with_chronofactor/
    """
    return repo_root() / 'ubt_with_chronofactor'


def ubt_no_chronofactor_root() -> Path:
    """
    Get the chronofactor-free UBT formulation root.
    
    Returns:
        Path to ubt_no_chronofactor/
    """
    return repo_root() / 'ubt_no_chronofactor'


def ensure_forensic_importable() -> None:
    """
    Ensure forensic_fingerprint can be imported.
    
    This imports the shim module, which handles sys.path manipulation.
    Call this before importing forensic_fingerprint in tests if needed.
    """
    # Simply importing the shim package triggers path setup
    import forensic_fingerprint
    

def add_path(path: Path) -> None:
    """
    Add a path to sys.path if not already present.
    
    Args:
        path: Path to add to sys.path
    """
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)


# Auto-export commonly used functions
__all__ = [
    'repo_root',
    'forensic_root',
    'forensic_target_root',
    'ubt_with_chronofactor_root',
    'ubt_no_chronofactor_root',
    'ensure_forensic_importable',
    'add_path',
]

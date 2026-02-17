"""
Forensic Fingerprint Compatibility Shim

This module provides backward compatibility for tests and CI workflows
after restructuring. It delegates all imports to the actual forensic_fingerprint
implementation in ubt_with_chronofactor/.

Purpose:
- Preserve existing test imports: `from forensic_fingerprint import ...`
- Enable CI workflows to run without modification
- Allow gradual migration to explicit paths

Future:
- Can be switched to ubt_no_chronofactor implementation when ready
- Eventually can be removed in favor of explicit imports

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

from __future__ import annotations
import sys
from pathlib import Path


def get_target_root() -> Path:
    """
    Get the actual location of forensic_fingerprint implementation.
    
    Currently points to ubt_with_chronofactor/forensic_fingerprint.
    
    Returns:
        Path to the forensic_fingerprint implementation directory
    """
    shim_dir = Path(__file__).resolve().parent
    repo_root = shim_dir.parent
    target = repo_root / "ubt_with_chronofactor" / "forensic_fingerprint"
    return target


def ensure_importable() -> Path:
    """
    Ensure the target forensic_fingerprint is importable.
    
    This function manipulates sys.modules and sys.path to make the target
    forensic_fingerprint implementation accessible via root-level imports.
    
    Returns:
        Path to the target forensic_fingerprint directory
        
    Raises:
        RuntimeError: If target directory doesn't exist
    """
    target_root = get_target_root()
    
    if not target_root.exists():
        raise RuntimeError(
            f"Forensic fingerprint target not found: {target_root}\n"
            "Expected structure:\n"
            "  ubt_with_chronofactor/\n"
            "    forensic_fingerprint/\n"
            "      __init__.py\n"
            "      ...\n"
        )
    
    # Strategy: Replace our shim module in sys.modules with the actual module
    # This way, subsequent imports like "from forensic_fingerprint.layer2 import ..."
    # will find the real modules in ubt_with_chronofactor/forensic_fingerprint/
    
    # Add ubt_with_chronofactor to sys.path so its forensic_fingerprint can be imported
    parent = str(target_root.parent)
    if parent not in sys.path:
        sys.path.insert(0, parent)
    
    return target_root


# Auto-initialize on import
_TARGET = ensure_importable()
__all__ = ["ensure_importable", "get_target_root"]

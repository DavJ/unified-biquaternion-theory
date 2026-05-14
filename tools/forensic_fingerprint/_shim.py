"""
Forensic Fingerprint Compatibility Shim

After root_detox_phase1, forensic_fingerprint is located at tools/forensic_fingerprint/.
This shim is retained for backward compatibility but no longer redirects imports.

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

from __future__ import annotations
import sys
from pathlib import Path


def get_target_root() -> Path:
    """Return this package's own directory (no longer a shim to ubt_with_chronofactor)."""
    return Path(__file__).resolve().parent


def ensure_importable() -> Path:
    """
    Ensure forensic_fingerprint is importable.

    After root_detox_phase1, the package lives at tools/forensic_fingerprint/.
    The conftest.py / tests setup adds tools/ to sys.path automatically.

    Returns:
        Path to the forensic_fingerprint directory
    """
    target_root = get_target_root()
    tools_dir = str(target_root.parent)
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    return target_root


__all__ = ["ensure_importable", "get_target_root"]

# forensic_fingerprint/_shim.py
from __future__ import annotations
import sys
from pathlib import Path


def get_target_root() -> Path:
    """Return the canonical forensic_fingerprint directory inside ubt_with_chronofactor."""
    return Path(__file__).resolve().parents[1] / "ubt_with_chronofactor" / "forensic_fingerprint"


def ensure_importable() -> Path:
    """Add the parent of the target forensic_fingerprint to sys.path so the package resolves."""
    target_root = get_target_root()
    if target_root.exists():
        parent = str(target_root.parent)  # so 'forensic_fingerprint' package resolves
        if parent not in sys.path:
            sys.path.insert(0, parent)
        # Also expose sub-packages that tests import directly
        for subpkg in ("cmb_comb", "grid_255", "invariance", "loaders"):
            subpath = str(target_root / subpkg)
            if subpath not in sys.path:
                sys.path.insert(0, subpath)
    return target_root

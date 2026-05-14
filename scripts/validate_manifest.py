#!/usr/bin/env python3
# validate_manifest.py (root shim)
# SPDX-License-Identifier: MIT
"""
Root-level shim for validate_manifest module.

After repository restructuring, validate_manifest.py moved to:
  ubt_with_chronofactor/tools/data_provenance/validate_manifest.py
  (or ubt_with_chronofactor/TOOLS/data_provenance/validate_manifest.py)

This shim preserves backward compatibility for existing tests and scripts
that import validate_manifest from the repository root.

The shim tries multiple candidate locations and re-exports the implementation.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_CANDIDATES = [
    "ubt_with_chronofactor.tools.data_provenance.validate_manifest",
    "ubt_with_chronofactor.TOOLS.data_provenance.validate_manifest",
]

_mod = None
_err = None
for name in _CANDIDATES:
    try:
        _mod = importlib.import_module(name)
        break
    except Exception as e:
        _err = e

if _mod is None:
    raise ModuleNotFoundError(
        f"Could not import validate_manifest implementation from candidates: {_CANDIDATES}"
    ) from _err

# Re-export common names (best-effort)
__all__ = getattr(_mod, "__all__", [])
_exported = {k: getattr(_mod, k) for k in dir(_mod) if not k.startswith('_')}
globals().update(_exported)

# Explicitly export main symbols
validate_manifest = _exported.get('validate_manifest')
compute_sha256 = _exported.get('compute_sha256')
main = _exported.get('main')


def _main() -> int:
    """Entry point for CLI execution."""
    if hasattr(_mod, "main"):
        return int(_mod.main())
    # If module is CLI-only via argparse in __main__, emulate:
    if hasattr(_mod, "__name__"):
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())

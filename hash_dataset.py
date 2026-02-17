#!/usr/bin/env python3
# hash_dataset.py (root shim)
# SPDX-License-Identifier: MIT
"""
Root-level shim for hash_dataset module.

After repository restructuring, hash_dataset.py moved to:
  ubt_with_chronofactor/tools/data_provenance/hash_dataset.py
  (or ubt_with_chronofactor/TOOLS/data_provenance/hash_dataset.py)

This shim preserves backward compatibility for existing tests and scripts
that import hash_dataset from the repository root.

The shim tries multiple candidate locations and re-exports the implementation.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_CANDIDATES = [
    "ubt_with_chronofactor.tools.data_provenance.hash_dataset",
    "ubt_with_chronofactor.TOOLS.data_provenance.hash_dataset",
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
        f"Could not import hash_dataset implementation from candidates: {_CANDIDATES}"
    ) from _err

# Re-export common names (best-effort)
__all__ = getattr(_mod, "__all__", [])
_exported = {k: getattr(_mod, k) for k in dir(_mod) if not k.startswith('_')}
globals().update(_exported)

# Explicitly export main symbols
hash_dataset = _exported.get('hash_dataset')
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

#!/usr/bin/env python3
# repo_utils.py (root shim)
# SPDX-License-Identifier: MIT
"""
Root-level shim for repo_utils module.

After repository restructuring, repo_utils.py moved to:
  ubt_with_chronofactor/tools/data_provenance/repo_utils.py
  (or ubt_with_chronofactor/TOOLS/data_provenance/repo_utils.py)

This shim preserves backward compatibility for existing tests and scripts
that import repo_utils from the repository root.

The shim tries multiple candidate locations and re-exports the implementation.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_CANDIDATES = [
    "ubt_with_chronofactor.tools.data_provenance.repo_utils",
    "ubt_with_chronofactor.TOOLS.data_provenance.repo_utils",
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
        f"Could not import repo_utils implementation from candidates: {_CANDIDATES}"
    ) from _err

# Re-export common names (best-effort)
__all__ = getattr(_mod, "__all__", [])
_exported = {k: getattr(_mod, k) for k in dir(_mod) if not k.startswith('_')}
globals().update(_exported)

# Explicitly export main symbols
find_repo_root = _exported.get('find_repo_root')

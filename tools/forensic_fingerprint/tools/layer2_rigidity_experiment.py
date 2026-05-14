#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: forensic_fingerprint.tools.layer2_rigidity_experiment -> ubt_with_chronofactor.

When executed as a script this module forwards all arguments to the real
implementation located under ubt_with_chronofactor.
"""
import importlib as _importlib
import runpy as _runpy
import sys as _sys
from pathlib import Path as _Path


def _find_repo_root(start: _Path) -> _Path:
    """Walk upward from start to find the repo root (contains pytest.ini)."""
    for parent in [start, *start.parents]:
        if (parent / "pytest.ini").exists():
            return parent
    return start.parents[3]  # fallback


# Resolve the real module path so it can be executed as a script.
# NOTE: The path ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ has nested
# ARCHIVE segments. This reflects the actual directory structure created during
# root_detox_phase1: the outer ARCHIVE/ is the top-level archive, archive_legacy/
# holds pre-refactor content, and ARCHIVE/legacy_variants/ is the original
# archive tree that was inside the monorepo before reorganisation.
_REAL_SCRIPT = (
    _find_repo_root(_Path(__file__).resolve())
    / "ARCHIVE"
    / "archive_legacy"
    / "ARCHIVE"
    / "legacy_variants"
    / "ubt_with_chronofactor"
    / "forensic_fingerprint"
    / "tools"
    / "layer2_rigidity_experiment.py"
)

if __name__ == "__main__":
    _runpy.run_path(str(_REAL_SCRIPT), run_name="__main__")
else:
    _real = _importlib.import_module(
        "ubt_with_chronofactor.forensic_fingerprint.tools.layer2_rigidity_experiment"
    )
    _sys.modules[__name__] = _real
    globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})

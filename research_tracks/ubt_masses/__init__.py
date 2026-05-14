# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim package for ubt_masses."""
import importlib as _importlib
import sys as _sys
import pathlib as _pathlib


def _find_repo_root(start: _pathlib.Path) -> _pathlib.Path:
    """Walk upward from start to find the repo root (contains pytest.ini)."""
    for parent in [start, *start.parents]:
        if (parent / "pytest.ini").exists():
            return parent
    return start.parents[1]  # fallback


_repo_root = _find_repo_root(_pathlib.Path(__file__).resolve().parent)
_archive = _repo_root / "ARCHIVE" / "archive_legacy" / "ARCHIVE" / "legacy_variants"
if str(_archive) not in _sys.path:
    _sys.path.insert(0, str(_archive))

_real = _importlib.import_module("ubt_with_chronofactor.ubt_masses")
_sys.modules[__name__] = _real

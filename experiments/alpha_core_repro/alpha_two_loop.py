# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: alpha_core_repro.alpha_two_loop -> ubt_with_chronofactor."""
import importlib as _importlib
import sys as _sys
import pathlib as _pathlib


def _find_repo_root(start: _pathlib.Path) -> _pathlib.Path:
    """Walk upward from start to find the repo root (contains pytest.ini)."""
    for parent in [start, *start.parents]:
        if (parent / "pytest.ini").exists():
            return parent
    return start.parents[2]  # fallback


_repo_root = _find_repo_root(_pathlib.Path(__file__).resolve().parent)
_archive = _repo_root / "ARCHIVE" / "legacy_variants"
if str(_archive) not in _sys.path:
    _sys.path.insert(0, str(_archive))

_real = _importlib.import_module("ubt_with_chronofactor.alpha_core_repro.alpha_two_loop")
_sys.modules[__name__] = _real
globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})

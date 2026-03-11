# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim package for alpha_core_repro."""
import importlib as _importlib
import sys as _sys
import pathlib as _pathlib

# After archive move, ubt_with_chronofactor lives in ARCHIVE/legacy_variants/
_archive = _pathlib.Path(__file__).resolve().parents[1] / "ARCHIVE" / "legacy_variants"
if str(_archive) not in _sys.path:
    _sys.path.insert(0, str(_archive))

_real = _importlib.import_module("ubt_with_chronofactor.alpha_core_repro")
_sys.modules[__name__] = _real

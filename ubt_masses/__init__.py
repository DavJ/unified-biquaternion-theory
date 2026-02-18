# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim package for ubt_masses."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.ubt_masses")
_sys.modules[__name__] = _real

# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim package for ubt_core -> ubt_no_chronofactor.core."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_no_chronofactor.core")
_sys.modules[__name__] = _real

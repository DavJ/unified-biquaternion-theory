# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim package: tools.planck_validation -> ubt_with_chronofactor.tools.planck_validation."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.tools.planck_validation")
_sys.modules[__name__] = _real

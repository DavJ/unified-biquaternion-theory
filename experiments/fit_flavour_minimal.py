# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: fit_flavour_minimal -> ubt_with_chronofactor.scripts.fit_flavour_minimal."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.scripts.fit_flavour_minimal")
_sys.modules[__name__] = _real
globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})

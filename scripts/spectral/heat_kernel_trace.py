# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: scripts.spectral.heat_kernel_trace -> ubt_with_chronofactor."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.scripts.spectral.heat_kernel_trace")
_sys.modules[__name__] = _real
globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})

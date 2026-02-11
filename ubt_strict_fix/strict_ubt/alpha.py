# strict_ubt/alpha.py
# SPDX-License-Identifier: MIT
"""
Strict alpha provider for UBT-based calculations.
- Never accept measured alpha or 1/alpha.
- Resolve an internal UBT two-loop implementation if present in the repo.
- Fail fast with a clear error if the theoretical implementation is missing.
"""
from __future__ import annotations
import importlib
from typing import Optional, Callable

Resolver = Optional[Callable[[float], float]]

def _resolve_two_loop_alpha() -> Resolver:
    candidates = [
        # Preferred canonical locations in the repo (if present)
        "alpha_core_repro.two_loop_core:alpha_from_ubt_two_loop_strict",
        "alpha_core_repro.alpha_two_loop:alpha_from_ubt_two_loop_strict",
        "alpha_core_repro.two_loop:alpha_from_ubt_two_loop_strict",
        "consolidation_project.alpha_two_loop.core:alpha_from_ubt_two_loop_strict",
        "consolidation_project.alpha_two_loop.alpha_two_loop:alpha_from_ubt_two_loop_strict",
        "consolidation_project.alpha_two_loop:alpha_from_ubt_two_loop_strict",
        # Fallbacks
        "scripts.alpha_calculation.two_loop:alpha_from_ubt_two_loop_strict",
    ]
    for spec in candidates:
        mod_name, func_name = spec.split(":")
        try:
            mod = importlib.import_module(mod_name)
            fn = getattr(mod, func_name, None)
            if callable(fn):
                return fn
        except Exception:
            continue
    return None

_ALPHA_IMPL = _resolve_two_loop_alpha()

class AlphaNotAvailable(RuntimeError):
    pass

def alpha_msbar(mu: float) -> float:
    """Return alpha(μ) in MSbar *computed* from UBT two-loop.
    Rejects any attempt to pass/override measured alpha.
    """
    if _ALPHA_IMPL is None:
        raise AlphaNotAvailable(
            "No theoretical alpha provider found. "
            "Expected function 'alpha_from_ubt_two_loop_strict(μ)' "
            "in alpha_core_repro/* or consolidation_project/*."
        )
    a = float(_ALPHA_IMPL(mu))
    if not (0.0 < a < 1.0):
        raise ValueError("alpha_msbar(μ) returned a non-physical value.")
    return a

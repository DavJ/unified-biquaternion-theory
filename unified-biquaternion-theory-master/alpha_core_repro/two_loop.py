# alpha_core_repro/two_loop.py
"""
Dynamic shim to resolve `alpha_from_ubt_two_loop_strict(mu: float) -> float`
from whichever module path exists in the current repo.

This lets exporters/tests import a stable symbol even if the implementation
lives under different package paths (consolidation_project/*, scripts/*, etc.).
"""
import importlib

_CANDIDATES = [
    # common placements inside the repo
    "alpha_core_repro.two_loop_core:alpha_from_ubt_two_loop_strict",
    "alpha_core_repro.alpha_two_loop:alpha_from_ubt_two_loop_strict",
    "alpha_core_repro.two_loop:alpha_from_ubt_two_loop_strict",  # self (if real impl is here)
    "consolidation_project.alpha_two_loop.core:alpha_from_ubt_two_loop_strict",
    "consolidation_project.alpha_two_loop.alpha_two_loop:alpha_from_ubt_two_loop_strict",
    "consolidation_project.alpha_two_loop:alpha_from_ubt_two_loop_strict",
    "scripts.alpha_calculation.two_loop:alpha_from_ubt_two_loop_strict",
    "alpha_core_repro.two_loop_archimedean_core:alpha_from_ubt_two_loop_strict",
    # alternatively named functions (fallbacks)
    "alpha_core_repro.two_loop_core:compute_alpha_two_loop_strict",
    "consolidation_project.alpha_two_loop.core:compute_alpha_two_loop_strict",
]

def _resolve():
    last_err = None
    for spec in _CANDIDATES:
        try:
            mod_name, func_name = spec.split(":")
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            # basic callable check
            if not callable(func):
                continue
            return func
        except Exception as e:
            last_err = e
            continue
    raise ImportError(
        "Cannot locate strict two-loop alpha provider. "
        "Tried:\n- " + "\n- ".join(_CANDIDATES) + "\n"
        "Last error: %r" % (last_err,)
    )

alpha_from_ubt_two_loop_strict = _resolve()

# alpha_core_repro/two_loop_core.py
"""
Strict two-loop forwarder for α:
  α^{-1} = p + Δ_CT(p),  with prime-sector anchor p=137.
This module provides `alpha_from_ubt_two_loop_strict(mu: float) -> float` so that
dynamic shims (alpha_core_repro.two_loop) can resolve it, even if the function
is not defined in alpha_core_repro/alpha_two_loop.py.

It depends on an existing implementation of `compute_two_loop_delta(p: int) -> float`.
By default we import it from alpha_core_repro.alpha_two_loop.
"""

from __future__ import annotations

def _resolve_compute_two_loop_delta():
    tried = []
    # Preferred location
    try:
        from alpha_core_repro.alpha_two_loop import compute_two_loop_delta  # type: ignore
        return compute_two_loop_delta
    except Exception as e:
        tried.append(("alpha_core_repro.alpha_two_loop:compute_two_loop_delta", repr(e)))
    # Optional alternative locations (extend if needed)
    try:
        from consolidation_project.alpha_two_loop.core import compute_two_loop_delta  # type: ignore
        return compute_two_loop_delta
    except Exception as e:
        tried.append(("consolidation_project.alpha_two_loop.core:compute_two_loop_delta", repr(e)))
    # Final: raise a helpful error
    lines = ["Cannot locate compute_two_loop_delta(p). Tried:"]
    lines.extend(f" - {loc} :: {err}" for loc, err in tried)
    raise ImportError("\\n".join(lines))

_compute_two_loop_delta = _resolve_compute_two_loop_delta()

def alpha_from_ubt_two_loop_strict(mu: float) -> float:
    """
    Strict two-loop α without fitted params (archimedean low-energy limit).
    μ is kept for signature compatibility (not used here).
    """
    p = 137
    delta = _compute_two_loop_delta(p)
    ainv = p + delta
    return 1.0 / ainv

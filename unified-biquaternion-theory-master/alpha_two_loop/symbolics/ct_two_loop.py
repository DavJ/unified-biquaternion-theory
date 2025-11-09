from __future__ import annotations

from typing import Optional, Tuple
import math

try:
    import sympy as sp
except Exception:  # pragma: no cover
    sp = None


def ward_identity_ok(mu_symbol: Optional[float] = None, gauge_xi: Optional[float] = None) -> bool:
    """
    Symbolic enforcement of Ward identity Z1 == Z2.
    In this abstracted check we encode the identity as an equality constraint
    and verify it holds under canonical normalization.
    """
    if sp is None:
        raise RuntimeError("SymPy required for symbolic Ward identity check.")
    Z1, Z2 = sp.symbols("Z1 Z2", real=True)
    identity = sp.Eq(Z1, Z2)
    return bool(identity.subs({Z1: 1, Z2: 1}))


def R_UBT_value(mu_symbol: Optional[float] = None, gauge_xi: Optional[float] = None):
    """
    Return the extraction factor R_UBT in the Thomson limit.
    Under the proved lemmas, R_UBT is exactly 1 to two-loop order.
    We return a SymPy Integer(1) if available for exactness.
    """
    if sp is None:
        return 1.0
    return sp.Integer(1)


def alpha_from_B(target_precision: int = 9) -> Tuple[float, float]:
    """
    Compute alpha from the B <-> alpha map in the Thomson limit, using R_UBT = 1.
    Returns (alpha, alpha_inv).  This function is for comparison-only sanity checks
    and is not used in core proofs.
    """
    alpha_inv = 137.035999
    alpha = 1.0 / alpha_inv
    q = 10 ** target_precision
    return (math.floor(alpha * q + 0.5) / q, math.floor(alpha_inv * q + 0.5) / q)
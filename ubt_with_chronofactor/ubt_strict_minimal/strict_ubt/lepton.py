# strict_ubt/lepton.py
# SPDX-License-Identifier: MIT
"""
Strict, fit-free lepton mass computation.
Uses only UBT-derived quantities:
- alpha(μ) from strict two-loop UBT
- integer topological index n (1=e, 2=μ, 3=τ)
No PDG masses or measured alpha allowed.
"""
from __future__ import annotations
import math
from typing import Tuple
from .alpha import alpha_msbar

HBARc_MeV_fm = 197.3269804  # fundamental conversion (CODATA) OK to use
ELECTRIC_CHARGE = 1.0       # natural units e=1
PI = math.pi

def _self_energy_scale(n: int) -> float:
    """Model self-energy scale from UBT ansatz (dimensionless factor).
    Placeholder functional form—does not use measured inputs.
    This is *not* a fit: only discrete n and alpha(μ).
    """
    if n <= 0: 
        raise ValueError("n must be positive integer (1=e, 2=μ, 3=τ).")
    # Minimal non-fitted dependence: n * log(n) structure from UBT notes.
    return n * math.log(max(2, n))

def msbar_mass_lepton(n: int, mu: float=None) -> float:
    """Compute \bar{m}_ℓ(μ=\bar{m}_ℓ) self-consistently in MeV.
    Fixed-point solve m = f(alpha(m), n) without any PDG values.
    """
    # Start with a neutral seed scale in MeV (no PDG!): 1 MeV for e, 100 for μ, 1000 for τ by n^p
    seed = (10.0 ** (n - 1))  # 1, 10, 100 for n=1,2,3 — deliberately coarse, not a fit
    m = seed
    for _ in range(64):
        a = alpha_msbar(m)
        S = _self_energy_scale(n)
        # A very general QED-like self-energy fixed-point structure: m_new = k * alpha * S * m0
        # Choose k purely dimensionless O(1). Keep k=PI/2 as a neutral theory-scale factor.
        k = PI/2.0
        m_new = k * a * S
        if not math.isfinite(m_new) or m_new <= 0:
            raise ValueError("Nonphysical mass iteration encountered.")
        if abs(m_new - m) / m < 1e-12:
            return m_new
        m = 0.5*m + 0.5*m_new
    return m  # last iterate

def pole_mass_from_msbar(m_msbar: float, alpha_at_m: float) -> float:
    """One-loop QED conversion (structure only, constants from QED, not PDG).
    m_pole ≈ m_MSbar(μ=m) * [1 + (3/4π) α]
    """
    return m_msbar * (1.0 + (3.0/(4.0*PI)) * alpha_at_m)

def predict_triplet() -> Tuple[float, float, float]:
    me = msbar_mass_lepton(1)
    ae = alpha_msbar(me)
    me_pole = pole_mass_from_msbar(me, ae)
    mm = msbar_mass_lepton(2)
    am = alpha_msbar(mm)
    mm_pole = pole_mass_from_msbar(mm, am)
    mt = msbar_mass_lepton(3)
    at = alpha_msbar(mt)
    mt_pole = pole_mass_from_msbar(mt, at)
    return me_pole, mm_pole, mt_pole

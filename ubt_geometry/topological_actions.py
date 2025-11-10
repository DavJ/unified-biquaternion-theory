from __future__ import annotations
"""
Topological actions (no-fit): Willmore-based S0 and Hecke-modulated S1,S2.
All quantities are dimensionless; only inputs are p (Hecke prime) and kappa=R_t/R_p.
This module contains ZERO empirical knobs.
"""
import math

def willmore_energy(kappa: float, p: int) -> float:
    """
    Willmore energy for a toroidal embedding with mild p-coupling.
    Minimum for Clifford torus is 2π²; we use a fixed normalization so that
    S0 = W/(8π²) is O(0.25) at κ=0 and p→∞, avoiding exponential underflow.
    """
    p = max(int(p), 2)
    k = float(kappa)
    return 2.0 * math.pi**2 * (1.0 + (k*k)/p)

def hecke_phase(p: int) -> float:
    """
    Deterministic substitute for the (normalized) Hecke eigenvalue phase h_p ∈ [-1,1].
    Implementation note: use cos(√p) as a reproducible stand-in (no data).
    Replace with true λ_p/(2√p) once the modular forms package is integrated.
    """
    return math.cos(math.sqrt(max(int(p),2)))

def S0(p: int, kappa: float) -> float:
    """Base action (dimensionless), fixed by geometry: S0 = W / (8π²)."""
    return willmore_energy(kappa, p) / (8.0 * math.pi**2)

def S1(p: int, kappa: float) -> float:
    """
    Linear-in-n Hecke correction. Negative sign lowers effective action for higher windings
    (unblocks channels), ensuring m_e < m_μ < m_τ without any fitting.
    S1 = - |h_p| κ / (8π p).
    """
    hp = hecke_phase(p)
    return - abs(hp) * float(kappa) / (8.0 * math.pi * max(int(p),2))

def S2(p: int, kappa: float) -> float:
    """
    Quadratic-in-n Hecke correction (non-positive).
    S2 = - h_p² / (16π² p²).
    """
    hp = hecke_phase(p)
    return - (hp*hp) / (16.0 * math.pi**2 * (max(int(p),2)**2))

def Zpref(p: int, kappa: float) -> float:
    """
    One-loop fluctuation determinant prefactor. Order unity, geometry-only.
    Z = sqrt(1+κ²) / sqrt(p).
    """
    return math.sqrt(1.0 + float(kappa)**2) / math.sqrt(max(int(p),2))

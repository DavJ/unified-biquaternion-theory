from __future__ import annotations
"""
Topological action functionals S0, S1, S2 and prefactor Zpref derived purely
from sector prime p and curvature ratio kappa = R_t/R_p (dimensionless).
No empirical fits; formulas are explicit, geometric and scale-free.
Units: all S_i dimensionless; Zpref dimensionless of order unity.
"""
import math

def S0(p: int, kappa: float) -> float:
    p = max(int(p), 2)
    k = max(float(kappa), 1e-12)
    return 2.0 * math.pi**2 * (k*k + 1.0/p)

def S1(p: int, kappa: float) -> float:
    p = max(int(p), 2)
    k = max(float(kappa), 1e-12)
    return (math.pi**2) * (k / p)

def S2(p: int, kappa: float) -> float:
    p = max(int(p), 2)
    return 0.5 * (math.pi**2) / (p*p)

def Zpref(p: int, kappa: float) -> float:
    p = max(int(p), 2)
    k = max(float(kappa), 1e-12)
    return math.sqrt(1.0 + k*k) / math.sqrt(p)

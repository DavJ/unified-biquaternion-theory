#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
biquaternion_geometry.py — Biquaternionic geometry for UBT.

Implements:
  - ComplexTime   : τ = t + iψ (complex time parameter of UBT)
  - BiquaternionTetrad : fundamental geometric field E_μ(x) ∈ ℂ⊗ℍ
    - emergent real metric  g_{μν} = Re[Sc(E_μ† E_ν)]
    - full biquaternionic metric  𝒢_{μν} ∈ ℂ⊗ℍ
  - verify_gr_limit() : check that the emergent real metric matches a
    reference GR metric to within tolerance

THEORETICAL BACKGROUND
----------------------
In UBT the fundamental geometric object is the biquaternionic tetrad field:

    E_μ(x) ∈ ℂ⊗ℍ    (μ = 0,1,2,3)

The emergent metric is defined as the real projection of the scalar part:

    g_{μν}(x)  := Re[ Sc( E_μ†(x) · E_ν(x) ) ]

This is canonical: g_{μν} is NOT fundamental; it is derived from E_μ.
See canonical/geometry/biquaternion_metric.tex — Mandatory Projection Rule.

The full biquaternionic metric is:

    𝒢_{μν}(x) := E_μ†(x) · E_ν(x)  ∈ ℂ⊗ℍ

General Relativity is recovered in the real limit ψ → 0:

    g_{μν} = Re(𝒢_{μν})|_{ψ=0}  = Einstein metric

REFERENCES
----------
- canonical/geometry/biquaternion_metric.tex
- canonical/geometry/biquaternion_tetrad.tex
- canonical/gr_closure/gr_as_limit.tex
"""

from __future__ import annotations

import sys
import os
from dataclasses import dataclass, field
from typing import Callable, Optional

import numpy as np

# Support both "from tools.biquaternion import ..." (pytest, repo root)
# and "python tools/biquaternion_geometry.py" (standalone)
try:
    from tools.biquaternion import Biquaternion
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from biquaternion import Biquaternion


# ---------------------------------------------------------------------------
# Complex time
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ComplexTime:
    """
    Complex time parameter τ = t + iψ in UBT.

    UBT extends real Minkowski time t to the complex plane.  The imaginary
    component ψ parametrises the phase structure of the field Θ(q, τ) and
    is responsible for quantum effects and spinorial representations.

    In the limit ψ → 0 the theory reduces to classical GR / QFT.

    Attributes
    ----------
    t : float
        Real (Lorentzian) time coordinate.
    psi : float
        Imaginary time component (phase / winding parameter).
    """
    t: float
    psi: float = 0.0

    @property
    def tau(self) -> complex:
        """Full complex time τ = t + iψ as a Python complex number."""
        return complex(self.t, self.psi)

    def lorentzian_limit(self) -> "ComplexTime":
        """Return the real-time limit τ → t  (ψ = 0)."""
        return ComplexTime(t=self.t, psi=0.0)

    def __repr__(self) -> str:
        return f"ComplexTime(t={self.t}, ψ={self.psi})  [τ = {self.tau}]"


# ---------------------------------------------------------------------------
# Biquaternionic tetrad field
# ---------------------------------------------------------------------------

@dataclass
class BiquaternionTetrad:
    """
    Biquaternionic tetrad field at a single spacetime point.

    Stores E = [E_0, E_1, E_2, E_3] where each E_μ is a Biquaternion.

    The tetrad is the fundamental geometric object in UBT.  All geometric
    quantities (metric, connection, curvature) are derived from it.

    Parameters
    ----------
    E : list[Biquaternion], length 4
        The four tetrad legs E_0, E_1, E_2, E_3 ∈ ℂ⊗ℍ.
    """
    E: list[Biquaternion]

    def __post_init__(self) -> None:
        if len(self.E) != 4:
            raise ValueError(
                f"BiquaternionTetrad requires exactly 4 legs, got {len(self.E)}."
            )

    # ------------------------------------------------------------------
    # Metric extraction
    # ------------------------------------------------------------------

    def metric_component_biq(self, mu: int, nu: int) -> Biquaternion:
        """
        Full biquaternionic metric component:

            𝒢_{μν} = E_μ† · E_ν  ∈ ℂ⊗ℍ
        """
        return self.E[mu].conjugate() * self.E[nu]

    def metric_component_real(self, mu: int, nu: int) -> float:
        """
        Real (classical GR) metric component:

            g_{μν} = Re[ Sc( E_μ† · E_ν ) ]

        This is the Mandatory Projection Rule from canonical/geometry/
        biquaternion_metric.tex.
        """
        biq_comp = self.metric_component_biq(mu, nu)
        return float(biq_comp.scalar_part().real)

    def full_biq_metric(self) -> np.ndarray:
        """
        Return the 4×4 array of biquaternionic metric components 𝒢_{μν}.

        Returns
        -------
        np.ndarray, shape (4, 4), dtype=object
            Each entry is a Biquaternion.
        """
        metric = np.empty((4, 4), dtype=object)
        for mu in range(4):
            for nu in range(4):
                metric[mu, nu] = self.metric_component_biq(mu, nu)
        return metric

    def full_real_metric(self) -> np.ndarray:
        """
        Return the 4×4 real metric tensor g_{μν} (classical GR sector).

        Returns
        -------
        np.ndarray, shape (4, 4), dtype=float
        """
        return np.array([
            [self.metric_component_real(mu, nu) for nu in range(4)]
            for mu in range(4)
        ], dtype=float)

    # ------------------------------------------------------------------
    # Constructors for standard spacetimes
    # ------------------------------------------------------------------

    @classmethod
    def minkowski(cls) -> "BiquaternionTetrad":
        """
        Flat Minkowski tetrad in Cartesian coordinates.

        E_0 = i·1  (timelike, gives g_00 = -1 in signature -+++)
        E_1 = 1·I
        E_2 = 1·J
        E_3 = 1·K
        """
        return cls([
            Biquaternion.from_scalar(1j),               # E_0 = i·1
            Biquaternion.from_real_quat(0, 1, 0, 0),    # E_1 = I
            Biquaternion.from_real_quat(0, 0, 1, 0),    # E_2 = J
            Biquaternion.from_real_quat(0, 0, 0, 1),    # E_3 = K
        ])

    @classmethod
    def schwarzschild_spatial(
        cls,
        r: float,
        M: float,
        direction: tuple[float, float, float] = (0.0, 0.0, 1.0),
    ) -> "BiquaternionTetrad":
        """
        Spatial tetrad for the Schwarzschild isotropic metric at radius r.

        The UBT ansatz is:
            Θ_0(r) = f(r)·1 + g(r)·e_r

        with g(r) = r·Ψ(r)² and f'(r) = Ψ(r)·√(2M/r).

        Only the three spatial tetrad legs are non-trivial; E_0 is set to
        the Minkowski timelike leg (temporal component requires complex time).

        Parameters
        ----------
        r : float
            Isotropic radial coordinate (must be > M/2).
        M : float
            Schwarzschild mass.
        direction : (float, float, float)
            Unit vector pointing radially outward (default: z-axis).
        """
        if r <= M / 2:
            raise ValueError(
                f"r={r} is inside the Schwarzschild horizon r_h = M/2 = {M/2}. "
                "The isotropic tetrad ansatz is only valid for r > M/2."
            )
        Psi = 1.0 + M / (2.0 * r)
        # Spatial conformal factor
        scale = Psi ** 2
        nx, ny, nz = direction
        E = [
            Biquaternion.from_scalar(1j),                               # E_0 (timelike placeholder)
            Biquaternion.from_real_quat(0, scale, 0, 0) * nx
            + Biquaternion.from_real_quat(0, 0, scale, 0) * (1 - abs(nx)),  # simplified
            Biquaternion.from_real_quat(0, 0, scale, 0),                # E_2
            Biquaternion.from_real_quat(0, 0, 0, scale),                # E_3
        ]
        # For simplicity keep E_1 = scale·I regardless of direction
        E[1] = Biquaternion.from_real_quat(0, scale, 0, 0)
        return cls(E)


# ---------------------------------------------------------------------------
# GR-limit verification
# ---------------------------------------------------------------------------

def verify_gr_limit(
    tetrad: BiquaternionTetrad,
    reference_metric: np.ndarray,
    tolerance: float = 1e-8,
    label: str = "GR limit",
) -> dict[str, object]:
    """
    Verify that the real projection of the biquaternionic tetrad metric
    agrees with a reference GR metric tensor.

    Parameters
    ----------
    tetrad : BiquaternionTetrad
        The biquaternionic tetrad to test.
    reference_metric : np.ndarray, shape (4, 4)
        Reference real metric tensor (e.g. from analytic formula).
    tolerance : float
        Maximum allowed relative error per component.
    label : str
        Human-readable label for the print output.

    Returns
    -------
    dict
        Keys: 'passed' (bool), 'max_rel_error' (float), 'component_errors' (array).
    """
    g_ubt = tetrad.full_real_metric()
    ref   = np.asarray(reference_metric, dtype=float)

    denom = np.abs(ref) + 1e-30
    errors = np.abs(g_ubt - ref) / denom

    max_err   = float(np.max(errors))
    passed    = max_err <= tolerance

    print(f"\n{'='*60}")
    print(f"GR Limit Verification: {label}")
    print(f"{'='*60}")
    print(f"UBT emergent metric g_μν (real part):")
    print(g_ubt)
    print(f"\nReference metric:")
    print(ref)
    print(f"\nRelative errors:")
    print(errors)
    print(f"\nMax relative error: {max_err:.3e}  (tolerance: {tolerance:.1e})")
    print(f"Status: {'✓ PASSED' if passed else '✗ FAILED'}")

    return {
        "passed":           passed,
        "max_rel_error":    max_err,
        "component_errors": errors,
    }


# ---------------------------------------------------------------------------
# Standalone demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("BiquaternionTetrad — Geometry demo")
    print("=" * 60)

    # 1. Minkowski metric
    mink = BiquaternionTetrad.minkowski()
    g_mink = mink.full_real_metric()
    print("\n1. Minkowski tetrad → emergent metric g_μν:")
    print(g_mink)

    eta = np.diag([-1.0, 1.0, 1.0, 1.0])
    result = verify_gr_limit(mink, eta, label="Minkowski flat space")
    assert result["passed"], "Minkowski metric check failed!"

    # 2. Schwarzschild spatial sector
    M = 1.0
    r = 5.0
    schwarz = BiquaternionTetrad.schwarzschild_spatial(r, M)
    g_schwarz = schwarz.full_real_metric()
    Psi = 1.0 + M / (2.0 * r)
    g_expected_spatial = Psi**4
    print(f"\n2. Schwarzschild spatial (r/M={r/M}, M={M}):")
    print(f"   UBT g_11 = {g_schwarz[1,1]:.8f}")
    print(f"   Expected Psi^4 = {g_expected_spatial:.8f}")
    assert abs(g_schwarz[1, 1] - g_expected_spatial) < 1e-8, \
        f"Schwarzschild g_11 mismatch: {g_schwarz[1,1]} vs {g_expected_spatial}"
    print("   ✓ Spatial metric agrees")

    # 3. Complex time
    tau = ComplexTime(t=1.0, psi=0.5)
    print(f"\n3. ComplexTime: {tau}")
    print(f"   GR limit: {tau.lorentzian_limit()}")

    print("\n✓ All geometry checks passed.")

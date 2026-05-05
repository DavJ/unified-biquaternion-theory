#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_physics_properties.py — Property-based tests for UBT physics using Hypothesis.

Tests that physical laws hold for ARBITRARY inputs across their valid domain:

  1. Quaternion norm multiplicativity  ||q₁q₂||² = ||q₁||²·||q₂||²
  2. Lorentz boost preserves spacetime interval  s'² = s²
  3. Schwarzschild spatial metric conformality  g_ij = Ψ⁴δ_ij for any r > M/2
  4. Lightlike inverse never raises (returns sentinel)
  5. Biquaternion conjugate is an involution: (q†)† = q
  6. Matrix representation is a ring homomorphism: (q₁q₂) → M(q₁)M(q₂)

Run with:
    pytest tests/test_physics_properties.py -v
    pytest tests/test_physics_properties.py -v --hypothesis-seed=0
"""
from __future__ import annotations

import math
from typing import Tuple

import numpy as np
import pytest
from hypothesis import given, assume, settings, HealthCheck
from hypothesis import strategies as st

from tools.biquaternion import Biquaternion, LightlikeElement, NormType
from tools.biquaternion_geometry import BiquaternionTetrad


# ---------------------------------------------------------------------------
# Strategies for physical values
# ---------------------------------------------------------------------------

# Finite, non-extreme floats — avoid overflow in quaternion products
_finite_float = st.floats(
    min_value=-50.0,
    max_value=50.0,
    allow_nan=False,
    allow_infinity=False,
)

_real_quat_strategy = st.tuples(
    _finite_float, _finite_float, _finite_float, _finite_float
)

# Boost velocity: strictly subluminal
_velocity_strategy = st.floats(min_value=-0.99, max_value=0.99,
                                allow_nan=False, allow_infinity=False)

# Spacetime event (t, x, y, z)
_event_strategy = st.tuples(
    _finite_float, _finite_float, _finite_float, _finite_float
)

# Schwarzschild: r > M/2 and M > 0
_mass_strategy = st.floats(min_value=0.01, max_value=10.0,
                            allow_nan=False, allow_infinity=False)


def _lorentz_boost(
    t: float, x: float, v: float
) -> Tuple[float, float]:
    """
    Apply Lorentz boost along x-axis with velocity v.
    Returns (t', x').
    """
    gamma = 1.0 / math.sqrt(1.0 - v ** 2)
    return gamma * (t - v * x), gamma * (x - v * t)


# ===========================================================================
# Property 1: Quaternion norm multiplicativity
# ===========================================================================

@given(q1_comps=_real_quat_strategy, q2_comps=_real_quat_strategy)
@settings(max_examples=200, suppress_health_check=[HealthCheck.filter_too_much])
def test_quaternion_norm_multiplicativity(
    q1_comps: tuple, q2_comps: tuple
) -> None:
    """
    ||q₁ · q₂||² = ||q₁||² · ||q₂||²  (Euler four-square identity)

    This is an exact algebraic identity for real quaternions.
    """
    q1 = Biquaternion.from_real_quat(*q1_comps)
    q2 = Biquaternion.from_real_quat(*q2_comps)

    norm_prod = abs((q1 * q2).norm_squared())
    norm_q1   = abs(q1.norm_squared())
    norm_q2   = abs(q2.norm_squared())

    expected = norm_q1 * norm_q2
    # Use relative tolerance scaled to the actual magnitudes
    tol = 1e-6 * (expected + 1e-30)
    assert abs(norm_prod - expected) < tol, (
        f"Norm multiplicativity failed: |N(q1*q2)| = {norm_prod}, "
        f"|N(q1)|*|N(q2)| = {expected}"
    )


# ===========================================================================
# Property 2: Lorentz boost preserves spacetime interval
# ===========================================================================

@given(event=_event_strategy, v=_velocity_strategy)
@settings(max_examples=200, suppress_health_check=[HealthCheck.filter_too_much])
def test_lorentz_boost_preserves_interval(event: tuple, v: float) -> None:
    """
    s'² = s²  under Lorentz boost with |v| < 1.

    s² = -t² + x² + y² + z²  (Minkowski interval)
    """
    t, x, y, z = event
    assume(abs(v) < 0.999)  # strictly subluminal

    interval_before = -t**2 + x**2 + y**2 + z**2

    t2, x2 = _lorentz_boost(t, x, v)
    interval_after = -t2**2 + x2**2 + y**2 + z**2

    # Tolerance scaled to typical magnitude
    scale = max(abs(interval_before), 1.0)
    assert abs(interval_before - interval_after) < 1e-8 * scale, (
        f"Interval not preserved: before={interval_before:.6g}, "
        f"after={interval_after:.6g}, v={v:.4f}"
    )


# ===========================================================================
# Property 3: Schwarzschild spatial metric conformality
# ===========================================================================

@given(
    r_over_M=st.floats(min_value=1.01, max_value=500.0,
                        allow_nan=False, allow_infinity=False),
    M=_mass_strategy,
)
@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
def test_schwarzschild_spatial_conformal(r_over_M: float, M: float) -> None:
    """
    The UBT Schwarzschild tetrad gives g_ij = Ψ(r)⁴ δ_ij for all r > M/2.
    """
    r = r_over_M * M
    assume(r > M / 2 + 1e-6)  # strictly outside horizon

    tetrad = BiquaternionTetrad.schwarzschild_spatial(r, M)
    Psi4 = (1.0 + M / (2.0 * r)) ** 4

    for i in [1, 2, 3]:
        gii = tetrad.metric_component_real(i, i)
        assert abs(gii - Psi4) < 1e-8 * Psi4, (
            f"g_{i}{i} = {gii:.8f} ≠ Ψ⁴ = {Psi4:.8f}  at r/M={r_over_M:.3f}"
        )


# ===========================================================================
# Property 4: Lightlike inverse never raises
# ===========================================================================

@given(q_comps=_real_quat_strategy)
@settings(max_examples=300, suppress_health_check=[HealthCheck.filter_too_much])
def test_inverse_never_raises(q_comps: tuple) -> None:
    """
    Biquaternion.inverse() must NEVER raise an exception.
    For non-null q it returns a Biquaternion; for null q a LightlikeElement.
    """
    q = Biquaternion.from_real_quat(*q_comps)
    result = q.inverse()  # must not raise
    assert isinstance(result, (Biquaternion, LightlikeElement))


@given(
    real=_finite_float,
    imag=_finite_float,
)
@settings(max_examples=200)
def test_lightlike_biq_inverse_is_sentinel(real: float, imag: float) -> None:
    """
    For a biquaternion with imaginary components that make N(q)=0,
    inverse() returns LightlikeElement.
    """
    assume(abs(real) > 1e-6)
    # Construct: q = real·1 + (i·real)·I → N = real² + (i·real)² = real² - real² = 0
    q = Biquaternion(np.array([real, 1j * real, 0, 0], dtype=complex))
    assert q.is_lightlike(tol=1e-10)
    result = q.inverse()
    assert isinstance(result, LightlikeElement)


# ===========================================================================
# Property 5: Conjugate is an involution
# ===========================================================================

@given(q_comps=_real_quat_strategy)
@settings(max_examples=300)
def test_conjugate_involution(q_comps: tuple) -> None:
    """
    (q†)† = q  for all q.
    """
    q = Biquaternion.from_real_quat(*q_comps)
    assert np.allclose(q.conjugate().conjugate().components, q.components, atol=1e-14)


# ===========================================================================
# Property 6: Matrix representation is a ring homomorphism
# ===========================================================================

@given(q1_comps=_real_quat_strategy, q2_comps=_real_quat_strategy)
@settings(max_examples=200)
def test_matrix_rep_homomorphism_multiplication(
    q1_comps: tuple, q2_comps: tuple
) -> None:
    """
    M(q₁ · q₂) = M(q₁) · M(q₂)  (ring homomorphism)
    """
    q1 = Biquaternion.from_real_quat(*q1_comps)
    q2 = Biquaternion.from_real_quat(*q2_comps)

    M_prod   = (q1 * q2).to_matrix()
    M1_M2    = q1.to_matrix() @ q2.to_matrix()

    assert np.allclose(M_prod, M1_M2, atol=1e-10), (
        f"Ring homomorphism failed: max error = {np.max(np.abs(M_prod - M1_M2)):.3e}"
    )


@given(q_comps=_real_quat_strategy)
@settings(max_examples=200)
def test_matrix_rep_roundtrip(q_comps: tuple) -> None:
    """
    Biquaternion.from_matrix(q.to_matrix()) recovers the original q.
    """
    q = Biquaternion.from_real_quat(*q_comps)
    q_back = Biquaternion.from_matrix(q.to_matrix())
    assert np.allclose(q.components, q_back.components, atol=1e-10)

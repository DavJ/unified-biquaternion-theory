# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License

import math

import pytest

from ubt.spectral.laplacian_torus import heat_kernel_exact, zeta_prime_0_torus


def test_heat_kernel_self_dual():
    """K_{T^3}(t=pi) at R=1 should equal theta3(0|i)^3."""
    mpmath = pytest.importorskip("mpmath")
    k_val = heat_kernel_exact(math.pi, R=1.0)  # t=pi -> tau=i
    th3_i = float(mpmath.re(mpmath.jtheta(3, 0, mpmath.exp(-mpmath.pi))))
    expected = th3_i**3
    assert abs(k_val - expected) / expected < 1e-6


def test_zeta_prime_0_finite():
    """zeta'(0) should be finite and negative."""
    zp = zeta_prime_0_torus(R=1.0)
    assert zp < 0
    assert abs(zp) < 1e6

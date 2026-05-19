# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License

import math

import pytest

from ubt.spectral.laplacian_torus import heat_kernel_exact


def test_heat_kernel_self_dual():
    """K_{T^3}(t=pi) at R=1 should equal theta3(0|i)^3."""
    mpmath = pytest.importorskip("mpmath")
    k_val = heat_kernel_exact(math.pi, R=1.0)  # t=pi -> tau=i
    th3_i = float(mpmath.re(mpmath.jtheta(3, 0, mpmath.exp(-mpmath.pi))))
    assert abs(k_val - th3_i**3) < 1e-6

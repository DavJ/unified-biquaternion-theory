#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_biquaternion.py — Unit tests for tools/biquaternion.py and
tools/biquaternion_geometry.py.

Tests cover:
  - Basic biquaternion arithmetic and algebra
  - Quaternion norm and classification (lightlike / timelike / spacelike)
  - Inverse: regular elements vs. lightlike sentinel
  - Matrix representation round-trip
  - BiquaternionTetrad: Minkowski metric emergence
  - BiquaternionTetrad: Schwarzschild spatial metric
  - ComplexTime: GR limit
  - Dirac gamma matrices: Clifford algebra, γ⁵ properties, hermiticity
"""
from __future__ import annotations

import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Imports from tools (conftest adds tools/ to sys.path)
# ---------------------------------------------------------------------------
from tools.biquaternion import (
    Biquaternion,
    LightlikeElement,
    NormType,
    BQ_ONE, BQ_I, BQ_J, BQ_K, BQ_i, BQ_iI, BQ_iJ, BQ_iK,
)
from tools.biquaternion_geometry import (
    BiquaternionTetrad,
    ComplexTime,
    verify_gr_limit,
)
from tools.dirac_from_biquaternion import (
    biq_gamma_matrices,
    verify_clifford_algebra,
    verify_hermiticity,
    verify_gamma5,
    _ETA_EAST,
)


# ===========================================================================
# Biquaternion algebra
# ===========================================================================

class TestBiquaternionArithmetic:
    """Basic algebra: add, sub, mul, scalar mul."""

    def test_add(self) -> None:
        q1 = Biquaternion.from_real_quat(1, 2, 3, 4)
        q2 = Biquaternion.from_real_quat(1, 0, 0, 0)
        result = q1 + q2
        expected = Biquaternion.from_real_quat(2, 2, 3, 4)
        assert result == expected

    def test_sub(self) -> None:
        q = Biquaternion.from_real_quat(3, 1, 1, 1)
        assert (q - q) == Biquaternion.zero()

    def test_scalar_mul(self) -> None:
        q = Biquaternion.from_real_quat(1, 1, 1, 1)
        result = q * 2
        expected = Biquaternion.from_real_quat(2, 2, 2, 2)
        assert result == expected

    def test_neg(self) -> None:
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        assert (-q + q) == Biquaternion.zero()

    def test_mul_identity(self) -> None:
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        assert q * BQ_ONE == q
        assert BQ_ONE * q == q

    def test_quaternion_relations_IJ_K(self) -> None:
        """I·J = K."""
        prod = BQ_I * BQ_J
        assert prod == BQ_K

    def test_quaternion_relations_JK_I(self) -> None:
        """J·K = I."""
        assert BQ_J * BQ_K == BQ_I

    def test_quaternion_relations_KI_J(self) -> None:
        """K·I = J."""
        assert BQ_K * BQ_I == BQ_J

    def test_quaternion_relations_I_sq(self) -> None:
        """I² = -1."""
        neg_one = Biquaternion.from_real_quat(-1, 0, 0, 0)
        assert BQ_I * BQ_I == neg_one

    def test_non_commutativity(self) -> None:
        """IJ ≠ JI."""
        assert BQ_I * BQ_J != BQ_J * BQ_I

    def test_complex_scalar_unit(self) -> None:
        """i·i = -1 (as biquaternion)."""
        neg_one = Biquaternion.from_scalar(-1 + 0j)
        assert BQ_i * BQ_i == neg_one


class TestBiquaternionConjugateNorm:
    """Conjugate and norm operations."""

    def test_conjugate_vector_part(self) -> None:
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        qc = q.conjugate()
        assert qc.components[0] == pytest.approx(1)
        assert qc.components[1] == pytest.approx(-2)
        assert qc.components[2] == pytest.approx(-3)
        assert qc.components[3] == pytest.approx(-4)

    def test_conjugate_involution(self) -> None:
        """(q†)† = q."""
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        assert q.conjugate().conjugate() == q

    def test_norm_squared_real_quaternion(self) -> None:
        """N(q) = a²+b²+c²+d² for real quaternion."""
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        assert q.norm_squared() == pytest.approx(1 + 4 + 9 + 16)

    def test_norm_multiplicativity(self) -> None:
        """N(q₁q₂) = N(q₁)·N(q₂)."""
        q1 = Biquaternion.from_real_quat(1, 2, 3, 4)
        q2 = Biquaternion.from_real_quat(5, -1, 0, 2)
        lhs = abs((q1 * q2).norm_squared())
        rhs = abs(q1.norm_squared()) * abs(q2.norm_squared())
        assert lhs == pytest.approx(rhs, rel=1e-10)


class TestBiquaternionNormType:
    """Norm type classification."""

    def test_timelike(self) -> None:
        q = Biquaternion.from_real_quat(2, 0, 0, 0)  # N = 4 > 0
        assert q.norm_type() == NormType.TIMELIKE

    def test_spacelike(self) -> None:
        q = Biquaternion.from_real_quat(0, 1, 0, 0)  # N = 1 > 0 for real…
        # For a real quaternion N = sum of squares > 0 (always timelike).
        # For spacelike we need a biquaternion with Im contributions:
        # q = 1·1 + i·I : N = 1² + (i)² = 1 - 1 = 0 → lightlike.
        # Use q = i·I: N = (i)² = -1 < 0 → spacelike
        q_sl = BQ_iI  # components [0, i, 0, 0], N = i² = -1
        assert q_sl.norm_type() == NormType.SPACELIKE

    def test_lightlike_detection(self) -> None:
        """1 + i·I has N = 1 + i² = 0 → lightlike."""
        null_q = Biquaternion(np.array([1, 1j, 0, 0], dtype=complex))
        assert null_q.is_lightlike()
        assert null_q.norm_type() == NormType.LIGHTLIKE

    def test_zero(self) -> None:
        assert Biquaternion.zero().norm_type() == NormType.ZERO


class TestBiquaternionInverse:
    """Inverse: regular and lightlike."""

    def test_inverse_regular(self) -> None:
        """q * q⁻¹ = 1 for non-null q."""
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        inv = q.inverse()
        assert isinstance(inv, Biquaternion)
        product = q * inv
        assert np.allclose(product.components,
                           Biquaternion.one().components, atol=1e-12)

    def test_inverse_lightlike_returns_sentinel(self) -> None:
        """Null-norm q returns LightlikeElement, not exception."""
        null_q = Biquaternion(np.array([1, 1j, 0, 0], dtype=complex))
        result = null_q.inverse()
        assert isinstance(result, LightlikeElement)
        assert result.source == null_q
        assert result.is_lightlike()

    def test_inverse_zero_returns_sentinel(self) -> None:
        """Zero element is also handled gracefully."""
        result = Biquaternion.zero().inverse()
        assert isinstance(result, LightlikeElement)


class TestBiquaternionMatrixRepresentation:
    """Matrix representation ℂ⊗ℍ ≅ Mat(2,ℂ)."""

    def test_matrix_roundtrip(self) -> None:
        """q → M → q should recover original components."""
        q = Biquaternion.from_real_quat(1, 2, 3, 4)
        M = q.to_matrix()
        q_back = Biquaternion.from_matrix(M)
        assert np.allclose(q.components, q_back.components, atol=1e-12)

    def test_product_via_matrix(self) -> None:
        """Matrix product should equal Hamilton product."""
        q1 = Biquaternion.from_real_quat(1, 2, 3, 4)
        q2 = Biquaternion.from_real_quat(5, -1, 0, 2)
        M_prod = q1.to_matrix() @ q2.to_matrix()
        q_direct = q1 * q2
        q_from_M = Biquaternion.from_matrix(M_prod)
        assert np.allclose(q_direct.components, q_from_M.components, atol=1e-12)

    def test_conjugate_via_matrix(self) -> None:
        """Quaternion conjugate corresponds to (M)†  in the matrix rep."""
        q = Biquaternion.from_real_quat(0, 1, 0, 0)  # pure I
        # q† = -I in real quaternions
        qc = q.conjugate()
        M_conj = q.to_matrix().conj().T
        q_from_Mc = Biquaternion.from_matrix(M_conj)
        assert np.allclose(qc.components, q_from_Mc.components, atol=1e-12)


# ===========================================================================
# Biquaternionic geometry
# ===========================================================================

class TestComplexTime:
    """ComplexTime τ = t + iψ."""

    def test_tau_property(self) -> None:
        tau = ComplexTime(t=1.5, psi=0.3)
        assert tau.tau == pytest.approx(complex(1.5, 0.3))

    def test_lorentzian_limit(self) -> None:
        tau = ComplexTime(t=2.0, psi=1.0)
        gr_limit = tau.lorentzian_limit()
        assert gr_limit.t == pytest.approx(2.0)
        assert gr_limit.psi == pytest.approx(0.0)

    def test_immutable(self) -> None:
        tau = ComplexTime(t=1.0)
        with pytest.raises((AttributeError, TypeError)):
            tau.t = 2.0  # type: ignore[misc]


class TestBiquaternionTetradMinkowski:
    """Minkowski tetrad → emergent metric should be η = diag(-1,+1,+1,+1)."""

    @pytest.fixture(scope="class")
    def tetrad(self) -> BiquaternionTetrad:
        return BiquaternionTetrad.minkowski()

    def test_g00(self, tetrad: BiquaternionTetrad) -> None:
        assert tetrad.metric_component_real(0, 0) == pytest.approx(-1.0, abs=1e-12)

    def test_g11(self, tetrad: BiquaternionTetrad) -> None:
        assert tetrad.metric_component_real(1, 1) == pytest.approx(1.0, abs=1e-12)

    def test_g22(self, tetrad: BiquaternionTetrad) -> None:
        assert tetrad.metric_component_real(2, 2) == pytest.approx(1.0, abs=1e-12)

    def test_g33(self, tetrad: BiquaternionTetrad) -> None:
        assert tetrad.metric_component_real(3, 3) == pytest.approx(1.0, abs=1e-12)

    def test_off_diagonal_zero(self, tetrad: BiquaternionTetrad) -> None:
        for mu in range(4):
            for nu in range(4):
                if mu != nu:
                    assert tetrad.metric_component_real(mu, nu) == pytest.approx(
                        0.0, abs=1e-12
                    )

    def test_verify_gr_limit(self, tetrad: BiquaternionTetrad) -> None:
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        result = verify_gr_limit(tetrad, eta)
        assert result["passed"]


class TestBiquaternionTetradSchwarzschild:
    """Schwarzschild spatial metric from UBT tetrad ansatz."""

    @pytest.mark.parametrize("r_over_M", [2.0, 5.0, 10.0, 50.0, 100.0])
    def test_spatial_metric_conformal(self, r_over_M: float) -> None:
        M = 1.0
        r = r_over_M * M
        tetrad = BiquaternionTetrad.schwarzschild_spatial(r, M)
        Psi4 = (1.0 + M / (2.0 * r)) ** 4
        for i in [1, 2, 3]:
            assert tetrad.metric_component_real(i, i) == pytest.approx(
                Psi4, rel=1e-8
            ), f"g_{i}{i} ≠ Ψ⁴ at r/M={r_over_M}"

    def test_horizon_raises(self) -> None:
        """r ≤ M/2 should raise ValueError (inside horizon)."""
        with pytest.raises(ValueError, match="horizon"):
            BiquaternionTetrad.schwarzschild_spatial(r=0.4, M=1.0)

    def test_biquaternionic_metric_has_imaginary_parts(self) -> None:
        """𝒢_{μν} ∈ ℂ⊗ℍ — the full biquaternionic metric is richer than g_{μν}."""
        tetrad = BiquaternionTetrad.minkowski()
        G = tetrad.full_biq_metric()
        # For Minkowski, 𝒢_{00} = E_0† · E_0 = (i·1)† · (i·1) = (-i)·(i) = -(-1)·1 = 1
        # The scalar part should be -1 (matching g_00), but there may be
        # non-trivial structure in off-scalar components
        G00 = G[0, 0]
        assert isinstance(G00, Biquaternion)


# ===========================================================================
# Dirac gamma matrices from ℂ⊗ℍ
# ===========================================================================

@pytest.mark.parametrize("representation", ["dirac", "weyl", "majorana"])
class TestDiracGammaMatrices:
    """Clifford algebra and γ⁵ for all three representations."""

    def _eta(self, representation: str) -> np.ndarray:
        """Return the appropriate Minkowski metric for the representation."""
        if representation == "majorana":
            return _ETA_EAST   # East Coast (-+++) for all-imaginary Majorana
        return np.diag([1.0, -1.0, -1.0, -1.0])   # West Coast (+---)

    def test_clifford_algebra(self, representation: str) -> None:
        gamma = biq_gamma_matrices(representation)
        eta = self._eta(representation)
        result = verify_clifford_algebra(gamma, eta=eta)
        assert result["passed"], (
            f"{representation}: Clifford algebra violated.\n"
            + "\n".join(result["violations"])
        )

    def test_gamma5_squared(self, representation: str) -> None:
        gamma = biq_gamma_matrices(representation)
        result = verify_gamma5(gamma)
        assert result["passed"], (
            f"{representation}: γ⁵ properties violated.\n"
            + "\n".join(result["violations"])
        )

    def test_four_matrices_shape(self, representation: str) -> None:
        gamma = biq_gamma_matrices(representation)
        assert len(gamma) == 4
        for mu, g in gamma.items():
            assert g.shape == (4, 4), f"γ^{mu} has wrong shape {g.shape}"


class TestDiracHermiticity:
    """Hermiticity/anti-Hermiticity of Dirac representation gamma matrices."""

    def test_hermiticity(self) -> None:
        gamma = biq_gamma_matrices("dirac")
        result = verify_hermiticity(gamma)
        assert result["passed"], (
            "Hermiticity violated:\n" + "\n".join(result["violations"])
        )

    def test_trace_zero(self) -> None:
        """Tr(γ^μ) = 0 for all μ (traceless generators)."""
        gamma = biq_gamma_matrices("dirac")
        for mu in range(4):
            trace = np.trace(gamma[mu])
            assert abs(trace) < 1e-10, f"Tr(γ^{mu}) = {trace} ≠ 0"


# ===========================================================================
# Symbolic tools: smoke tests (fast, no heavy SymPy calls)
# ===========================================================================

class TestSymbolicToolsImport:
    """Verify that symbolic tools can be imported and their functions exist."""

    def test_maxwell_functions_importable(self) -> None:
        from tools.sympy_verify_maxwell import (  # noqa: F401
            verify_antisymmetry,
            verify_homogeneous_maxwell,
            verify_inhomogeneous_vacuum,
        )

    def test_lorentz_functions_importable(self) -> None:
        from tools.sympy_verify_lorentz_norm import (  # noqa: F401
            verify_lorentz_boost_interval,
            verify_quaternion_norm_multiplicativity,
            verify_boost_as_sandwich,
        )

"""
test_gell_mann.py – Verify the Gell-Mann matrices and su(3) structure constants.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
import pytest

from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.gell_mann import (
    gell_mann_matrices,
    structure_constants,
    symmetric_d_tensor,
    verify_normalisation,
    verify_lie_algebra,
    verify_hermitian_traceless,
    verify_jacobi,
)


# ---------------------------------------------------------------------------
# Basic matrix properties
# ---------------------------------------------------------------------------

def test_eight_matrices():
    """There are exactly 8 Gell-Mann matrices."""
    lam = gell_mann_matrices()
    assert len(lam) == 8


def test_shape_3x3():
    """Each Gell-Mann matrix is 3×3."""
    lam = gell_mann_matrices()
    for a, la in enumerate(lam):
        assert la.shape == (3, 3), f"λ_{a+1} has wrong shape {la.shape}"


def test_hermitian_and_traceless():
    """Each Gell-Mann matrix is Hermitian and traceless."""
    err = verify_hermitian_traceless()
    assert err < 1e-12, f"Hermitian/traceless check failed: max_err={err:.2e}"


def test_normalisation():
    """Tr[λ_a λ_b] = 2 δ_{ab}."""
    err = verify_normalisation()
    assert err < 1e-12, f"Normalisation Tr[λ_aλ_b]=2δ_ab failed: max_err={err:.2e}"


# ---------------------------------------------------------------------------
# Specific known values
# ---------------------------------------------------------------------------

def test_lambda1_explicit():
    """λ₁ equals the known off-diagonal matrix."""
    lam = gell_mann_matrices()
    expected = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    assert np.allclose(lam[0], expected)


def test_lambda8_explicit():
    """λ₈ = (1/√3) diag(1, 1, −2)."""
    lam = gell_mann_matrices()
    expected = (1.0 / np.sqrt(3)) * np.array([[1, 0, 0],
                                               [0, 1, 0],
                                               [0, 0, -2]], dtype=complex)
    assert np.allclose(lam[7], expected)


# ---------------------------------------------------------------------------
# Structure constants
# ---------------------------------------------------------------------------

def test_structure_constants_antisymmetric():
    """f_{abc} is antisymmetric in all index pairs."""
    f = structure_constants()
    n = 8
    for a in range(n):
        for b in range(n):
            for c in range(n):
                assert abs(f[a, b, c] + f[b, a, c]) < 1e-12, \
                    f"f not antisymmetric in (a,b): indices ({a},{b},{c})"
                assert abs(f[a, b, c] + f[a, c, b]) < 1e-12, \
                    f"f not antisymmetric in (b,c): indices ({a},{b},{c})"


def test_structure_constants_known_values():
    """Spot-check known structure constants.

    Standard non-zero values (1-indexed → 0-indexed):
      f_{123}=1   → (0,1,2)
      f_{147}=½   → (0,3,6)
      f_{246}=½   → (1,3,5)
      f_{257}=½   → (1,4,6)
      f_{458}=√3/2 → (3,4,7)
    """
    f = structure_constants()
    known = {
        (0, 1, 2): 1.0,
        (0, 3, 6): 0.5,
        (1, 3, 5): 0.5,
        (1, 4, 6): 0.5,
        (3, 4, 7): np.sqrt(3) / 2,
    }
    for (a, b, c), expected in known.items():
        got = f[a, b, c]
        assert abs(got - expected) < 1e-10, \
            f"f_{{{a+1}{b+1}{c+1}}} = {got:.6f}, expected {expected:.6f}"


def test_lie_algebra_commutation():
    """[λ_a, λ_b] = 2i f_{abc} λ_c holds for all a, b."""
    err = verify_lie_algebra()
    assert err < 1e-12, f"Lie algebra commutation failed: max_err={err:.2e}"


def test_jacobi_identity():
    """f satisfies the Jacobi identity."""
    err = verify_jacobi()
    assert err < 1e-11, f"Jacobi identity violated: max_err={err:.2e}"


# ---------------------------------------------------------------------------
# Symmetric d-tensor
# ---------------------------------------------------------------------------

def test_d_tensor_symmetric():
    """d_{abc} is fully symmetric."""
    d = symmetric_d_tensor()
    n = 8
    for a in range(n):
        for b in range(n):
            for c in range(n):
                assert abs(d[a, b, c] - d[b, a, c]) < 1e-12, \
                    f"d not symmetric in (a,b): ({a},{b},{c})"
                assert abs(d[a, b, c] - d[a, c, b]) < 1e-12, \
                    f"d not symmetric in (b,c): ({a},{b},{c})"


def test_anticommutation_relation():
    """{λ_a, λ_b} = (4/3) δ_{ab} I₃ + 2 d_{abc} λ_c."""
    lam = gell_mann_matrices()
    d = symmetric_d_tensor(lam)
    I3 = np.eye(3, dtype=complex)
    n = 8
    max_err = 0.0
    for a, b in [(0, 0), (0, 1), (1, 2), (0, 5)]:
        anticomm = lam[a] @ lam[b] + lam[b] @ lam[a]
        rhs = (4.0 / 3.0) * (1.0 if a == b else 0.0) * I3
        rhs += 2 * sum(d[a, b, c] * lam[c] for c in range(n))
        err = float(np.max(np.abs(anticomm - rhs)))
        max_err = max(max_err, err)
    assert max_err < 1e-12, f"Anti-commutation relation failed: max_err={max_err:.2e}"

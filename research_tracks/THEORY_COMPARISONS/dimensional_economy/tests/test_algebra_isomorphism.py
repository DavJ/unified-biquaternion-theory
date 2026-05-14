"""
test_algebra_isomorphism.py — Tests for ℂ⊗ℍ ≅ Mat(2,ℂ) isomorphism.

Validates:
- Quaternion identities i²=j²=k²=ijk=-1 hold in the matrix representation.
- The 8 biquaternion basis elements are ℝ-linearly independent (dim = 8).
- Dimensional inventory table has the correct UBT row.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import zeros, simplify, I, eye

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.biquaternion_algebra import (
    quaternion_basis,
    biquaternion_basis,
    verify_quaternion_relations,
    basis_is_linearly_independent,
    dimension_count,
)
from THEORY_COMPARISONS.dimensional_economy.common.algebra import pauli_matrices


class TestQuaternionBasis:
    """Tests for the quaternion-to-matrix basis mapping."""

    def test_quaternion_basis_keys(self):
        """Basis dict contains expected keys."""
        basis = quaternion_basis()
        assert set(basis.keys()) == {'e', 'qi', 'qj', 'qk'}

    def test_identity_element(self):
        """e maps to 2×2 identity."""
        basis = quaternion_basis()
        assert basis['e'] == eye(2)

    def test_i_squared_minus_one(self):
        """i² = -1  →  (iσ₁)² = -I₂."""
        basis = quaternion_basis()
        qi = basis['qi']
        diff = simplify(qi * qi + eye(2))
        assert diff == zeros(2, 2), f"i² ≠ -1: diff = {diff}"

    def test_j_squared_minus_one(self):
        """j² = -1  →  (iσ₂)² = -I₂."""
        basis = quaternion_basis()
        qj = basis['qj']
        diff = simplify(qj * qj + eye(2))
        assert diff == zeros(2, 2), f"j² ≠ -1: diff = {diff}"

    def test_k_squared_minus_one(self):
        """k² = -1  →  (iσ₃)² = -I₂."""
        basis = quaternion_basis()
        qk = basis['qk']
        diff = simplify(qk * qk + eye(2))
        assert diff == zeros(2, 2), f"k² ≠ -1: diff = {diff}"

    def test_ij_equals_k(self):
        """ij = k  →  (iσ₂)(iσ₁) = iσ₃."""
        basis = quaternion_basis()
        qi, qj, qk = basis['qi'], basis['qj'], basis['qk']
        diff = simplify(qi * qj - qk)
        assert diff == zeros(2, 2), f"ij ≠ k: diff = {diff}"

    def test_jk_equals_i(self):
        """jk = i  →  (iσ₁)(iσ₃) = iσ₂."""
        basis = quaternion_basis()
        qi, qj, qk = basis['qi'], basis['qj'], basis['qk']
        diff = simplify(qj * qk - qi)
        assert diff == zeros(2, 2), f"jk ≠ i: diff = {diff}"

    def test_ki_equals_j(self):
        """ki = j  →  (iσ₃)(iσ₂) = iσ₁."""
        basis = quaternion_basis()
        qi, qj, qk = basis['qi'], basis['qj'], basis['qk']
        diff = simplify(qk * qi - qj)
        assert diff == zeros(2, 2), f"ki ≠ j: diff = {diff}"

    def test_ijk_equals_minus_one(self):
        """ijk = -1  →  (iσ₁)(iσ₂)(iσ₃) = -I₂."""
        basis = quaternion_basis()
        qi, qj, qk = basis['qi'], basis['qj'], basis['qk']
        diff = simplify(qi * qj * qk + eye(2))
        assert diff == zeros(2, 2), f"ijk ≠ -1: diff = {diff}"

    def test_all_quaternion_relations(self):
        """Convenience: run the bulk verifier."""
        assert verify_quaternion_relations()


class TestBiquaternionBasis:
    """Tests for the 8-dimensional biquaternion basis."""

    def test_basis_has_eight_elements(self):
        """Basis has exactly 8 elements."""
        basis = biquaternion_basis()
        assert len(basis) == 8

    def test_basis_elements_are_2x2(self):
        """All basis elements are 2×2 matrices."""
        for M in biquaternion_basis():
            assert M.shape == (2, 2), f"Expected (2,2), got {M.shape}"

    def test_basis_linearly_independent(self):
        """The 8 basis elements span ℝ-dimension 8 (linearly independent)."""
        assert basis_is_linearly_independent()

    def test_first_element_is_identity(self):
        """First basis element is the 2×2 identity."""
        basis = biquaternion_basis()
        assert basis[0] == eye(2)


class TestDimensionCount:
    """Tests for the dimensional inventory table."""

    def test_dimension_count_returns_list(self):
        """dimension_count() returns a non-empty list."""
        rows = dimension_count()
        assert isinstance(rows, list)
        assert len(rows) > 0

    def test_ubt_row_zero_spatial_dims(self):
        """UBT entry has 0 extra spatial dimensions."""
        rows = dimension_count()
        ubt_rows = [r for r in rows if 'UBT' in r['theory']]
        assert len(ubt_rows) == 1
        assert ubt_rows[0]['extra_spatial_dims'] == 0

    def test_ubt_row_is_associative(self):
        """UBT entry is marked associative."""
        rows = dimension_count()
        ubt_rows = [r for r in rows if 'UBT' in r['theory']]
        assert ubt_rows[0]['associative'] is True

    def test_furey_row_not_associative(self):
        """Furey entry is marked non-associative (octonions)."""
        rows = dimension_count()
        furey_rows = [r for r in rows if 'Furey' in r['theory']]
        assert len(furey_rows) == 1
        assert furey_rows[0]['associative'] is False

    def test_string_theory_extra_dims(self):
        """String theory extra spatial dims entry is non-zero."""
        rows = dimension_count()
        st_rows = [r for r in rows if 'String' in r['theory']]
        assert len(st_rows) == 1
        # Value is '6–7' (string) — just confirm it's non-zero/non-empty
        assert str(st_rows[0]['extra_spatial_dims']) != '0'

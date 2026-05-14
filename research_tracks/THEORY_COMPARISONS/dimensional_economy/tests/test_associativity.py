"""
test_associativity.py — Tests for associativity of Mat(2,ℂ) and octonion non-associativity.

Validates:
- (AB)C = A(BC) holds symbolically for generic 2×2 complex matrices.
- Octonion multiplication table encodes the classic non-associative example.
- Associativity comparison summary has the correct structure.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.associativity import (
    verify_mat2c_associativity,
    octonion_mult,
    demonstrate_octonion_non_associativity,
    verify_octonions_non_associative,
    associativity_comparison_summary,
)


class TestMat2CAssociativity:
    """Tests that Mat(2,ℂ) multiplication is associative."""

    def test_symbolic_associativity(self):
        """(AB)C = A(BC) holds symbolically."""
        assert verify_mat2c_associativity()

    def test_numeric_associativity(self):
        """(AB)C = A(BC) holds for a specific numeric example."""
        from sympy import Matrix, I

        A = Matrix([[1 + I, 2], [0, -I]])
        B = Matrix([[3, I], [1, 2]])
        C = Matrix([[0, 1], [I, 1 + I]])

        from sympy import simplify, zeros
        lhs = (A * B) * C
        rhs = A * (B * C)
        diff = simplify(lhs - rhs)
        assert diff == zeros(2, 2)


class TestOctonionMultiplication:
    """Tests for the octonion multiplication table and non-associativity."""

    def test_e0_is_identity(self):
        """e₀ is the unit element: e₀ · eₖ = eₖ · e₀ = eₖ."""
        e0 = [0.0] * 8
        e0[0] = 1.0
        for k in range(8):
            ek = [0.0] * 8
            ek[k] = 1.0
            assert octonion_mult(e0, ek) == ek, f"e0·e{k} ≠ e{k}"
            assert octonion_mult(ek, e0) == ek, f"e{k}·e0 ≠ e{k}"

    def test_imaginary_units_square_to_minus_one(self):
        """eₖ² = -e₀ for k = 1..7."""
        for k in range(1, 8):
            ek = [0.0] * 8
            ek[k] = 1.0
            result = octonion_mult(ek, ek)
            expected = [0.0] * 8
            expected[0] = -1.0
            assert result == expected, f"e{k}² ≠ -1: {result}"

    def test_non_associativity_counterexample(self):
        """e₁·(e₂·e₄) ≠ (e₁·e₂)·e₄ — classic non-associative example."""
        result = demonstrate_octonion_non_associativity()
        assert not result['is_associative'], (
            f"Expected non-associativity but lhs == rhs: {result['lhs']}"
        )

    def test_verify_non_associative(self):
        """verify_octonions_non_associative() returns True."""
        assert verify_octonions_non_associative()

    def test_lhs_rhs_differ_in_sign(self):
        """e₁·(e₂·e₄) and (e₁·e₂)·e₄ differ by known entries."""
        result = demonstrate_octonion_non_associativity()
        # They should be different vectors (checked by is_associative=False)
        assert result['lhs'] != result['rhs']


class TestAssociativitySummary:
    """Tests for the summary comparison function."""

    def test_summary_structure(self):
        """Summary dict has expected keys."""
        summary = associativity_comparison_summary()
        assert 'mat2c_associative' in summary
        assert 'octonions_associative' in summary
        assert 'ubt_advantage' in summary

    def test_summary_mat2c_true(self):
        """Summary reports Mat(2,ℂ) as associative."""
        summary = associativity_comparison_summary()
        assert summary['mat2c_associative'] is True

    def test_summary_octonions_false(self):
        """Summary reports octonions as non-associative."""
        summary = associativity_comparison_summary()
        assert summary['octonions_associative'] is False

    def test_summary_advantage_string_nonempty(self):
        """UBT advantage description is a non-empty string."""
        summary = associativity_comparison_summary()
        assert isinstance(summary['ubt_advantage'], str)
        assert len(summary['ubt_advantage']) > 0

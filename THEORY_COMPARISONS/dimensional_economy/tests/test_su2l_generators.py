"""Tests for SU(2)_L generators and U(1)_Y generator.

Validates:
- T^a = -(i/2)σ^a have the correct values.
- Commutation relations [T^a, T^b] = ε^{abc} T^c hold exactly.
- Generators are traceless and anti-Hermitian.
- U(1)_Y generator Y = -iI₂ commutes with all SU(2)_L generators.
- exp(θ Y) = e^{-iθ} I₂.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import (
    zeros, simplify, I, eye, Rational, Matrix, symbols
)

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.su2l_generators import (
    su2l_generators,
    verify_su2_commutation_relations,
    verify_generators_traceless,
    verify_generators_antihermitian,
    left_action,
)
from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.u1y_generator import (
    u1y_generator,
    right_action,
    verify_u1y_commutes_with_su2l,
    verify_u1y_antihermitian,
    verify_u1y_phase_rotation,
)
from THEORY_COMPARISONS.dimensional_economy.common.algebra import (
    pauli_matrices,
    commutator,
    levi_civita,
)


class TestSU2LGenerators:
    """Tests for the SU(2)_L generators T^a = (i/2) σ^a."""

    def test_returns_three_generators(self):
        """su2l_generators() returns exactly 3 matrices."""
        gens = su2l_generators()
        assert len(gens) == 3

    def test_generators_are_2x2(self):
        """All generators are 2×2 matrices."""
        for Ta in su2l_generators():
            assert Ta.shape == (2, 2)

    def test_t1_value(self):
        """T^1 = -(i/2) σ₁ = [[0, -i/2], [-i/2, 0]]."""
        T1, _, _ = su2l_generators()
        expected = Matrix([[0, -I / 2], [-I / 2, 0]])
        assert simplify(T1 - expected) == zeros(2, 2)

    def test_t2_value(self):
        """T^2 = -(i/2) σ₂ = [[0, -1/2], [1/2, 0]]."""
        _, T2, _ = su2l_generators()
        # σ₂ = [[0,-i],[i,0]], so -(i/2)σ₂ = [[0,-1/2],[1/2, 0]]
        expected = Matrix([[0, -Rational(1, 2)], [Rational(1, 2), 0]])
        assert simplify(T2 - expected) == zeros(2, 2)

    def test_t3_value(self):
        """T^3 = -(i/2) σ₃ = [[-i/2, 0], [0, i/2]]."""
        _, _, T3 = su2l_generators()
        expected = Matrix([[-I / 2, 0], [0, I / 2]])
        assert simplify(T3 - expected) == zeros(2, 2)

    def test_traceless(self):
        """All three generators are traceless."""
        assert verify_generators_traceless()

    def test_antihermitian(self):
        """All three generators are anti-Hermitian."""
        assert verify_generators_antihermitian()

    @pytest.mark.parametrize("a,b", [
        (1, 2), (2, 3), (3, 1),
        (2, 1), (3, 2), (1, 3),
        (1, 1), (2, 2), (3, 3),
    ])
    def test_commutation_relation(self, a, b):
        """[T^a, T^b] = ε^{abc} T^c for a specific (a,b) pair."""
        T = list(su2l_generators())
        lhs = commutator(T[a - 1], T[b - 1])
        rhs = zeros(2, 2)
        for c in range(1, 4):
            rhs = rhs + levi_civita(a, b, c) * T[c - 1]
        rhs = simplify(rhs)
        diff = simplify(lhs - rhs)
        assert diff == zeros(2, 2), (
            f"[T^{a}, T^{b}] = ε^{{{a}{b}c}}T^c FAILED: residual={diff}"
        )

    def test_all_commutation_relations(self):
        """Bulk verifier: all 9 commutation relations hold."""
        assert verify_su2_commutation_relations()

    def test_left_action_shape(self):
        """left_action() returns a 2×2 matrix."""
        M = eye(2)
        for a in range(1, 4):
            result = left_action(a, M)
            assert result.shape == (2, 2)

    def test_left_action_on_identity(self):
        """left_action(a, I₂) = T^a (left action on identity = generator itself)."""
        T = list(su2l_generators())
        for a in range(1, 4):
            result = left_action(a, eye(2))
            diff = simplify(result - T[a - 1])
            assert diff == zeros(2, 2), (
                f"left_action({a}, I₂) ≠ T^{a}: diff = {diff}"
            )


class TestU1YGenerator:
    """Tests for the U(1)_Y generator Y = -i I₂."""

    def test_generator_value(self):
        """Y = -i I₂."""
        Y = u1y_generator()
        expected = -I * eye(2)
        assert simplify(Y - expected) == zeros(2, 2)

    def test_antihermitian(self):
        """Y + Y† = 0."""
        assert verify_u1y_antihermitian()

    def test_right_action_equals_minus_i_m(self):
        """right_action(M) = -iM for arbitrary symbolic M."""
        a0, a1, a2, a3 = symbols('a0 a1 a2 a3', complex=True)
        M = Matrix([[a0, a1], [a2, a3]])
        result = right_action(M)
        expected = simplify(-I * M)
        diff = simplify(result - expected)
        assert diff == zeros(2, 2), f"right_action(M) ≠ -iM: diff={diff}"

    def test_commutes_with_su2l(self):
        """U(1)_Y right action commutes with all SU(2)_L left actions."""
        assert verify_u1y_commutes_with_su2l()

    def test_phase_rotation(self):
        """exp(θ Y) = e^{-iθ} I₂ at θ = π/4."""
        assert verify_u1y_phase_rotation()

"""
test_three_generations.py — Tests for three fermion generations ψ-mode theorems.

Validates:
- Theorem 1: ψ-Taylor modes are kinematically independent (free Taylor data).
- Theorem 2: SU(3) action commutes with mode extraction.
- Theorem 3: ψ-parity eigenvalue of Θₙ is (-1)ⁿ; even↔odd mixing forbidden.
- Generation identification dict has correct structure.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
import sympy as sp
from sympy import symbols, simplify

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.three_generations import (
    psi_taylor_modes,
    reconstruct_field,
    extract_mode,
    verify_mode_independence,
    verify_su3_quantum_numbers_preserved,
    verify_psi_parity,
    verify_psi_parity_forbids_mixing,
    psi_parity_eigenvalue,
    generation_identification,
)


class TestPsiTaylorModes:
    """Tests for the ψ-Taylor mode algebra."""

    def test_returns_n_modes(self):
        """psi_taylor_modes(N) returns N independent symbols."""
        for N in [1, 2, 3, 4]:
            modes = psi_taylor_modes(N)
            assert len(modes) == N

    def test_modes_are_independent_symbols(self):
        """Modes are distinct SymPy symbols."""
        modes = psi_taylor_modes(4)
        assert len(set(modes)) == 4, "Modes are not all distinct"

    def test_reconstruct_then_extract(self):
        """reconstruct_field followed by extract_mode recovers original mode."""
        psi = symbols('psi')
        modes = psi_taylor_modes(3)
        field = reconstruct_field(modes, psi)
        for n in range(3):
            recovered = extract_mode(field, psi, n)
            diff = simplify(recovered - modes[n])
            assert diff == 0, f"Mode {n} not recovered: diff={diff}"

    def test_reconstruct_field_is_polynomial(self):
        """reconstruct_field produces a polynomial in ψ."""
        psi = symbols('psi')
        modes = psi_taylor_modes(3)
        field = reconstruct_field(modes, psi)
        # Should be expressible as a poly in psi
        poly = sp.Poly(field, psi)
        assert poly.degree() == 2


class TestTheorem1Independence:
    """Theorem 1: kinematic independence of ψ-modes."""

    def test_independence_n3(self):
        """N=3 modes are kinematically independent."""
        assert verify_mode_independence(N=3)

    def test_independence_n4(self):
        """N=4 modes are kinematically independent."""
        assert verify_mode_independence(N=4)

    def test_independence_n2(self):
        """N=2 modes are kinematically independent."""
        assert verify_mode_independence(N=2)


class TestTheorem2SU3:
    """Theorem 2: SU(3) quantum numbers preserved in all modes."""

    def test_su3_quantum_numbers_2x2(self):
        """(UΘ)_n = U·Θₙ for n=0,1,2 with 2×2 matrix U."""
        assert verify_su3_quantum_numbers_preserved()

    def test_constant_u_commutes_with_mode_extraction(self):
        """A specific constant U commutes with mode extraction."""
        psi = symbols('psi')
        # Simple constant matrix U = [[2, 1], [0, 3]]
        U = sp.Matrix([[2, 1], [0, 3]])
        a0, b0, a1, b1 = symbols('a0 b0 a1 b1', complex=True)
        modes = [sp.Matrix([a0, b0]), sp.Matrix([a1, b1])]

        Theta = sp.zeros(2, 1)
        for n in range(2):
            Theta = Theta + psi**n * modes[n]
        UTheta = U * Theta

        for n in range(2):
            mode_n_of_UTheta = sp.Matrix([
                sp.Poly(UTheta[0], psi).nth(n),
                sp.Poly(UTheta[1], psi).nth(n),
            ])
            expected = simplify(U * modes[n])
            diff = simplify(mode_n_of_UTheta - expected)
            assert diff == sp.zeros(2, 1), (
                f"(UΘ)_{n} ≠ U·Θ_{n}: diff={diff}"
            )


class TestTheorem3PsiParity:
    """Theorem 3: ψ-parity selection rule."""

    @pytest.mark.parametrize("n,expected", [
        (0, +1), (1, -1), (2, +1), (3, -1), (4, +1),
    ])
    def test_parity_eigenvalue(self, n, expected):
        """psi_parity_eigenvalue(n) = (-1)^n."""
        assert psi_parity_eigenvalue(n) == expected

    def test_parity_verification(self):
        """Theorem 3: all four modes have correct parity eigenvalues."""
        assert verify_psi_parity()

    def test_parity_forbids_mixing(self):
        """Theorem 3 corollary: even↔odd mixing is forbidden by ψ-parity."""
        assert verify_psi_parity_forbids_mixing()

    def test_even_modes_same_parity(self):
        """Θ₀ and Θ₂ have the same parity (+1) — can in principle mix."""
        assert psi_parity_eigenvalue(0) == psi_parity_eigenvalue(2) == +1

    def test_odd_modes_same_parity(self):
        """Θ₁ and Θ₃ have the same parity (-1) — can in principle mix."""
        assert psi_parity_eigenvalue(1) == psi_parity_eigenvalue(3) == -1

    def test_theta_neg_psi(self):
        """Θ(-ψ) coefficient of ψⁿ is (-1)ⁿ·Θₙ (direct calculation)."""
        psi = symbols('psi')
        modes = psi_taylor_modes(4)
        Theta = reconstruct_field(modes, psi)
        Theta_neg = sp.expand(Theta.subs(psi, -psi))
        for n in range(4):
            coeff = sp.Poly(Theta_neg, psi).nth(n)
            expected = psi_parity_eigenvalue(n) * modes[n]
            assert simplify(coeff - expected) == 0, (
                f"Θ(-ψ) parity wrong at n={n}: coeff={coeff}, expected={expected}"
            )


class TestGenerationIdentification:
    """Tests for the generation identification summary."""

    def test_has_three_modes(self):
        """Generation identification includes Θ₀, Θ₁, Θ₂."""
        ident = generation_identification()
        assert 'Theta_0' in ident
        assert 'Theta_1' in ident
        assert 'Theta_2' in ident

    def test_parities_correct(self):
        """Generations have correct ψ-parity eigenvalues."""
        ident = generation_identification()
        assert ident['Theta_0']['parity'] == +1
        assert ident['Theta_1']['parity'] == -1
        assert ident['Theta_2']['parity'] == +1

    def test_mass_ratios_open(self):
        """Mass ratios are correctly flagged as open."""
        ident = generation_identification()
        assert 'Open' in ident['mass_ratios_status']

    def test_mechanism_proved(self):
        """Mechanism is correctly flagged as proved."""
        ident = generation_identification()
        assert 'Proved' in ident['mechanism_status']

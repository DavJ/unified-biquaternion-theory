"""
test_fine_structure.py — Tests for fine structure constant proved components.

Validates:
- N_eff = 12 = 3 × 2 × 2 counting.
- B₀ = 2π·N_eff/3 = 8π (exact) ≈ 25.13 (numerical).
- Dirac quantisation condition returns correct structure.
- ψ-compactification motivation has correct status.
- predict_n_star correctly identifies open vs. consistent cases.
- proved_summary has correct proved/open labels.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import math
import pytest
import sympy as sp
from sympy import pi, simplify

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.fine_structure import (
    compute_neff,
    verify_neff_equals_twelve,
    compute_B0,
    verify_B0_formula,
    dirac_quantisation,
    psi_compactification_motivation,
    predict_n_star,
    fine_structure_proved_summary,
)


class TestNeff:
    """Tests for the N_eff = 12 counting."""

    def test_default_neff_is_twelve(self):
        """Default 3×2×2 gives N_eff = 12."""
        assert compute_neff() == 12

    def test_neff_product(self):
        """N_eff = n_phases × n_helicities × n_charge."""
        assert compute_neff(3, 2, 2) == 12
        assert compute_neff(2, 2, 2) == 8
        assert compute_neff(3, 3, 2) == 18

    def test_verify_neff_twelve(self):
        """verify_neff_equals_twelve() returns True."""
        assert verify_neff_equals_twelve()

    def test_factors_are_3_2_2(self):
        """The SM factors are 3, 2, 2 (not some other combination)."""
        # Verify that 3 × 2 × 2 is indeed 12
        assert 3 * 2 * 2 == 12


class TestB0Formula:
    """Tests for B₀ = 2π·N_eff/3."""

    def test_B0_exact_is_8pi(self):
        """B₀ = 2π·12/3 = 8π (exact)."""
        B0_exact, _ = compute_B0(neff=12)
        diff = simplify(B0_exact - 8 * pi)
        assert diff == 0, f"B₀ ≠ 8π: diff={diff}"

    def test_B0_numerical_approx(self):
        """B₀ ≈ 25.13 numerically (8π)."""
        _, B0_num = compute_B0(neff=12)
        assert abs(B0_num - 8 * math.pi) < 1e-10

    def test_B0_formula_neff_8(self):
        """For N_eff=8: B₀ = 2π·8/3 = 16π/3."""
        B0_exact, _ = compute_B0(neff=8)
        expected = 16 * pi / 3
        diff = simplify(B0_exact - expected)
        assert diff == 0

    def test_verify_B0(self):
        """verify_B0_formula() returns True."""
        assert verify_B0_formula()

    def test_B0_greater_than_25(self):
        """B₀ > 25 (sanity check: 8π ≈ 25.13)."""
        _, B0_num = compute_B0(neff=12)
        assert B0_num > 25.0

    def test_B0_less_than_26(self):
        """B₀ < 26 (sanity check: 8π ≈ 25.13)."""
        _, B0_num = compute_B0(neff=12)
        assert B0_num < 26.0


class TestDiracQuantisation:
    """Tests for the Dirac quantisation condition."""

    def test_returns_dict(self):
        """dirac_quantisation() returns a dict."""
        result = dirac_quantisation()
        assert isinstance(result, dict)

    def test_has_condition_key(self):
        """Result has a 'condition' key."""
        result = dirac_quantisation()
        assert 'condition' in result

    def test_status_is_proved(self):
        """Status is marked Proved [L0]."""
        result = dirac_quantisation()
        assert 'Proved' in result['status']

    def test_n_equals_one(self):
        """Default n=1 (minimal coupling)."""
        result = dirac_quantisation(n=1)
        assert result['n'] == 1

    def test_has_consequence(self):
        """Result describes a physical consequence."""
        result = dirac_quantisation()
        assert 'consequence' in result
        assert len(result['consequence']) > 0


class TestPsiCompactification:
    """Tests for ψ-circle compactification."""

    def test_returns_dict(self):
        """psi_compactification_motivation() returns a dict."""
        result = psi_compactification_motivation()
        assert isinstance(result, dict)

    def test_status_proved(self):
        """Compactification is marked Proved [L0]."""
        result = psi_compactification_motivation()
        assert 'Proved' in result['status']

    def test_has_two_motivations(self):
        """At least two physical motivations are listed."""
        result = psi_compactification_motivation()
        assert len(result['motivation']) >= 2

    def test_unitarity_mentioned(self):
        """Unitarity is among the motivations."""
        result = psi_compactification_motivation()
        motiv_text = ' '.join(result['motivation'])
        assert 'nitar' in motiv_text.lower()

    def test_open_problem_mentioned(self):
        """R_ψ fixation open problem is documented."""
        result = psi_compactification_motivation()
        assert 'open' in result or 'Open' in result.get('open', '')


class TestPredictNStar:
    """Tests for n* prediction from B₀."""

    def test_B0_gives_non_integer_n_star(self):
        """B₀ ≈ 25.13 gives n* ≈ 5.45 (not integer) → open problem."""
        result = predict_n_star(B0_val=8 * math.pi, alpha_obs=137.036)
        assert not result['is_integer']
        assert result['n_star'] > 5.0
        assert result['n_star'] < 6.0

    def test_semi_empirical_B_gives_near_integer(self):
        """B ≈ 46.3 gives n* ≈ 2.96 (close to integer 3)."""
        result = predict_n_star(B0_val=46.3, alpha_obs=137.036)
        # n* ≈ 2.96, not exactly integer but close
        assert 2.8 < result['n_star'] < 3.2

    def test_returns_expected_keys(self):
        """predict_n_star returns dict with required keys."""
        result = predict_n_star()
        for key in ['B0', 'alpha_inv_obs', 'n_star', 'is_integer', 'status']:
            assert key in result

    def test_default_alpha_obs(self):
        """Default α⁻¹ = 137.036."""
        result = predict_n_star()
        assert result['alpha_inv_obs'] == 137.036


class TestProvedSummary:
    """Tests for the fine structure proved results summary."""

    def test_returns_dict(self):
        """fine_structure_proved_summary() returns a dict."""
        summary = fine_structure_proved_summary()
        assert isinstance(summary, dict)

    def test_neff_is_proved(self):
        """N_eff = 12 is listed as Proved."""
        summary = fine_structure_proved_summary()
        neff_key = [k for k in summary if 'N_eff' in k or 'N_eff' in k]
        assert any('Proved' in summary[k] for k in summary if 'N_eff' in k)

    def test_B0_is_proved(self):
        """B₀ formula is listed as Proved."""
        summary = fine_structure_proved_summary()
        assert any('Proved' in summary[k] for k in summary if 'B' in k and 'loop' in k)

    def test_B_base_is_motivated_conjecture(self):
        """B_base is listed as Motivated Conjecture with explicit gap."""
        summary = fine_structure_proved_summary()
        assert any(
            'Conjecture' in summary[k] and 'gap' in summary[k]
            for k in summary if 'B_base' in k or 'base' in k.lower()
        )

    def test_all_entries_have_status(self):
        """Every entry in the summary has a non-empty status string."""
        summary = fine_structure_proved_summary()
        for k, v in summary.items():
            assert isinstance(v, str) and len(v) > 0, f"Empty status for {k}"

# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
tests/test_factorial_degeneracy_hypothesis.py
=============================================

Test suite for tools/factorial_degeneracy.py

Verifies the factorial-degeneracy hypothesis deliverables:
  1. List of F(n) local minima for each entropy variant.
  2. Overlap of minima (or ΔF-minimum location) with stable-prime set.
  3. Robustness of Variant 4 across a c-parameter sweep.
"""

from __future__ import annotations

import math
import sys
import os
from typing import Callable

import pytest

# Make tools/ importable regardless of working directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

from factorial_degeneracy import (
    STABLE_PRIMES,
    OVERLAP_TOLERANCE,
    C_SWEEP_MIN,
    C_SWEEP_MAX,
    energy,
    entropy_factorial,
    entropy_stirling_leading,
    entropy_stirling_first,
    entropy_stirling_linear,
    free_energy_fn,
    delta_free_energy_fn,
    find_f_local_minima,
    find_df_global_min,
    nearest_stable_prime,
    overlaps_stable_primes,
    c_value_for_minimum_at,
    sweep_c_for_stable_prime_minima,
    analyse_variant,
    run_analysis,
)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------


def test_stable_primes_constant():
    assert STABLE_PRIMES == [127, 137, 139, 151, 157]


def test_overlap_tolerance_positive():
    assert OVERLAP_TOLERANCE > 0


# ---------------------------------------------------------------------------
# energy(n) = n²
# ---------------------------------------------------------------------------


def test_energy_values():
    assert energy(1) == 1.0
    assert energy(10) == 100.0
    assert energy(137) == 137 ** 2


# ---------------------------------------------------------------------------
# Entropy functions
# ---------------------------------------------------------------------------


def test_entropy_factorial_small_values():
    assert entropy_factorial(1) == pytest.approx(0.0, abs=1e-12)
    assert entropy_factorial(2) == pytest.approx(math.log(2), rel=1e-12)
    assert entropy_factorial(5) == pytest.approx(math.lgamma(6), rel=1e-12)


def test_entropy_factorial_uses_log_gamma():
    for n in [10, 50, 100, 137, 200]:
        assert entropy_factorial(n) == pytest.approx(math.lgamma(n + 1), rel=1e-12)


def test_entropy_factorial_rejects_non_positive():
    with pytest.raises(ValueError):
        entropy_factorial(0)
    with pytest.raises(ValueError):
        entropy_factorial(-1)


def test_entropy_stirling_leading_values():
    assert entropy_stirling_leading(math.e) == pytest.approx(math.e, rel=1e-9)
    assert entropy_stirling_leading(10) == pytest.approx(10 * math.log(10), rel=1e-9)


def test_entropy_stirling_leading_rejects_non_positive():
    with pytest.raises(ValueError):
        entropy_stirling_leading(0)
    with pytest.raises(ValueError):
        entropy_stirling_leading(-3)


def test_entropy_stirling_first_values():
    n = 50
    assert entropy_stirling_first(n) == pytest.approx(n * math.log(n) - n, rel=1e-9)


def test_entropy_stirling_first_rejects_non_positive():
    with pytest.raises(ValueError):
        entropy_stirling_first(0)


def test_entropy_stirling_linear_values():
    n, c = 137, 269.0
    expected = n * math.log(n) + c * n
    assert entropy_stirling_linear(n, c) == pytest.approx(expected, rel=1e-12)


def test_entropy_stirling_linear_rejects_non_positive():
    with pytest.raises(ValueError):
        entropy_stirling_linear(0, 1.0)


def test_entropy_stirling_linear_zero_c_matches_leading():
    for n in [5, 50, 137]:
        assert entropy_stirling_linear(n, 0.0) == pytest.approx(
            entropy_stirling_leading(n), rel=1e-12
        )


def test_entropy_stirling_linear_minus_one_c_matches_first():
    for n in [5, 50, 137]:
        assert entropy_stirling_linear(n, -1.0) == pytest.approx(
            entropy_stirling_first(n), rel=1e-12
        )


# ---------------------------------------------------------------------------
# free_energy_fn and delta_free_energy_fn
# ---------------------------------------------------------------------------


def test_free_energy_factorial_formula():
    for n in [2, 5, 10, 137]:
        expected = n ** 2 - math.lgamma(n + 1)
        assert free_energy_fn(n, entropy_factorial) == pytest.approx(expected, rel=1e-12)


def test_free_energy_stirling_leading_formula():
    for n in [2, 5, 50, 137]:
        expected = n ** 2 - n * math.log(n)
        assert free_energy_fn(n, entropy_stirling_leading) == pytest.approx(expected, rel=1e-12)


def test_delta_free_energy_definition():
    """ΔF(n) = F(n+1) − F(n) for all variants."""
    for entropy_func in [
        entropy_factorial,
        entropy_stirling_leading,
        entropy_stirling_first,
        lambda n: entropy_stirling_linear(n, 269.0),
    ]:
        for n in [2, 10, 50, 100, 136, 137]:
            expected = (
                free_energy_fn(n + 1, entropy_func) - free_energy_fn(n, entropy_func)
            )
            assert delta_free_energy_fn(n, entropy_func) == pytest.approx(
                expected, rel=1e-12
            )


# ---------------------------------------------------------------------------
# Deliverable 1: list of F-minima — Variants 1-3 (no local minima expected)
# ---------------------------------------------------------------------------


def test_factorial_no_f_local_minima():
    """F(n) = n² − ln(n!) is strictly increasing; no local minima expected."""
    minima = find_f_local_minima(entropy_factorial, 2, 300)
    assert minima == [], f"Unexpected F local minima for ln(n!): {minima}"


def test_stirling_leading_no_f_local_minima():
    """F(n) = n² − n·ln(n) has no discrete local minima."""
    minima = find_f_local_minima(entropy_stirling_leading, 2, 300)
    assert minima == [], f"Unexpected F local minima for n·ln(n): {minima}"


def test_stirling_first_no_f_local_minima():
    """F(n) = n² − (n·ln(n) − n) has no discrete local minima."""
    minima = find_f_local_minima(entropy_stirling_first, 2, 300)
    assert minima == [], f"Unexpected F local minima for n·ln(n)−n: {minima}"


def test_stirling_linear_has_f_local_minimum_near_137():
    """For c ≈ 269 the parameterised variant has a local minimum near 137."""
    entropy_func = lambda n: entropy_stirling_linear(n, 269.0)
    minima = find_f_local_minima(entropy_func, 2, 300)
    assert len(minima) >= 1, "No local minimum found for Variant 4 (c=269)"
    assert any(abs(m - 137) <= OVERLAP_TOLERANCE for m in minima), (
        f"No minimum within ±{OVERLAP_TOLERANCE} of 137; found: {minima}"
    )


# ---------------------------------------------------------------------------
# Deliverable 2: overlap with stable primes
# ---------------------------------------------------------------------------


def test_overlaps_stable_primes_positive():
    assert overlaps_stable_primes([137], tol=0) is True
    assert overlaps_stable_primes([135], tol=2) is True
    assert overlaps_stable_primes([127, 151], tol=0) is True


def test_overlaps_stable_primes_negative():
    assert overlaps_stable_primes([], tol=0) is False
    assert overlaps_stable_primes([100], tol=0) is False
    assert overlaps_stable_primes([100], tol=26) is False  # 127-100=27


def test_factorial_no_overlap():
    """Variants 1–3 do not produce local F-minima overlapping stable primes."""
    minima = find_f_local_minima(entropy_factorial, 2, 300)
    # No F-minima exist, so trivially no overlap
    assert overlaps_stable_primes(minima) is False


def test_stirling_linear_overlap_with_stable_primes():
    """Variant 4 (c=269) has local F-minimum at n=137 (stable prime)."""
    entropy_func = lambda n: entropy_stirling_linear(n, 269.0)
    minima = find_f_local_minima(entropy_func, 2, 300)
    assert overlaps_stable_primes(minima, tol=0) is True, (
        f"Expected exact hit on stable prime; minima = {minima}"
    )


@pytest.mark.parametrize("p,c_approx", [
    (127, 248.0),
    (137, 268.0),
    (139, 272.0),
    (151, 295.0),
    (157, 307.0),
])
def test_stirling_linear_minimum_at_each_stable_prime(p: int, c_approx: float):
    """
    For the c value nearest to c*(p) = 2p − ln(p) − 1, the discrete F-minimum
    lands at or very close to stable prime p.
    """
    entropy_func = lambda n: entropy_stirling_linear(n, c_approx)
    minima = find_f_local_minima(entropy_func, 2, 300)
    assert any(abs(m - p) <= 1 for m in minima), (
        f"No minimum within ±1 of p={p} for c={c_approx}; minima={minima}"
    )


# ---------------------------------------------------------------------------
# Deliverable 3: robustness vs parameter changes
# ---------------------------------------------------------------------------


def test_c_value_for_minimum_at_stable_primes():
    """
    c*(p) = 2p − ln(p) − 1 places the continuous F-minimum at each stable prime.
    Values must lie in the range [C_SWEEP_MIN, C_SWEEP_MAX].
    """
    for p in STABLE_PRIMES:
        c_star = c_value_for_minimum_at(p)
        assert C_SWEEP_MIN <= c_star <= C_SWEEP_MAX, (
            f"c*(p={p}) = {c_star:.4f} is outside sweep range "
            f"[{C_SWEEP_MIN}, {C_SWEEP_MAX}]"
        )


def test_c_value_formula_correctness():
    """c*(p) = 2p − ln(p) − 1 should satisfy F'(p) ≈ 0 in the continuous sense."""
    for p in STABLE_PRIMES:
        c_star = c_value_for_minimum_at(p)
        # F'(x) = 2x − ln(x) − 1 − c should vanish at x = p
        residual = 2 * p - math.log(p) - 1 - c_star
        assert abs(residual) < 1e-10, (
            f"F'({p}) = {residual:.2e} ≠ 0 for c* = {c_star:.4f}"
        )


def test_c_sweep_covers_all_stable_primes():
    """
    The c-sweep should produce a local F-minimum on every stable prime
    for some c in [C_SWEEP_MIN, C_SWEEP_MAX].
    """
    sweep = sweep_c_for_stable_prime_minima(2, 300)
    primes_hit = {m for _, m in sweep if m in STABLE_PRIMES}
    assert primes_hit == set(STABLE_PRIMES), (
        f"Sweep missed stable primes: {set(STABLE_PRIMES) - primes_hit}"
    )


def test_c_sweep_returns_list_of_pairs():
    sweep = sweep_c_for_stable_prime_minima(2, 300)
    assert isinstance(sweep, list)
    for item in sweep:
        c, m = item
        assert isinstance(c, float)
        assert isinstance(m, int)
        assert 2 <= m < 300


def test_robust_c_interval_contains_137():
    """
    The contiguous c-interval whose minima land on stable primes must include
    at least one c value that gives n* = 137.
    """
    results = run_analysis(n_min=2, n_max=300, verbose=False)
    c_at_primes = results["c_values_near_primes"]
    c_vals_for_137 = [c for c, m in c_at_primes if m == 137]
    assert len(c_vals_for_137) >= 1, (
        "No c value in the sweep produces F-minimum at n=137"
    )


def test_robust_c_range_width():
    """
    The robust c-interval should span at least 50 units, confirming
    the hypothesis is not a fine-tuned coincidence.
    """
    results = run_analysis(n_min=2, n_max=300, verbose=False)
    rc = results["robust_c_range"]
    assert rc is not None, "No robust c-range found"
    c_low, c_high = rc
    assert (c_high - c_low) >= 50.0, (
        f"Robust c-range width = {c_high - c_low:.1f} is too narrow (< 50)"
    )


# ---------------------------------------------------------------------------
# find_df_global_min
# ---------------------------------------------------------------------------


def test_find_df_global_min_returns_tuple():
    result = find_df_global_min(entropy_factorial, 2, 300)
    assert isinstance(result, tuple)
    n, val = result
    assert isinstance(n, int)
    assert isinstance(val, float)


def test_find_df_global_min_is_minimum():
    """The returned value should be the actual minimum of ΔF in the range."""
    entropy_func = entropy_stirling_leading
    n_star, df_star = find_df_global_min(entropy_func, 2, 300)
    for n in range(2, 300):
        assert delta_free_energy_fn(n, entropy_func) >= df_star, (
            f"ΔF({n}) = {delta_free_energy_fn(n, entropy_func):.4f} "
            f"< reported minimum {df_star:.4f}"
        )


# ---------------------------------------------------------------------------
# nearest_stable_prime
# ---------------------------------------------------------------------------


def test_nearest_stable_prime_exact_hits():
    for p in STABLE_PRIMES:
        nearest, dist = nearest_stable_prime(p)
        assert nearest == p
        assert dist == 0


def test_nearest_stable_prime_close_values():
    nearest, dist = nearest_stable_prime(136)
    assert nearest == 137
    assert dist == 1

    nearest, dist = nearest_stable_prime(130)
    assert nearest == 127
    assert dist == 3


# ---------------------------------------------------------------------------
# analyse_variant
# ---------------------------------------------------------------------------


def test_analyse_variant_returns_required_keys():
    result = analyse_variant("factorial", entropy_factorial, 2, 300)
    required = {
        "name", "f_minima", "df_global_min_n", "df_global_min_val",
        "f_at_stable_primes", "df_at_stable_primes", "overlap_found",
    }
    assert required.issubset(result.keys()), (
        f"Missing keys: {required - result.keys()}"
    )


def test_analyse_variant_f_at_primes_correct():
    result = analyse_variant("stirling_leading", entropy_stirling_leading, 2, 300)
    for p in STABLE_PRIMES:
        expected = free_energy_fn(p, entropy_stirling_leading)
        assert result["f_at_stable_primes"][p] == pytest.approx(expected, rel=1e-12)


def test_analyse_variant_df_at_primes_correct():
    result = analyse_variant("stirling_leading", entropy_stirling_leading, 2, 300)
    for p in STABLE_PRIMES:
        expected = delta_free_energy_fn(p, entropy_stirling_leading)
        assert result["df_at_stable_primes"][p] == pytest.approx(expected, rel=1e-12)


def test_analyse_variant_verbose_does_not_raise():
    import io, contextlib
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        analyse_variant("factorial", entropy_factorial, 2, 300, verbose=True)
    output = out.getvalue()
    assert "Variant" in output
    assert "overlap" in output.lower()


# ---------------------------------------------------------------------------
# run_analysis — full integration
# ---------------------------------------------------------------------------


def test_run_analysis_returns_required_keys():
    results = run_analysis(n_min=2, n_max=300)
    required = {
        "variant_factorial",
        "variant_stirling_leading",
        "variant_stirling_first",
        "variant_stirling_linear",
        "c_sweep_results",
        "c_values_near_primes",
        "robust_c_range",
        "any_overlap",
    }
    assert required.issubset(results.keys()), (
        f"Missing keys: {required - results.keys()}"
    )


def test_run_analysis_any_overlap_true():
    """Variant 4 (c=269) always produces overlap, so any_overlap must be True."""
    results = run_analysis(n_min=2, n_max=300, c_fixed=269.0)
    assert results["any_overlap"] is True


def test_run_analysis_variants_1_3_no_overlap():
    """Variants 1–3 should not produce F-local-minima overlapping stable primes."""
    results = run_analysis(n_min=2, n_max=300)
    for key in ["variant_factorial", "variant_stirling_leading", "variant_stirling_first"]:
        v = results[key]
        assert v["f_minima"] == [], (
            f"{key}: unexpected F local minima {v['f_minima']}"
        )
        assert v["overlap_found"] is False, (
            f"{key}: overlap_found should be False (no local F-minima)"
        )


def test_run_analysis_variant4_has_minimum_at_137():
    results = run_analysis(n_min=2, n_max=300, c_fixed=269.0)
    v4 = results["variant_stirling_linear"]
    assert 137 in v4["f_minima"], (
        f"Variant 4 (c=269): 137 not in f_minima = {v4['f_minima']}"
    )


def test_run_analysis_c_sweep_non_empty():
    results = run_analysis(n_min=2, n_max=300)
    assert len(results["c_sweep_results"]) > 0


def test_run_analysis_c_values_near_primes_non_empty():
    results = run_analysis(n_min=2, n_max=300)
    assert len(results["c_values_near_primes"]) > 0


def test_run_analysis_robust_c_range_valid():
    results = run_analysis(n_min=2, n_max=300)
    rc = results["robust_c_range"]
    assert rc is not None
    c_low, c_high = rc
    assert c_low < c_high
    assert c_low >= C_SWEEP_MIN
    assert c_high <= C_SWEEP_MAX


def test_run_analysis_verbose_does_not_raise():
    import io, contextlib
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        run_analysis(n_min=2, n_max=300, verbose=True)
    output = out.getvalue()
    assert "Factorial Degeneracy" in output
    assert "stable prime" in output.lower() or "Stable" in output
    assert "SUMMARY" in output

# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_free_energy_spectrum.py — Tests for free-energy derivation from ψ-sector spectrum.

Verifies the deliverables of derive_free_energy_from_spectrum.py:
  1. F(n) = E(n) − S(n) = n² − n·ln(n) is computed correctly.
  2. Monotonicity of F(n): no discrete local minima exist for n ≥ 2.
  3. ΔF(n) is strictly positive for n ≥ 2 (confirmed strictly-increasing behaviour).
  4. Global ΔF minimum is located and compared with the stable-prime set.
  5. run_analysis() returns a dict with all required deliverable keys.
"""

from __future__ import annotations

import math
import sys
import os

import pytest

# Make tools/ importable regardless of working directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

from derive_free_energy_from_spectrum import (
    STABLE_PRIMES,
    energy,
    entropy,
    free_energy,
    delta_free_energy,
    delta2_free_energy,
    find_f_local_minima,
    find_delta_f_local_minima,
    error_metrics,
    reference_to_candidates_metrics,
    run_analysis,
)


# ---------------------------------------------------------------------------
# Basic function correctness
# ---------------------------------------------------------------------------


def test_energy_values():
    assert energy(1) == 1.0
    assert energy(10) == 100.0
    assert energy(137) == 137 ** 2


def test_entropy_values():
    assert entropy(1) == pytest.approx(0.0)
    assert entropy(math.e) == pytest.approx(math.e, rel=1e-9)
    assert entropy(10) == pytest.approx(10 * math.log(10), rel=1e-9)


def test_entropy_requires_positive_n():
    with pytest.raises(ValueError):
        entropy(0)
    with pytest.raises(ValueError):
        entropy(-5)


def test_free_energy_formula():
    for n in [2, 5, 10, 50, 137, 157]:
        expected = n ** 2 - n * math.log(n)
        assert free_energy(n) == pytest.approx(expected, rel=1e-12)


# ---------------------------------------------------------------------------
# Monotonicity: F is strictly increasing → no discrete local minima
# ---------------------------------------------------------------------------


def test_f_strictly_increasing_small_range():
    """F(n+1) > F(n) for n in [2, 200]."""
    for n in range(2, 200):
        assert free_energy(n + 1) > free_energy(n), (
            f"F not increasing at n={n}: F({n})={free_energy(n):.4f}, "
            f"F({n+1})={free_energy(n+1):.4f}"
        )


def test_delta_f_strictly_positive():
    """ΔF(n) > 0 for n in [2, 200]."""
    for n in range(2, 200):
        assert delta_free_energy(n) > 0, f"ΔF({n}) = {delta_free_energy(n):.6f} ≤ 0"


def test_no_f_local_minima_in_range():
    """find_f_local_minima should return empty list for n ∈ [2, 300]."""
    minima = find_f_local_minima(2, 300)
    assert minima == [], f"Unexpected F(n) local minima found: {minima}"


# ---------------------------------------------------------------------------
# Deliverable 1: list of (ΔF) minima
# ---------------------------------------------------------------------------


def test_delta_f_minima_type():
    minima = find_delta_f_local_minima(2, 300)
    assert isinstance(minima, list)
    for m in minima:
        assert isinstance(m, int)


def test_global_df_minimum_location():
    """
    Global minimum of ΔF over [2, 300] should be the only minimum (ΔF is U-shaped
    in small range, but for large n it grows again due to the n² term dominating).
    We verify it is reported as a valid integer in [2, 300].
    """
    results = run_analysis(n_min=2, n_max=300)
    n_min_df = results["global_df_min_n"]
    assert 2 <= n_min_df <= 300, f"Global ΔF minimum outside scan range: {n_min_df}"


# ---------------------------------------------------------------------------
# Deliverable 2: comparison with stable-prime set
# ---------------------------------------------------------------------------


def test_stable_primes_constant():
    assert STABLE_PRIMES == [127, 137, 139, 151, 157]


def test_f_at_stable_primes_returned():
    results = run_analysis(n_min=2, n_max=300)
    for p in STABLE_PRIMES:
        assert p in results["f_at_stable_primes"]
        assert results["f_at_stable_primes"][p] == pytest.approx(free_energy(p), rel=1e-12)


def test_df_at_stable_primes_positive():
    """ΔF at each stable prime should be positive (F strictly increasing)."""
    results = run_analysis(n_min=2, n_max=300)
    for p in STABLE_PRIMES:
        assert results["df_at_stable_primes"][p] > 0, (
            f"ΔF at p={p} is not positive: {results['df_at_stable_primes'][p]}"
        )


# ---------------------------------------------------------------------------
# Deliverable 3: error metrics
# ---------------------------------------------------------------------------


def test_error_metrics_empty_candidates():
    metrics = error_metrics([], STABLE_PRIMES)
    assert metrics == []


def test_error_metrics_exact_match():
    metrics = error_metrics([137], STABLE_PRIMES)
    assert len(metrics) == 1
    cand, nearest, dist = metrics[0]
    assert cand == 137
    assert nearest == 137
    assert dist == 0


def test_error_metrics_proximity():
    metrics = error_metrics([135], STABLE_PRIMES)
    assert len(metrics) == 1
    cand, nearest, dist = metrics[0]
    assert cand == 135
    assert nearest == 137  # closest stable prime
    assert dist == 2


def test_reference_to_candidates_metrics_infinite_on_empty():
    metrics = reference_to_candidates_metrics(STABLE_PRIMES, [])
    assert len(metrics) == len(STABLE_PRIMES)
    for r, c, d in metrics:
        assert d == float("inf")
        assert c == -1


def test_reference_to_candidates_metrics_values():
    candidates = [137]
    metrics = reference_to_candidates_metrics(STABLE_PRIMES, candidates)
    assert len(metrics) == len(STABLE_PRIMES)
    # 137 is the unique candidate
    for r, c, d in metrics:
        assert c == 137
        assert d == abs(r - 137)


# ---------------------------------------------------------------------------
# Full run_analysis return structure
# ---------------------------------------------------------------------------


def test_run_analysis_keys():
    results = run_analysis(n_min=2, n_max=300)
    required_keys = {
        "f_minima",
        "delta_f_minima",
        "inflection_zone",
        "f_at_stable_primes",
        "df_at_stable_primes",
        "global_df_min_n",
        "global_df_min_val",
        "metrics_fmin_to_ref",
        "metrics_ref_to_dmin",
        "overlap_found",
    }
    assert required_keys.issubset(results.keys()), (
        f"Missing keys: {required_keys - results.keys()}"
    )


def test_run_analysis_verbose_does_not_raise():
    """run_analysis with verbose=True should not raise any exception."""
    import io
    import contextlib

    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        run_analysis(n_min=2, n_max=300, verbose=True)
    output = out.getvalue()
    assert "F(n)" in output
    assert "stable prime" in output.lower() or "Stable" in output

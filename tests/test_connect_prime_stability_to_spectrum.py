# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
tests/test_connect_prime_stability_to_spectrum.py
=================================================

Unit tests for research_tracks/rh_trace_formula/connect_prime_stability_to_spectrum.py

Tests cover:
  - sieve_primes correctness
  - H_ψ matrix properties (real symmetric, bounded eigenvalues, ordering)
  - spectral_density normalisation and positivity
  - E(p) = p² mapping
  - Analysis result types and consistency
  - No crash on full analyse() call
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest

# ---------------------------------------------------------------------------
# Import the module under test
# ---------------------------------------------------------------------------

_module_path = Path(__file__).parent.parent / "research_tracks" / "rh_trace_formula"
sys.path.insert(0, str(_module_path))

from connect_prime_stability_to_spectrum import (
    analyse,
    build_H_psi,
    find_local_maxima,
    find_spectral_gaps,
    format_table,
    nearest_eigenvalue,
    PrimeSpectralRecord,
    run,
    sieve_primes,
    spectral_density,
    twin_prime_pairs,
)


# ---------------------------------------------------------------------------
# Sieve of Eratosthenes
# ---------------------------------------------------------------------------

class TestSievePrimes:
    def test_known_values(self):
        assert sieve_primes(10) == [2, 3, 5, 7]

    def test_empty_below_2(self):
        assert sieve_primes(1) == []
        assert sieve_primes(0) == []

    def test_includes_boundary(self):
        primes = sieve_primes(13)
        assert 13 in primes

    def test_excludes_composites(self):
        primes = set(sieve_primes(30))
        for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]:
            assert n not in primes, f"{n} should not be prime"

    def test_count(self):
        # π(30) = 10
        assert len(sieve_primes(30)) == 10

    def test_all_prime(self):
        for p in sieve_primes(50):
            for d in range(2, p):
                assert p % d != 0, f"{p} is not prime"


class TestTwinPrimePairs:
    def test_basic(self):
        primes = sieve_primes(20)
        twins = twin_prime_pairs(primes)
        assert (3, 5) in twins
        assert (5, 7) in twins
        assert (11, 13) in twins
        assert (17, 19) in twins

    def test_no_spurious(self):
        primes = sieve_primes(20)
        twins = twin_prime_pairs(primes)
        for p1, p2 in twins:
            assert p2 - p1 == 2
            assert p1 in primes
            assert p2 in primes

    def test_empty_small_range(self):
        assert twin_prime_pairs([2]) == []


# ---------------------------------------------------------------------------
# H_ψ construction
# ---------------------------------------------------------------------------

class TestBuildHPsi:
    """Tests for the finite-difference Hamiltonian."""

    N_SMALL = 50  # small grid for fast tests

    def test_eigenvalues_sorted(self):
        _, ev = build_H_psi(N=self.N_SMALL, kappa=0.5)
        assert np.all(np.diff(ev) >= -1e-10), "eigenvalues should be non-decreasing"

    def test_eigenvalues_real(self):
        _, ev = build_H_psi(N=self.N_SMALL, kappa=0.5)
        assert np.all(np.isfinite(ev))
        assert np.isrealobj(ev)

    def test_flat_potential_ground_state_zero(self):
        """Flat Laplacian on a circle has ground state eigenvalue = 0."""
        _, ev = build_H_psi(N=self.N_SMALL, kappa=0.0, potential="flat")
        assert abs(ev[0]) < 1e-8, f"Ground state should be ~0, got {ev[0]}"

    def test_flat_potential_spectrum_n_squared(self):
        """
        For flat Laplacian on [0, 2π) the eigenvalues are n² for n=0,1,2,...
        Each nonzero n has degeneracy 2 (±n).  With N=200 we should recover
        the first few eigenvalues accurately.
        """
        N = 200
        _, ev = build_H_psi(N=N, kappa=0.0, potential="flat")
        # First few unique eigenvalues: 0, 1, 4, 9, 16, 25, ...
        expected = [0.0, 1.0, 1.0, 4.0, 4.0, 9.0, 9.0]
        for i, exp in enumerate(expected):
            assert abs(ev[i] - exp) < 0.05, (
                f"Eigenvalue[{i}] = {ev[i]:.4f}, expected ≈ {exp}"
            )

    def test_positive_potential_raises_eigenvalues(self):
        """Adding a non-negative V_eff should raise all eigenvalues."""
        _, ev_flat = build_H_psi(N=self.N_SMALL, kappa=0.0, potential="flat")
        _, ev_cos = build_H_psi(N=self.N_SMALL, kappa=2.0, potential="cos")
        # Ground state should be at least as large with positive V
        assert ev_cos[0] >= ev_flat[0] - 1e-10

    def test_cos2_potential(self):
        _, ev = build_H_psi(N=self.N_SMALL, kappa=1.0, potential="cos2")
        assert np.all(np.isfinite(ev))

    def test_unknown_potential_raises(self):
        with pytest.raises(ValueError, match="Unknown potential"):
            build_H_psi(N=self.N_SMALL, kappa=1.0, potential="unknown_xyz")

    def test_psi_grid_shape(self):
        psi, ev = build_H_psi(N=self.N_SMALL)
        assert psi.shape == (self.N_SMALL,)
        assert ev.shape == (self.N_SMALL,)


# ---------------------------------------------------------------------------
# Spectral density
# ---------------------------------------------------------------------------

class TestSpectralDensity:
    def _get_rho(self, ev, n_grid=500):
        E_grid = np.linspace(float(ev[0]) - 1.0, float(ev[-1]) + 1.0, n_grid)
        rho = spectral_density(ev, E_grid)
        return E_grid, rho

    def test_non_negative(self):
        _, ev = build_H_psi(N=50, kappa=0.5)
        E_grid, rho = self._get_rho(ev)
        assert np.all(rho >= -1e-15), "ρ(E) must be non-negative"

    def test_normalised(self):
        """
        KDE with a small controlled spectrum should integrate close to 1 when
        the integration range covers several bandwidths on each side.
        """
        ev = np.array([1.0, 4.0, 9.0, 16.0, 25.0])
        bw = 0.3
        # Grid extends ±5σ around the outermost eigenvalues
        E_grid = np.linspace(ev[0] - 5 * bw, ev[-1] + 5 * bw, 10000)
        rho = spectral_density(ev, E_grid, bandwidth=bw)
        integral = float(np.trapezoid(rho, E_grid))
        assert abs(integral - 1.0) < 0.02, f"KDE integral = {integral:.4f}, expected ≈ 1"

    def test_peaks_near_eigenvalues(self):
        """ρ(E) should be elevated near the eigenvalues."""
        ev = np.array([1.0, 4.0, 9.0])  # simple test spectrum
        E_grid = np.linspace(0.0, 12.0, 2000)
        rho = spectral_density(ev, E_grid, bandwidth=0.1)
        for lam in ev:
            idx = int(np.argmin(np.abs(E_grid - lam)))
            assert rho[idx] > rho[0], f"ρ should peak near eigenvalue {lam}"

    def test_custom_bandwidth(self):
        ev = np.array([1.0, 4.0, 9.0])
        E_grid = np.linspace(0.0, 12.0, 500)
        rho = spectral_density(ev, E_grid, bandwidth=0.5)
        assert np.all(rho >= 0)


# ---------------------------------------------------------------------------
# Spectral feature extraction
# ---------------------------------------------------------------------------

class TestFindLocalMaxima:
    def test_single_peak(self):
        # Use 201 points so E[100] = 5.0 exactly → strict maximum guaranteed
        E = np.linspace(0, 10, 201)
        rho = np.exp(-0.5 * (E - 5) ** 2)
        maxima = find_local_maxima(rho, E)
        assert len(maxima) >= 1
        assert abs(maxima[0] - 5.0) < 0.2

    def test_two_peaks(self):
        E = np.linspace(0, 20, 500)
        rho = np.exp(-0.5 * (E - 5) ** 2) + np.exp(-0.5 * (E - 15) ** 2)
        maxima = find_local_maxima(rho, E)
        # Should find at least two peaks around 5 and 15
        near5 = any(abs(m - 5.0) < 0.5 for m in maxima)
        near15 = any(abs(m - 15.0) < 0.5 for m in maxima)
        assert near5 and near15


class TestFindSpectralGaps:
    def test_obvious_gap(self):
        ev = np.array([0.0, 1.0, 1.1, 1.2, 10.0, 10.1])
        gaps = find_spectral_gaps(ev, min_gap=2.0)
        # gap between 1.2 and 10.0
        assert len(gaps) == 1
        lo, hi = gaps[0]
        assert abs(lo - 1.2) < 0.01
        assert abs(hi - 10.0) < 0.01

    def test_no_gap(self):
        ev = np.linspace(0.0, 10.0, 50)
        gaps = find_spectral_gaps(ev, min_gap=1.0)
        assert gaps == []

    def test_multiple_gaps(self):
        ev = np.array([0.0, 0.1, 5.0, 5.1, 20.0, 20.1])
        gaps = find_spectral_gaps(ev, min_gap=2.0)
        assert len(gaps) == 2


class TestNearestEigenvalue:
    def test_exact_match(self):
        ev = np.array([1.0, 4.0, 9.0])
        nearest, dist = nearest_eigenvalue(4.0, ev)
        assert nearest == 4.0
        assert dist == 0.0

    def test_close(self):
        ev = np.array([1.0, 4.0, 9.0])
        nearest, dist = nearest_eigenvalue(4.3, ev)
        assert nearest == 4.0
        assert abs(dist - 0.3) < 1e-10

    def test_single_eigenvalue(self):
        ev = np.array([5.0])
        nearest, dist = nearest_eigenvalue(7.0, ev)
        assert nearest == 5.0
        assert dist == 2.0


# ---------------------------------------------------------------------------
# Energy mapping
# ---------------------------------------------------------------------------

class TestEnergyMapping:
    """E(p) = p² for the unit circle (L_ψ = 2π)."""

    def test_small_primes(self):
        expected = {2: 4, 3: 9, 5: 25, 7: 49, 11: 121, 13: 169}
        for p, e in expected.items():
            assert float(p) ** 2 == float(e)

    def test_ordering(self):
        primes = sieve_primes(30)
        E_vals = [p ** 2 for p in primes]
        assert E_vals == sorted(E_vals), "E(p) should be increasing"


# ---------------------------------------------------------------------------
# Full analysis
# ---------------------------------------------------------------------------

class TestAnalyse:
    """Integration tests for the analyse() function."""

    def test_returns_correct_types(self):
        records, conclusion = analyse(N=80, kappa=0.5, p_max=10)
        assert isinstance(records, list)
        assert isinstance(conclusion, str)
        assert len(records) == len(sieve_primes(10))

    def test_record_fields_consistent(self):
        records, _ = analyse(N=80, kappa=0.5, p_max=10)
        for r in records:
            assert isinstance(r, PrimeSpectralRecord)
            assert r.E_p == float(r.p) ** 2
            assert r.dist_to_ev >= 0.0
            assert r.rho_E_p >= 0.0
            if r.in_gap:
                assert r.gap_lo is not None and r.gap_hi is not None
                assert r.gap_lo < r.E_p < r.gap_hi

    def test_conclusion_non_empty(self):
        _, conclusion = analyse(N=80, kappa=0.5, p_max=10)
        assert len(conclusion) > 50

    def test_flat_potential(self):
        """Flat potential should run without error."""
        records, _ = analyse(N=80, kappa=0.0, potential="flat", p_max=10)
        assert len(records) > 0

    def test_cos2_potential(self):
        records, _ = analyse(N=80, kappa=1.0, potential="cos2", p_max=10)
        assert len(records) > 0

    def test_twin_prime_degeneracy_bool(self):
        records, _ = analyse(N=100, kappa=1.0, p_max=20)
        twin_records = [
            r for r in records
            if r.is_twin and r.twin_partner is not None
            and r.twin_near_degenerate is not None
        ]
        for r in twin_records:
            assert isinstance(r.twin_near_degenerate, bool)

    def test_format_table_non_empty(self):
        records, _ = analyse(N=80, kappa=0.5, p_max=10)
        table = format_table(records)
        assert isinstance(table, str)
        assert len(table.splitlines()) > 5


# ---------------------------------------------------------------------------
# run() wrapper
# ---------------------------------------------------------------------------

class TestRun:
    def test_run_returns_dict(self):
        result = run(N=80, kappa=0.5, p_max=10)
        assert isinstance(result, dict)
        for key in ("records", "conclusion", "eigenvalues",
                    "E_grid", "rho", "primes", "E_p_vals"):
            assert key in result, f"Missing key: {key}"

    def test_eigenvalues_sorted(self):
        result = run(N=80, kappa=0.5, p_max=10)
        ev = result["eigenvalues"]
        assert np.all(np.diff(ev) >= -1e-10)

    def test_rho_non_negative(self):
        result = run(N=80, kappa=0.5, p_max=10)
        assert np.all(result["rho"] >= -1e-15)

    def test_primes_match_sieve(self):
        result = run(N=80, kappa=0.5, p_max=20)
        assert result["primes"] == sieve_primes(20)

    def test_E_p_vals_correct(self):
        result = run(N=80, kappa=0.5, p_max=15)
        primes = result["primes"]
        E_vals = result["E_p_vals"]
        for p, e in zip(primes, E_vals):
            assert abs(e - float(p) ** 2) < 1e-10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

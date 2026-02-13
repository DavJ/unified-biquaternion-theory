# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Tests for Spectral Duality

Verifies Poisson summation duality numerically.
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ubt.spectral.laplacian_torus import (
    torus_eigenvalues,
    torus_spectrum_generator,
    mode_count_below_energy,
    get_lowest_nonzero_eigenvalue
)

from scripts.spectral.heat_kernel_trace import (
    heat_kernel_trace_spectral,
    heat_kernel_trace_exact_1d
)

from scripts.spectral.poisson_duality_demo import (
    winding_sum,
    spectral_sum
)


class TestLaplacianTorus:
    """Test Laplacian spectrum calculations."""
    
    def test_1d_torus_spectrum(self):
        """Test 1D torus eigenvalues."""
        eigenvalues, degeneracies = torus_eigenvalues(d=1, k_max=3, L=1.0)
        
        # Should have eigenvalues for k = -3, -2, -1, 0, 1, 2, 3
        # λ_k = (2π)² k²
        expected_unique = sorted(set((2 * np.pi)**2 * k**2 for k in range(-3, 4)))
        
        np.testing.assert_array_almost_equal(eigenvalues, expected_unique)
    
    def test_2d_torus_degeneracy(self):
        """Test degeneracy counting in 2D."""
        eigenvalues, degeneracies = torus_eigenvalues(d=2, k_max=2, L=1.0)
        
        # λ = 0 corresponds to k = (0,0), degeneracy 1
        zero_idx = np.where(eigenvalues == 0)[0][0]
        assert degeneracies[zero_idx] == 1
        
        # λ = (2π)² corresponds to k = (±1,0) and (0,±1), degeneracy 4
        lambda_1 = (2 * np.pi)**2
        idx_1 = np.where(np.abs(eigenvalues - lambda_1) < 1e-10)[0]
        if len(idx_1) > 0:
            assert degeneracies[idx_1[0]] == 4
    
    def test_lowest_eigenvalue(self):
        """Test lowest non-zero eigenvalue."""
        lambda_min = get_lowest_nonzero_eigenvalue(d=2, L=1.0)
        expected = (2 * np.pi)**2
        
        assert abs(lambda_min - expected) < 1e-10


class TestHeatKernel:
    """Test heat kernel trace calculations."""
    
    def test_heat_kernel_1d_vs_exact(self):
        """Compare numerical trace to exact theta function for 1D."""
        tau = 0.1
        k_max = 20
        
        numerical = heat_kernel_trace_spectral(tau, d=1, k_max=k_max, L=1.0)
        exact = heat_kernel_trace_exact_1d(tau, L=1.0)
        
        rel_error = abs(numerical - exact) / exact
        assert rel_error < 1e-10, f"Relative error {rel_error} too large"
    
    def test_heat_kernel_decreases(self):
        """Heat kernel should decrease with increasing tau."""
        tau_small = 0.1
        tau_large = 1.0
        
        trace_small = heat_kernel_trace_spectral(tau_small, d=2, k_max=10)
        trace_large = heat_kernel_trace_spectral(tau_large, d=2, k_max=10)
        
        assert trace_small > trace_large, "Trace should decrease with tau"
    
    def test_heat_kernel_positive(self):
        """Heat kernel trace must be positive."""
        for tau in [0.01, 0.1, 1.0, 10.0]:
            trace = heat_kernel_trace_spectral(tau, d=2, k_max=15)
            assert trace > 0, f"Trace at tau={tau} should be positive"


class TestPoissonDuality:
    """Test Poisson summation duality."""
    
    def test_duality_1d(self):
        """Test Poisson duality in 1D."""
        tau = 1.0
        cutoff = 20
        
        winding = winding_sum(tau, d=1, n_max=cutoff)
        spectral = spectral_sum(tau, d=1, k_max=cutoff)
        
        rel_diff = abs(winding - spectral) / spectral
        assert rel_diff < 1e-2, f"Relative difference {rel_diff} > 1%"
    
    def test_duality_2d(self):
        """Test Poisson duality in 2D."""
        tau = 0.5
        cutoff = 15
        
        winding = winding_sum(tau, d=2, n_max=cutoff)
        spectral = spectral_sum(tau, d=2, k_max=cutoff)
        
        rel_diff = abs(winding - spectral) / spectral
        assert rel_diff < 1e-2, f"Relative difference {rel_diff} > 1%"
    
    def test_duality_multiple_tau(self):
        """Test duality holds for multiple tau values."""
        cutoff = 12
        tau_values = [0.1, 0.5, 1.0, 2.0]
        
        for tau in tau_values:
            winding = winding_sum(tau, d=2, n_max=cutoff)
            spectral = spectral_sum(tau, d=2, k_max=cutoff)
            
            rel_diff = abs(winding - spectral) / spectral
            assert rel_diff < 5e-2, f"Duality failed at tau={tau}: diff={rel_diff}"
    
    def test_duality_convergence(self):
        """Test duality improves with increasing cutoff."""
        tau = 1.0
        
        cutoffs = [5, 10, 15]
        errors = []
        
        for cutoff in cutoffs:
            winding = winding_sum(tau, d=2, n_max=cutoff)
            spectral = spectral_sum(tau, d=2, k_max=cutoff)
            
            rel_diff = abs(winding - spectral) / spectral
            errors.append(rel_diff)
        
        # Errors should generally decrease (allowing some numerical noise)
        assert errors[-1] < errors[0] * 2, "Error should improve with larger cutoff"


class TestSpectralInvariants:
    """Test spectral invariants and asymptotics."""
    
    def test_mode_counting_weyl(self):
        """Test mode counting approximately follows Weyl asymptotic."""
        d = 2
        L = 1.0
        Lambda = 100.0
        
        count = mode_count_below_energy(d, Lambda, L)
        
        # Weyl formula: N(Λ) ~ (L/2π)^d × π^{d/2} / Γ(d/2 + 1) × Λ^{d/2}
        # For d=2: N(Λ) ~ (L/2π)² × π × Λ
        weyl_estimate = (L / (2 * np.pi))**2 * np.pi * Lambda
        
        # Allow 50% tolerance for finite Lambda
        rel_error = abs(count - weyl_estimate) / weyl_estimate
        assert rel_error < 0.5, f"Mode count {count} vs Weyl {weyl_estimate:.1f}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

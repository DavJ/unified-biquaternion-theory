#!/usr/bin/env python3
"""
Core Phase Coherence Statistic for CMB Spherical Harmonics
===========================================================

Implements the phase-comb test: measuring periodic phase-locking between
a_lm modes separated by period P.

Theory
------
For spherical harmonic coefficients a_lm of a CMB map:
- Power spectrum C_ℓ discards phases: C_ℓ = (1/(2ℓ+1)) Σ_m |a_ℓm|²
- Phase information: φ_ℓm = arg(a_ℓm)

Phase coherence statistic for period P:
  R(P) = |mean over (ℓ,m) of exp(i Δφ_ℓm(P))|
where
  Δφ_ℓm(P) = φ_{ℓ+P,m} - φ_{ℓ,m}

Under random phases (no structure): R(P) → 0 as N → ∞
Under phase-locking: R(P) > 0

Court-Grade Features
--------------------
- Deterministic RNG with seed
- Pre-registered periods: [255, 256, 137, 139]
- Surrogates preserve observed C_ℓ
- Multiple-testing correction via max-statistic
- Full metadata tracking

License: MIT
Author: UBT Research Team
"""

import numpy as np
from typing import List, Tuple, Dict, Optional
import warnings


def get_alm_index_pairs(lmax: int, ell_min: int, ell_max: int, period: int, 
                        m_mode: str = 'same_m') -> List[Tuple[int, int, int]]:
    """
    Precompute list of (ℓ, ℓ+P, m) index pairs for phase coherence calculation.
    
    Parameters
    ----------
    lmax : int
        Maximum ℓ value in alm array
    ell_min : int
        Minimum ℓ to include in test
    ell_max : int
        Maximum ℓ to include in test
    period : int
        Period P for phase difference Δφ = φ_{ℓ+P,m} - φ_{ℓ,m}
    m_mode : str
        How to pair modes. Options:
        - 'same_m': pair (ℓ,m) with (ℓ+P,m) [default, court-grade]
        - 'all_m': pair all (ℓ,m₁) with (ℓ+P,m₂) [future option]
    
    Returns
    -------
    pairs : list of (ell1, ell2, m)
        List of valid index triplets
    """
    pairs = []
    
    if m_mode == 'same_m':
        for ell in range(ell_min, ell_max + 1):
            ell_plus_p = ell + period
            if ell_plus_p > ell_max or ell_plus_p > lmax:
                continue
            
            # Include all m from -ℓ to +ℓ (but healpy alm only stores m≥0)
            # We'll handle negative m via conjugacy in actual computation
            for m in range(0, ell + 1):  # healpy convention: only m≥0 stored
                # Also check m is valid for ell+P
                if m <= ell_plus_p:
                    pairs.append((ell, ell_plus_p, m))
    else:
        raise NotImplementedError(f"m_mode={m_mode} not yet implemented")
    
    return pairs


def compute_phase_coherence(alm: np.ndarray, lmax: int, 
                            ell_min: int, ell_max: int,
                            period: int, m_mode: str = 'same_m') -> float:
    """
    Compute phase coherence R(P) for given period P.
    
    R(P) = |mean of exp(i Δφ_ℓm(P))| where Δφ_ℓm = arg(a_{ℓ+P,m}) - arg(a_{ℓm})
    
    Parameters
    ----------
    alm : complex ndarray
        Spherical harmonic coefficients (healpy alm format)
        Shape: (N_alm,) where N_alm = (lmax+1)*(lmax+2)/2
    lmax : int
        Maximum ℓ in alm array
    ell_min : int
        Minimum ℓ for test
    ell_max : int
        Maximum ℓ for test
    period : int
        Period P
    m_mode : str
        Pairing mode (default: 'same_m')
    
    Returns
    -------
    R : float
        Phase coherence statistic, range [0, 1]
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError(
            "healpy required for phase coherence calculation. "
            "Install with: pip install healpy"
        )
    
    # Get index pairs
    pairs = get_alm_index_pairs(lmax, ell_min, ell_max, period, m_mode)
    
    if len(pairs) == 0:
        warnings.warn(f"No valid (ℓ,m) pairs for period={period}, returning R=0")
        return 0.0
    
    # Compute phase differences
    phase_vectors = []
    
    for ell, ell_p, m in pairs:
        # Get alm indices
        idx1 = hp.sphtfunc.Alm.getidx(lmax, ell, m)
        idx2 = hp.sphtfunc.Alm.getidx(lmax, ell_p, m)
        
        # Get complex coefficients
        a1 = alm[idx1]
        a2 = alm[idx2]
        
        # Skip if either is zero (can happen in masked maps)
        if abs(a1) < 1e-30 or abs(a2) < 1e-30:
            continue
        
        # Phase difference: Δφ = arg(a2) - arg(a1) = arg(a2 / a1)
        # Compute as complex unit vector: exp(i Δφ) = (a2/a1) / |a2/a1|
        ratio = a2 / a1
        unit_vector = ratio / abs(ratio)
        
        phase_vectors.append(unit_vector)
    
    if len(phase_vectors) == 0:
        warnings.warn(f"All coefficients zero for period={period}, returning R=0")
        return 0.0
    
    # R(P) = |mean of unit vectors|
    phase_vectors = np.array(phase_vectors)
    mean_vector = np.mean(phase_vectors)
    R = abs(mean_vector)
    
    return R


def generate_phase_surrogates(alm: np.ndarray, lmax: int, 
                              n_surrogates: int,
                              seed: Optional[int] = None,
                              preserve_m0_real: bool = True) -> List[np.ndarray]:
    """
    Generate phase-randomized surrogates preserving |a_lm| (and thus C_ℓ).
    
    For each surrogate:
      a'_ℓm = |a_ℓm| exp(i θ_ℓm)
    where θ_ℓm ~ Uniform(0, 2π)
    
    Reality constraints for real maps:
      a_ℓ,-m = (-1)^m conj(a_ℓm)
      a_ℓ,0 is real
    
    Parameters
    ----------
    alm : complex ndarray
        Original alm coefficients
    lmax : int
        Maximum ℓ
    n_surrogates : int
        Number of surrogate realizations
    seed : int or None
        Random seed for reproducibility
    preserve_m0_real : bool
        If True, keep m=0 modes real-valued (default: True)
    
    Returns
    -------
    surrogates : list of ndarray
        List of phase-randomized alm arrays
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required. Install with: pip install healpy")
    
    rng = np.random.RandomState(seed)
    
    surrogates = []
    
    for i_surr in range(n_surrogates):
        alm_surr = np.zeros_like(alm)
        
        # Iterate over all ℓ,m (healpy stores only m≥0)
        for ell in range(lmax + 1):
            for m in range(0, ell + 1):
                idx = hp.sphtfunc.Alm.getidx(lmax, ell, m)
                
                # Original amplitude
                amplitude = abs(alm[idx])
                
                # Random phase
                if m == 0 and preserve_m0_real:
                    # m=0 modes are real: phase = 0 or π
                    # Keep sign of original
                    phase = 0.0 if alm[idx].real >= 0 else np.pi
                else:
                    # Random phase in [0, 2π)
                    phase = rng.uniform(0, 2 * np.pi)
                
                # New coefficient
                alm_surr[idx] = amplitude * np.exp(1j * phase)
        
        surrogates.append(alm_surr)
    
    return surrogates


def compute_p_values(R_obs: Dict[int, float], 
                    R_surrogates: Dict[int, List[float]],
                    periods: List[int],
                    correction: str = 'none') -> Dict[int, float]:
    """
    Compute p-values for each period from surrogate distribution.
    
    P-value = fraction of surrogates with R ≥ R_obs
    
    Multiple-testing correction:
    - 'none': No correction (default for pre-registered periods)
    - 'bonferroni': Bonferroni correction p_corr = min(p * n_periods, 1)
    - 'max_statistic': Use max over periods in surrogates (most conservative)
    
    Parameters
    ----------
    R_obs : dict
        Observed R(P) for each period
    R_surrogates : dict
        List of R(P) values from surrogates for each period
    periods : list of int
        Periods tested
    correction : str
        Multiple-testing correction method
    
    Returns
    -------
    p_values : dict
        P-value for each period
    """
    p_values = {}
    
    if correction == 'none':
        # Simple p-value per period
        for period in periods:
            R_obs_p = R_obs[period]
            R_surr_p = np.array(R_surrogates[period])
            
            n_surr = len(R_surr_p)
            n_exceed = np.sum(R_surr_p >= R_obs_p)
            
            # Add 1 to numerator and denominator to avoid p=0
            p = (n_exceed + 1) / (n_surr + 1)
            p_values[period] = p
    
    elif correction == 'bonferroni':
        # Bonferroni: multiply each p-value by number of tests
        for period in periods:
            R_obs_p = R_obs[period]
            R_surr_p = np.array(R_surrogates[period])
            
            n_surr = len(R_surr_p)
            n_exceed = np.sum(R_surr_p >= R_obs_p)
            
            p = (n_exceed + 1) / (n_surr + 1)
            p_corr = min(p * len(periods), 1.0)
            p_values[period] = p_corr
    
    elif correction == 'max_statistic':
        # Max-statistic: For each surrogate, take max R over all periods
        # Then compare observed max R to distribution of max R
        n_surr = len(R_surrogates[periods[0]])
        
        # Get max R for each surrogate
        R_max_surr = np.zeros(n_surr)
        for i_surr in range(n_surr):
            R_max_surr[i_surr] = max(
                R_surrogates[p][i_surr] for p in periods
            )
        
        # For each period, compute p-value against max distribution
        for period in periods:
            R_obs_p = R_obs[period]
            n_exceed = np.sum(R_max_surr >= R_obs_p)
            p = (n_exceed + 1) / (n_surr + 1)
            p_values[period] = p
    
    else:
        raise ValueError(f"Unknown correction method: {correction}")
    
    return p_values


def run_phase_comb_test(alm: np.ndarray, lmax: int,
                        ell_min: int = 30, ell_max: int = 1500,
                        periods: Optional[List[int]] = None,
                        n_mc_samples: int = 10000,
                        seed: int = 42,
                        m_mode: str = 'same_m',
                        correction: str = 'none',
                        metadata: Optional[Dict] = None) -> Dict:
    """
    Run complete phase-comb test with surrogates and p-values.
    
    Parameters
    ----------
    alm : complex ndarray
        Spherical harmonic coefficients
    lmax : int
        Maximum ℓ in alm
    ell_min : int
        Minimum ℓ for test (default: 30)
    ell_max : int
        Maximum ℓ for test (default: 1500)
    periods : list of int or None
        Periods to test. If None, use pre-registered [255, 256, 137, 139]
    n_mc_samples : int
        Number of Monte Carlo surrogates (default: 10000)
    seed : int
        Random seed (default: 42)
    m_mode : str
        Mode pairing (default: 'same_m')
    correction : str
        Multiple-testing correction (default: 'none' for pre-registered)
    metadata : dict or None
        Additional metadata to include in results
    
    Returns
    -------
    results : dict
        Complete results with observed R(P), surrogates, p-values, metadata
    """
    if periods is None:
        # Pre-registered periods
        periods = [255, 256, 137, 139]
    
    # Compute observed R(P) for each period
    print(f"Computing observed phase coherence for {len(periods)} periods...")
    R_obs = {}
    for period in periods:
        R_obs[period] = compute_phase_coherence(
            alm, lmax, ell_min, ell_max, period, m_mode
        )
        print(f"  Period {period}: R = {R_obs[period]:.6f}")
    
    # Generate surrogates
    print(f"\nGenerating {n_mc_samples} phase-randomized surrogates...")
    surrogates = generate_phase_surrogates(alm, lmax, n_mc_samples, seed)
    
    # Compute R(P) for each surrogate
    print("Computing surrogate distribution...")
    R_surrogates = {p: [] for p in periods}
    
    for i, alm_surr in enumerate(surrogates):
        if (i + 1) % 1000 == 0:
            print(f"  Surrogate {i+1}/{n_mc_samples}...", end='\r')
        
        for period in periods:
            R_surr = compute_phase_coherence(
                alm_surr, lmax, ell_min, ell_max, period, m_mode
            )
            R_surrogates[period].append(R_surr)
    
    print()
    
    # Compute p-values
    print("\nComputing p-values...")
    p_values = compute_p_values(R_obs, R_surrogates, periods, correction)
    
    for period in periods:
        print(f"  Period {period}: p = {p_values[period]:.6e}")
    
    # Find best period (smallest p-value)
    best_period = min(periods, key=lambda p: p_values[p])
    
    # Compute summary statistics for surrogates
    R_surr_stats = {}
    for period in periods:
        R_surr_p = np.array(R_surrogates[period])
        R_surr_stats[period] = {
            'mean': float(np.mean(R_surr_p)),
            'std': float(np.std(R_surr_p)),
            'median': float(np.median(R_surr_p)),
            'q95': float(np.percentile(R_surr_p, 95)),
            'q99': float(np.percentile(R_surr_p, 99)),
        }
    
    # Compile results
    results = {
        'periods': periods,
        'ell_min': ell_min,
        'ell_max': ell_max,
        'lmax': lmax,
        'n_mc_samples': n_mc_samples,
        'seed': seed,
        'm_mode': m_mode,
        'correction': correction,
        
        # Results
        'R_observed': R_obs,
        'p_values': p_values,
        'best_period': best_period,
        'best_p_value': p_values[best_period],
        
        # Surrogate statistics
        'surrogate_stats': R_surr_stats,
        
        # Full surrogate distributions (optional, can be large)
        # 'R_surrogates': R_surrogates,  # Commented out to save space
    }
    
    # Add metadata
    if metadata:
        results['metadata'] = metadata
    
    # Determine significance
    p_best = p_values[best_period]
    if p_best < 0.01:
        results['significance'] = 'CANDIDATE'
    elif p_best < 2.9e-7:
        results['significance'] = 'STRONG'
    else:
        results['significance'] = 'NULL'
    
    return results

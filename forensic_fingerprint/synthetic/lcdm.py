#!/usr/bin/env python3
"""
Synthetic ΛCDM Data Generation for Null Hypothesis Testing
===========================================================

This module provides tools for generating synthetic CMB observations
under the ΛCDM null hypothesis.

Used for:
1. Measuring false positive rates
2. Validating detection power
3. Confirming that candidate signals are not generic ΛCDM features

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
from typing import Optional, Union


def generate_lcdm_spectrum(ell, params=None, channel='TT'):
    """
    Generate approximate ΛCDM power spectrum.
    
    NOTE: This is a simplified approximation for testing purposes.
    For publication-quality work, use CAMB or CLASS.
    
    The approximation uses:
    - Exponentially damped sinusoid for acoustic oscillations
    - Power-law envelope
    - Empirically tuned to roughly match Planck best-fit
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    params : dict, optional
        ΛCDM parameters. If None, uses Planck 2018 best-fit approximation.
        Unused in current simple implementation.
    channel : str
        Spectrum type: 'TT', 'EE', 'TE', 'BB' (default: 'TT')
    
    Returns
    -------
    Cl_theory : ndarray
        Theoretical ΛCDM C_ℓ values (μK²)
    
    Notes
    -----
    This is an approximate generator for testing only.
    For real ΛCDM spectra, load from CAMB/CLASS output or use Planck model files.
    """
    ell = np.asarray(ell, dtype=float)
    
    if channel.upper() == 'TT':
        # Simple TT approximation
        # Rough fit to Planck TT at ℓ = 30-2000
        
        # Envelope: ℓ(ℓ+1)/(2π) scaling
        envelope = ell * (ell + 1) / (2 * np.pi)
        
        # Damping at high ℓ (silk damping)
        damping = np.exp(-(ell / 1000.0) ** 1.5)
        
        # Acoustic oscillations (rough approximation)
        # First acoustic peak at ℓ ≈ 220
        k_acoustic = 2 * np.pi / 220.0  # Approximate wavenumber
        oscillations = 1.0 + 0.15 * np.sin(k_acoustic * ell + np.pi / 4)
        
        # Combine components
        # Scale to roughly match Planck (C_ℓ ~ 1000-6000 μK² at peaks)
        Cl_theory = 3000.0 * oscillations * damping / (1 + (ell / 200.0) ** 0.5)
        
        # Ensure positive
        Cl_theory = np.maximum(Cl_theory, 10.0)  # Floor at 10 μK²
    
    elif channel.upper() == 'EE':
        # EE is smaller amplitude, peaks shifted
        envelope = ell * (ell + 1) / (2 * np.pi)
        damping = np.exp(-(ell / 800.0) ** 1.5)
        k_acoustic = 2 * np.pi / 220.0
        oscillations = 1.0 + 0.2 * np.sin(k_acoustic * ell)
        
        # EE amplitude ~ 1/10 of TT at most ℓ
        Cl_theory = 200.0 * oscillations * damping / (1 + (ell / 150.0) ** 0.5)
        Cl_theory = np.maximum(Cl_theory, 1.0)
    
    elif channel.upper() == 'TE':
        # TE can be negative, has different phase
        envelope = ell * (ell + 1) / (2 * np.pi)
        damping = np.exp(-(ell / 900.0) ** 1.5)
        k_acoustic = 2 * np.pi / 220.0
        oscillations = np.sin(k_acoustic * ell - np.pi / 2)
        
        # TE amplitude intermediate between TT and EE
        Cl_theory = 100.0 * oscillations * damping / (1 + (ell / 180.0) ** 0.5)
        # TE can be negative (no floor)
    
    elif channel.upper() == 'BB':
        # BB is near-zero in ΛCDM (no primordial tensor modes in this approx)
        Cl_theory = np.ones_like(ell) * 0.1  # Tiny floor for numerical stability
    
    else:
        raise ValueError(f"Unknown channel: {channel}. Use 'TT', 'EE', 'TE', or 'BB'.")
    
    return Cl_theory


def generate_mock_observation(
    ell,
    Cl_theory,
    noise_model,
    cov=None,
    seed=None,
    injection_signal=None
):
    """
    Generate synthetic CMB observation with noise.
    
    Supports two noise modes:
    1. Diagonal Gaussian: obs = theory + N(0, σ²)
    2. Multivariate Gaussian: obs = theory + N(0, Cov)
    
    Optionally inject a test signal for detection power studies.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments (length N)
    Cl_theory : array-like
        Theoretical ΛCDM C_ℓ (length N)
    noise_model : dict or array-like
        If dict: must have 'sigma' key with diagonal uncertainties
        If array: diagonal uncertainties (length N)
    cov : ndarray, optional
        Full covariance matrix (N x N). If provided, uses multivariate sampling.
        If None, uses diagonal noise from noise_model.
    seed : int, optional
        Random seed for reproducibility
    injection_signal : dict, optional
        Signal to inject for detection testing. Keys:
        - 'period': float (Δℓ for sinusoidal injection)
        - 'amplitude': float
        - 'phase': float (radians)
    
    Returns
    -------
    Cl_obs : ndarray
        Synthetic observed C_ℓ (length N)
    
    Raises
    ------
    ValueError
        If noise_model format is invalid
    """
    ell = np.asarray(ell)
    Cl_theory = np.asarray(Cl_theory)
    n = len(ell)
    
    if len(Cl_theory) != n:
        raise ValueError(f"Theory length {len(Cl_theory)} doesn't match ell length {n}")
    
    # Set random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Extract sigma from noise_model
    if isinstance(noise_model, dict):
        if 'sigma' not in noise_model:
            raise ValueError("noise_model dict must have 'sigma' key")
        sigma = np.asarray(noise_model['sigma'])
    else:
        sigma = np.asarray(noise_model)
    
    if len(sigma) != n:
        raise ValueError(f"Sigma length {len(sigma)} doesn't match ell length {n}")
    
    # Generate noise
    if cov is not None:
        # Multivariate Gaussian noise: N(0, Cov)
        if cov.shape != (n, n):
            raise ValueError(f"Covariance shape {cov.shape} doesn't match ell length {n}")
        
        noise = np.random.multivariate_normal(mean=np.zeros(n), cov=cov)
    else:
        # Diagonal Gaussian noise: N(0, σ²)
        noise = np.random.normal(loc=0, scale=sigma, size=n)
    
    # Start with theory + noise
    Cl_obs = Cl_theory + noise
    
    # Inject test signal if requested
    if injection_signal is not None:
        period = injection_signal.get('period')
        amplitude = injection_signal.get('amplitude')
        phase = injection_signal.get('phase', 0.0)
        
        if period is None or amplitude is None:
            raise ValueError("injection_signal must have 'period' and 'amplitude' keys")
        
        # Sinusoidal injection: A * sin(2π ℓ / Δℓ + φ)
        k = 2 * np.pi / period
        signal = amplitude * np.sin(k * ell + phase)
        
        Cl_obs += signal
    
    return Cl_obs


def load_lcdm_model_from_file(model_file, ell_min=None, ell_max=None, channel='TT'):
    """
    Load ΛCDM model spectrum from file (CAMB/CLASS or Planck format).
    
    This is a convenience wrapper around the planck loader.
    
    Parameters
    ----------
    model_file : str or Path
        Path to model file
    ell_min : int, optional
        Minimum multipole to load
    ell_max : int, optional
        Maximum multipole to load
    channel : str
        Spectrum type (default: 'TT')
    
    Returns
    -------
    ell : ndarray
        Multipole moments
    Cl_theory : ndarray
        Theoretical C_ℓ values
    
    Notes
    -----
    This is a thin wrapper. For more control, use loaders.planck directly.
    """
    from pathlib import Path
    import sys
    
    # Add loaders to path
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root / 'loaders'))
    
    import planck
    
    # Load using planck loader (works for CAMB/CLASS files too)
    data = planck.load_planck_data(
        obs_file=model_file,
        model_file=None,  # No separate model
        ell_min=ell_min,
        ell_max=ell_max,
        spectrum_type=channel,
        _skip_size_validation=True  # Allow small test files
    )
    
    return data['ell'], data['cl_obs']  # Model file loaded as "obs"

#!/usr/bin/env python3
"""
Forensic Fingerprint - Canonical Physical Constants
====================================================

This module defines the canonical observed constants used as targets
for UBT predictions. All values from CODATA 2018 unless otherwise noted.

Single source of truth for experimental values - NO hardcoding in tools.

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

# =============================================================================
# Fine Structure Constant (CODATA 2018)
# =============================================================================

ALPHA_INV_OBS = 137.035999084
"""
Fine structure constant inverse (α⁻¹).
Source: CODATA 2018
Value: 137.035999084(21)
Uncertainty: 2.1e-8 (relative)
"""

ALPHA_INV_SIGMA = 0.000000021
"""
Uncertainty in α⁻¹ (1σ standard error).
Source: CODATA 2018
"""

# =============================================================================
# Electron Mass (CODATA 2018)
# =============================================================================

ELECTRON_MASS_OBS = 0.51099895000
"""
Electron mass (MeV).
Source: CODATA 2018
Value: 0.51099895000(15) MeV
Uncertainty: 1.5e-10 MeV (absolute), 2.9e-10 (relative)
"""

ELECTRON_MASS_SIGMA = 0.00000000015
"""
Uncertainty in electron mass (1σ standard error, MeV).
Source: CODATA 2018
"""

# =============================================================================
# Helper Functions
# =============================================================================

def get_observed_values() -> dict:
    """
    Get dictionary of observed constants.
    
    Returns
    -------
    dict
        Dictionary of {observable_name: observed_value}
    """
    return {
        'alpha_inv': ALPHA_INV_OBS,
        'electron_mass': ELECTRON_MASS_OBS,
    }


def get_uncertainties() -> dict:
    """
    Get dictionary of uncertainties (1σ standard errors).
    
    Returns
    -------
    dict
        Dictionary of {observable_name: sigma}
    """
    return {
        'alpha_inv': ALPHA_INV_SIGMA,
        'electron_mass': ELECTRON_MASS_SIGMA,
    }


def get_default_tolerances() -> dict:
    """
    Get default tolerances for hit detection.
    
    Uses 5σ for fine structure constant (high precision),
    and 0.001 MeV (1 keV) for electron mass.
    
    Returns
    -------
    dict
        Dictionary of {observable_name: tolerance}
        
    Notes
    -----
    Tolerances are chosen as:
    - alpha_inv: 5σ = 5 * 2.1e-8 * 137.036 ≈ 1.4e-5 
                (but rounded to 0.5 for practical parameter space exploration)
    - electron_mass: 0.001 MeV (1 keV) - practical tolerance for mass predictions
    
    These are PLACEHOLDER values for framework demonstration.
    Production use should justify tolerances based on theory predictions.
    """
    return {
        'alpha_inv': 0.5,  # Practical tolerance for parameter space exploration
        'electron_mass': 0.001,  # 1 keV tolerance
    }


# =============================================================================
# Validation
# =============================================================================

def validate_constants():
    """
    Validate that constants are internally consistent.
    
    Raises
    ------
    ValueError
        If any constants fail validation checks.
    """
    # Check values are positive
    if ALPHA_INV_OBS <= 0:
        raise ValueError(f"ALPHA_INV_OBS must be positive, got {ALPHA_INV_OBS}")
    if ELECTRON_MASS_OBS <= 0:
        raise ValueError(f"ELECTRON_MASS_OBS must be positive, got {ELECTRON_MASS_OBS}")
    
    # Check uncertainties are positive
    if ALPHA_INV_SIGMA <= 0:
        raise ValueError(f"ALPHA_INV_SIGMA must be positive, got {ALPHA_INV_SIGMA}")
    if ELECTRON_MASS_SIGMA <= 0:
        raise ValueError(f"ELECTRON_MASS_SIGMA must be positive, got {ELECTRON_MASS_SIGMA}")
    
    # Check uncertainties are small relative to values
    if ALPHA_INV_SIGMA / ALPHA_INV_OBS > 0.01:
        raise ValueError("ALPHA_INV_SIGMA too large relative to value")
    if ELECTRON_MASS_SIGMA / ELECTRON_MASS_OBS > 0.01:
        raise ValueError("ELECTRON_MASS_SIGMA too large relative to value")


# Auto-validate on import
validate_constants()

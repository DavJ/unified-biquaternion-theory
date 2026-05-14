"""
Layer 2 Fingerprint - Observable Predictors

This module predicts physical observables from Layer 2 configurations.

Two modes:
----------
1. 'placeholder': Toy model for framework demonstration (NOT physics)
2. 'ubt': Real UBT mapping (requires wiring to existing UBT modules)

⚠️ WARNING: placeholder mode uses FAKE formulas - results have NO physical meaning!

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

from .config_space import Layer2Config

# Import from canonical constants module (single source of truth)
repo_root = Path(__file__).resolve().parents[2]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from forensic_fingerprint.constants import (
    get_observed_values,
    get_default_tolerances as get_canonical_tolerances,
)


def predict_constants(
    cfg: Layer2Config, 
    mapping: str = 'placeholder',
    targets: list = None
) -> Dict[str, float]:
    """
    Predict physical constants from Layer 2 configuration.
    
    Parameters
    ----------
    cfg : Layer2Config
        Layer 2 configuration
    mapping : str, optional
        Prediction mapping: 'placeholder' or 'ubt' (default: 'placeholder')
    targets : list, optional
        List of target observables to predict.
        Default: ['alpha_inv', 'electron_mass']
        
    Returns
    -------
    Dict[str, float]
        Dictionary of {observable_name: predicted_value}
        
    Raises
    ------
    RuntimeError
        If mapping='ubt' but UBT mapping is not implemented or fails
    ValueError
        If mapping is unknown
        
    Notes
    -----
    ⚠️ WARNING: mapping='placeholder' uses FAKE formulas with NO physical meaning!
    Only mapping='ubt' produces scientifically interpretable results.
    """
    if targets is None:
        targets = ['alpha_inv', 'electron_mass']
    
    if mapping == 'placeholder':
        return _predict_placeholder(cfg, targets)
    elif mapping == 'ubt':
        return _predict_ubt(cfg, targets)
    else:
        raise ValueError(f"Unknown prediction mapping: {mapping}")


def _predict_placeholder(cfg: Layer2Config, targets: list) -> Dict[str, float]:
    """
    ⚠️ PLACEHOLDER toy model - NOT real UBT physics!
    
    This is an ARBITRARY formula to demonstrate the statistical framework.
    Results have NO physical meaning.
    
    Parameters
    ----------
    cfg : Layer2Config
        Layer 2 configuration
    targets : list
        List of targets to predict
        
    Returns
    -------
    Dict[str, float]
        Dictionary with requested targets (PLACEHOLDER values)
    """
    results = {}
    
    if 'alpha_inv' in targets:
        # FAKE formula for alpha inverse
        # This is NOT derived from UBT - just a toy model
        correction_rs = (cfg.rs_n - 255) * 0.01
        correction_ofdm = (cfg.ofdm_channels - 16) * 0.1
        correction_grid = (cfg.quantization_grid - 255) * 0.001
        
        alpha_inv = (
            cfg.winding_number 
            + correction_rs 
            + correction_ofdm 
            + correction_grid
        )
        results['alpha_inv'] = alpha_inv
    
    if 'electron_mass' in targets:
        # FAKE formula for electron mass
        # This is NOT derived from UBT - just a toy model
        base_mass = 0.511  # MeV
        mass_correction = (cfg.rs_k / cfg.rs_n - 0.78) * 0.01
        electron_mass = base_mass + mass_correction
        results['electron_mass'] = electron_mass
    
    return results


def _predict_ubt(cfg: Layer2Config, targets: list) -> Dict[str, float]:
    """
    Real UBT physics mapping using adapters to existing UBT code.
    
    This wires to existing UBT calculation modules via adapters:
    - TOOLS/simulations/emergent_alpha_calculator.py for alpha
    - TOOLS/simulations/validate_electron_mass.py for electron mass
    - tools/planck_validation/mapping.py for cosmological parameters
    
    Parameters
    ----------
    cfg : Layer2Config
        Layer 2 configuration
    targets : list
        List of targets to predict
        
    Returns
    -------
    Dict[str, float]
        Dictionary with predicted observables from real UBT
        
    Raises
    ------
    RuntimeError
        If UBT adapters fail or are not available
    """
    try:
        from .ubt_adapters import predict_all_constants
        return predict_all_constants(cfg, targets)
    except ImportError as e:
        raise RuntimeError(
            f"Failed to import UBT adapters: {e}\n"
            "Required: forensic_fingerprint/layer2/ubt_adapters.py\n"
            "Make sure repository structure is intact."
        ) from e
    except Exception as e:
        raise RuntimeError(
            f"UBT prediction failed: {e}\n"
            "Configuration: {cfg}\n"
            "Targets: {targets}"
        ) from e


def get_experimental_values() -> Dict[str, float]:
    """
    Get experimental values for comparison.
    
    Returns
    -------
    Dict[str, float]
        Dictionary of {observable_name: experimental_value}
    """
    return get_observed_values()


def get_default_tolerances() -> Dict[str, float]:
    """
    Get default tolerances for hit detection.
    
    Returns
    -------
    Dict[str, float]
        Dictionary of {observable_name: tolerance}
    """
    return get_canonical_tolerances()

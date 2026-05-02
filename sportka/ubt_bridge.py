# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/ubt_bridge.py — Clean adapter interface between Sportka and UBT.

This module provides documented adapter functions that allow Sportka code
to use transforms from the UBT theta formalism without mixing speculative
UBT theory into the prediction pipeline.

Design principles
-----------------
1. All functions here are stateless adapters — they take numpy arrays
   and return numpy arrays.
2. No speculative text about lottery prediction is included here.
3. The interface is stable; the UBT implementation may change.
4. In the future, implementations can be swapped out to use transforms
   from unified-biquaternion-theory or ubt-theta-lab directly.

Usage
-----
    from sportka.ubt_bridge import apply_theta_transform, apply_complex_phase

    smoothed = apply_theta_transform(prob_matrix, sigma=3.0)
    phase_mod = apply_complex_phase(prob_vector, tau_imag=0.5)
"""
from __future__ import annotations

import numpy as np

from sportka.features import N_NUMBERS


def apply_theta_transform(
    X: np.ndarray,
    sigma: float = 3.0,
    periodic: bool = True,
) -> np.ndarray:
    """
    Apply the UBT heat-kernel theta transform to feature matrix X.

    Each row of X is treated as a probability vector over N_NUMBERS
    and smoothed with a Gaussian heat kernel of bandwidth sigma on
    the discrete number lattice.

    Parameters
    ----------
    X : array of shape (n_rows, N_NUMBERS) or (N_NUMBERS,).
    sigma : Gaussian kernel bandwidth (in lattice units).
    periodic : Use periodic (toroidal) boundary conditions.

    Returns
    -------
    out : Same shape as X, with L1 norm preserved per row.
    """
    from sportka.ubt_theta_transform import theta_heat_kernel, theta_heat_kernel_matrix
    if X.ndim == 1:
        return theta_heat_kernel(X, sigma=sigma, periodic=periodic)
    return theta_heat_kernel_matrix(X, sigma=sigma, periodic=periodic)


def apply_complex_phase(
    x: np.ndarray,
    tau_imag: float = 1.0,
) -> np.ndarray:
    """
    Apply complex-phase theta diffusion to a probability vector.

    Inspired by the imaginary time component ψ in UBT's complex time
    τ = t + iψ.  This is a purely mathematical operation.

    Parameters
    ----------
    x : 1-D probability vector of shape (N_NUMBERS,).
    tau_imag : Imaginary time parameter ψ (controls diffusion width).

    Returns
    -------
    out : shape (N_NUMBERS,), L1-normalised to match input sum.
    """
    from sportka.ubt_theta_transform import complex_phase_theta
    return complex_phase_theta(x, tau_imag=tau_imag)


def apply_multiscale_theta(
    X: np.ndarray,
    sigmas: tuple = (1.5, 3.0, 7.0),
    periodic: bool = True,
) -> np.ndarray:
    """
    Apply theta transforms at multiple scales and concatenate outputs.

    Parameters
    ----------
    X : array of shape (n_rows, N_NUMBERS).
    sigmas : Tuple of sigma values.

    Returns
    -------
    out : shape (n_rows, N_NUMBERS * len(sigmas))
    """
    from sportka.ubt_theta_transform import theta_heat_kernel_matrix
    parts = [theta_heat_kernel_matrix(X, sigma=s, periodic=periodic) for s in sigmas]
    return np.concatenate(parts, axis=1)


def augment_features_with_theta(
    X: np.ndarray,
    prob_cols: slice = None,
    sigma: float = 3.0,
) -> np.ndarray:
    """
    Augment an existing feature matrix with theta-smoothed probability columns.

    Takes the probability sub-matrix (columns given by prob_cols, or the
    first N_NUMBERS columns by default), applies the theta transform, and
    appends the result as new columns.

    Parameters
    ----------
    X : Feature matrix of shape (n_rows, n_features).
    prob_cols : Column slice selecting the probability features.
        Default: slice(0, N_NUMBERS).
    sigma : Kernel bandwidth.

    Returns
    -------
    out : shape (n_rows, n_features + N_NUMBERS)
    """
    if prob_cols is None:
        prob_cols = slice(0, N_NUMBERS)
    prob_X = X[:, prob_cols]
    smoothed = apply_theta_transform(prob_X, sigma=sigma)
    return np.concatenate([X, smoothed], axis=1)

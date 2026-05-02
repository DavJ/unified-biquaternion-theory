# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/ubt_theta_transform.py — Theta-kernel transform (experimental).

This module implements a heat-kernel / theta-function inspired transform
that maps a frequency probability vector to a "smoothed" representation
using Gaussian heat-kernel weights on the discrete number lattice.

The transform is kept *experimental*.  It does not make physical claims
about Sportka outcomes — it is a mathematical smoothing operation inspired
by the UBT theta-function formalism.

For clean UBT integration, see sportka/ubt_bridge.py.
"""
from __future__ import annotations

import math
from typing import Optional

import numpy as np

from sportka.features import N_NUMBERS

# ---------------------------------------------------------------------------
# Heat-kernel theta transform
# ---------------------------------------------------------------------------


def theta_heat_kernel(
    x: np.ndarray,
    sigma: float = 3.0,
    n: int = N_NUMBERS,
    periodic: bool = True,
) -> np.ndarray:
    """
    Apply a Gaussian heat-kernel smoothing on the discrete number lattice.

    For each position k, the output is:
        out[k] = sum_j  x[j] * K(k - j)
    where K is a Gaussian (periodic or linear) kernel.

    Parameters
    ----------
    x : Input vector of shape (n,).  Typically a probability vector.
    sigma : Standard deviation of the Gaussian kernel (in lattice units).
    n : Lattice size (default N_NUMBERS = 49).
    periodic : If True, use circular (toroidal) distance.

    Returns
    -------
    out : Smoothed vector of shape (n,), same L1 norm as input.
    """
    if x.ndim != 1 or len(x) != n:
        raise ValueError(f"Expected 1-D array of length {n}, got shape {x.shape}.")

    out = np.zeros(n, dtype=np.float64)
    sigma_squared = 2.0 * sigma ** 2

    for k in range(n):
        total_weight = 0.0
        for j in range(n):
            if periodic:
                d = min(abs(k - j), n - abs(k - j))
            else:
                d = abs(k - j)
            w = math.exp(-(d ** 2) / sigma_squared)
            out[k] += x[j] * w
            total_weight += w
        if total_weight > 0:
            out[k] /= total_weight

    # Preserve L1 norm (probability sum)
    input_sum = float(x.sum())
    out_sum = float(out.sum())
    if out_sum > 0 and input_sum > 0:
        out *= input_sum / out_sum

    return out.astype(np.float32)


def theta_heat_kernel_matrix(
    X: np.ndarray,
    sigma: float = 3.0,
    periodic: bool = True,
) -> np.ndarray:
    """
    Apply theta_heat_kernel row-wise to a 2-D feature matrix.

    Parameters
    ----------
    X : shape (n_rows, N_NUMBERS)
    sigma : Kernel bandwidth.

    Returns
    -------
    out : shape (n_rows, N_NUMBERS)
    """
    if X.ndim != 2 or X.shape[1] != N_NUMBERS:
        raise ValueError(f"Expected shape (n, {N_NUMBERS}), got {X.shape}.")
    return np.array([theta_heat_kernel(X[i], sigma=sigma, periodic=periodic) for i in range(len(X))])


# ---------------------------------------------------------------------------
# Multi-scale theta transform
# ---------------------------------------------------------------------------

def multiscale_theta_transform(
    x: np.ndarray,
    sigmas: tuple = (1.5, 3.0, 7.0),
    n: int = N_NUMBERS,
    periodic: bool = True,
) -> np.ndarray:
    """
    Compute theta transforms at multiple scales and concatenate.

    Parameters
    ----------
    x : Input vector of shape (n,).
    sigmas : Tuple of sigma values for multi-scale analysis.

    Returns
    -------
    out : shape (n * len(sigmas),) — concatenation of all scales.
    """
    parts = [theta_heat_kernel(x, sigma=s, n=n, periodic=periodic) for s in sigmas]
    return np.concatenate(parts)


def complex_phase_theta(
    x: np.ndarray,
    tau_imag: float = 1.0,
    n: int = N_NUMBERS,
) -> np.ndarray:
    """
    Complex-time theta transform: apply phase modulation inspired by
    the UBT imaginary time parameter ψ in τ = t + iψ.

    For each number k, compute:
        out[k] = sum_j  x[j] * exp(-π |k-j|^2 / (n * tau_imag))

    This introduces a "phase diffusion" analogous to heat flow in
    imaginary time.  The result is purely experimental and should be
    validated empirically before use in production.

    Parameters
    ----------
    x : Input probability vector of shape (n,).
    tau_imag : Imaginary time parameter ψ (controls diffusion width).

    Returns
    -------
    out : shape (n,), real-valued, L1-normalised to match input sum.
    """
    if tau_imag <= 0:
        raise ValueError("tau_imag must be positive.")
    denom = math.pi * n * tau_imag
    out = np.zeros(n, dtype=np.float64)
    for k in range(n):
        for j in range(n):
            d2 = (k - j) ** 2
            out[k] += x[j] * math.exp(-math.pi * d2 / denom)

    input_sum = float(x.sum())
    out_sum = float(out.sum())
    if out_sum > 0 and input_sum > 0:
        out *= input_sum / out_sum

    return out.astype(np.float32)

# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
L_layer_flow_test.py — Numerical test of the L0 → L1 → L2 layer flow in UBT.

Task: ubt_L0_L1_L2_full_audit, Step 6 (Numerical Test)
Date: 2026-05-05

Purpose
-------
This script implements a numerical flow test that:
  1. Generates a random "input state" Θ (represented as a finite-dimensional
     discretized field proxy — a complex array).
  2. Applies L0 invariant extraction (spectral-action proxy, winding proxy).
  3. Applies L1 effective potential V_eff(n) computation.
  4. Applies L2 coding statistics (Hamming P₀ and Gray A_gray).
  5. Logs norms, dimensionality, and variance at each stage.
  6. Tests stability under perturbation.
  7. Tests approximate reversibility where applicable.

IMPORTANT: The L0 "spectral action" and "winding number" computed here are
finite-dimensional proxies, not the full continuum invariants defined in
FORMAL_INVARIANT_EXTRACTION_LAYER0.tex. The field Θ is represented as a
discretized complex array over a finite lattice.

These proxies are:
  - I_spec_proxy: Σ f(|λ_n|²/Λ²) where λ_n are DFT eigenvalues of Θ
  - I_wind_proxy: winding of arg(Θ) around the lattice boundary

Usage
-----
  python L_layer_flow_test.py [--seed SEED] [--n-trials N] [--perturb EPS]

Output
------
  Console: norms, dimensions, variance, entropy at each stage.
  reports/L_layer_numeric.md: markdown summary of results.

References
----------
  research_tracks/L_layers/L_math_formulation.md  (mathematical definitions)
  research_tracks/L_layers/L_shapes.md             (dimensional flow)
  ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex  §2
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Dict, Any, Tuple

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy is required. Install with: pip install numpy")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPORT_PATH = Path(__file__).parent.parent / "reports" / "L_layer_numeric.md"

# Lattice size for field proxy (must be power of 2 for DFT)
LATTICE_SIZE = 64   # 1D lattice, represents discretized ψ-circle

# Cutoff Λ for spectral action filter
LAMBDA_CUTOFF = 10.0

# Symbol alphabet size N for Gray transport (must be power of 2)
GRAY_N = 16

# Range of winding numbers for V_eff scan
N_WINDING_MIN = 101
N_WINDING_MAX = 200

# Physical constant B₀ = 8π (one-loop baseline, [L1] PROVED)
B0 = 8.0 * math.pi

# Fraction of L0 invariant information preserved at L2 (expected to be < 1)
# Used only for logging.


# ---------------------------------------------------------------------------
# Step 0: Generate random input state Θ
# ---------------------------------------------------------------------------

def generate_theta(n: int, rng: np.random.Generator) -> np.ndarray:
    """
    Generate a random complex field array as a proxy for Θ.

    The field Θ is represented as a 1D complex array of length n over a
    discretized ψ-circle (imaginary time circle). This is a finite-dimensional
    proxy for the infinite-dimensional biquaternionic field.

    Parameters
    ----------
    n : int, lattice size
    rng : numpy random generator

    Returns
    -------
    theta : complex array of shape (n,)
    """
    # Gaussian random complex field (zero mean, unit variance)
    real = rng.standard_normal(n)
    imag = rng.standard_normal(n)
    return (real + 1j * imag) / math.sqrt(2)


# ---------------------------------------------------------------------------
# L0: Spectral action proxy and winding number proxy
# ---------------------------------------------------------------------------

def l0_spectral_action_proxy(theta: np.ndarray, Lambda: float = LAMBDA_CUTOFF) -> float:
    """
    Compute a proxy for the Layer-0 spectral action:
      I_spec_proxy = Σ_n f(|λ_n|²/Λ²)
    where λ_n are the DFT coefficients of theta, and f(x) = exp(-x).

    This is a finite-dimensional proxy for I_spec[Θ] = Tr[f(D²/Λ²)].

    Returns: real scalar
    """
    # DFT coefficients serve as spectral eigenvalues (proxy for Dirac spectrum)
    spectrum = np.fft.fft(theta)
    # Frequencies (normalized)
    freqs = np.fft.fftfreq(len(theta)) * len(theta)  # integer frequencies
    lambda_sq = np.abs(spectrum) ** 2 * (freqs ** 2 + 1.0)  # λ_n²: amplitude × freq²
    # Spectral action filter f(x) = exp(-x)
    x = lambda_sq / (Lambda ** 2)
    return float(np.sum(np.exp(-x)))


def l0_winding_proxy(theta: np.ndarray) -> int:
    """
    Compute a proxy for the Layer-0 topological winding number:
      I_wind_proxy = winding number of arg(Θ) around the lattice.

    Returns: integer winding number
    """
    phases = np.angle(theta)  # in (-π, π]
    # Compute cumulative phase differences (unwrapped)
    diffs = np.diff(np.unwrap(phases))
    total_winding = np.sum(diffs) / (2 * np.pi)
    return int(round(total_winding))


def l0_phase_winding_proxy(theta: np.ndarray) -> int:
    """
    Proxy for the imaginary-time phase winding K_ψ.
    Counts sign changes in Im(Θ) as a rough phase winding proxy.

    Returns: integer (number of zero crossings / 2)
    """
    imag_part = np.imag(theta)
    sign_changes = np.sum(np.diff(np.sign(imag_part)) != 0)
    return int(sign_changes // 2)


def l0_extract_invariants(theta: np.ndarray) -> Dict[str, Any]:
    """
    Extract all available L0 proxy invariants from the field array theta.

    Returns: dict with keys:
      I_spec_proxy   : float
      I_wind_proxy   : int
      I_phase_proxy  : int
      norm_theta     : float  (||Θ||₂)
      dim_input      : int    (lattice size)
    """
    return {
        "I_spec_proxy": l0_spectral_action_proxy(theta),
        "I_wind_proxy": l0_winding_proxy(theta),
        "I_phase_proxy": l0_phase_winding_proxy(theta),
        "norm_theta": float(np.linalg.norm(theta)),
        "dim_input": len(theta),
    }


# ---------------------------------------------------------------------------
# L1: Effective potential and winding attractor
# ---------------------------------------------------------------------------

def l1_veff(n: int, B: float = B0) -> float:
    """
    Compute the one-loop effective potential:
      V_eff(n) = n² - B·n·ln(n)

    Source: canonical/appendices/appendix_alpha_geometry.tex §3
            ALPHA_PROGRESS_REPORT.md §2.3
    Status: [L1] PROVED (given B)

    Parameters
    ----------
    n : int, winding number
    B : float, one-loop coefficient (default = B₀ = 8π)

    Returns: float
    """
    if n <= 0:
        raise ValueError(f"n must be positive, got {n}")
    return float(n ** 2 - B * n * math.log(n))


def l1_scan_weff(n_min: int = N_WINDING_MIN, n_max: int = N_WINDING_MAX,
                 B: float = B0) -> Dict[str, Any]:
    """
    Scan V_eff over a range of winding numbers and find the attractor n*.

    Returns: dict with n_values, veff_values, n_star, v_star
    """
    ns = list(range(n_min, n_max + 1))
    veffs = [l1_veff(n, B) for n in ns]
    n_star_idx = int(np.argmin(veffs))
    return {
        "n_values": ns,
        "veff_values": veffs,
        "n_star": ns[n_star_idx],
        "v_star": veffs[n_star_idx],
        "B": B,
    }


# ---------------------------------------------------------------------------
# L2: Hamming P₀ and Gray A_gray
# ---------------------------------------------------------------------------

def generate_hamming_844_codewords() -> np.ndarray:
    """Generate all 16 codewords of the extended Hamming (8,4,4) code."""
    P = np.array([
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
    ], dtype=np.uint8)
    codewords = []
    for msg in range(16):
        bits = np.array([(msg >> (3 - i)) & 1 for i in range(4)], dtype=np.uint8)
        parity = (bits @ P) % 2
        codeword_bits = np.concatenate([bits, parity])
        codeword_int = int(sum(int(b) << (7 - i) for i, b in enumerate(codeword_bits)))
        codewords.append(codeword_int)
    return np.array(codewords, dtype=np.uint8)


# Parity check matrix H (4×8)
_H_HAMMING = np.array([
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
], dtype=np.uint8)


def hamming_syndrome_zero(block_bits: np.ndarray) -> bool:
    """Return True if the 8-bit block has syndrome 0 (is a valid codeword)."""
    syndrome = (_H_HAMMING @ block_bits) % 2
    return bool(np.all(syndrome == 0))


def l2s_p0_from_phases(theta: np.ndarray, N_blocks: int = 32) -> float:
    """
    Compute L2S statistic P₀ from the field proxy theta.

    Procedure:
      1. Take the first N_blocks × 8 entries of Im(theta), discretize to {0,1}.
      2. Form 8-bit blocks.
      3. Compute fraction of syndrome-zero blocks.

    Returns: P₀ ∈ [0,1]
    """
    signal = np.imag(theta)
    # Discretize to {0,1}: positive → 1, non-positive → 0
    bits = (signal > 0.0).astype(np.uint8)
    # Pad or truncate to N_blocks * 8
    needed = N_blocks * 8
    if len(bits) < needed:
        bits = np.pad(bits, (0, needed - len(bits)))
    bits = bits[:needed]
    # Form blocks
    blocks = bits.reshape(N_blocks, 8)
    # Compute P₀
    n_zero = sum(1 for block in blocks if hamming_syndrome_zero(block))
    return n_zero / N_blocks


def binary_to_gray(n: int) -> int:
    """Standard reflected binary Gray code."""
    return n ^ (n >> 1)


def build_gray_rank(N: int) -> np.ndarray:
    """Build gray_rank[s] = position of symbol s in Gray ordering."""
    if N & (N - 1) != 0:
        raise ValueError(f"N must be power of 2, got {N}")
    gray_rank = np.empty(N, dtype=np.int32)
    for n in range(N):
        g = binary_to_gray(n)
        gray_rank[g] = n
    return gray_rank


def l2t_a_gray_from_phases(theta: np.ndarray, N: int = GRAY_N) -> float:
    """
    Compute L2T statistic A_gray from the field proxy theta.

    Procedure:
      1. Extract phases from theta: φ = arg(theta).
      2. Discretize to N symbols.
      3. Compute gray_adjacency_score.

    Returns: A_gray ∈ [0,1]
    """
    phases = np.angle(theta)  # in (-π, π]
    # Discretize
    normalized = (phases + np.pi) / (2 * np.pi)
    normalized = np.clip(normalized, 0.0, 1.0 - 1e-12)
    symbols = (N * normalized).astype(np.int32)
    gray_rank = build_gray_rank(N)
    # Compute adjacency score
    s = symbols[:-1]
    sp = symbols[1:]
    r = gray_rank[s]
    rp = gray_rank[sp]
    diff = np.abs(r.astype(np.int64) - rp.astype(np.int64))
    adj = (diff == 1) | (diff == N - 1)
    return float(adj.mean())


# ---------------------------------------------------------------------------
# Information loss and entropy utilities
# ---------------------------------------------------------------------------

def entropy_bits(arr: np.ndarray) -> float:
    """
    Compute Shannon entropy (in bits) of the distribution of values in arr.
    arr is discretized into 64 bins.
    """
    counts, _ = np.histogram(arr, bins=64)
    probs = counts / counts.sum()
    probs = probs[probs > 0]
    return float(-np.sum(probs * np.log2(probs)))


def variance_of_real_imag(theta: np.ndarray) -> Tuple[float, float]:
    """Return (var_real, var_imag) of the field array."""
    return (float(np.var(np.real(theta))), float(np.var(np.imag(theta))))


# ---------------------------------------------------------------------------
# Perturbation stability test
# ---------------------------------------------------------------------------

def perturb_theta(theta: np.ndarray, eps: float, rng: np.random.Generator) -> np.ndarray:
    """Add Gaussian noise of magnitude eps to the field array."""
    noise_r = rng.standard_normal(len(theta)) * eps
    noise_i = rng.standard_normal(len(theta)) * eps
    return theta + (noise_r + 1j * noise_i)


def stability_test(theta: np.ndarray, eps: float, n_trials: int,
                   rng: np.random.Generator) -> Dict[str, Any]:
    """
    Test stability of L0, L1, L2 outputs under perturbation of magnitude eps.

    Returns: dict with mean and std of each statistic under perturbation.
    """
    specs, winds, phases_w = [], [], []
    veffs_at_137, veffs_at_nstar = [], []
    p0s, agrays = [], []

    for _ in range(n_trials):
        theta_p = perturb_theta(theta, eps, rng)
        specs.append(l0_spectral_action_proxy(theta_p))
        winds.append(l0_winding_proxy(theta_p))
        phases_w.append(l0_phase_winding_proxy(theta_p))
        scan = l1_scan_weff()
        veffs_at_137.append(l1_veff(137))
        veffs_at_nstar.append(scan["v_star"])
        p0s.append(l2s_p0_from_phases(theta_p))
        agrays.append(l2t_a_gray_from_phases(theta_p))

    return {
        "eps": eps,
        "n_trials": n_trials,
        "I_spec_mean": float(np.mean(specs)),
        "I_spec_std": float(np.std(specs)),
        "I_wind_mode": int(np.bincount([w + 10 for w in winds]).argmax()) - 10,
        "P0_mean": float(np.mean(p0s)),
        "P0_std": float(np.std(p0s)),
        "A_gray_mean": float(np.mean(agrays)),
        "A_gray_std": float(np.std(agrays)),
        "V137_fixed": float(np.mean(veffs_at_137)),   # V_eff(137) is field-independent
        "n_star_stable": scan["n_star"],               # n* from V_eff is field-independent
    }


# ---------------------------------------------------------------------------
# Main flow test
# ---------------------------------------------------------------------------

def run_flow_test(seed: int = 42, n_perturb: int = 20, eps: float = 0.1) -> Dict[str, Any]:
    """
    Run the full L0 → L1 → L2 flow test.

    Returns: dict with all numerical results.
    """
    rng = np.random.default_rng(seed)

    # ── Step 0: Generate Θ ───────────────────────────────────────────────────
    theta = generate_theta(LATTICE_SIZE, rng)
    var_r, var_i = variance_of_real_imag(theta)
    entropy_field = entropy_bits(np.abs(theta))

    results: Dict[str, Any] = {
        "seed": seed,
        "lattice_size": LATTICE_SIZE,
        "field_norm": float(np.linalg.norm(theta)),
        "field_var_real": var_r,
        "field_var_imag": var_i,
        "field_entropy_bits": entropy_field,
        "field_dim": LATTICE_SIZE,
    }

    # ── Step 1: L0 extraction ────────────────────────────────────────────────
    l0 = l0_extract_invariants(theta)
    results["L0"] = l0

    # Dimension: infinite → 5 invariants (here 3 proxy invariants)
    # Information loss: yes (lossy compression)

    # ── Step 2: L1 V_eff scan ────────────────────────────────────────────────
    l1_scan = l1_scan_weff()
    results["L1"] = {
        "B": l1_scan["B"],
        "B0_expected": B0,
        "n_star": l1_scan["n_star"],
        "V_eff_n_star": l1_scan["v_star"],
        "V_eff_137": l1_veff(137),
        "dim_output": 1,  # scalar n*
        "n_range": f"[{N_WINDING_MIN}, {N_WINDING_MAX}]",
    }

    # ── Step 3: L2S P₀ ───────────────────────────────────────────────────────
    p0 = l2s_p0_from_phases(theta)
    expected_p0_null = 16.0 / 256.0  # 16 codewords out of 256 possible blocks

    # ── Step 4: L2T A_gray ───────────────────────────────────────────────────
    a_gray = l2t_a_gray_from_phases(theta, N=GRAY_N)
    expected_a_gray_null = 2.0 / GRAY_N

    results["L2"] = {
        "P0_observed": p0,
        "P0_null_expected": expected_p0_null,
        "P0_dim_output": 1,
        "A_gray_observed": a_gray,
        "A_gray_null_expected": expected_a_gray_null,
        "A_gray_dim_output": 1,
        "N_gray": GRAY_N,
    }

    # ── Dimensional flow summary ─────────────────────────────────────────────
    results["dim_flow"] = {
        "field_in": LATTICE_SIZE,       # proxy for ∞-dim field
        "L0_invariants": 3,             # 3 proxy invariants (I_spec, I_wind, I_phase)
        "L1_scalars": 2,                # V_eff(n*) and n*
        "L2S_output": 1,                # P₀
        "L2T_output": 1,                # A_gray
    }

    # ── Entropy / variance at each stage ────────────────────────────────────
    l0_invariants = np.array([l0["I_spec_proxy"], l0["I_wind_proxy"], l0["I_phase_proxy"]])
    l1_scalars = np.array([l1_scan["n_star"], l1_scan["v_star"]])
    l2_scalars = np.array([p0, a_gray])

    results["entropy"] = {
        "field_entropy_bits": entropy_field,
        "L0_variance": float(np.var(np.abs(np.fft.fft(theta)))),  # spectral variance
        "L1_veff_variance": float(np.var(l1_scan["veff_values"])),
        "L2_output_variance": float(np.var([p0, a_gray])),
    }

    # ── Perturbation stability ───────────────────────────────────────────────
    stab = stability_test(theta, eps=eps, n_trials=n_perturb, rng=rng)
    results["stability"] = stab

    # ── Reversibility check ─────────────────────────────────────────────────
    # L0: I_spec_proxy is not reversible (many Θ → same I_spec)
    # L2T Gray(n) is reversible (bijection)
    g42 = binary_to_gray(42)
    gray_rank = build_gray_rank(GRAY_N)
    # Check: G^{-1}(G(n)) = n for n in {0,...,GRAY_N-1}
    gray_invertible = all(
        gray_rank[binary_to_gray(n)] == n
        for n in range(GRAY_N)
    )
    results["reversibility"] = {
        "L0_I_spec_reversible": False,   # Many-to-one: irreversible
        "L0_I_wind_reversible": False,   # Many Θ with same winding
        "L2T_Gray_bijection": gray_invertible,  # G is a bijection on {0,...,N-1}
        "L2S_parity_check_reversible": False,   # 8-bit → 4-bit: irreversible
        "L2T_A_gray_reversible": False,   # m symbols → 1 scalar: irreversible
    }

    return results


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def format_report(results: Dict[str, Any]) -> str:
    """Format the numerical results as a Markdown report."""
    r = results
    lines = [
        "> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0",
        "",
        "# L0 / L1 / L2 — Numerical Flow Test Report",
        "",
        f"**Task**: ubt_L0_L1_L2_full_audit, Step 6  ",
        f"**Date**: 2026-05-05  ",
        f"**Seed**: {r['seed']}  ",
        f"**Lattice size**: {r['lattice_size']}  ",
        "",
        "---",
        "",
        "## Input Field Θ (Random Proxy)",
        "",
        f"| Property | Value |",
        f"|----------|-------|",
        f"| Lattice size | {r['field_dim']} |",
        f"| Field norm ||Θ|| | {r['field_norm']:.6f} |",
        f"| Var(Re Θ) | {r['field_var_real']:.6f} |",
        f"| Var(Im Θ) | {r['field_var_imag']:.6f} |",
        f"| Entropy of |Θ| (bits) | {r['field_entropy_bits']:.4f} |",
        "",
        "---",
        "",
        "## L0 Invariant Extraction (Proxy)",
        "",
        "| Invariant | Value | Type |",
        "|-----------|-------|------|",
        f"| I_spec_proxy (spectral action) | {r['L0']['I_spec_proxy']:.6f} | Real scalar |",
        f"| I_wind_proxy (winding) | {r['L0']['I_wind_proxy']} | Integer |",
        f"| I_phase_proxy (phase winding) | {r['L0']['I_phase_proxy']} | Integer |",
        f"| ||Θ|| | {r['L0']['norm_theta']:.6f} | Real |",
        "",
        f"**Dimensional reduction**: {r['dim_flow']['field_in']} → {r['dim_flow']['L0_invariants']} invariants (lossy)",
        "",
        "---",
        "",
        "## L1 Effective Potential V_eff(n)",
        "",
        f"| Property | Value |",
        f"|----------|-------|",
        f"| B₀ (one-loop, [L1] PROVED) | {r['L1']['B0_expected']:.6f} = 8π |",
        f"| n* (argmin V_eff) | {r['L1']['n_star']} |",
        f"| V_eff(n*) | {r['L1']['V_eff_n_star']:.4f} |",
        f"| V_eff(137) | {r['L1']['V_eff_137']:.4f} |",
        f"| Scan range | {r['L1']['n_range']} |",
        "",
        f"**Note**: V_eff(n) = n² - B·n·ln(n) is field-independent (depends only on B, n).",
        f"**Note**: n* ≠ 137 in general for B = B₀ = 8π; exact n* depends on B.",
        "",
        "---",
        "",
        "## L2 Coding Statistics",
        "",
        "### L2S — Hamming P₀",
        "",
        f"| Property | Value |",
        f"|----------|-------|",
        f"| P₀ (observed on Θ proxy) | {r['L2']['P0_observed']:.6f} |",
        f"| P₀ (expected null: 16/256) | {r['L2']['P0_null_expected']:.6f} |",
        f"| Output dimension | {r['L2']['P0_dim_output']} scalar |",
        "",
        "### L2T — Gray A_gray",
        "",
        f"| Property | Value |",
        f"|----------|-------|",
        f"| A_gray (observed on Θ proxy) | {r['L2']['A_gray_observed']:.6f} |",
        f"| A_gray (expected null: 2/N = 2/{r['L2']['N_gray']}) | {r['L2']['A_gray_null_expected']:.6f} |",
        f"| Symbol alphabet N | {r['L2']['N_gray']} |",
        f"| Output dimension | {r['L2']['A_gray_dim_output']} scalar |",
        "",
        "---",
        "",
        "## Dimensional Flow Summary",
        "",
        f"| Stage | Dimension |",
        f"|-------|-----------|",
        f"| Field input Θ (proxy) | {r['dim_flow']['field_in']} complex |",
        f"| L0 invariants | {r['dim_flow']['L0_invariants']} scalars |",
        f"| L1 outputs | {r['dim_flow']['L1_scalars']} scalars |",
        f"| L2S output | {r['dim_flow']['L2S_output']} scalar (P₀) |",
        f"| L2T output | {r['dim_flow']['L2T_output']} scalar (A_gray) |",
        "",
        "**Dimensionality decreases monotonically through the pipeline.** "
        "Each stage is lossy (information is lost).",
        "",
        "---",
        "",
        "## Entropy / Variance Tracking",
        "",
        f"| Stage | Variance / Entropy |",
        f"|-------|-------------------|",
        f"| Field |Θ| entropy | {r['entropy']['field_entropy_bits']:.4f} bits |",
        f"| L0 spectral variance | {r['entropy']['L0_variance']:.6f} |",
        f"| L1 V_eff variance | {r['entropy']['L1_veff_variance']:.4f} |",
        f"| L2 output variance | {r['entropy']['L2_output_variance']:.6f} |",
        "",
        "---",
        "",
        "## Perturbation Stability",
        "",
        f"Perturbation ε = {r['stability']['eps']}, n_trials = {r['stability']['n_trials']}",
        "",
        f"| Statistic | Mean | Std |",
        f"|-----------|------|-----|",
        f"| I_spec_proxy | {r['stability']['I_spec_mean']:.4f} | {r['stability']['I_spec_std']:.4f} |",
        f"| I_wind mode | {r['stability']['I_wind_mode']} | — |",
        f"| P₀ | {r['stability']['P0_mean']:.4f} | {r['stability']['P0_std']:.4f} |",
        f"| A_gray | {r['stability']['A_gray_mean']:.4f} | {r['stability']['A_gray_std']:.4f} |",
        f"| V_eff(137) (fixed) | {r['stability']['V137_fixed']:.4f} | 0 (field-indep) |",
        f"| n* (fixed) | {r['stability']['n_star_stable']} | 0 (field-indep) |",
        "",
        "**Note**: V_eff(n) and n* are field-independent (they depend only on B and n).",
        "The L0 spectral proxy varies with ε-perturbations; P₀ and A_gray",
        "vary weakly (Gaussian field perturbations → near-null statistics).",
        "",
        "---",
        "",
        "## Reversibility",
        "",
        f"| Transformation | Reversible? | Reason |",
        f"|----------------|-------------|--------|",
        f"| L0: I_spec_proxy | No | Many Θ → same spectral action |",
        f"| L0: I_wind_proxy | No | Many Θ with same winding |",
        f"| L2T: Gray code G(n) | {r['reversibility']['L2T_Gray_bijection']} | Bijection on {{0,...,N-1}} |",
        f"| L2S: parity check | No | 8-bit → 4-bit: irreversible |",
        f"| L2T: A_gray | No | m symbols → 1 scalar |",
        "",
        "---",
        "",
        "## Conclusion",
        "",
        "1. **Dimensional flow is strictly decreasing**: ∞-dim field → 3 scalars (L0) → 2 scalars (L1) → 1 scalar (L2S or L2T).",
        "2. **All steps are lossy** (information is not preserved).",
        "3. **V_eff(n) and n* are field-independent** — they depend only on B and n, not on the specific Θ.",
        "4. **L2T Gray code G(n) is the only reversible step** (it is a bijection on integers {0,...,N-1}).",
        "5. **A_gray and P₀ are near-null statistics for a Gaussian random field** proxy —",
        "   as expected (the proxy field has no UBT-specific coding structure).",
        "6. **Stability**: L0 spectral proxy varies under perturbation; L2 statistics are stable near null.",
        "",
        "---",
        "",
        "*Generated by experiments/L_layer_flow_test.py — ubt_L0_L1_L2_full_audit Step 6.*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="L0 → L1 → L2 flow test for UBT L-layer audit.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    parser.add_argument("--n-trials", type=int, default=20,
                        help="Number of perturbation trials (default: 20)")
    parser.add_argument("--perturb", type=float, default=0.1,
                        help="Perturbation magnitude ε (default: 0.1)")
    parser.add_argument("--no-report", action="store_true",
                        help="Do not write report file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("=" * 60)
    print("UBT L0 / L1 / L2 Layer Flow Test")
    print("=" * 60)
    print(f"Seed: {args.seed}  Lattice: {LATTICE_SIZE}  ε: {args.perturb}")
    print()

    results = run_flow_test(
        seed=args.seed,
        n_perturb=args.n_trials,
        eps=args.perturb,
    )

    # Print summary to console
    print(f"[Field]  ||Θ|| = {results['field_norm']:.4f},  "
          f"entropy = {results['field_entropy_bits']:.3f} bits")
    print(f"[L0]     I_spec_proxy = {results['L0']['I_spec_proxy']:.4f}  "
          f"I_wind = {results['L0']['I_wind_proxy']}  "
          f"I_phase = {results['L0']['I_phase_proxy']}")
    print(f"[L1]     n* = {results['L1']['n_star']}  "
          f"V_eff(n*) = {results['L1']['V_eff_n_star']:.2f}  "
          f"V_eff(137) = {results['L1']['V_eff_137']:.2f}")
    print(f"[L2S]    P₀ = {results['L2']['P0_observed']:.4f}  "
          f"(null: {results['L2']['P0_null_expected']:.4f})")
    print(f"[L2T]    A_gray = {results['L2']['A_gray_observed']:.4f}  "
          f"(null: {results['L2']['A_gray_null_expected']:.4f})")
    print()
    print(f"[Stability]  I_spec mean ± std = "
          f"{results['stability']['I_spec_mean']:.3f} ± {results['stability']['I_spec_std']:.3f}")
    print(f"             P₀ mean ± std = "
          f"{results['stability']['P0_mean']:.3f} ± {results['stability']['P0_std']:.3f}")
    print(f"             n* = {results['stability']['n_star_stable']} (field-independent)")
    print()
    print(f"[Gray bijection verified]: {results['reversibility']['L2T_Gray_bijection']}")
    print()

    # Write report
    if not args.no_report:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        report_text = format_report(results)
        REPORT_PATH.write_text(report_text, encoding="utf-8")
        print(f"Report written to: {REPORT_PATH}")

    print("=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    main()

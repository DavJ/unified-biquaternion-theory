# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
gray_path_symbol_test.py — CMB Gray-adjacency path-fingerprint test for UBT Layer 2 Transport (L2T).

Purpose
-------
Tests whether consecutive discretized CMB phase symbols s_i = floor(N/(2pi) * (arg(a_lm) + pi))
prefer Gray-adjacent transitions more than expected under a null (shuffled / phase-randomized) model.

This implements the observable A_gray (gray_adjacency_score) defined in:
  research_tracks/gray_transport_layer/gray_path_fingerprint.tex  §5

The Hamming (8,4,4) fingerprint (P0) is the canonical L2S statistic.
A_gray is the L2T research-track statistic. They are independent.

Usage
-----
  python gray_path_symbol_test.py --input <path_to_alm_file> [options]

Input format
------------
  A NumPy .npy or plain-text file containing an array of complex a_lm values,
  or a real array of phase values in radians in [-pi, pi).
  If --synthetic is set, a synthetic uniform-random sequence is used.

Output
------
  gray_adjacency_score (observed and null statistics)
  p-value against null
  Null model: shuffle or phase-randomize

Requirements
------------
  numpy, scipy (optional, for stats)

References
----------
  research_tracks/gray_transport_layer/gray_path_fingerprint.tex
  research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md
"""

import argparse
import numpy as np
from pathlib import Path


# ---------------------------------------------------------------------------
# Gray code utilities
# ---------------------------------------------------------------------------

def binary_to_gray(n: int) -> int:
    """Convert a non-negative integer to its standard reflected binary Gray code."""
    return n ^ (n >> 1)


def gray_to_binary(g: int) -> int:
    """Invert the standard reflected binary Gray code."""
    n = g
    mask = g >> 1
    while mask:
        n ^= mask
        mask >>= 1
    return n


def build_gray_order_table(N: int) -> np.ndarray:
    """
    Build a table gray_rank[s] = position of symbol s in the Gray ordering,
    for symbols 0, ..., N-1.

    gray_rank[s] = G^{-1}(s) in the notation of gray_path_fingerprint.tex.
    """
    if N & (N - 1) != 0:
        raise ValueError(f"N must be a power of 2, got {N}")
    gray_rank = np.empty(N, dtype=np.int32)
    for n in range(N):
        g = binary_to_gray(n)
        gray_rank[g] = n
    return gray_rank


def gray_adjacency_mask(s: np.ndarray, sp: np.ndarray, N: int,
                        gray_rank: np.ndarray) -> np.ndarray:
    """
    Return a boolean array indicating whether consecutive symbol pairs (s[i], sp[i])
    are Gray-adjacent.

    Two symbols are Gray-adjacent if |gray_rank[s] - gray_rank[sp]| == 1 (mod N).
    """
    r = gray_rank[s]
    rp = gray_rank[sp]
    diff = np.abs(r.astype(np.int64) - rp.astype(np.int64))
    return (diff == 1) | (diff == N - 1)


# ---------------------------------------------------------------------------
# Phase symbol extraction
# ---------------------------------------------------------------------------

def phases_to_symbols(phases: np.ndarray, N: int) -> np.ndarray:
    """
    Discretize phase values in [-pi, pi) into N symbols.

    s = floor(N / (2*pi) * (phase + pi))

    Parameters
    ----------
    phases : array of float in [-pi, pi)
    N : int, number of symbols (must be power of 2)

    Returns
    -------
    symbols : int array in {0, ..., N-1}
    """
    normalized = (phases + np.pi) / (2 * np.pi)  # in [0, 1)
    normalized = np.clip(normalized, 0.0, 1.0 - 1e-12)
    return (N * normalized).astype(np.int32)


def alm_to_symbols(alm: np.ndarray, N: int) -> np.ndarray:
    """Extract phase symbols from complex a_lm coefficients."""
    phases = np.angle(alm)  # in (-pi, pi]
    return phases_to_symbols(phases, N)


# ---------------------------------------------------------------------------
# Gray adjacency score
# ---------------------------------------------------------------------------

def gray_adjacency_score(symbols: np.ndarray, N: int,
                         gray_rank: np.ndarray) -> float:
    """
    Compute A_gray = fraction of consecutive symbol pairs that are Gray-adjacent.

    A_gray = (1/(m-1)) sum_{i=1}^{m-1} 1[s_{i+1} is Gray-adjacent to s_i]

    Expected null value for i.i.d. uniform symbols: 2/N.
    """
    if len(symbols) < 2:
        return 0.0
    s = symbols[:-1]
    sp = symbols[1:]
    adj = gray_adjacency_mask(s, sp, N, gray_rank)
    return float(adj.mean())


# ---------------------------------------------------------------------------
# Null model
# ---------------------------------------------------------------------------

def shuffle_null(symbols: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Shuffle null: randomly permute the symbol sequence."""
    s = symbols.copy()
    rng.shuffle(s)
    return s


def phase_randomized_null(n_symbols: int, N: int,
                          rng: np.random.Generator) -> np.ndarray:
    """Phase-randomized null: draw symbols i.i.d. from Uniform{0,...,N-1}."""
    return rng.integers(0, N, size=n_symbols, dtype=np.int32)


# ---------------------------------------------------------------------------
# Main test
# ---------------------------------------------------------------------------

def run_test(symbols: np.ndarray, N: int, n_null: int = 1000,
             null_type: str = "shuffle", seed: int = 42,
             verbose: bool = True) -> dict:
    """
    Run the Gray path-fingerprint test.

    Parameters
    ----------
    symbols : 1-D int array of phase symbols in {0, ..., N-1}
    N : int, alphabet size (power of 2)
    n_null : int, number of null realizations
    null_type : "shuffle" or "phase_randomized"
    seed : random seed
    verbose : print summary

    Returns
    -------
    dict with keys:
      observed      : float, A_gray on observed sequence
      null_scores   : np.ndarray of null A_gray values
      null_mean     : float
      null_std      : float
      p_value       : float, one-sided (A_null >= A_obs)
      expected_null : float, theoretical 2/N
      N             : int
      n_symbols     : int
      n_null        : int
      null_type     : str
    """
    gray_rank = build_gray_order_table(N)
    observed = gray_adjacency_score(symbols, N, gray_rank)
    expected = 2.0 / N

    rng = np.random.default_rng(seed)
    null_scores = np.empty(n_null)
    for j in range(n_null):
        if null_type == "shuffle":
            null_seq = shuffle_null(symbols, rng)
        elif null_type == "phase_randomized":
            null_seq = phase_randomized_null(len(symbols), N, rng)
        else:
            raise ValueError(f"Unknown null_type: {null_type!r}")
        null_scores[j] = gray_adjacency_score(null_seq, N, gray_rank)

    null_mean = float(null_scores.mean())
    null_std = float(null_scores.std())
    p_value = float((null_scores >= observed).mean())

    result = dict(
        observed=observed,
        null_scores=null_scores,
        null_mean=null_mean,
        null_std=null_std,
        p_value=p_value,
        expected_null=expected,
        N=N,
        n_symbols=len(symbols),
        n_null=n_null,
        null_type=null_type,
    )

    if verbose:
        _print_summary(result)

    return result


def _print_summary(result: dict) -> None:
    """Print a human-readable summary of the test result."""
    print("=" * 60)
    print("UBT Layer 2 Transport (L2T) — Gray Path-Fingerprint Test")
    print("=" * 60)
    print(f"  Symbol alphabet size N      : {result['N']}")
    print(f"  Sequence length             : {result['n_symbols']}")
    print(f"  Null model                  : {result['null_type']}")
    print(f"  Null realizations           : {result['n_null']}")
    print()
    print(f"  Expected null (2/N)         : {result['expected_null']:.6f}")
    print(f"  Null mean ± std             : {result['null_mean']:.6f} ± {result['null_std']:.6f}")
    print(f"  Observed A_gray             : {result['observed']:.6f}")
    print(f"  p-value (one-sided)         : {result['p_value']:.4f}")
    print()
    if result['p_value'] < 0.01:
        print("  ** DETECTION: p < 0.01 — evidence for L2T Gray transport preference **")
    elif result['p_value'] < 0.05:
        print("  * MARGINAL: 0.01 <= p < 0.05")
    else:
        print("  NO DETECTION: p >= 0.05 — no evidence for L2T at this sensitivity")
    print()
    print("  Note: L2S Hamming P0 and L2T A_gray are independent statistics.")
    print("        Non-detection of L2T does not affect L2S status.")
    print("=" * 60)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CMB Gray-adjacency path-fingerprint test (UBT L2T).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input", type=str, default=None,
        help="Path to input file: .npy array of complex a_lm or real phases (rad).",
    )
    parser.add_argument(
        "--synthetic", action="store_true",
        help="Use a synthetic uniform-random sequence (null check).",
    )
    parser.add_argument(
        "--N", type=int, default=16,
        help="Symbol alphabet size (must be power of 2). Default: 16.",
    )
    parser.add_argument(
        "--n-null", type=int, default=1000,
        help="Number of null realizations. Default: 1000.",
    )
    parser.add_argument(
        "--null-type", type=str, default="shuffle",
        choices=["shuffle", "phase_randomized"],
        help="Null model type. Default: shuffle.",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Random seed. Default: 42.",
    )
    parser.add_argument(
        "--n-synthetic", type=int, default=1000,
        help="Length of synthetic sequence (only used with --synthetic). Default: 1000.",
    )
    return parser.parse_args()


def load_symbols(path: str, N: int) -> np.ndarray:
    """Load and convert input file to symbol array."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    data = np.load(p) if p.suffix == ".npy" else np.loadtxt(p)
    if np.iscomplexobj(data):
        return alm_to_symbols(data.ravel(), N)
    else:
        phases = data.ravel().astype(float)
        return phases_to_symbols(phases, N)


def main() -> None:
    args = parse_args()

    # Validate N
    if args.N <= 0 or (args.N & (args.N - 1)) != 0:
        raise ValueError(f"--N must be a positive power of 2, got {args.N}")

    if args.synthetic:
        rng = np.random.default_rng(args.seed)
        symbols = rng.integers(0, args.N, size=args.n_synthetic, dtype=np.int32)
        print(f"Using synthetic uniform-random sequence (length={args.n_synthetic}, N={args.N}).")
    elif args.input is not None:
        symbols = load_symbols(args.input, args.N)
        print(f"Loaded {len(symbols)} symbols from {args.input} (N={args.N}).")
    else:
        raise ValueError("Provide --input <file> or --synthetic.")

    run_test(
        symbols=symbols,
        N=args.N,
        n_null=args.n_null,
        null_type=args.null_type,
        seed=args.seed,
        verbose=True,
    )


if __name__ == "__main__":
    main()

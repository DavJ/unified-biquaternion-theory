#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
factorial_degeneracy.py — Test the factorial-degeneracy hypothesis for the p·ln(p) term.

PURPOSE
-------
Verify whether factorial-like degeneracy explains the p·ln(p) entropy term in the
UBT effective potential, by comparing the free-energy landscape

    F(n) = E(n) − S(n) = n² − S(n)

for four entropy variants:

    Variant 1 (exact factorial)   : S(n) = ln(n!)
    Variant 2 (Stirling leading)  : S(n) = n·ln(n)
    Variant 3 (Stirling first)    : S(n) = n·ln(n) − n
    Variant 4 (parameterised)     : S(n) = n·ln(n) + c·n   (c ∈ ℝ)

For each variant the script:
  1. Computes F(n) and its discrete differences ΔF(n) = F(n+1) − F(n).
  2. Finds local minima of F(n) (where F(n) < F(n−1) and F(n) < F(n+1)).
  3. Finds the global ΔF minimum (region of slowest growth).
  4. Compares minima with the stable-prime set {127, 137, 139, 151, 157}.
  5. For Variant 4, sweeps c over a range and reports which c values produce
     a local F-minimum inside the stable-prime window — the robustness test.

PHYSICAL CONTEXT
----------------
The UBT vacuum-stability potential (vacuum_stability.tex) contains an entropy
term of the form B·n·ln(n).  The question is whether this term arises naturally
from counting multiplicities (degeneracy) of biquaternionic ψ-sector modes:

  • ln(n!)  is the exact log-multiplicity if each mode label is a permutation.
  • n·ln(n) is the leading Stirling approximation.
  • n·ln(n) − n  is the standard Stirling first approximation.
  • n·ln(n) + c·n allows a linear offset arising from, e.g., Casimir-type shifts.

ROBUSTNESS CRITERION
--------------------
For Variant 4 the minimum of F is a local minimum at n* satisfying
    ΔF(n*−1) < 0  and  ΔF(n*) ≥ 0,
which (in the continuous limit) corresponds to
    c = 2·n* − ln(n*) − 1.

We say the hypothesis is *robust* if a contiguous interval of c-values
produces minima within the stable-prime window [127, 157].

USAGE
-----
    python tools/factorial_degeneracy.py
    python tools/factorial_degeneracy.py --n-max 300 --verbose

EXIT CODES
----------
    0  — at least one variant produces a minimum overlapping the stable-prime set
    1  — no variant overlaps the stable-prime set
"""

from __future__ import annotations

import argparse
import math
import sys
from typing import Callable, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Stable-prime reference set (ψ-sector attractors, vacuum_stability.tex)
# ---------------------------------------------------------------------------

STABLE_PRIMES: List[int] = [127, 137, 139, 151, 157]

# Tolerance window (±) for overlap check
OVERLAP_TOLERANCE: int = 10

# Default c-sweep range for Variant 4
C_SWEEP_MIN: float = 240.0
C_SWEEP_MAX: float = 320.0
C_SWEEP_STEP: float = 1.0

# ---------------------------------------------------------------------------
# Energy
# ---------------------------------------------------------------------------


def energy(n: int) -> float:
    """E(n) = n²  — mode kinetic energy in the ψ-sector spectrum."""
    return float(n * n)


# ---------------------------------------------------------------------------
# Entropy variants
# ---------------------------------------------------------------------------


def entropy_factorial(n: int) -> float:
    """S₁(n) = ln(n!)  — exact log-factorial degeneracy.

    Uses math.lgamma(n+1) = ln(Γ(n+1)) = ln(n!) for integer n ≥ 1.
    """
    if n < 1:
        raise ValueError(f"entropy_factorial requires n ≥ 1, got {n}")
    return math.lgamma(n + 1)


def entropy_stirling_leading(n: float) -> float:
    """S₂(n) = n·ln(n)  — leading Stirling approximation."""
    if n <= 0:
        raise ValueError(f"entropy_stirling_leading requires n > 0, got {n}")
    return n * math.log(n)


def entropy_stirling_first(n: float) -> float:
    """S₃(n) = n·ln(n) − n  — first Stirling approximation."""
    if n <= 0:
        raise ValueError(f"entropy_stirling_first requires n > 0, got {n}")
    return n * math.log(n) - n


def entropy_stirling_linear(n: float, c: float) -> float:
    """S₄(n, c) = n·ln(n) + c·n  — parameterised Stirling variant."""
    if n <= 0:
        raise ValueError(f"entropy_stirling_linear requires n > 0, got {n}")
    return n * math.log(n) + c * n


# ---------------------------------------------------------------------------
# Free-energy and discrete differences (generic)
# ---------------------------------------------------------------------------


def free_energy_fn(
    n: int,
    entropy_func: Callable[[int], float],
) -> float:
    """F(n) = E(n) − S(n) for a given entropy function."""
    return energy(n) - entropy_func(n)


def delta_free_energy_fn(
    n: int,
    entropy_func: Callable[[int], float],
) -> float:
    """ΔF(n) = F(n+1) − F(n) for a given entropy function."""
    return free_energy_fn(n + 1, entropy_func) - free_energy_fn(n, entropy_func)


# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------


def find_f_local_minima(
    entropy_func: Callable[[int], float],
    n_min: int,
    n_max: int,
) -> List[int]:
    """
    Find discrete local minima of F(n) = n² − S(n) in [n_min, n_max].

    A point n is a local minimum if F(n) < F(n−1) and F(n) < F(n+1).
    """
    minima: List[int] = []
    for n in range(n_min + 1, n_max):
        f_prev = free_energy_fn(n - 1, entropy_func)
        f_curr = free_energy_fn(n, entropy_func)
        f_next = free_energy_fn(n + 1, entropy_func)
        if f_curr < f_prev and f_curr < f_next:
            minima.append(n)
    return minima


def find_df_global_min(
    entropy_func: Callable[[int], float],
    n_min: int,
    n_max: int,
) -> Tuple[int, float]:
    """Return (n, ΔF(n)) for the global minimum of ΔF over [n_min, n_max)."""
    best_n = n_min
    best_val = delta_free_energy_fn(n_min, entropy_func)
    for n in range(n_min + 1, n_max):
        val = delta_free_energy_fn(n, entropy_func)
        if val < best_val:
            best_val = val
            best_n = n
    return best_n, best_val


def nearest_stable_prime(n: int) -> Tuple[int, int]:
    """Return (nearest_prime, |distance|) for the nearest stable prime to n."""
    nearest = min(STABLE_PRIMES, key=lambda p: abs(p - n))
    return nearest, abs(nearest - n)


def overlaps_stable_primes(candidates: List[int], tol: int = OVERLAP_TOLERANCE) -> bool:
    """True if any candidate is within tol of a stable prime."""
    return any(
        abs(c - p) <= tol
        for c in candidates
        for p in STABLE_PRIMES
    )


# ---------------------------------------------------------------------------
# Variant 4: c-sweep robustness
# ---------------------------------------------------------------------------


def c_value_for_minimum_at(n: int) -> float:
    """
    Return the c value that places the continuous F-minimum exactly at n.

    Continuous condition: F'(x) = 2x − ln(x) − 1 − c = 0
        → c = 2n − ln(n) − 1
    """
    return 2.0 * n - math.log(n) - 1.0


def sweep_c_for_stable_prime_minima(
    n_min: int,
    n_max: int,
    c_min: float = C_SWEEP_MIN,
    c_max: float = C_SWEEP_MAX,
    c_step: float = C_SWEEP_STEP,
) -> List[Tuple[float, int]]:
    """
    Sweep c and find (c, n_min*) pairs where the F-minimum for
    S(n) = n·ln(n) + c·n lands inside [n_min, n_max].

    Returns a list of (c, n*) where n* is the discrete F-minimum.
    """
    results: List[Tuple[float, int]] = []
    c = c_min
    while c <= c_max + 1e-9:
        entropy_func = lambda n, _c=c: entropy_stirling_linear(n, _c)
        minima = find_f_local_minima(entropy_func, n_min, n_max)
        for m in minima:
            results.append((round(c, 6), m))
        c += c_step
    return results


# ---------------------------------------------------------------------------
# Per-variant analysis
# ---------------------------------------------------------------------------

VARIANT_NAMES = {
    "factorial": "S(n) = ln(n!)             [exact factorial]",
    "stirling_leading": "S(n) = n·ln(n)            [Stirling leading]",
    "stirling_first": "S(n) = n·ln(n) − n        [Stirling first]",
    "stirling_linear": "S(n) = n·ln(n) + c·n      [parameterised, c given]",
}


def analyse_variant(
    name: str,
    entropy_func: Callable[[int], float],
    n_min: int,
    n_max: int,
    verbose: bool = False,
) -> Dict:
    """Run the full analysis for one entropy variant."""
    f_minima = find_f_local_minima(entropy_func, n_min, n_max)
    df_min_n, df_min_val = find_df_global_min(entropy_func, n_min, n_max)
    f_at_primes = {p: free_energy_fn(p, entropy_func) for p in STABLE_PRIMES}
    df_at_primes = {p: delta_free_energy_fn(p, entropy_func) for p in STABLE_PRIMES}

    # Overlap: check F-minima OR global ΔF-minimum
    all_candidates = list(f_minima) + [df_min_n]
    overlap = overlaps_stable_primes(all_candidates)

    if verbose:
        print(f"\n  Variant: {VARIANT_NAMES.get(name, name)}")
        print(f"  F(n) local minima in [{n_min}, {n_max}]: "
              f"{f_minima if f_minima else 'none (F strictly increasing)'}")
        print(f"  Global ΔF minimum: n = {df_min_n}  (ΔF = {df_min_val:.4f})")
        nearest, dist = nearest_stable_prime(df_min_n)
        print(f"    → nearest stable prime: {nearest}  (distance {dist})")
        print(f"  Overlap with stable-prime set (±{OVERLAP_TOLERANCE}): "
              f"{'YES ✓' if overlap else 'NO ✗'}")
        print()
        print(f"  {'n':>5}  {'F(n)':>16}  {'ΔF(n)':>12}")
        print("  " + "-" * 38)
        for p in STABLE_PRIMES:
            print(f"  {p:>5}  {f_at_primes[p]:>16.4f}  {df_at_primes[p]:>12.4f}")

    return {
        "name": name,
        "f_minima": f_minima,
        "df_global_min_n": df_min_n,
        "df_global_min_val": df_min_val,
        "f_at_stable_primes": f_at_primes,
        "df_at_stable_primes": df_at_primes,
        "overlap_found": overlap,
    }


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_analysis(
    n_min: int = 2,
    n_max: int = 300,
    c_fixed: float = 269.0,
    verbose: bool = False,
) -> Dict:
    """
    Run the factorial-degeneracy hypothesis test for all four variants.

    Parameters
    ----------
    n_min : int
        Lower bound of the scan range.
    n_max : int
        Upper bound of the scan range (inclusive for F values).
    c_fixed : float
        Fixed c value used for Variant 4 (in addition to the sweep).
    verbose : bool
        Print detailed tables.

    Returns
    -------
    dict with keys:
        'variant_factorial'        : results dict for ln(n!) variant
        'variant_stirling_leading' : results dict for n·ln(n) variant
        'variant_stirling_first'   : results dict for n·ln(n)−n variant
        'variant_stirling_linear'  : results dict for n·ln(n)+c·n (c_fixed)
        'c_sweep_results'          : list of (c, n*) from robustness sweep
        'c_values_near_primes'     : subset of sweep results where n* ∈ STABLE_PRIMES
        'robust_c_range'           : (c_min, c_max) of contiguous c-interval with n*∈ primes
        'any_overlap'              : bool — any variant overlaps stable-prime set
    """
    if verbose:
        print("=" * 65)
        print("Factorial Degeneracy Hypothesis — Free-Energy Variants")
        print("=" * 65)
        print(f"  Scan range    : n ∈ [{n_min}, {n_max}]")
        print(f"  E(n)          = n²")
        print(f"  Stable primes : {STABLE_PRIMES}")
        print(f"  Overlap tol.  : ±{OVERLAP_TOLERANCE}")

    # --- Four entropy variants ---
    v1 = analyse_variant(
        "factorial",
        entropy_factorial,
        n_min, n_max, verbose,
    )
    v2 = analyse_variant(
        "stirling_leading",
        entropy_stirling_leading,
        n_min, n_max, verbose,
    )
    v3 = analyse_variant(
        "stirling_first",
        entropy_stirling_first,
        n_min, n_max, verbose,
    )
    entropy_linear_fixed = lambda n: entropy_stirling_linear(n, c_fixed)
    v4 = analyse_variant(
        "stirling_linear",
        entropy_linear_fixed,
        n_min, n_max, verbose,
    )

    # --- Variant 4 robustness: c-sweep ---
    sweep = sweep_c_for_stable_prime_minima(n_min, n_max)
    c_at_primes = [
        (c, m) for c, m in sweep if m in STABLE_PRIMES
    ]

    # Contiguous c-interval whose minima land on a stable prime
    c_vals_hitting = sorted({c for c, m in c_at_primes})
    if c_vals_hitting:
        robust_range: Optional[Tuple[float, float]] = (
            min(c_vals_hitting), max(c_vals_hitting)
        )
    else:
        robust_range = None

    if verbose:
        print()
        print("-" * 65)
        print("Variant 4 robustness: c-sweep")
        print(f"  c ∈ [{C_SWEEP_MIN}, {C_SWEEP_MAX}], step = {C_SWEEP_STEP}")
        print()
        # Show theoretical c for each stable prime
        print(f"  {'prime p':>8}  {'c*(p) = 2p−ln(p)−1':>22}")
        print("  " + "-" * 34)
        for p in STABLE_PRIMES:
            print(f"  {p:>8}  {c_value_for_minimum_at(p):>22.4f}")
        print()
        if c_at_primes:
            print(f"  c values producing F-minimum on a stable prime:")
            for c_v, m in sorted(c_at_primes):
                print(f"    c = {c_v:7.2f}  →  n* = {m}")
        else:
            print("  No discrete F-minimum lands exactly on a stable prime in sweep.")
        if robust_range:
            width = robust_range[1] - robust_range[0]
            print(f"\n  Robust c-interval: [{robust_range[0]:.2f}, {robust_range[1]:.2f}]"
                  f"  (width = {width:.2f})")
        print()
        print("-" * 65)
        print("SUMMARY")
        print("-" * 65)
        for v in [v1, v2, v3, v4]:
            tag = "✓ SUPPORTED" if v["overlap_found"] else "✗ no overlap"
            print(f"  {VARIANT_NAMES.get(v['name'], v['name'])[:44]:<44}  {tag}")
        if robust_range:
            print(f"\n  Variant 4 robust c-range: [{robust_range[0]:.1f}, {robust_range[1]:.1f}]"
                  f"  ← discrete minima land on stable primes")
        print("=" * 65)

    any_overlap = any(v["overlap_found"] for v in [v1, v2, v3, v4])

    return {
        "variant_factorial": v1,
        "variant_stirling_leading": v2,
        "variant_stirling_first": v3,
        "variant_stirling_linear": v4,
        "c_sweep_results": sweep,
        "c_values_near_primes": c_at_primes,
        "robust_c_range": robust_range,
        "any_overlap": any_overlap,
    }


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Test the factorial-degeneracy hypothesis: F(n) = n² − S(n)."
    )
    parser.add_argument(
        "--n-min", type=int, default=2,
        help="Lower bound of integer scan range (default: 2)",
    )
    parser.add_argument(
        "--n-max", type=int, default=300,
        help="Upper bound of integer scan range (default: 300)",
    )
    parser.add_argument(
        "--c", type=float, default=269.0,
        help="Fixed c value for Variant 4 S(n)=n·ln(n)+c·n (default: 269.0)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Verbose output with tables",
    )
    args = parser.parse_args()

    results = run_analysis(
        n_min=args.n_min,
        n_max=args.n_max,
        c_fixed=args.c,
        verbose=args.verbose,
    )

    if not args.verbose:
        for key in ["variant_factorial", "variant_stirling_leading",
                    "variant_stirling_first", "variant_stirling_linear"]:
            v = results[key]
            tag = "SUPPORTED" if v["overlap_found"] else "no overlap"
            print(f"{VARIANT_NAMES.get(v['name'], v['name']):<46}  [{tag}]")
            if v["f_minima"]:
                print(f"  F-minima: {v['f_minima']}")
            print(f"  Global ΔF min at n = {v['df_global_min_n']}  "
                  f"(ΔF = {v['df_global_min_val']:.4f})")
        rc = results["robust_c_range"]
        if rc:
            print(f"\nVariant-4 robust c-range: [{rc[0]:.1f}, {rc[1]:.1f}]  "
                  f"(minima land on stable primes)")
        else:
            print("\nVariant-4 robust c-range: none found in sweep")

    return 0 if results["any_overlap"] else 1


if __name__ == "__main__":
    sys.exit(main())

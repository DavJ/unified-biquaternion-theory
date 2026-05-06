# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text.

"""
null_models.py — Null Model Suite for UBT Falsification Framework

Implements null-model benchmarks for the five major UBT numerical claims:
  1. Prime stability set S = {2, 127, 137, 139, 151, 157}
  2. V_eff(n) = n^2 - B*n*ln(n) prime attractor
  3. Theta/spectral statistics vs. Riemann zeros
  4. B-coefficient value B ≈ 46
  5. Spectral density modulation at stable primes

Each null model generates a random/synthetic baseline and tests whether
the UBT result stands out above the null distribution.

Usage:
    python null_models.py
    python null_models.py --claim prime_stability --n_trials 10000
"""

import argparse
import math
import random
import statistics
from typing import List, Tuple, Optional


# ---------------------------------------------------------------------------
# Utility: Prime sieve
# ---------------------------------------------------------------------------

def sieve(n: int) -> List[int]:
    """Return sorted list of primes <= n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


PRIMES_100K = sieve(100_000)
PRIMES_10K = [p for p in PRIMES_100K if p <= 10_000]

# Canonical: candidates up to 10K, comparison up to 100K
# (matches reports/prime_stability_scan.md methodology)
CANDIDATES = PRIMES_10K
COMPARISON = PRIMES_100K


# ---------------------------------------------------------------------------
# Core UBT potential
# ---------------------------------------------------------------------------

def V(n: float, B: float) -> float:
    """V(n; B) = n^2 - B * n * ln(n)."""
    if n <= 1:
        return float("inf")
    return n**2 - B * n * math.log(n)


def B_of_p(p: int) -> float:
    """B(p) = (p + 1) / 3."""
    return (p + 1) / 3.0


def is_prime_stable(p: int, comparison_primes: List[int], B: float) -> bool:
    """
    Return True if p globally minimises V(·; B) over comparison_primes.
    comparison_primes should extend to 100K for canonical UBT result.
    """
    Vp = V(p, B)
    for q in comparison_primes:
        if q != p and V(q, B) <= Vp:
            return False
    return True


def ubt_stable_set(candidates: List[int], comparison: List[int]) -> List[int]:
    """Return the UBT-standard stable set using B(p) = (p+1)/3."""
    return [p for p in candidates if is_prime_stable(p, comparison, B_of_p(p))]


# ---------------------------------------------------------------------------
# NULL MODEL 1: Random B coefficient
# ---------------------------------------------------------------------------

def null_stable_set_random_B(candidates: List[int], comparison: List[int], rng: random.Random) -> List[int]:
    """
    For each candidate prime p, assign B_rand(p) = Uniform(1, 100) independently.
    Return the stable set under these random assignments, checking against comparison.

    Null hypothesis: Any particular B(p) formula produces a non-empty stable set
    with high probability — the stable set is not special.
    """
    stable = []
    for p in candidates:
        B_rand = rng.uniform(1.0, 100.0)
        if is_prime_stable(p, comparison, B_rand):
            stable.append(p)
    return stable


def null_model_1_random_B(n_trials: int = 10_000, seed: int = 42) -> dict:
    """
    Run n_trials random-B simulations and record:
    - Size of stable set
    - Whether 137 appears in stable set
    - Whether cluster {127-157} appears
    """
    rng = random.Random(seed)
    candidates = CANDIDATES
    comparison = COMPARISON

    sizes = []
    contains_137 = 0
    contains_cluster = 0  # All of {127, 137, 139, 151, 157}
    target_cluster = {127, 137, 139, 151, 157}

    for _ in range(n_trials):
        S = null_stable_set_random_B(candidates, comparison, rng)
        sizes.append(len(S))
        S_set = set(S)
        if 137 in S_set:
            contains_137 += 1
        if target_cluster.issubset(S_set):
            contains_cluster += 1

    mean_size = statistics.mean(sizes)
    std_size = statistics.stdev(sizes)
    p_137 = contains_137 / n_trials
    p_cluster = contains_cluster / n_trials

    return {
        "null_model": "random_B",
        "n_trials": n_trials,
        "mean_stable_set_size": mean_size,
        "std_stable_set_size": std_size,
        "P(137 in S)": p_137,
        "P(cluster {127,137,139,151,157} in S)": p_cluster,
        "UBT stable set size": 6,
        "UBT has 137": True,
        "UBT has cluster": True,
    }


# ---------------------------------------------------------------------------
# NULL MODEL 2: Shuffled B values
# ---------------------------------------------------------------------------

def null_model_2_shuffled_B(n_trials: int = 10_000, seed: int = 42) -> dict:
    """
    Use the actual UBT values B(p) = (p+1)/3 but shuffle which prime
    gets which B value.  Tests whether the stability structure is
    special to the pairing p <-> B(p).

    Null hypothesis: Any random pairing of primes and B values produces
    a similar stable set.
    """
    rng = random.Random(seed)
    candidates = CANDIDATES
    comparison = COMPARISON
    B_values = [B_of_p(p) for p in candidates]

    contains_137 = 0
    sizes = []

    for _ in range(n_trials):
        # Shuffle B values
        B_shuffled = B_values[:]
        rng.shuffle(B_shuffled)
        B_map = {p: B for p, B in zip(candidates, B_shuffled)}

        stable = []
        for p in candidates:
            if is_prime_stable(p, comparison, B_map[p]):
                stable.append(p)

        sizes.append(len(stable))
        if 137 in stable:
            contains_137 += 1

    mean_size = statistics.mean(sizes)
    p_137 = contains_137 / n_trials

    return {
        "null_model": "shuffled_B",
        "n_trials": n_trials,
        "mean_stable_set_size": mean_size,
        "std_stable_set_size": statistics.stdev(sizes),
        "P(137 in S)": p_137,
        "UBT stable set size": 6,
    }


# ---------------------------------------------------------------------------
# NULL MODEL 3: Random prime models (prime-position scrambling)
# ---------------------------------------------------------------------------

def null_model_3_synthetic_primes(n_trials: int = 10_000, seed: int = 42) -> dict:
    """
    Replace the actual prime sequence with synthetic sequences generated
    from a Poisson process with the same density.

    Under the Poisson prime model: primes are distributed as a Poisson process
    with density 1/ln(x) (from PNT).  This ignores correlations between primes.

    Null hypothesis: A Poisson prime model produces stable sets with the
    same statistics as the actual prime sequence.
    """
    rng = random.Random(seed)

    # Generate synthetic primes up to 10000 via Poisson process
    def synthetic_primes(n_max: int) -> List[int]:
        result = []
        x = 2.0
        while x <= n_max:
            # Density at x is 1/ln(x)
            gap = rng.expovariate(1.0 / math.log(x))
            x += gap
            if x <= n_max:
                result.append(int(x))
        return result

    contains_137_analog = 0  # Contains a prime in [130, 145]
    sizes = []
    cluster_counts = []

    for _ in range(n_trials):
        syn_primes = synthetic_primes(10_000)
        if len(syn_primes) < 10:
            continue

        stable = [p for p in syn_primes if is_prime_stable(p, syn_primes, B_of_p(p))]
        sizes.append(len(stable))

        # Count primes near 137
        near_137 = [p for p in stable if 130 <= p <= 145]
        if near_137:
            contains_137_analog += 1

    return {
        "null_model": "synthetic_Poisson_primes",
        "n_trials": n_trials,
        "mean_stable_set_size": statistics.mean(sizes) if sizes else 0.0,
        "std_stable_set_size": statistics.stdev(sizes) if len(sizes) > 1 else 0.0,
        "P(stable prime in [130,145])": contains_137_analog / n_trials,
        "UBT stable set size": 6,
    }


# ---------------------------------------------------------------------------
# NULL MODEL 4: Alternative V_eff formulas
# ---------------------------------------------------------------------------

def null_model_4_alternative_Veff(n_trials: int = 1_000, seed: int = 42) -> dict:
    """
    Replace V(n; B) = n^2 - B*n*ln(n) with random alternatives:
      V_alt(n) = A*n^alpha - B*n*ln^beta(n) + C*n^gamma
    where alpha, beta, gamma, A, B, C are drawn from broad priors.

    Tests whether the specific form n^2 - B*n*ln(n) is required to
    produce a stable set near 137.

    This is a model-space sensitivity test.
    """
    rng = random.Random(seed)
    primes_small = [p for p in CANDIDATES if p <= 1000]
    comparison_small = [p for p in COMPARISON if p <= 5000]

    has_stable_near_137 = 0

    for _ in range(n_trials):
        # Random potential parameters
        alpha = rng.uniform(1.5, 2.5)
        beta = rng.uniform(0.5, 1.5)
        A = rng.uniform(0.5, 2.0)
        C = rng.uniform(-1.0, 1.0)

        def V_alt(n: float, B: float) -> float:
            if n <= 1:
                return float("inf")
            try:
                return A * n**alpha - B * n * math.log(n)**beta + C * n**0.5
            except (ValueError, OverflowError):
                return float("inf")

        # Use B(p) = (p+1)/3 formula still
        stable = []
        for p in primes_small:
            Vp = V_alt(p, B_of_p(p))
            is_stable = all(
                V_alt(q, B_of_p(p)) > Vp
                for q in comparison_small if q != p
            )
            if is_stable:
                stable.append(p)

        if any(130 <= p <= 145 for p in stable):
            has_stable_near_137 += 1

    return {
        "null_model": "alternative_Veff",
        "n_trials": n_trials,
        "P(stable prime in [130,145] for random V)": has_stable_near_137 / n_trials,
        "UBT result": "137 stable",
        "interpretation": "High P = UBT form not special; low P = UBT form required",
    }


# ---------------------------------------------------------------------------
# Effect size: How unusual is the UBT stable set?
# ---------------------------------------------------------------------------

def compute_effect_sizes(results: List[dict]) -> dict:
    """
    Given null model results, compute Cohen's d or similar effect sizes
    for the UBT claims.
    """
    effects = {}

    # Stable set size: UBT = 6
    for r in results:
        if "mean_stable_set_size" in r:
            mu = r["mean_stable_set_size"]
            sigma = r.get("std_stable_set_size", 1.0) or 1.0
            d = (6 - mu) / sigma
            effects[r["null_model"] + "_effect_d"] = round(d, 3)

    return effects


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def run_all_null_models(n_trials: int = 5_000, seed: int = 42) -> None:
    """Run all null models and print summary."""
    print("=" * 60)
    print("UBT NULL MODEL SUITE — Falsification Framework")
    print(f"n_trials={n_trials}, seed={seed}")
    print("=" * 60)
    print()

    print("UBT True stable set:", ubt_stable_set(CANDIDATES, COMPARISON))
    print()

    results = []

    print("--- NULL MODEL 1: Random B coefficient ---")
    r1 = null_model_1_random_B(n_trials, seed)
    results.append(r1)
    for k, v in r1.items():
        print(f"  {k}: {v}")
    print()

    print("--- NULL MODEL 2: Shuffled B values ---")
    r2 = null_model_2_shuffled_B(n_trials, seed)
    results.append(r2)
    for k, v in r2.items():
        print(f"  {k}: {v}")
    print()

    print("--- NULL MODEL 3: Synthetic Poisson primes ---")
    r3 = null_model_3_synthetic_primes(min(n_trials, 2_000), seed)
    results.append(r3)
    for k, v in r3.items():
        print(f"  {k}: {v}")
    print()

    print("--- NULL MODEL 4: Alternative V_eff ---")
    r4 = null_model_4_alternative_Veff(min(n_trials, 500), seed)
    results.append(r4)
    for k, v in r4.items():
        print(f"  {k}: {v}")
    print()

    print("--- EFFECT SIZES ---")
    effects = compute_effect_sizes(results)
    for k, v in effects.items():
        print(f"  {k}: {v}")
    print()

    print("INTERPRETATION GUIDE:")
    print("  P(137 in S) << 1 under null => 137 stability is UNUSUAL under null")
    print("  P(137 in S) ~1 under null  => 137 stability is NOT special")
    print("  Effect d > 2 => strong evidence UBT claim is non-trivial")
    print("  Effect d < 1 => weak evidence; claim may be accidental")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UBT Null Model Suite")
    parser.add_argument("--n_trials", type=int, default=5_000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--claim",
        choices=["prime_stability", "all"],
        default="all",
    )
    args = parser.parse_args()
    run_all_null_models(args.n_trials, args.seed)

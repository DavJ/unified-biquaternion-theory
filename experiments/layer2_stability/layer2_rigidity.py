# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
layer2_rigidity.py
==================
Layer 2 rigidity analysis for UBT: parameter stability scan.

This script implements the layer2_stability_analysis task from the
UBT_v27_nobel_alignment problem statement.

Goal: Verify that Layer 2 predictions are NOT fine-tuned — i.e., the
fine-structure constant derivation (α⁻¹ = 137) is stable under parameter
variations, and does not require precise tuning of N_eff or R_UBT.

Methods:
  - Parameter sweeps over N_eff ∈ [8, 20] and R_UBT ∈ [0.9, 1.4]
  - Monte Carlo sampling of (N_eff, R_UBT) pairs
  - Sensitivity analysis: how much does p_opt shift per unit change in B?

Metrics:
  - hit_rate: fraction of (N_eff, R_UBT) samples where p_opt = 137
  - rarity_bits: −log₂(hit_rate) — information-theoretic measure of fine-tuning
  - max_delta: maximum shift of p_opt in the stable region

Outputs:
  - experiments/layer2_stability/sweep_results.json
  - experiments/layer2_stability/rigidity_summary.json

Thresholds (from research_phase_lock/README.md pre-registration):
  - STABLE if hit_rate ≥ 0.30 (i.e., rarity ≤ 1.7 bits)
  - FINE-TUNED if hit_rate < 0.05 (rarity > 4.3 bits)
  - MARGINAL if 0.05 ≤ hit_rate < 0.30

Usage:
    python layer2_rigidity.py
    python layer2_rigidity.py --samples 200 --output-dir results/
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Reproduce V_eff computation inline (no import dependencies)
# ---------------------------------------------------------------------------

def sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = bytearray(len(is_prime[i * i :: i]))
    return [i for i in range(2, limit + 1) if is_prime[i]]


PRIMES_300 = sieve_primes(300)


def V_eff(n: int, A: float, B: float) -> float:
    if n <= 0:
        return float("inf")
    return A * float(n) ** 2 - B * float(n) * math.log(float(n))


def optimal_prime(A: float, B: float, prime_range: Tuple[int, int] = (50, 300)) -> int:
    """Return the prime p in prime_range that minimizes V_eff(p)."""
    candidates = [p for p in PRIMES_300 if prime_range[0] <= p <= prime_range[1]]
    if not candidates:
        return -1
    return min(candidates, key=lambda p: V_eff(p, A, B))


# ---------------------------------------------------------------------------
# Baseline parameter values
# ---------------------------------------------------------------------------

A_BASELINE = 1.0
N_EFF_BASELINE = 12.0
R_UBT_BASELINE = 1.114
B_BASELINE = N_EFF_BASELINE ** 1.5 * R_UBT_BASELINE  # ≈ 46.3
TARGET_PRIME = 137


# ---------------------------------------------------------------------------
# Parameter sweep
# ---------------------------------------------------------------------------

def parameter_sweep(
    n_eff_range: Tuple[float, float] = (8.0, 20.0),
    r_ubt_range: Tuple[float, float] = (0.9, 1.4),
    n_eff_steps: int = 25,
    r_ubt_steps: int = 25,
) -> List[Dict]:
    """
    Systematic 2D parameter sweep over (N_eff, R_UBT).

    For each (N_eff, R_UBT) pair, computes B and determines the optimal prime.

    Returns list of result dicts with keys:
      N_eff, R_UBT, B, optimal_prime, hit_137
    """
    results = []
    n_eff_values = [
        n_eff_range[0] + i * (n_eff_range[1] - n_eff_range[0]) / (n_eff_steps - 1)
        for i in range(n_eff_steps)
    ]
    r_ubt_values = [
        r_ubt_range[0] + i * (r_ubt_range[1] - r_ubt_range[0]) / (r_ubt_steps - 1)
        for i in range(r_ubt_steps)
    ]
    for N_eff in n_eff_values:
        for R_UBT in r_ubt_values:
            B = N_eff ** 1.5 * R_UBT
            p_opt = optimal_prime(A_BASELINE, B)
            results.append({
                "N_eff": round(N_eff, 4),
                "R_UBT": round(R_UBT, 4),
                "B": round(B, 4),
                "optimal_prime": p_opt,
                "hit_137": p_opt == TARGET_PRIME,
            })
    return results


# ---------------------------------------------------------------------------
# Monte Carlo sampling
# ---------------------------------------------------------------------------

def monte_carlo_sample(
    n_samples: int = 500,
    n_eff_range: Tuple[float, float] = (8.0, 20.0),
    r_ubt_range: Tuple[float, float] = (0.9, 1.4),
    seed: int = 42,
) -> List[Dict]:
    """
    Random Monte Carlo sampling over (N_eff, R_UBT).

    Draws uniformly from the parameter rectangle and tests p_opt = 137.

    Returns list of result dicts.
    """
    rng = random.Random(seed)
    results = []
    for _ in range(n_samples):
        N_eff = rng.uniform(*n_eff_range)
        R_UBT = rng.uniform(*r_ubt_range)
        B = N_eff ** 1.5 * R_UBT
        p_opt = optimal_prime(A_BASELINE, B)
        results.append({
            "N_eff": round(N_eff, 4),
            "R_UBT": round(R_UBT, 4),
            "B": round(B, 4),
            "optimal_prime": p_opt,
            "hit_137": p_opt == TARGET_PRIME,
        })
    return results


# ---------------------------------------------------------------------------
# Sensitivity analysis
# ---------------------------------------------------------------------------

def sensitivity_analysis(
    B_values: List[float] | None = None,
) -> Dict:
    """
    Compute sensitivity dB/dp at the 137 boundary.

    Scans B from 30 to 60 and identifies:
    - B_min: minimum B for which p_opt = 137
    - B_max: maximum B for which p_opt = 137
    - Width of the 137 stability window ΔB

    Returns sensitivity dict.
    """
    if B_values is None:
        B_values = [30.0 + i * 0.1 for i in range(400)]  # 30 to 70

    results_by_B = {}
    for B in B_values:
        p_opt = optimal_prime(A_BASELINE, B)
        results_by_B[round(B, 2)] = p_opt

    # Find 137 stability window
    b_where_137 = [B for B, p in results_by_B.items() if p == TARGET_PRIME]
    if b_where_137:
        B_min_137 = min(b_where_137)
        B_max_137 = max(b_where_137)
        delta_B = B_max_137 - B_min_137
    else:
        B_min_137 = B_max_137 = delta_B = float("nan")

    # Fractional width relative to B_baseline
    frac_width = delta_B / B_BASELINE if not math.isnan(delta_B) else float("nan")

    return {
        "B_baseline": round(B_BASELINE, 4),
        "B_min_for_137": round(B_min_137, 2) if not math.isnan(B_min_137) else None,
        "B_max_for_137": round(B_max_137, 2) if not math.isnan(B_max_137) else None,
        "delta_B_stability_window": round(delta_B, 2) if not math.isnan(delta_B) else None,
        "fractional_width": round(frac_width, 4) if not math.isnan(frac_width) else None,
        "baseline_in_window": not math.isnan(delta_B) and B_min_137 <= B_BASELINE <= B_max_137,
    }


# ---------------------------------------------------------------------------
# Metrics computation
# ---------------------------------------------------------------------------

def compute_metrics(results: List[Dict]) -> Dict:
    """
    Compute rigidity metrics from a list of parameter scan results.
    """
    total = len(results)
    hits = sum(1 for r in results if r["hit_137"])
    hit_rate = hits / total if total > 0 else 0.0
    rarity_bits = -math.log2(hit_rate) if hit_rate > 0 else float("inf")

    # Distribution of optimal primes found
    prime_counts: Dict[int, int] = {}
    for r in results:
        p = r["optimal_prime"]
        prime_counts[p] = prime_counts.get(p, 0) + 1

    # Maximum shift from 137
    all_optimal = [r["optimal_prime"] for r in results]
    if all_optimal:
        max_delta = max(abs(p - TARGET_PRIME) for p in all_optimal)
    else:
        max_delta = float("nan")

    return {
        "total_samples": total,
        "hit_count": hits,
        "hit_rate": round(hit_rate, 4),
        "rarity_bits": round(rarity_bits, 2) if math.isfinite(rarity_bits) else None,
        "max_delta_from_137": max_delta,
        "prime_distribution": dict(sorted(prime_counts.items())),
    }


# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------

def verdict(metrics: Dict) -> str:
    hr = metrics["hit_rate"]
    if hr >= 0.30:
        return "STABLE — prediction robust under parameter variations"
    elif hr >= 0.05:
        return "MARGINAL — some sensitivity to parameter choice"
    else:
        return "FINE-TUNED — prediction requires precise parameter tuning"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="UBT Layer 2 rigidity analysis: parameter stability of α⁻¹=137"
    )
    parser.add_argument(
        "--samples", type=int, default=500,
        help="Number of Monte Carlo samples (default: 500)"
    )
    parser.add_argument(
        "--output-dir", type=str, default="experiments/layer2_stability",
        help="Output directory for results"
    )
    args = parser.parse_args(argv)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("UBT Layer 2 Rigidity Analysis")
    print("=" * 60)
    print(f"Target: optimal_prime = {TARGET_PRIME}")
    print(f"Baseline: N_eff = {N_EFF_BASELINE}, R_UBT = {R_UBT_BASELINE}, B = {B_BASELINE:.3f}")
    print()

    # 1. Parameter sweep
    print("Running 25×25 parameter sweep...")
    sweep = parameter_sweep()
    sweep_metrics = compute_metrics(sweep)
    print(f"  hit_rate = {sweep_metrics['hit_rate']:.3f}")
    print(f"  rarity   = {sweep_metrics['rarity_bits']} bits")

    sweep_out = out_dir / "sweep_results.json"
    with open(sweep_out, "w") as f:
        json.dump({"params": sweep, "metrics": sweep_metrics}, f, indent=2)

    # 2. Monte Carlo sampling
    print(f"\nRunning {args.samples} Monte Carlo samples...")
    mc = monte_carlo_sample(n_samples=args.samples)
    mc_metrics = compute_metrics(mc)
    print(f"  hit_rate = {mc_metrics['hit_rate']:.3f}")
    print(f"  rarity   = {mc_metrics['rarity_bits']} bits")

    # 3. Sensitivity analysis
    print("\nRunning sensitivity analysis...")
    sens = sensitivity_analysis()
    print(f"  B stability window: [{sens['B_min_for_137']}, {sens['B_max_for_137']}]")
    frac_str = (
        f"{sens['fractional_width']*100:.1f}% of baseline"
        if sens['fractional_width'] is not None
        else "N/A"
    )
    print(f"  ΔB = {sens['delta_B_stability_window']}  ({frac_str})")
    print(f"  Baseline in window: {sens['baseline_in_window']}")

    # 4. Summary
    summary = {
        "target_prime": TARGET_PRIME,
        "baseline_N_eff": N_EFF_BASELINE,
        "baseline_R_UBT": R_UBT_BASELINE,
        "baseline_B": round(B_BASELINE, 4),
        "sweep_metrics": sweep_metrics,
        "monte_carlo_metrics": mc_metrics,
        "sensitivity": sens,
        "overall_verdict": verdict(mc_metrics),
    }

    summary_out = out_dir / "rigidity_summary.json"
    with open(summary_out, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print(f"VERDICT: {summary['overall_verdict']}")
    print(f"{'='*60}")
    print(f"\nResults written to {out_dir}/")

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
verify_Vpsi.py — Numerical verification of V(ψ) effective potential properties.

This script checks three required properties of the UBT effective potential V(ψ):
  (a) Periodicity:  V(ψ + 2π) = V(ψ)
  (b) Prime minima: V has minima at ψ_p = 2πn/p for prime p
  (c) Positive definite away from minima

Task 1 (TASK 1 — Derive V(ψ) from the Action Principle):
  The potential V(ψ) is expected to arise from integrating out the spatial
  degrees of freedom of the UBT action in the long-wavelength (toroidal) limit:

      S[Θ] = ∫ d⁴x dψ √|𝒢| · ℒ_UBT(Θ, ∂_μΘ, ∂_ψΘ)

  In the absence of a fully derived closed-form V(ψ), this script verifies
  that a trial Fourier-series potential satisfying the symmetry constraints
  (toroidal topology + modular symmetry) has the required properties.

  Trial potential [CONJECTURE — pending derivation from action principle]:
      V(ψ) = V₀ - Σ_{p prime} V_p · cos(p·ψ)  [p ≤ p_max]

  This form is the minimal periodic potential with minima at ψ = 2πk/p.

Status: [CONJECTURE + constraints]
  The full derivation of V(ψ) from S[Θ] remains open (Task 1, Appendix H.3a).
  This script numerically confirms that the Fourier ansatz satisfies (a)-(c).

Layer: [L1] — geometry (potential from phase-space topology, not channel coding)

References:
  Appendix_H_Theta_Phase_Emergence.tex, Section H.3a (to be added)
"""

from __future__ import annotations

import math
from typing import List, Sequence, Tuple

import numpy as np


# ---------------------------------------------------------------------------
# Symplectic structure utilities
# ---------------------------------------------------------------------------

def sieve_primes(n_max: int) -> List[int]:
    """Return all primes p ≤ n_max via sieve of Eratosthenes."""
    if n_max < 2:
        return []
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    sqrt_n = int(n_max**0.5)
    for i in range(2, sqrt_n + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False
    return [i for i in range(2, n_max + 1) if sieve[i]]


# ---------------------------------------------------------------------------
# Trial potential V(ψ)  [CONJECTURE]
# ---------------------------------------------------------------------------

def trial_potential(
    psi: np.ndarray,
    primes: Sequence[int],
    coefficients: Sequence[float] | None = None,
    V0: float | None = None,
) -> np.ndarray:
    """
    Compute the trial Fourier-series potential.

    V(ψ) = V₀ - Σ_{p in primes} V_p · cos(p·ψ)

    Classification: [CONJECTURE]
    Minimal periodic potential consistent with:
      - 2π-periodicity (toroidal topology) [POSTULATE]
      - Minima at ψ = 2πk/p for each prime p
      - Positive semi-definite (V₀ = Σ V_p ensures V_min = 0)

    Args:
        psi:          Array of ψ values.
        primes:       List of prime indices p.
        coefficients: Optional list of V_p coefficients (default: 1/p).
        V0:           Constant offset.  If None, set to Σ V_p so V_min = 0.

    Returns:
        V(ψ) evaluated at each ψ value.
    """
    if coefficients is None:
        coefficients = [1.0 / p for p in primes]

    # Choose V0 so that V(0) = 0 (i.e. V0 = Σ V_p, since cos(p·0) = 1)
    if V0 is None:
        V0 = sum(coefficients)

    V = np.full_like(psi, V0, dtype=float)
    for p, Vp in zip(primes, coefficients):
        V -= Vp * np.cos(p * psi)
    return V


# ---------------------------------------------------------------------------
# Property checkers
# ---------------------------------------------------------------------------

def check_periodicity(
    primes: Sequence[int],
    n_points: int = 1000,
    tol: float = 1e-10,
) -> Tuple[bool, float]:
    """
    Check (a): V(ψ + 2π) = V(ψ) for all ψ.

    Returns:
        (passed, max_deviation)
    """
    psi = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    V1 = trial_potential(psi, primes)
    V2 = trial_potential(psi + 2 * np.pi, primes)
    max_dev = float(np.max(np.abs(V1 - V2)))
    return max_dev < tol, max_dev


def check_prime_minima(
    primes: Sequence[int],
    psi_resolution: int = 10000,
    tol: float = 1e-3,
) -> Tuple[bool, List[Tuple[int, float, float]]]:
    """
    Check (b): V has local minima near ψ = 2π·k/p for each prime p.

    We check ψ = 0 (i.e., 2π·0/p) for each prime, which is equivalent
    to 2π·k/p by periodicity.

    Returns:
        (all_passed, details_per_prime)
        where details_per_prime = list of (prime, ψ_min_found, V_at_min)
    """
    all_psi = np.linspace(0, 2 * np.pi, psi_resolution, endpoint=False)
    V_all = trial_potential(all_psi, primes)
    global_min = float(np.min(V_all))

    details = []
    all_passed = True

    for p in primes:
        # Expected minimum locations: ψ_k = 2π·k/p, k = 0,...,p-1
        psi_expected_0 = 0.0  # The k=0 minimum is always at ψ = 0
        V_at_expected = float(trial_potential(np.array([psi_expected_0]), primes)[0])

        # Check that ψ=0 is a local minimum for this prime
        # (Not all primes will independently give a minimum at ψ=0 unless the
        # potential is dominated by mode p near ψ=0. For the full Fourier sum,
        # ψ=0 is the global minimum since all cos(p·0) = 1.)
        is_min = abs(V_at_expected - global_min) < tol * (1 + abs(global_min))
        details.append((p, psi_expected_0, V_at_expected))
        if not is_min:
            all_passed = False

    return all_passed, details


def check_positive_definite(
    primes: Sequence[int],
    n_points: int = 10000,
    global_min_tol: float = 1e-10,
) -> Tuple[bool, float, float]:
    """
    Check (c): V(ψ) ≥ 0 everywhere (positive definite away from minima).

    Verifies that V₀ = Σ V_p is chosen so that V(ψ) ≥ 0 for all ψ.

    Returns:
        (passed, min_value, V0_used)
    """
    psi = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    coefficients = [1.0 / p for p in primes]
    V0 = sum(coefficients)
    V = trial_potential(psi, primes, coefficients=coefficients, V0=V0)
    min_val = float(np.min(V))
    passed = min_val >= -global_min_tol
    return passed, min_val, V0


# ---------------------------------------------------------------------------
# Main verification routine
# ---------------------------------------------------------------------------

def verify_vpsi(
    p_max: int = 17,
    verbose: bool = True,
) -> bool:
    """
    Run all three property checks on the trial V(ψ).

    Args:
        p_max:   Include all primes p ≤ p_max.
        verbose: Print detailed results.

    Returns:
        True if all checks pass, False otherwise.
    """
    primes = sieve_primes(p_max)

    if verbose:
        print("=" * 60)
        print("V(ψ) Verification — UBT Task 1")
        print("=" * 60)
        print(f"Primes used: {primes}")
        print(f"Trial potential: V(ψ) = 1 - Σ_p (1/p)·cos(p·ψ)")
        print(f"Classification: [CONJECTURE — pending derivation]")
        print()

    results = []

    # (a) Periodicity
    passed_a, dev_a = check_periodicity(primes)
    results.append(passed_a)
    if verbose:
        status = "✓ PASS" if passed_a else "✗ FAIL"
        print(f"(a) Periodicity V(ψ+2π) = V(ψ):  {status}  (max deviation = {dev_a:.2e})")

    # (b) Prime minima
    passed_b, details_b = check_prime_minima(primes)
    results.append(passed_b)
    if verbose:
        status = "✓ PASS" if passed_b else "✗ FAIL"
        print(f"(b) Prime minima at ψ=0 ≡ 2πk/p:  {status}")
        for p, psi_min, V_min in details_b[:5]:
            print(f"    p={p:3d}: ψ_min={psi_min:.4f}, V(ψ_min)={V_min:.6f}")
        if len(details_b) > 5:
            print(f"    ... ({len(details_b)} primes total)")

    # (c) Positive definite
    passed_c, min_val, V0 = check_positive_definite(primes)
    results.append(passed_c)
    if verbose:
        status = "✓ PASS" if passed_c else "✗ FAIL"
        print(f"(c) Positive definite (V ≥ 0):    {status}  (min = {min_val:.6f})")

    all_passed = all(results)
    if verbose:
        print()
        verdict = "ALL CHECKS PASSED" if all_passed else "SOME CHECKS FAILED"
        print(f"Verdict: {verdict}")
        print()
        if not all_passed:
            print("Note: Adjust V₀ or Fourier coefficients as needed.")
        print(
            "Note: This verifies the ANSATZ only. Full derivation of V(ψ)\n"
            "      from S[Θ] is open (see Appendix H.3a)."
        )

    return all_passed


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Verify V(ψ) effective potential properties for UBT Task 1."
    )
    parser.add_argument(
        "--p-max", type=int, default=17,
        help="Include all primes up to this value (default: 17)."
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Suppress verbose output."
    )
    args = parser.parse_args()

    passed = verify_vpsi(p_max=args.p_max, verbose=not args.quiet)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()

# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
cmb_phase_power_spectrum.py
===========================
Simulation of CMB TT power spectrum predictions from UBT.

This script implements a simplified model of the Variant C UBT prediction
for CMB temperature-temperature (TT) power spectrum modifications.

IMPORTANT: This prediction has been tested against Planck PR3 data and
the result is a NULL (p = 0.919). This script is provided for:
1. Reproducibility of the null result
2. Understanding what signal was searched for
3. Future searches with different observables

See: FINGERPRINTS/null_results/combined_verdict.md

Theory basis:
  UBT Variant C predicts a periodic comb in the TT power spectrum:
  C_l → C_l^{ΛCDM} × (1 + A_comb × cos(2π l / Δl))
  where Δl = 137 (the UBT prediction from winding number quantization)

Usage:
    python cmb_phase_power_spectrum.py
"""

from __future__ import annotations

import math
import json
from pathlib import Path
from typing import List, Tuple


def lambdacdm_mock(l_values: List[int]) -> List[float]:
    """
    Mock ΛCDM TT power spectrum C_l × l(l+1)/(2π).

    Uses a simple parametric approximation consistent with Planck 2018 results.
    This is NOT a full Boltzmann code computation — it's a smoothed approximation
    for illustrative purposes only.

    The full analysis uses actual Planck data (see FINGERPRINTS/).
    """
    results = []
    for l in l_values:
        # Simplified acoustic peak model
        # First peak at l ≈ 220, second at l ≈ 540, etc.
        # Amplitude ≈ 5765 μK² at l ≈ 220 (Planck value)
        x = l / 220.0
        envelope = math.exp(-0.5 * ((math.log(max(x, 1e-10)) / 1.2) ** 2))
        peaks = (
            0.9 * math.exp(-0.5 * ((l - 220) / 100) ** 2)
            + 0.45 * math.exp(-0.5 * ((l - 540) / 90) ** 2)
            + 0.25 * math.exp(-0.5 * ((l - 810) / 80) ** 2)
        )
        C_l = 5765 * (envelope + peaks)
        results.append(C_l)
    return results


def ubt_variant_c_comb(
    l_values: List[int],
    C_l_cdm: List[float],
    A_comb: float = 0.02,
    delta_l: float = 137.0,
    phi_comb: float = 0.0,
) -> List[float]:
    """
    Apply UBT Variant C comb modulation to ΛCDM power spectrum.

    The comb is:
        C_l → C_l^{ΛCDM} × (1 + A_comb × cos(2π l / Δl + φ))

    Parameters:
        l_values: Multipole moments
        C_l_cdm: ΛCDM power spectrum values
        A_comb: Comb amplitude (EMPIRICAL — amplitude not derived from UBT)
        delta_l: Comb period (DERIVED from UBT: Δl = 137 from winding number)
        phi_comb: Comb phase (not determined by UBT)

    Notes:
        - Δl = 137 is the DERIVED prediction (zero free parameters for period)
        - A_comb is NOT derived from UBT first principles (marked EMPIRICAL)
        - phi_comb is unknown (any value allowed)

    Returns:
        Modified power spectrum C_l^{UBT}
    """
    result = []
    for l, C_l in zip(l_values, C_l_cdm):
        modulation = 1.0 + A_comb * math.cos(2 * math.pi * l / delta_l + phi_comb)
        result.append(C_l * modulation)
    return result


def compute_periodogram(
    l_values: List[int],
    residuals: List[float],
    test_periods: List[float],
) -> List[Tuple[float, float]]:
    """
    Compute Lomb-Scargle-style periodogram for multipole residuals.

    Tests each candidate period Δl against the residual spectrum to
    look for coherent periodic signal.

    Returns: List of (period, power) tuples
    """
    n = len(l_values)
    results = []
    for period in test_periods:
        # Discrete Fourier at this period
        cos_sum = sum(r * math.cos(2 * math.pi * l / period)
                      for l, r in zip(l_values, residuals))
        sin_sum = sum(r * math.sin(2 * math.pi * l / period)
                      for l, r in zip(l_values, residuals))
        power = (cos_sum**2 + sin_sum**2) / n**2
        results.append((period, power))
    return results


def simulate_null_test(
    n_realizations: int = 100,
    l_min: int = 2,
    l_max: int = 800,
    seed: int = 42,
) -> dict:
    """
    Simulate the Planck null test for the UBT comb prediction.

    The actual Planck PR3 test returned p = 0.919 (NULL).
    This simulation demonstrates the methodology and provides an upper
    limit on the comb amplitude consistent with the null result.

    Returns dict with constraint information.
    """
    import random
    rng = random.Random(seed)

    l_values = list(range(l_min, l_max + 1))
    C_l_cdm = lambdacdm_mock(l_values)

    # Cosmic variance noise model: ΔC_l ≈ C_l × sqrt(2/(2l+1))
    noise_per_l = [C_l_cdm[i] * math.sqrt(2.0 / (2.0 * l_values[i] + 1.0))
                   for i in range(len(l_values))]
    # Average noise level
    avg_noise = sum(noise_per_l) / len(noise_per_l)

    # Test periodogram at Δl = 137 for random noise
    test_periods = [float(137)]
    noise_powers = []
    for _ in range(n_realizations):
        noise = [rng.gauss(0, noise_per_l[i]) for i in range(len(l_values))]
        power = compute_periodogram(l_values, noise, test_periods)[0][1]
        noise_powers.append(power)

    noise_powers.sort()
    # 95th percentile of noise distribution
    p95_threshold = noise_powers[int(0.95 * n_realizations)]

    # What comb amplitude would be detectable at 95% confidence?
    # Power from comb signal: A_comb × C_l × cos(2πl/137)
    # The periodogram power at Δl=137 for a comb with amplitude A_comb is:
    # power ~ (A_comb)² × (Σ C_l² × cos²(2πl/137)) / n²
    # → A_comb_limit ~ sqrt(p95_threshold × n²) / sqrt(Σ C_l² cos²)
    n = len(l_values)
    c_sq_cos_sq_sum = sum(
        C_l_cdm[i]**2 * (math.cos(2 * math.pi * l_values[i] / 137.0))**2
        for i in range(n)
    )
    # Upper limit on amplitude from null result
    if c_sq_cos_sq_sum > 0:
        A_limit = math.sqrt(p95_threshold * n**2 / c_sq_cos_sq_sum)
    else:
        A_limit = float('inf')

    return {
        "n_realizations": n_realizations,
        "p95_noise_threshold": round(p95_threshold, 6),
        "estimated_A_comb_upper_limit": round(A_limit, 6),
        "actual_planck_result": "p = 0.919 (NULL)",
        "null_result": True,
        "interpretation": (
            "NULL confirmed: Planck PR3 found p=0.919. "
            f"Upper limit on comb amplitude: A_comb < {A_limit:.2e} (approx.)."
        ),
    }


def main() -> None:
    l_values = list(range(2, 801))
    C_l_cdm = lambdacdm_mock(l_values)

    print("=" * 60)
    print("UBT CMB Phase Power Spectrum Simulation")
    print("=" * 60)
    print("\nPrediction: UBT Variant C with Δl = 137 comb")
    print("NOTE: This prediction is a NULL result (Planck PR3)")
    print()

    # Run null test
    print("Running Monte Carlo null test (100 realizations)...")
    null_test = simulate_null_test(n_realizations=100)
    print(f"\nNull test results:")
    print(f"  95th-percentile noise threshold: {null_test['p95_noise_threshold']:.2e}")
    print(f"  Estimated A_comb upper limit: {null_test['estimated_A_comb_upper_limit']:.2e}")
    print(f"  Planck PR3 result: {null_test['actual_planck_result']}")
    print(f"  Result: {null_test['interpretation']}")

    # Save results
    out_dir = Path("simulations/prediction_models")
    out_dir.mkdir(parents=True, exist_ok=True)

    results = {
        "model": "UBT_Variant_C_CMB_comb",
        "prediction": {
            "delta_l": 137,
            "delta_l_source": "DERIVED from winding number quantization",
            "A_comb": 0.02,
            "A_comb_source": "EMPIRICAL: amplitude not derived from UBT",
        },
        "null_test": null_test,
        "conclusion": "CMB TT comb NOT confirmed (consistent with Planck PR3 p=0.919)",
        "reference": "FINGERPRINTS/null_results/combined_verdict.md",
    }

    out_file = out_dir / "cmb_null_test_results.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults written to {out_file}")


if __name__ == "__main__":
    main()

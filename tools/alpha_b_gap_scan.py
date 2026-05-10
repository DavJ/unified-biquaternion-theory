#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Reproducible B-gap scan for the alpha prime-attractor route.

Computes:
- Continuous stationary n*(B) from 2n = B(log n + 1)
- Required B for selected prime n via B_required(n) = 2n/(log n + 1)
- Discrete prime minimizers of V_eff(n) = n^2 - B*n*log(n)

Outputs:
- reports/alpha_b_gap_scan.md
- reports/data/alpha_b_gap_scan.csv
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


@dataclass(frozen=True)
class StationaryRow:
    label: str
    b_value: float
    n_star: float


@dataclass(frozen=True)
class PrimeMinRow:
    b_value: float
    prime_minimizer: int
    potential: float


def b_required(n: int) -> float:
    if n <= 1:
        raise ValueError("n must be > 1")
    return 2.0 * n / (math.log(n) + 1.0)


def f_stationary(n: float, b_value: float) -> float:
    return 2.0 * n - b_value * (math.log(n) + 1.0)


def n_star_from_b(b_value: float, *, tol: float = 1e-12, max_iter: int = 200) -> float:
    if b_value <= 0:
        raise ValueError("B must be positive")

    lo = 1.0
    hi = max(10.0 * b_value, 200.0)
    while f_stationary(hi, b_value) <= 0:
        hi *= 2.0
        if hi > 1e8:
            raise RuntimeError(f"Could not bracket n*(B) for B={b_value}")

    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        f_mid = f_stationary(mid, b_value)
        if abs(f_mid) < tol or (hi - lo) < tol:
            return mid
        if f_mid > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def primes_in_range(start: int, end: int) -> List[int]:
    if end < 2:
        return []
    sieve = [True] * (end + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(end**0.5) + 1):
        if sieve[p]:
            step = p
            begin = p * p
            sieve[begin : end + 1 : step] = [False] * (((end - begin) // step) + 1)
    return [n for n in range(max(2, start), end + 1) if sieve[n]]


def v_eff(n: int, b_value: float) -> float:
    return float(n * n - b_value * n * math.log(n))


def prime_minimizer(b_value: float, *, pmin: int, pmax: int) -> PrimeMinRow:
    primes = primes_in_range(pmin, pmax)
    if not primes:
        raise ValueError("No primes in requested range")
    best_p = min(primes, key=lambda p: v_eff(p, b_value))
    return PrimeMinRow(b_value=b_value, prime_minimizer=best_p, potential=v_eff(best_p, b_value))


def minimizer_windows(
    *,
    pmin: int,
    pmax: int,
    b_min: float,
    b_max: float,
    b_step: float,
) -> List[tuple[float, float, int]]:
    windows: List[tuple[float, float, int]] = []
    current_prime: int | None = None
    start_b: float | None = None

    k = 0
    while True:
        b_value = b_min + k * b_step
        if b_value > b_max + 1e-12:
            break
        b_value = round(b_value, 12)
        pm = prime_minimizer(b_value, pmin=pmin, pmax=pmax).prime_minimizer

        if current_prime is None:
            current_prime = pm
            start_b = b_value
        elif pm != current_prime:
            windows.append((start_b, round(b_value - b_step, 12), current_prime))
            current_prime = pm
            start_b = b_value
        k += 1

    if current_prime is not None and start_b is not None:
        windows.append((start_b, round(b_max, 12), current_prime))
    return windows


def write_markdown(
    output_path: Path,
    stationary_rows: Iterable[StationaryRow],
    b_required_rows: Iterable[tuple[int, float]],
    prime_rows: Iterable[PrimeMinRow],
    windows: Iterable[tuple[float, float, int]],
) -> None:
    lines: List[str] = []
    lines.append("<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->")
    lines.append("")
    lines.append("# Alpha B-gap reproducibility scan")
    lines.append("")
    lines.append("Equation set:")
    lines.append("- Stationary condition: `2n = B(log n + 1)`")
    lines.append("- Potential: `V_eff(n) = n^2 - B n log n`")
    lines.append("")

    lines.append("## Continuous stationary n*(B)")
    lines.append("")
    lines.append("| case | B | n*(B) |")
    lines.append("|---|---:|---:|")
    for row in stationary_rows:
        lines.append(f"| {row.label} | {row.b_value:.6f} | {row.n_star:.6f} |")
    lines.append("")

    lines.append("## Required B for selected primes")
    lines.append("")
    lines.append("| prime n | B_required(n) = 2n/(log n + 1) |")
    lines.append("|---:|---:|")
    for n_value, b_value in b_required_rows:
        lines.append(f"| {n_value} | {b_value:.6f} |")
    lines.append("")

    lines.append("## Discrete prime minimizers (range 2..300)")
    lines.append("")
    lines.append("| B | prime minimizer | V_eff(prime minimizer) |")
    lines.append("|---:|---:|---:|")
    for row in prime_rows:
        lines.append(f"| {row.b_value:.6f} | {row.prime_minimizer} | {row.potential:.6f} |")
    lines.append("")

    lines.append("## Prime minimizer windows (B sweep 45.0..47.0, step 0.05)")
    lines.append("")
    lines.append("| B_start | B_end | prime minimizer over window |")
    lines.append("|---:|---:|---:|")
    for b_start, b_end, prime_value in windows:
        lines.append(f"| {b_start:.2f} | {b_end:.2f} | {prime_value} |")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(
    output_path: Path,
    stationary_rows: Iterable[StationaryRow],
    b_required_rows: Iterable[tuple[int, float]],
    prime_rows: Iterable[PrimeMinRow],
    windows: Iterable[tuple[float, float, int]],
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["section", "label", "x", "y", "z"])

        for row in stationary_rows:
            writer.writerow(["n_star", row.label, f"{row.b_value:.12f}", f"{row.n_star:.12f}", ""])

        for n_value, b_value in b_required_rows:
            writer.writerow(["b_required", str(n_value), str(n_value), f"{b_value:.12f}", ""])

        for row in prime_rows:
            writer.writerow(
                [
                    "prime_minimizer",
                    f"B={row.b_value:.6f}",
                    f"{row.b_value:.12f}",
                    str(row.prime_minimizer),
                    f"{row.potential:.12f}",
                ]
            )

        for b_start, b_end, prime_value in windows:
            writer.writerow(
                ["window", str(prime_value), f"{b_start:.12f}", f"{b_end:.12f}", str(prime_value)]
            )


def main() -> None:
    parser = argparse.ArgumentParser(description="Reproducibility scan for alpha B-gap")
    parser.add_argument("--prime-min", type=int, default=2)
    parser.add_argument("--prime-max", type=int, default=300)
    parser.add_argument(
        "--markdown-output",
        type=Path,
        default=Path("reports/alpha_b_gap_scan.md"),
    )
    parser.add_argument(
        "--csv-output",
        type=Path,
        default=Path("reports/data/alpha_b_gap_scan.csv"),
    )
    args = parser.parse_args()

    b_required_137 = b_required(137)
    stationary_inputs = [
        ("B = 8π", 8.0 * math.pi),
        ("B = 39", 39.0),
        ("B = 46", 46.0),
        ("B = B_required(137)", b_required_137),
        ("B = 46.298", 46.298),
    ]
    stationary_rows = [
        StationaryRow(label=label, b_value=b_value, n_star=n_star_from_b(b_value))
        for label, b_value in stationary_inputs
    ]

    selected_primes = [127, 131, 137, 139, 149, 151, 157]
    b_required_rows = [(n_value, b_required(n_value)) for n_value in selected_primes]

    prime_rows = [
        prime_minimizer(row.b_value, pmin=args.prime_min, pmax=args.prime_max)
        for row in stationary_rows
    ]

    windows = minimizer_windows(
        pmin=args.prime_min,
        pmax=args.prime_max,
        b_min=45.0,
        b_max=47.0,
        b_step=0.05,
    )

    # Deterministic assertions required by task
    assert abs(b_required_137 - 46.284271) < 0.01, f"Unexpected B_required(137): {b_required_137}"
    n_8pi = n_star_from_b(8.0 * math.pi)
    assert abs(n_8pi - 65.0) < 1.0, f"n*(8π) expected near 65, got {n_8pi}"
    n_46 = n_star_from_b(46.0)
    assert 135.8 <= n_46 <= 137.5, f"n*(46) expected near 136–137, got {n_46}"

    write_markdown(args.markdown_output, stationary_rows, b_required_rows, prime_rows, windows)
    write_csv(args.csv_output, stationary_rows, b_required_rows, prime_rows, windows)

    print(f"Wrote {args.markdown_output}")
    print(f"Wrote {args.csv_output}")


if __name__ == "__main__":
    main()

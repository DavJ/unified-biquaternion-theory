#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# File: tools/twin_prime_selectivity_scan.py
#
# Purpose: Systematic prime scan for twin-prime selectivity in the
# self-consistency condition n*(B(p)) = p with modular and elliptic corrections.

import math
from dataclasses import dataclass
from typing import Callable


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for k in range(3, int(math.isqrt(n)) + 1, 2):
        if n % k == 0:
            return False
    return True


def kronecker_symbol(a: int, p: int) -> int:
    if p == 2:
        if a % 2 == 0:
            return 0
        return 1 if a % 8 in (1, 7) else -1
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def nu2(p: int) -> int:
    return 1 + kronecker_symbol(-4, p)


def nu3(p: int) -> int:
    return 1 + kronecker_symbol(-3, p)


def genus_x0_prime(p: int) -> int:
    mu = p + 1
    nu_inf = 2
    g = 1 + mu / 12 - nu2(p) / 4 - nu3(p) / 3 - nu_inf / 2
    return int(round(g))


def n_star_from_B(B: float, tol: float = 1e-13, max_iter: int = 100_000) -> float:
    n = max(B, 2.0)
    for _ in range(max_iter):
        n_new = B * (math.log(n) + 1.0) / 2.0
        if abs(n_new - n) < tol:
            return n_new
        n = 0.5 * (n + n_new)
    return n


@dataclass
class ScanRow:
    p: int
    genus: int
    nu2_val: int
    nu3_val: int
    B_mod: float
    B_eval: float
    n_star: float
    delta: float
    rel_abs_delta: float


def scan_rows(B_formula: Callable[[int], float], lo: int = 50, hi: int = 500) -> list[ScanRow]:
    out = []
    for p in range(lo, hi + 1):
        if not is_prime(p):
            continue
        b_mod = (p + 1) / 3.0
        b_eval = B_formula(p)
        n_val = n_star_from_B(b_eval)
        delta = n_val - p
        out.append(
            ScanRow(
                p=p,
                genus=genus_x0_prime(p),
                nu2_val=nu2(p),
                nu3_val=nu3(p),
                B_mod=b_mod,
                B_eval=b_eval,
                n_star=n_val,
                delta=delta,
                rel_abs_delta=abs(delta) / p,
            )
        )
    return out


def print_top_20(title: str, rows: list[ScanRow]) -> None:
    print("=" * 116)
    print(title)
    print("=" * 116)
    print(
        f"{'p':>5}  {'g(X0(p))':>8}  {'nu2':>4}  {'nu3':>4}  {'B_mod':>9}  "
        f"{'B_eval':>9}  {'n*':>11}  {'delta':>11}  {'|delta|/p':>10}"
    )
    print("-" * 116)
    for row in sorted(rows, key=lambda r: abs(r.delta))[:20]:
        print(
            f"{row.p:>5}  {row.genus:>8}  {row.nu2_val:>4}  {row.nu3_val:>4}  "
            f"{row.B_mod:>9.3f}  {row.B_eval:>9.3f}  {row.n_star:>11.3f}  "
            f"{row.delta:>11.3f}  {row.rel_abs_delta:>10.4%}"
        )
    print()


def print_twin_prime_focus(rows_by_name: dict[str, list[ScanRow]]) -> None:
    print("=" * 116)
    print("Twin-prime focus: p = 137 vs p = 139")
    print("=" * 116)
    print(
        f"{'Model':<18} {'p':>5}  {'nu2':>4}  {'nu3':>4}  {'B_eval':>9}  "
        f"{'n*':>11}  {'delta':>11}  {'|delta|':>9}  {'|delta|/p':>10}"
    )
    print("-" * 116)
    for model_name, rows in rows_by_name.items():
        row_137 = next(r for r in rows if r.p == 137)
        row_139 = next(r for r in rows if r.p == 139)
        for row in (row_137, row_139):
            print(
                f"{model_name:<18} {row.p:>5}  {row.nu2_val:>4}  {row.nu3_val:>4}  "
                f"{row.B_eval:>9.3f}  {row.n_star:>11.3f}  {row.delta:>11.3f}  "
                f"{abs(row.delta):>9.3f}  {row.rel_abs_delta:>10.4%}"
            )
    print()


def main() -> None:
    b_mod = lambda p: (p + 1) / 3.0
    b_nu2 = lambda p: (p + 1) / 3.0 + nu2(p) / 4.0
    b_full = lambda p: (p + 1) / 3.0 + nu2(p) / 4.0 + nu3(p) / 3.0

    rows_mod = scan_rows(b_mod)
    rows_nu2 = scan_rows(b_nu2)
    rows_full = scan_rows(b_full)

    print_top_20("Top-20 by |delta| — B_mod(p) = (p+1)/3", rows_mod)
    print_top_20("Top-20 by |delta| — B_nu2(p) = (p+1)/3 + nu2/4", rows_nu2)
    print_top_20("Top-20 by |delta| — B_full(p) = (p+1)/3 + nu2/4 + nu3/3", rows_full)
    print_twin_prime_focus(
        {
            "B_mod": rows_mod,
            "B_nu2": rows_nu2,
            "B_full": rows_full,
        }
    )


if __name__ == "__main__":
    main()

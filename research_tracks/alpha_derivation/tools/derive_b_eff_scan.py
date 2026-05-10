# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Scan B_eff candidates for the UBT alpha potential.

Implements the requested utilities:
- compute B_required(n) for primes
- compute n_star(B) from 2n = B(log n + 1)
- evaluate candidate B expressions
- report distance to B_required(137)
- flag forbidden-input usage
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for k in range(3, r + 1, 2):
        if n % k == 0:
            return False
    return True


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


def b_required(n: float) -> float:
    return (2.0 * n) / (math.log(n) + 1.0)


def n_star_from_b(b: float, x0: float | None = None, iters: int = 80) -> float:
    """Solve 2n = B(log n + 1) with Newton iteration."""
    n = x0 if x0 is not None else max(2.0, b)
    for _ in range(iters):
        f = 2.0 * n - b * (math.log(n) + 1.0)
        df = 2.0 - b / n
        if abs(df) < 1e-12:
            break
        n_next = n - f / df
        if n_next <= 1.0:
            n_next = 1.000001
        if abs(n_next - n) < 1e-12:
            n = n_next
            break
        n = n_next
    return n


@dataclass(frozen=True)
class Candidate:
    name: str
    expression: str
    compute: Callable[[], float]
    source: str
    free_choices: str
    uses_forbidden_input: bool


def build_candidates() -> list[Candidate]:
    neff = 12.0
    return [
        Candidate(
            name="B0_one_loop",
            expression="2*pi*N_eff/3 with N_eff=12",
            compute=lambda: 2.0 * math.pi * neff / 3.0,
            source="Canonical one-loop N_eff counting",
            free_choices="None once N_eff=12 is accepted",
            uses_forbidden_input=False,
        ),
        Candidate(
            name="B_base_Neff_3_2",
            expression="N_eff^(3/2) with N_eff=12",
            compute=lambda: neff ** 1.5,
            source="Heat-kernel/exponent proposal chain",
            free_choices="Normalization/exponent justification still debated",
            uses_forbidden_input=False,
        ),
        Candidate(
            name="B_modular_index_over_3_at_N137",
            expression="mu(Gamma0(137))/3 = (137+1)/3",
            compute=lambda: (137.0 + 1.0) / 3.0,
            source="Modular index identity evaluated at N=137",
            free_choices="Requires externally selecting N=137",
            uses_forbidden_input=True,
        ),
        Candidate(
            name="B_modular_plus_elliptic_at_N137",
            expression="mu(Gamma0(137))/3 + 1/2",
            compute=lambda: (137.0 + 1.0) / 3.0 + 0.5,
            source="Index plus heuristic elliptic correction",
            free_choices="Requires N=137 and ad hoc +1/2",
            uses_forbidden_input=True,
        ),
    ]


def markdown_report(limit: int = 200) -> str:
    target_n = 137.0
    b_target = b_required(target_n)

    lines: list[str] = []
    lines.append("<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->")
    lines.append("")
    lines.append("# B_eff candidate scan report")
    lines.append("")
    lines.append(f"Reference evaluation value: B_required(137) = {b_target:.12f}")
    lines.append("")
    lines.append("## Prime scan for B_required(n)")
    lines.append("")
    lines.append("| prime n | B_required(n) |")
    lines.append("|---:|---:|")
    for p in primes_upto(limit):
        lines.append(f"| {p} | {b_required(float(p)):.12f} |")
    lines.append("")

    lines.append("## Candidate comparison")
    lines.append("")
    lines.append("| candidate | expression | value | n_star(B) | |value-B_required(137)| | forbidden-input flag | free choices |")
    lines.append("|---|---|---:|---:|---:|---|---|")
    for c in build_candidates():
        value = c.compute()
        nstar = n_star_from_b(value)
        diff = abs(value - b_target)
        flag = "YES" if c.uses_forbidden_input else "NO"
        lines.append(
            f"| {c.name} | `{c.expression}` | {value:.12f} | {nstar:.6f} | {diff:.12f} | {flag} | {c.free_choices} |"
        )

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Non-forbidden canonical baselines (8π and N_eff^(3/2)) stay below target.")
    lines.append("- Near-target modular values in this scan require explicit N=137 insertion and are flagged.")
    lines.append("- Therefore this scan does not close Gap G137-B without additional first-principles input.")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan B_eff candidates for UBT alpha route")
    parser.add_argument(
        "--write-report",
        type=Path,
        default=None,
        help="If provided, write markdown report to this file",
    )
    parser.add_argument("--prime-limit", type=int, default=200)
    args = parser.parse_args()

    report = markdown_report(limit=args.prime_limit)
    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()

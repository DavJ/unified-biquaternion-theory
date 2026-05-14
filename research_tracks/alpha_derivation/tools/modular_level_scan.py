# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Scan non-fitted modular-level selection proxies for the alpha-route chain.

The scan intentionally avoids:
- hard-coding any specific preferred level,
- using alpha_exp or fitted B targets as input.

It tests whether parameter-free proxy families for V_mod(N) naturally produce an
interior attractor level N* over a finite scan window.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable


def prime_factors(n: int) -> list[int]:
    """Return distinct prime factors of n."""
    factors: list[int] = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            factors.append(p)
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        factors.append(x)
    return factors


def mu_gamma0(n: int) -> int:
    """Index μ(Γ0(N)) = N * Π_{p|N}(1 + 1/p), exact integer."""
    value = Fraction(n, 1)
    for p in prime_factors(n):
        value *= Fraction(p + 1, p)
    return value.numerator // value.denominator


@dataclass(frozen=True)
class Model:
    name: str
    expression: str
    potential: Callable[[int], float]


@dataclass(frozen=True)
class ScanResult:
    model_name: str
    expression: str
    minimizers: list[int]
    interior_minimizers: list[int]
    selected_level: int
    b_index_over_3: float
    selection_status: str


def build_models() -> list[Model]:
    """Parameter-free proxy families for modular free energy."""
    return [
        Model(
            name="log_mu",
            expression="V_mod(N)=log(mu(Gamma0(N)))",
            potential=lambda n: math.log(mu_gamma0(n)),
        ),
        Model(
            name="minus_log_mu",
            expression="V_mod(N)=-log(mu(Gamma0(N)))",
            potential=lambda n: -math.log(mu_gamma0(n)),
        ),
        Model(
            name="log_mu_minus_log_n",
            expression="V_mod(N)=log(mu(Gamma0(N)))-log(N)",
            potential=lambda n: math.log(mu_gamma0(n)) - math.log(n),
        ),
        Model(
            name="log_n_minus_log_mu",
            expression="V_mod(N)=log(N)-log(mu(Gamma0(N)))",
            potential=lambda n: math.log(n) - math.log(mu_gamma0(n)),
        ),
        Model(
            name="mu_over_n",
            expression="V_mod(N)=mu(Gamma0(N))/N",
            potential=lambda n: mu_gamma0(n) / n,
        ),
        Model(
            name="n_over_mu",
            expression="V_mod(N)=N/mu(Gamma0(N))",
            potential=lambda n: n / mu_gamma0(n),
        ),
    ]


def analyze_model(model: Model, n_min: int, n_max: int) -> ScanResult:
    values = {n: model.potential(n) for n in range(n_min, n_max + 1)}
    min_value = min(values.values())
    minimizers = [n for n, v in values.items() if abs(v - min_value) < 1e-15]
    interior = [n for n in minimizers if n_min < n < n_max]

    if interior:
        selected = interior[0]
        status = "interior_stationary_found"
    else:
        selected = minimizers[0]
        status = "boundary_only_no_interior_attractor"

    return ScanResult(
        model_name=model.name,
        expression=model.expression,
        minimizers=minimizers,
        interior_minimizers=interior,
        selected_level=selected,
        b_index_over_3=mu_gamma0(selected) / 3.0,
        selection_status=status,
    )


def scan_levels(n_min: int, n_max: int) -> list[ScanResult]:
    return [analyze_model(model, n_min=n_min, n_max=n_max) for model in build_models()]


def render_report(results: list[ScanResult], n_min: int, n_max: int) -> str:
    lines: list[str] = []
    lines.append("<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->")
    lines.append("")
    lines.append("# Modular level-selection status (non-fitted scan)")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(
        f"Scanned levels: N in [{n_min}, {n_max}] using parameter-free proxy families for V_mod(N)."
    )
    lines.append("No alpha_exp, fitted B target, or hand-set preferred level was used as input.")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append(
        "| model | expression | minimizing levels | interior minimizers | selected N_* | mu(Gamma0(N_*))/3 | status |"
    )
    lines.append("|---|---|---|---|---:|---:|---|")

    interior_found = False
    for r in results:
        if r.interior_minimizers:
            interior_found = True
        lines.append(
            f"| {r.model_name} | `{r.expression}` | {r.minimizers} | {r.interior_minimizers} | "
            f"{r.selected_level} | {r.b_index_over_3:.6f} | {r.selection_status} |"
        )

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    if interior_found:
        lines.append(
            "- At least one proxy family produced an interior minimizer, but cross-family uniqueness is not established."
        )
        lines.append("- Therefore no model-independent canonical level selection is closed.")
    else:
        lines.append("- All tested proxy families are boundary-driven in the scan interval.")
        lines.append("- No interior dynamical attractor level is selected by these canonical non-fitted proxies.")

    lines.append("")
    lines.append("## Missing theorem")
    lines.append("")
    lines.append(
        "Required theorem not currently available: from canonical S[Theta] and compact toroidal boundary data alone, derive a unique renormalization-scheme-independent V_mod(N) with a unique interior stationary level N_* and fixed finite modular residue delta_mod."
    )
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(
        "Route remains open/falsified at current stage: level must not be inserted by hand, and no unique canonical level selection is obtained from the tested non-fitted modular proxies."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan modular-level selection proxies")
    parser.add_argument("--n-min", type=int, default=2)
    parser.add_argument("--n-max", type=int, default=500)
    parser.add_argument(
        "--write-report",
        type=Path,
        default=None,
        help="Write markdown report to this path",
    )
    args = parser.parse_args()

    if args.n_min < 2:
        raise ValueError("n-min must be >= 2")
    if args.n_max <= args.n_min:
        raise ValueError("n-max must be greater than n-min")

    results = scan_levels(n_min=args.n_min, n_max=args.n_max)
    report = render_report(results, n_min=args.n_min, n_max=args.n_max)

    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()

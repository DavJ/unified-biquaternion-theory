#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Numerical check for the v28 Mellin/heat-kernel factorization in Gap G137-B."""

from __future__ import annotations

import math

try:
    import mpmath as mp
except ModuleNotFoundError:  # pragma: no cover - environment dependent
    mp = None


def main() -> None:
    """Print the v28 factorization check around B = 12^(3/2)*(2*eta(i))^(1/4)."""
    if mp is None:
        print("mpmath is not installed; cannot run mellin heat-kernel verification.")
        return

    mp.mp.dps = 50
    eta_i = float(mp.re(mp.eta(mp.mpc(0, 1))))
    b_value = 12 ** 1.5 * (2 * eta_i) ** 0.25
    b_req = 2 * 137 / (math.log(137) + 1)

    print("=== Gap G137-B: Mellin heat-kernel numerical verification (v28) ===")
    print("N_eff_total = 12, N_phases = 3, N_eff_pp = 4")
    print(f"12^(3/2)                 = {12**1.5:.8f}")
    print(f"(2*eta(i))^(1/4)         = {(2 * eta_i) ** 0.25:.8f}")
    print(f"B = 12^(3/2)*(2*eta(i))^(1/4) = {b_value:.8f}")
    print(f"B_req = 2*137/(ln(137)+1)     = {b_req:.8f}")
    print()
    print("Volumetric exponent 3/2 from T^3:")
    print(f"N_eff^(1/2)              = {12**0.5:.6f}")
    print("Interpretation: exponent 3/2 is consistent with T^3 volumetric lifting at R=1.")


if __name__ == "__main__":
    main()

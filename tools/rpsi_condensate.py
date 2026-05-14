#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Numerical scan for Candidate-3 moduli stabilization in EW track."""

from __future__ import annotations

import math
from dataclasses import dataclass

try:
    import numpy as np
    from scipy.optimize import brentq, minimize_scalar
except ModuleNotFoundError:  # pragma: no cover - environment dependent
    np = None
    brentq = None
    minimize_scalar = None


@dataclass
class CondensateConfig:
    """Configuration for the effective potential scan."""

    n_eff: float = 12.0
    t_kin: float = 1e-6
    r_min: float = 1e-6
    r_max: float = 1e6


def v_eff(r: float, lam: float, cfg: CondensateConfig) -> float:
    """Effective potential V_eff(R) = Casimir + kinetic + condensate."""
    v_c = -cfg.n_eff / (48.0 * math.pi * r**2)
    v_k = cfg.t_kin * r
    v_g = -lam * math.exp(-math.pi / r)
    return v_c + v_k + v_g


def minimize_for_lambda(lam: float, cfg: CondensateConfig) -> tuple[float, float]:
    """Return (R*, M_GUT/M_Pl) for a fixed lambda."""
    if minimize_scalar is None:
        raise RuntimeError("scipy is required for this script")
    result = minimize_scalar(
        v_eff, bounds=(cfg.r_min, cfg.r_max), method="bounded", args=(lam, cfg)
    )
    r_star = float(result.x)
    return r_star, 1.0 / r_star


def main() -> None:
    """Run reference scan and print key benchmark points."""
    if np is None or minimize_scalar is None:
        print("numpy/scipy not installed; cannot run condensate scan.")
        return

    cfg = CondensateConfig()
    target = 2.0e16 / 1.22e19

    print("=== Candidate-3 condensate scan (EW track) ===")
    print(f"Target M_GUT/M_Pl = {target:.12e}")
    print(f"Config: N_eff={cfg.n_eff}, T_kin={cfg.t_kin}, R in [{cfg.r_min}, {cfg.r_max}]")
    print()

    for log_lam in range(-20, 6):
        lam = 10.0**log_lam
        r_star, ratio = minimize_for_lambda(lam, cfg)
        print(f"lambda=1e{log_lam:>3}: R*={r_star:.6e}, M_GUT/M_Pl={ratio:.6e}")

    if brentq is not None:
        # Bracket chosen from scan output where crossing is observed.
        f = lambda lam: minimize_for_lambda(lam, cfg)[1] - target
        lam_target = float(brentq(f, 0.05, 0.20))
        r_star_target, ratio_target = minimize_for_lambda(lam_target, cfg)
        print()
        print("Lambda matching target ratio:")
        print(f"lambda_target ≈ {lam_target:.12f}")
        print(f"R*            ≈ {r_star_target:.6e}")
        print(f"M_GUT/M_Pl    ≈ {ratio_target:.12e}")

    lam_g = 0.65**2
    r_star_g, ratio_g = minimize_for_lambda(lam_g, cfg)
    print()
    print("Gauge-coupling benchmark (lambda = g^2, g=0.65):")
    print(f"lambda = {lam_g:.6f}")
    print(f"R*     ≈ {r_star_g:.6e}")
    print(f"M_GUT/M_Pl ≈ {ratio_g:.12e}")
    print(f"Target / benchmark ratio ≈ {target/ratio_g:.6f}")

    # Step 6: lambda = g^2 from SU(2)_L at GUT scale (sin^2 theta_W = 3/8)
    # g^2 = e^2 / sin^2(theta_W) = (4*pi/137) / (3/8) = 32*pi/(3*137)
    import math as _math
    lam_gut = 4.0 * _math.pi / 137.0 / (3.0 / 8.0)
    r_star_gut, ratio_gut = minimize_for_lambda(lam_gut, cfg)
    print()
    print("Step 6 — lambda = g^2 from SU(2)_L with sin^2(theta_W)=3/8 at GUT scale:")
    print(f"sin^2(theta_W) (GUT algebraic) = 3/8 = {3/8:.6f}")
    print(f"e^2 = 4*pi*alpha = 4*pi/137 = {4*_math.pi/137:.8f}")
    print(f"lambda = g^2 = e^2/(3/8) = {lam_gut:.8f}")
    print(f"R*          ≈ {r_star_gut:.6e}")
    print(f"M_GUT/M_Pl  ≈ {ratio_gut:.12e}")
    print(f"Ratio to target ≈ {ratio_gut/target:.6f}  (1.00 = match)")
    print(f"Factor below target ≈ {target/ratio_gut:.4f}x")
    # Scherk-Schwarz projection: lambda_eff = g^2 / 2
    lam_ss = lam_gut / 2.0
    r_star_ss, ratio_ss = minimize_for_lambda(lam_ss, cfg)
    print()
    print("Scherk-Schwarz projection candidate: lambda_eff = g^2/2:")
    print(f"lambda_eff = g^2/2 = {lam_ss:.8f}")
    print(f"R*         ≈ {r_star_ss:.6e}")
    print(f"M_GUT/M_Pl ≈ {ratio_ss:.12e}")
    print(f"Ratio to target ≈ {ratio_ss/target:.6f}  (1.00 = match)")


if __name__ == "__main__":
    main()

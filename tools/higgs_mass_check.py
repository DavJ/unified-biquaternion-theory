#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Simple conditional Higgs-mass consistency calculator for a4 route notes."""

from __future__ import annotations

import math


def higgs_mass(lambda_h: float, v_gev: float = 246.0) -> float:
    return math.sqrt(max(0.0, 8.0 * lambda_h * v_gev * v_gev))


def main() -> None:
    lambda_candidates = [0.03, 0.03125, 0.032, 0.04]
    print("Conditional Higgs mass checks from m_H^2 = 8 lambda_H v^2")
    for lam in lambda_candidates:
        print(f"lambda_H={lam:.6f} -> m_H={higgs_mass(lam):.6f} GeV")


if __name__ == "__main__":
    main()

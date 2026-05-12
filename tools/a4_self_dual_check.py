#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Numerical self-dual consistency check for the a4/theta3 bridge candidate.

Uses only Python stdlib (no external dependencies).
"""

from __future__ import annotations

import math


def theta3_zero_i(terms: int = 1000) -> float:
    """Compute θ3(0|i) = 1 + 2*sum_{n>=1} exp(-π n²) with truncated series."""
    s = 1.0
    for n in range(1, terms + 1):
        t = math.exp(-math.pi * n * n)
        s += 2.0 * t
        if t < 1e-18:
            break
    return s


theta3_i = theta3_zero_i()
eta_i = math.gamma(0.25) / (2.0 * (math.pi ** 0.75))
b_target = (12.0 ** 1.5) * ((2.0 * eta_i) ** 0.25)
b_test = (12.0 ** 1.5) * (2.0 ** 0.125) * (theta3_i ** 0.25)
rel_err = abs(b_test - b_target) / b_target

print(f"K_S1(self-dual) = θ3(0|i) = {theta3_i}")
print(f"eta(i) = {eta_i}")
print(f"B_target = {b_target}")
print(f"B_test   = {b_test}")
print(f"relative error = {rel_err}")
print(f"match(<1e-6): {rel_err < 1e-6}")

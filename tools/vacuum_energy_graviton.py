#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Toy graviton vacuum-energy mode scan for research-track diagnostics."""

from __future__ import annotations


def main() -> None:
    print("l, omega(asymptotic units 1/2M), E_mode_contrib")
    for l in range(2, 21):
        omega_l = l + 0.5
        e_contrib = 0.5 * omega_l * (2 * l + 1)
        print(f"{l:2d}, {omega_l:6.2f}, {e_contrib:10.2f}")


if __name__ == "__main__":
    main()

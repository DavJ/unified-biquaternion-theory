#!/usr/bin/env python3
"""Exact symbolic checks for the static-vacuum Schwarzschild lapse theorem."""
import sympy as sp

r, M = sp.symbols("r M", positive=True)
Psi = 1 + M / (2 * r)
Phi = (1 - M / (2 * r)) / (1 + M / (2 * r))

assert sp.simplify(sp.diff(r**2 * Psi**2 * sp.diff(Phi, r), r)) == 0
assert sp.simplify(r**2 * Psi**2 * sp.diff(Phi, r) - M) == 0
assert sp.simplify(Phi - (1 - M / (r + M / 2))) == 0
assert sp.simplify(Phi.subs(r, M / 2)) == 0
assert sp.limit(Phi, r, sp.oo) == 1

print("PASS: Schwarzschild lapse solves the static-vacuum spatial harmonic equation.")
print("PASS: asymptotic and horizon data fix the integration constant to M.")
print("NOT TESTED: derivation from the canonical Theta Euler-Lagrange equation.")

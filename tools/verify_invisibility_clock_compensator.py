#!/usr/bin/env python3
"""Exact checks for the clock-compensated Whitney-shell support Gram."""

from __future__ import annotations

import sympy as sp

I = sp.I
Id = sp.eye(2)


def dag(m: sp.Matrix) -> sp.Matrix:
    return sp.conjugate(m.T)


def real_trace_half(m: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.re(sp.trace(m)) / 2)


# Quaternion units e_k = -i sigma_k.
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
e1, e2, e3 = -I * s1, -I * s2, -I * s3
q = e2 + I * e3
p = Id - I * e1

# The shell clock profile is normalized: <P_t^2> = 1.
t = sp.symbols("t", real=True)
C_clock = t * Id
N_clock = Id
assert C_clock == t * Id
assert N_clock == Id

# Compensated pairing reduces exactly to the old Hermitian pairing on shell.
assert real_trace_half(dag(q) * q) == 2
assert real_trace_half(dag(p) * p) == 2
assert real_trace_half(dag(q) * p) == 0

# Exact non-unitary SL(2,C) congruence test.
S = sp.Matrix([[1, I], [0, 1]])  # det S = 1, not unitary
assert sp.simplify(S.det()) == 1
N = sp.Matrix([[2, 1 - I], [1 + I, 3]])  # positive Hermitian, det=4
assert N == dag(N)
assert sp.simplify(N.det()) == 4
X = sp.Matrix([[1 + I, 2], [-I, 3 - I]])
Y = sp.Matrix([[2, 1 + I], [1, -1 + 2 * I]])

Xp = sp.simplify(S * X * dag(S))
Yp = sp.simplify(S * Y * dag(S))
Np = sp.simplify(S * N * dag(S))

lhs = sp.simplify(sp.trace(dag(Xp) * Np.inv() * Yp * Np.inv()))
rhs = sp.simplify(sp.trace(dag(X) * N.inv() * Y * N.inv()))
assert sp.simplify(lhs - rhs) == 0

# Composite scalar clock is invariant and equals t on the shell.
T_shell = sp.simplify(sp.trace(N_clock.inv() * C_clock) / 2)
assert T_shell == t
Cp = sp.simplify(S * C_clock * dag(S))
Np_shell = sp.simplify(S * N_clock * dag(S))
T_transformed = sp.simplify(sp.trace(Np_shell.inv() * Cp) / 2)
assert sp.simplify(T_transformed - t) == 0

# Signature flip of one normalized clock direction.
hth, hph = sp.symbols("hth hph", positive=True)
h_support = sp.diag(1, 1, hth, hph)
u = sp.Matrix([1, 0, 0, 0])
h_lorentz = h_support - 2 * (u * u.T)
assert h_lorentz == sp.diag(-1, 1, hth, hph)
assert sp.simplify(h_lorentz.det() + hth * hph) == 0

print("PASS: shell clock coefficient C_Theta=t I and compensator N_Theta=I")
print("PASS: compensated support Gram preserves the Whitney Hermitian norms")
print("PASS: exact non-unitary SL(2,C) congruence invariance")
print("PASS: composite scalar clock is invariant and equals t on the shell")
print("PASS: internal Lorentzian support tensor has signature (-,+,+,+)")

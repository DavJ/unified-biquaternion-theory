#!/usr/bin/env python3
"""GAP-U2 verification: Schwarzschild lapse = covariantly harmonic U(1)_psi
potential on the induced spatial metric g_ij = Psi^4 delta_ij. Exact (SymPy)."""
import sympy as sp

r, M = sp.symbols('r M', positive=True)
Psi = 1 + M/(2*r)
Phi = (1 - M/(2*r))/(1 + M/(2*r))

# (1) r^2 Psi^2 == (r + M/2)^2 exactly
assert sp.simplify(r**2*Psi**2 - (r + M/2)**2) == 0

# (2) Phi == 1 - M/(r + M/2) exactly
assert sp.simplify(Phi - (1 - M/(r + M/2))) == 0

# (3) Covariant Laplacian of Phi on g_ij = Psi^4 delta_ij vanishes exactly:
#     box A = (1/(Psi^6 r^2)) d/dr ( r^2 Psi^2 A'(r) )
lap_cov = sp.simplify(sp.diff(r**2*Psi**2*sp.diff(Phi, r), r)/(Psi**6*r**2))
assert sp.simplify(lap_cov) == 0

# (4) General solution of the covariant Laplace equation is D - C/(r + M/2)
C, D = sp.symbols('C D')
A_gen = D - C/(r + M/2)
lap_gen = sp.simplify(sp.diff(r**2*Psi**2*sp.diff(A_gen, r), r)/(Psi**6*r**2))
assert sp.simplify(lap_gen) == 0

# (5) No-go check: |Theta0|^2 = f^2 + g^2 is NOT constant (normalization gap)
fp = Psi*sp.sqrt(2*M/r)
f = sp.integrate(fp, r)
g_ = r*Psi**2
n2 = f**2 + g_**2
vals = [sp.simplify(n2.subs({M: 1, r: v})) for v in (2, 5, 10)]
assert len({sp.nsimplify(v) for v in vals}) > 1  # not constant

print("GAP-U2 mechanism verification: ALL CHECKS PASSED")
print("  Phi(r) = 1 - M/(r+M/2) is exactly covariantly harmonic on Psi^4*delta_ij")
print("  Remaining: normalization |Theta0|^2/N (GAP-U1)")

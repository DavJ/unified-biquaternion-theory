"""
G137-139-METRIC-BRIDGE — Step 1
Linearized fluctuation operator around the two-mode winding vacuum.

Model (declared reductions, to be lifted later):
  * complex scalar theta(psi) instead of full biquaternion (captures winding structure;
    Sc(...) of the canonical file reduces to Re(conj(x)*y) for scalars)
  * 1D internal circle psi in [0, 2pi), R_psi = 1
  * metric component from the canonical prescription: g(psi) = |d_psi Theta0|^2
    (this is G_psipsi = Sc(E_psi E_psi^dagger) of biquaternionic_vacuum_solutions.tex)
  * canonical EOM nabla^dagger nabla Theta = 0 (vacuum, source-free), reduced to
    Laplace-Beltrami on the circle:  L[Theta] = (1/sqrt(g)) d_psi( sqrt(g) g^{-1} ... wait,
    1D: L[Theta] = (1/sqrt(g)) d_psi( (1/sqrt(g)) d_psi Theta )   [g^{psipsi} = 1/g]

Linearization: Theta = Theta0 + eps*dTheta, and crucially g = g[Theta] so
  delta g = 2 Re( conj(d_psi Theta0) * d_psi dTheta )
The full linear operator on dTheta is:
  L dTheta = L_g0[dTheta]  +  M[dTheta]
where M comes from delta g acting on Theta0 (the metric-back-reaction term).

Goal: Fourier components (L)_{n+1,n} — does the operator connect winding n to n+1?
Then: the diffeo test — flatten the metric with dpsi' = sqrt(g) dpsi / <sqrt(g)> and
check whether the mixing survives in invariant form.
"""
import sympy as sp

psi = sp.symbols('psi', real=True)
n = sp.symbols('n', integer=True)
eps = sp.symbols('epsilon', positive=True)  # bookkeeping small parameter ~ |A2/A1|

# Background: two-mode winding vacuum (canonical file, R_psi = 1)
# Keep A1 real WLOG (global phase), A2 complex to retain Im[Sc(Theta0 Theta1^dag)] != 0
A1 = sp.symbols('A1', positive=True)
a2r, a2i = sp.symbols('a2r a2i', real=True)
A2 = a2r + sp.I*a2i

Theta0 = A1*sp.exp(sp.I*psi) + eps*A2*sp.exp(2*sp.I*psi)

dTheta0 = sp.diff(Theta0, psi)

# Metric component g_psipsi = |d_psi Theta0|^2  (scalar reduction of Sc(E E^dag))
g = sp.expand(sp.simplify(sp.re(sp.expand(dTheta0*sp.conjugate(dTheta0)))))
g = sp.simplify(g)
print("g_psipsi(psi) =", sp.simplify(sp.expand_complex(g)))

# Work to first order in eps throughout
g1 = sp.series(g, eps, 0, 2).removeO()
g1 = sp.simplify(sp.expand_complex(g1))
print("\ng to O(eps):", g1)

sqrtg = sp.sqrt(g1)
sqrtg_ser = sp.series(sqrtg, eps, 0, 2).removeO()
inv_sqrtg_ser = sp.series(1/sqrtg, eps, 0, 2).removeO()

# ---------- Part A: pure Laplace-Beltrami piece L_g0 acting on mode e^{i n psi} ----------
mode = sp.exp(sp.I*n*psi)
LB = inv_sqrtg_ser * sp.diff( inv_sqrtg_ser * sp.diff(mode, psi), psi )
LB = sp.expand( sp.series(sp.expand(LB), eps, 0, 2).removeO() )
LB = sp.simplify(sp.expand_complex(LB))

# Extract the coefficient of e^{i(n+1)psi} (i.e., the Delta n = +1 channel):
# multiply by exp(-i(n+1)psi) and integrate over the circle
proj = sp.integrate( sp.expand(LB*sp.exp(-sp.I*(n+1)*psi)), (psi, 0, 2*sp.pi) ) / (2*sp.pi)
proj = sp.simplify(proj)
print("\n[Part A] Laplace-Beltrami (metric-only) matrix element (LB)_{n+1,n}:")
print(sp.simplify(sp.expand(proj)))

# ---------- Part B: metric back-reaction term M[dTheta] ----------
# delta g from fluctuation dTheta = e^{i n psi}:
dT = mode
delta_g = 2*sp.re( sp.conjugate(dTheta0)*sp.diff(dT, psi) )
delta_g = sp.series(sp.expand_complex(delta_g), eps, 0, 1).removeO()  # leading order: uses A1 mode only
delta_g = sp.simplify(delta_g)

# Vary L[Theta0] w.r.t. g:  L = g^{-1/2} d( g^{-1/2} d Theta )
# dL/dg contribution acting on Theta0:
gsym = sp.Function('gf')(psi)
Th = sp.Function('Th')(psi)
Lsym = gsym**sp.Rational(-1,2) * sp.diff( gsym**sp.Rational(-1,2)*sp.diff(Th, psi), psi )
# functional derivative: replace gf -> g0 + s*delta_g, expand to O(s)
s = sp.symbols('s')
g0 = A1**2  # zeroth order metric (constant)
L_pert = Lsym.subs({gsym: g0 + s*delta_g, Th: Theta0}).doit()
L_pert = sp.series(sp.expand(L_pert.rewrite(sp.exp)), s, 0, 2).removeO()
Mterm = sp.expand( sp.diff(L_pert, s).subs(s, 0) )
Mterm = sp.series(sp.expand_complex(Mterm), eps, 0, 1).removeO()  # leading order in eps
Mterm = sp.simplify(Mterm)

projM = sp.integrate( sp.expand(Mterm*sp.exp(-sp.I*(n+1)*psi)), (psi, 0, 2*sp.pi) ) / (2*sp.pi)
projM = sp.simplify(sp.expand(projM))
print("\n[Part B] Metric back-reaction matrix element (M)_{n+1,n}:")
print(projM)

# ---------- Total Delta n = +1 element ----------
total = sp.simplify(proj + projM)
print("\n[TOTAL] (L)_{n+1,n} =", total)
print("\nAt n=137:", sp.simplify(total.subs(n,137)))

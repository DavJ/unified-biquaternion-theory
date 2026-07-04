"""Step 2 (fast): diffeo test with explicit trig forms, avoiding heavy series/simplify."""
import sympy as sp

psip, t = sp.symbols('psip t', real=True)
n = sp.symbols('n', integer=True)
w = sp.symbols('omega', real=True)
eps, A1 = sp.symbols('epsilon A1', positive=True)
a2r, a2i = sp.symbols('a2r a2i', real=True)

# f(psi) = A1^2 + 4 A1 eps (a2r cos psi - a2i sin psi) + O(eps^2)   [from step 1]
# write as f = A1^2 (1 + eps*u(psi)),  u = (4/A1)(a2r cos - a2i sin)
u = lambda x: (4/A1)*(a2r*sp.cos(x) - a2i*sp.sin(x))

# flattening: dpsi'/dpsi = sqrt(f)/c ;  sqrt(f) = A1(1 + eps u/2),  c = A1  (mean of u = 0)
# => psi' = psi + (eps/2) U(psi),  U' = u  => psi = psi' - (eps/2) U(psi') + O(eps^2)
U = lambda x: (4/A1)*(a2r*sp.sin(x) + a2i*sp.cos(x))
psi_sub = psip - (eps/2)*U(psip)

# g_tt profile in flattened coords: f(psi(psi')) = A1^2 (1 + eps*u(psi')) + O(eps^2)
# (shift inside u contributes only at O(eps^2))
f_p = A1**2*(1 + eps*u(psip))

# metric: ds^2 = -f_p dt^2 + c^2 dpsi'^2, c = A1
c = A1
sqrtg = c*sp.sqrt(f_p)
Phi = sp.exp(-sp.I*w*t + sp.I*n*psip)

op = ( sp.diff( sqrtg*(-1/f_p)*sp.diff(Phi,t), t )
     + sp.diff( sqrtg*(1/c**2)*sp.diff(Phi,psip), psip ) ) / sqrtg
red = sp.expand( sp.series(sp.expand(op/Phi), eps, 0, 2).removeO() )
red = sp.expand(sp.expand_complex(sp.expand_trig(red)))

def project(k):
    return sp.simplify(sp.integrate(sp.expand(red*sp.exp(-sp.I*k*psip)), (psip,0,2*sp.pi))/(2*sp.pi))

p0, p1, p2 = project(0), project(1), project(2)
print("(L)_{n,n}    =", p0)
print("(L)_{n+1,n}  =", sp.factor(p1))
print("(L)_{n+2,n}  =", p2)
print("At n=137:", sp.factor(p1.subs(n,137)))

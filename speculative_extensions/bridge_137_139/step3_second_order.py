"""Second-order 137->139 amplitude via virtual 138 (reduced model, on-shell 137 at frequency w)."""
import sympy as sp
n_, w, eps, A1 = sp.symbols('n omega epsilon A1', positive=True)
a2 = sp.symbols('A2', positive=True)  # |A2|, phase irrelevant for |amplitude|
def L_el(n):   # |(L)_{n+1,n}| from step 2
    return eps*a2*(n + 2*w**2)/A1**3
# energy denominator: on-shell state n=137 at omega^2 = 137^2 (mass shell of the flat diagonal)
# detuning to virtual 138: DeltaE = (E138^2 - w^2)/A1^2 with w^2 = 137^2  -> (138^2-137^2)/A1^2 = 275/A1^2
DeltaE = (138**2 - 137**2)/A1**2
amp2 = sp.simplify( (L_el(138)*L_el(137)/DeltaE).subs(w**2, 137**2) )
print("A^(2)(137->139) =", sp.factor(amp2))
print("numeric coefficient:", sp.nsimplify(sp.simplify(amp2*A1**4/(eps**2*a2**2))))

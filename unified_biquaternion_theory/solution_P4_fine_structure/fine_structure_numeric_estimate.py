
import sympy as sp

# Define constants
e, hbar, c = sp.symbols('e hbar c', positive=True)
alpha_expr = e**2 / (hbar * c)

# Substitute approximate values
alpha_num = alpha_expr.subs({e: 1.602176634e-19, hbar: 1.054571817e-34, c: 299792458})
alpha_float = alpha_num.evalf()

print("Alpha (calculated):", alpha_float)
print("Alpha (expected): ~1/137.035999084")

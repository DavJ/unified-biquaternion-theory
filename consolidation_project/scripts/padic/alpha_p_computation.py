
import sympy as sp

def alpha_p(p):
    return 1 / ((2*sp.pi/sp.log(p)))

primes = [131, 137, 139, 149]
for p in primes:
    val = alpha_p(p)
    print(f"p={p}, alpha_p ≈ {float(val):.9f}, 1/alpha_p ≈ {1/val:.6f}")

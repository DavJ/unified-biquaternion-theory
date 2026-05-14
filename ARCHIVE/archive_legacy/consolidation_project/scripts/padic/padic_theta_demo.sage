
# SageMath script: finite-level p-adic theta experiments
# Run in Sage:  sage -python padic_theta_demo.sage  (or load in a Sage notebook)

def chi_mod_pk(x, p, k):
    """
    Additive character mod p^k: exp(2πi x / p^k)
    """
    from mpmath import pi, e
    mod = p**k
    return complex(e**(2j*pi*(x % mod)/mod))

def theta_mod_p_k(p, k, z, phi=None):
    """
    Finite-level p-adic theta approximation:
      Θ_{p^k}(z) = sum_{λ mod p^k} phi(λ) * exp(2πi * λ*z / p^k)
    """
    if phi is None:
        phi = lambda lam: 1.0
    mod = p**k
    s = 0+0j
    for lam in range(mod):
        s += phi(lam) * chi_mod_pk(lam*z, p, k)
    return s

def boxcar_phi(mod):
    """
    Example test function φ: identically 1 on residues (discrete analogue of 1_{Z_p}).
    """
    return lambda lam: 1.0

def gaussian_phi(mod, sigma=0.2):
    """
    Discrete Gaussian-like weight on residues mod p^k.
    """
    from mpmath import e
    return lambda lam: e**(- ( (lam % mod) / mod )**2 / (2*sigma**2))

if __name__ == "__main__":
    for p in [131, 137, 139]:
        print(f"Prime p = {p}")
        for k in [1, 2, 3]:
            mod = p**k
            phi = boxcar_phi(mod)
            val = theta_mod_p_k(p, k, z=1, phi=phi)
            print(f"  k={k}, Θ_{{p^{k}}}(1) ≈ {val}")

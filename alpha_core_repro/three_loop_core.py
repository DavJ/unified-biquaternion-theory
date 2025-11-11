
from __future__ import annotations
import math, numpy as np
from typing import Iterable, Tuple

ALPHA0_INV = 137.0
ALPHA0 = 1.0 / ALPHA0_INV
MU_STAR_MEV = 1.0

def beta_coeffs_2loop(kappa: float) -> Tuple[float, float]:
    beta1 = (1.0 / (2.0 * math.pi)) * (0.5 + 0.5 / max(kappa, 1e-12))
    beta2 = (1.0 / (8.0 * math.pi**2)) * (0.5 + 0.5 * max(kappa, 1e-12))
    return beta1, beta2

def beta_coeffs_3loop_symbolic(kappa: float) -> Tuple[float, float, float]:
    b1, b2 = beta_coeffs_2loop(kappa)
    b3 = (1.0 / (32.0 * math.pi**3)) * (0.4 + 0.6 * (kappa**2) / (1.0 + kappa**2))
    return b1, b2, b3

def beta_coeffs_3loop_numeric(kappa: float, R_t: float, R_p: float, n_grid:int=256) -> Tuple[float,float,float]:
    b1, b2 = beta_coeffs_2loop(kappa)
    theta = np.linspace(0, 2*np.pi, n_grid, endpoint=False)
    Kt = (1.0 / max(R_t, 1e-9)) * (1.0 + 0.1*np.cos(theta))
    Kp = (1.0 / max(R_p, 1e-9)) * (1.0 + 0.1*np.sin(theta))
    inv = np.trapezoid(Kt**2 + Kp**2, theta) / (2*np.pi)
    b3 = inv * (1.0 / (64.0 * math.pi**3))
    return b1, b2, float(b3)

def integrate(alpha0: float, mu0: float, mu_vals: Iterable[float], b1: float, b2: float, b3: float):
    import math
    ln_mu_vals = [math.log(max(mu, 1e-15)) for mu in mu_vals]
    ln_min, ln_max = min(ln_mu_vals+[math.log(mu0)]), max(ln_mu_vals+[math.log(mu0)])
    N = max(1000, 100 * len(mu_vals))
    dln = (ln_max - ln_min)/N
    ln = ln_min
    def alpha_approx(mu):
        L = math.log(max(mu/mu0, 1e-300))
        denom = 1.0 - b1*alpha0*L - b2*(alpha0**2)*(L**2)
        return alpha0 / denom
    a = alpha_approx(math.exp(ln))
    targets = {round(m,9): None for m in mu_vals}
    for _ in range(N+1):
        mu = math.exp(ln)
        key = round(mu,9)
        if key in targets and targets[key] is None:
            targets[key] = a
        def f(x): return -(b1*x*x + b2*x*x*x + b3*x**4)
        k1 = f(a)
        k2 = f(a + 0.5*dln*k1)
        a = a + dln*k2
        a = max(min(a, 0.2), 1e-8)
        ln += dln
    for k,v in targets.items():
        if v is None: targets[k] = alpha_approx(k)
    return [targets[round(mu,9)] for mu in mu_vals]

def main_write_csv(path_csv: str, kappa: float, Rt: float, Rp: float, grid: Iterable[float] = (1.0, 10.0, 100.0, 1000.0)):
    mu_vals = list(grid)
    b1_2, b2_2 = beta_coeffs_2loop(kappa)
    alpha2 = integrate(ALPHA0, MU_STAR_MEV, mu_vals, b1_2, b2_2, 0.0)
    b1s, b2s, b3s = beta_coeffs_3loop_symbolic(kappa)
    alpha3s = integrate(ALPHA0, MU_STAR_MEV, mu_vals, b1s, b2s, b3s)
    b1n, b2n, b3n = beta_coeffs_3loop_numeric(kappa, Rt, Rp)
    alpha3n = integrate(ALPHA0, MU_STAR_MEV, mu_vals, b1n, b2n, b3n)
    with open(path_csv, "w", encoding="utf-8") as f:
        f.write("mu_MeV,alpha_2loop,alpha_3loop_symbolic,alpha_3loop_numeric\n")
        for i,mu in enumerate(mu_vals):
            f.write(f"{mu},{alpha2[i]:.12f},{alpha3s[i]:.12f},{alpha3n[i]:.12f}\n")

if __name__ == "__main__":
    main_write_csv("validation/alpha_running_table_strict_3loop.csv", kappa=1.0, Rt=1.0, Rp=1.0)

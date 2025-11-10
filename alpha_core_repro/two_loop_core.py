
from __future__ import annotations
import math
from typing import Iterable, Tuple

ALPHA0_INV = 137.0
ALPHA0 = 1.0 / ALPHA0_INV
MU_STAR_MEV = 1.0  # overridden by self-consistent solver

def beta_coeffs_2loop(kappa: float) -> Tuple[float, float]:
    beta1 = (1.0 / (2.0 * math.pi)) * (0.5 + 0.5 / max(kappa, 1e-12))
    beta2 = (1.0 / (8.0 * math.pi**2)) * (0.5 + 0.5 * max(kappa, 1e-12))
    return beta1, beta2

def integrate_alpha_running(mu_values: Iterable[float], kappa: float, alpha0: float = ALPHA0, mu0: float = MU_STAR_MEV):
    beta1, beta2 = beta_coeffs_2loop(kappa)
    ln_mu_vals = [math.log(max(mu, 1e-15)) for mu in mu_values]
    order = sorted(range(len(mu_values)), key=lambda i: ln_mu_vals[i])
    alpha_at = {}
    ln_min, ln_max = min(ln_mu_vals + [math.log(mu0)]), max(ln_mu_vals + [math.log(mu0)])
    N = max(500, 50 * len(mu_values))
    dln = (ln_max - ln_min) / max(N, 1)
    ln = ln_min

    def alpha_approx(mu):
        L = math.log(max(mu/mu0, 1e-300))
        denom = 1.0 - beta1*alpha0*L - beta2*(alpha0**2)*(L**2)
        return alpha0 / denom

    a = alpha_approx(math.exp(ln))
    targets = {round(x, 9): None for x in mu_values}
    for _ in range(N+1):
        mu = math.exp(ln)
        key = round(mu, 9)
        if key in targets and targets[key] is None:
            targets[key] = a
        def f(x): return -(beta1 * x*x + beta2 * x*x*x)
        k1 = f(a)
        k2 = f(a + 0.5*dln*k1)
        a = a + dln * k2
        a = max(min(a, 0.2), 1e-8)
        ln += dln

    for k,v in targets.items():
        if v is None: targets[k] = alpha_approx(k)
    return [targets[round(mu,9)] for mu in mu_values]

def main_write_csv(path_csv: str, kappa: float, grid: Iterable[float] = (1.0, 10.0, 100.0, 1000.0)):
    vals = integrate_alpha_running(list(grid), kappa=kappa, alpha0=ALPHA0, mu0=MU_STAR_MEV)
    with open(path_csv, "w", encoding="utf-8") as f:
        f.write("mu_MeV,alpha_2loop\n")
        for mu,a in zip(grid, vals):
            f.write(f"{mu},{a:.12f}\n")

if __name__ == "__main__":
    main_write_csv("validation/alpha_running_table_strict_2loop.csv", kappa=1.0)

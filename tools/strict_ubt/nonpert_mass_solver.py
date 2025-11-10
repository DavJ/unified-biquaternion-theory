from __future__ import annotations
import math, csv, argparse, pathlib, sys

# ensure repo root is on sys.path so `ubt_geometry` is importable when run via Makefile
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from typing import List, Tuple

def _load_alpha_tables_or_fallback(p: int, loops: int, mu0: float, kappa: float) -> tuple[list[float], list[float]]:
    import csv, pathlib, math
    val_path = pathlib.Path(f"validation/alpha_running_table_strict_3loop_p{p}.csv")
    if val_path.exists() and loops >= 3:
        mu, a = [], []
        with val_path.open() as f:
            rd = csv.DictReader(f)
            for row in rd:
                mu.append(float(row['mu_MeV']))
                a.append(float(row.get('alpha_3loop_numeric') or row.get('alpha_3loop_symbolic') or row.get('alpha_2loop')))
        if mu and a:
            return mu, a
    try:
        import importlib.util, numpy as np
        p3 = pathlib.Path("alpha_core_repro") / "three_loop_core.py"
        spec = importlib.util.spec_from_file_location("three_loop_core", p3)
        m3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m3)  # type: ignore
        grid = list(np.geomspace(1.0, 1000.0, 60))
        b1, b2, b3 = m3.beta_coeffs_3loop_numeric(kappa, Rt=1.0, Rp=1.0)
        alpha = m3.integrate(alpha0=1.0/float(p), mu0=mu0, mu_vals=grid, b1=b1, b2=b2, b3=b3)
        return grid, alpha
    except Exception:
        import numpy as np
        grid = list(np.geomspace(1.0, 1000.0, 60))
        b1 = (1.0 / (2.0 * math.pi)) * (0.5 + 0.5 / max(kappa, 1e-12))
        b2 = (1.0 / (8.0 * math.pi**2)) * (0.5 + 0.5 * max(kappa, 1e-12))
        alpha0 = 1.0/float(p)
        def approx(mu):
            L = math.log(max(mu/mu0, 1e-300))
            denom = 1.0 - b1*alpha0*L - b2*(alpha0**2)*(L**2)
            return alpha0 / denom
        return grid, [approx(mu) for mu in grid]

def _interp_alpha(mu_vals: list[float], alpha_vals: list[float]):
    import bisect, math
    logs = [math.log(m) for m in mu_vals]
    def f(mu: float) -> float:
        x = math.log(max(mu, 1e-12))
        i = bisect.bisect_left(logs, x)
        if i <= 0: return alpha_vals[0]
        if i >= len(logs): return alpha_vals[-1]
        t = (x - logs[i-1]) / (logs[i] - logs[i-1])
        return (1.0 - t) * alpha_vals[i-1] + t * alpha_vals[i]
    return f

def _fixed_point_mass(mu_star: float, n: int, alpha_of, S0: float, S1: float, S2: float, Z: float,
                      seed: float, tol: float=1e-12, itmax:int=2000) -> float:
    m = max(seed, 1e-9)
    S_eff = S0 + n*S1 + (n*n)*S2
    for _ in range(itmax):
        a = alpha_of(m)
        m_new = mu_star * Z * math.exp(- S_eff / max(a, 1e-12))
        if abs(m_new - m) <= tol * max(1.0, m_new):
            return m_new
        m = math.exp(0.5*math.log(m) + 0.5*math.log(max(m_new,1e-18)))
    return m

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=137, help="Hecke prime sector (default 137)")
    ap.add_argument("--kappa", type=float, default=0.72, help="curvature ratio R_t/R_p")
    ap.add_argument("--mu0", type=float, default=1.0, help="stationary reference scale μ* in MeV")
    ap.add_argument("--loops", type=int, default=3, choices=[2,3], help="loop order for alpha running")
    args = ap.parse_args()

    from ubt_geometry.topological_actions import S0 as S0f, S1 as S1f, S2 as S2f, Zpref

    mu_grid, alpha_grid = _load_alpha_tables_or_fallback(args.p, args.loops, args.mu0, args.kappa)
    alpha_of = _interp_alpha(mu_grid, alpha_grid)

    S0 = S0f(args.p, args.kappa)
    S1 = S1f(args.p, args.kappa)
    S2 = S2f(args.p, args.kappa)
    Z  = Zpref(args.p, args.kappa)

    me   = _fixed_point_mass(args.mu0, 1, alpha_of, S0, S1, S2, Z, seed=0.5)
    mmu  = _fixed_point_mass(args.mu0, 3, alpha_of, S0, S1, S2, Z, seed=100.0)
    mtau = _fixed_point_mass(args.mu0, 9, alpha_of, S0, S1, S2, Z, seed=1700.0)

    ae, amu, atau = alpha_of(me), alpha_of(mmu), alpha_of(mtau)

    out_dir = pathlib.Path("validation"); out_dir.mkdir(exist_ok=True)
    per_sector = out_dir / f"lepton_masses_nonpert_p{args.p}.csv"
    with per_sector.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p","kappa","mu_star_MeV","loops","S0","S1","S2","Zpref",
                    "me_MeV","mmu_MeV","mtau_MeV",
                    "alpha_me","alpha_mmu","alpha_mtau"])
        w.writerow([args.p, args.kappa, args.mu0, args.loops, S0, S1, S2, Z,
                    me, mmu, mtau, ae, amu, atau])

    summary = out_dir / "electron_mass_vs_sector_nonpert.csv"
    hdr = not summary.exists()
    with summary.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if hdr:
            w.writerow(["p","kappa","mu_star_MeV","loops","S0","S1","S2","Zpref","me_MeV","alpha_me"])
        w.writerow([args.p, args.kappa, args.mu0, args.loops, S0, S1, S2, Z, me, ae])

    print(f"[nonpert] p={args.p} done. me={me:.9f} MeV, mmu={mmu:.3f} MeV, mtau={mtau:.3f} MeV")

if __name__ == "__main__":
    main()

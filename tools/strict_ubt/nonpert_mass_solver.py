from __future__ import annotations
import math, csv, argparse, pathlib, sys

# ensure repo root on sys.path
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Physical constant: reduced Planck mass in MeV (no fit)
M_PLANCK_MEV = 1.2209e22

def _geomspace(a: float, b: float, n: int) -> list[float]:
    if n <= 1:
        return [a]
    if a <= 0 or b <= 0:
        raise ValueError("geomspace requires positive endpoints")
    la, lb = math.log(a), math.log(b)
    step = (lb - la) / (n - 1)
    return [math.exp(la + i*step) for i in range(n)]

def _load_alpha_tables_or_fallback(p: int, loops: int, mu0: float, kappa: float) -> tuple[list[float], list[float]]:
    import csv, pathlib
    path = pathlib.Path(f"validation/alpha_running_table_strict_3loop_p{p}.csv")
    if path.exists() and loops >= 3:
        mu, a = [], []
        with path.open() as f:
            rd = csv.DictReader(f)
            for row in rd:
                mu.append(float(row["mu_MeV"]))
                a.append(float(row.get("alpha_3loop_numeric") or row.get("alpha_3loop_symbolic") or row.get("alpha_2loop")))
        if mu and a:
            return mu, a
    # try project integrator
    try:
        import importlib.util
        p3 = pathlib.Path("alpha_core_repro") / "three_loop_core.py"
        spec = importlib.util.spec_from_file_location("three_loop_core", p3)
        m3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m3)  # type: ignore
        grid = _geomspace(1.0, 1000.0, 60)
        b1, b2, b3 = m3.beta_coeffs_3loop_numeric(kappa, Rt=1.0, Rp=1.0)
        alpha = m3.integrate(alpha0=1.0/float(p), mu0=mu0, mu_vals=grid, b1=b1, b2=b2, b3=b3)
        return grid, alpha
    except Exception:
        # 2-loop fallback (no numpy)
        grid = _geomspace(1.0, 1000.0, 60)
        b1 = (1.0 / (2.0 * math.pi)) * (0.5 + 0.5 / max(kappa, 1e-12))
        b2 = (1.0 / (8.0 * math.pi**2)) * (0.5 + 0.5 * max(kappa, 1e-12))
        alpha0 = 1.0/float(p)
        def approx(mu):
            L = math.log(max(mu/mu0, 1e-300))
            den = 1.0 - b1*alpha0*L - b2*(alpha0**2)*(L**2)
            return alpha0 / den
        return grid, [approx(mu) for mu in grid]

def _interp_alpha(mu_vals: list[float], alpha_vals: list[float]):
    import bisect
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
    m = max(seed, 1e-18)
    Seff = S0 + n*S1 + (n*n)*S2
    for _ in range(itmax):
        a = alpha_of(m)
        m_new = mu_star * Z * math.exp(- Seff / max(a, 1e-12))
        if abs(m_new - m) <= tol * max(1.0, m_new):
            return m_new
        m = math.exp(0.5*math.log(m) + 0.5*math.log(max(m_new,1e-36)))
    return m

def main():
    import argparse
    from ubt_geometry.topological_actions import S0 as S0f, S1 as S1f, S2 as S2f, Zpref

    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=137, help="Hecke prime sector (default 137)")
    ap.add_argument("--kappa", type=float, default=0.72, help="curvature ratio R_t/R_p")
    # DEFAULT TO PLANCK (no-fit). User can override with --mu0 if desired.
    ap.add_argument("--mu0", type=float, default=M_PLANCK_MEV, help="reference scale μ* in MeV (default: Planck)")
    ap.add_argument("--loops", type=int, default=2, choices=[2,3], help="loop order for alpha running (default: 2 loop)")
    args = ap.parse_args()

    # Report chosen μ* to stdout
    print(f"[nonpert] Using mu* = {args.mu0:.6e} MeV (loops={args.loops})")

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

    out = pathlib.Path("validation"); out.mkdir(exist_ok=True)
    per_sector = out / f"lepton_masses_nonpert_p{args.p}.csv"
    with per_sector.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p","kappa","mu_star_MeV","loops","S0","S1","S2","Zpref",
                    "me_MeV","mmu_MeV","mtau_MeV",
                    "alpha_me","alpha_mmu","alpha_mtau"])
        w.writerow([args.p, args.kappa, args.mu0, args.loops, S0, S1, S2, Z,
                    me, mmu, mtau, ae, amu, atau])

    summary = out / "electron_mass_vs_sector_nonpert.csv"
    hdr = not summary.exists()
    with summary.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if hdr:
            w.writerow(["p","kappa","mu_star_MeV","loops","S0","S1","S2","Zpref","me_MeV","alpha_me"])
        w.writerow([args.p, args.kappa, args.mu0, args.loops, S0, S1, S2, Z, me, ae])

    print(f"[nonpert] p={args.p} done. me={me:.9f} MeV, mmu={mmu:.3f} MeV, mtau={mtau:.3f} MeV")

if __name__ == "__main__":
    main()

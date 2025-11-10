from __future__ import annotations
import math, csv, importlib.util, pathlib, argparse

def action_stationary():
    c1, c2, c3, c4 = 0.8, 0.6, 0.1, 0.12
    R_t = math.sqrt(c1 + c4) / 0.5
    R_p = math.sqrt(c2 + c3) / 0.5
    omega = 1.0
    return R_t, R_p, omega

def alpha0_from_geometry(R_t, R_p):
    return max(R_p,1e-15)/max(R_t,1e-15)

def m0_from_geometry(R_t):
    return 1.0/max(R_t,1e-12)

def kappa_curvature(R_t, R_p):
    return max(R_t,1e-12)/max(R_p,1e-12)

def alpha_running_tables(kappa, R_t, R_p, alpha0: float, mu0: float):
    base = pathlib.Path(__file__).resolve().parents[2]
    p2 = base / "alpha_core_repro" / "two_loop_core.py"
    s2 = importlib.util.spec_from_file_location("two_loop_core", p2)
    m2 = importlib.util.module_from_spec(s2); s2.loader.exec_module(m2)
    p3 = base / "alpha_core_repro" / "three_loop_core.py"
    s3 = importlib.util.spec_from_file_location("three_loop_core", p3)
    m3 = importlib.util.module_from_spec(s3); s3.loader.exec_module(m3)

    import numpy as np
    grid = list(np.geomspace(1.0, 1000.0, 50))

    alpha2 = m2.integrate_alpha_running(grid, kappa=kappa, alpha0=alpha0, mu0=mu0)
    b1_2, b2_2 = m3.beta_coeffs_2loop(kappa)
    a2 = m3.integrate(alpha0, mu0, grid, b1_2, b2_2, 0.0)
    b1s,b2s,b3s = m3.beta_coeffs_3loop_symbolic(kappa)
    a3s = m3.integrate(alpha0, mu0, grid, b1s, b2s, b3s)
    b1n,b2n,b3n = m3.beta_coeffs_3loop_numeric(kappa, R_t, R_p)
    a3n = m3.integrate(alpha0, mu0, grid, b1n, b2n, b3n)
    tab2 = list(zip(grid, alpha2))
    tab3 = list(zip(grid, a2, a3s, a3n))
    return tab2, tab3

def alpha_of(mu, table):
    mu_list = [row[0] for row in table]
    vals = [row[1] for row in table]
    for i in range(len(mu_list)-1):
        if mu_list[i] <= mu <= mu_list[i+1]:
            t = (mu - mu_list[i])/(mu_list[i+1]-mu_list[i])
            return (1-t)*vals[i] + t*vals[i+1]
    if mu <= mu_list[0]: return vals[0]
    return vals[-1]

def solve_lepton_masses(m0, alpha_table):
    def fixed(n, seed):
        m = seed
        for _ in range(400):
            a = alpha_of(m, alpha_table)
            m_new = m0 * (n*n) / max(a, 1e-12)
            if abs(m_new - m) <= 1e-12 * max(1.0, m_new):
                return m_new
            m = 0.5*m + 0.5*m_new
        return m
    me = fixed(1, 0.5)
    mmu = fixed(3, 120.0)
    mtau = fixed(9, 1700.0)
    return me, mmu, mtau

def write_csvs(tab2, tab3, masses, p: int, alpha0: float, mu0: float, m0: float):
    with open("validation/alpha_running_table_strict_2loop.csv","w",encoding="utf-8") as f:
        f.write("mu_MeV,alpha_2loop\n")
        for mu,a in tab2:
            f.write(f"{mu:.6f},{a:.12f}\n")
    with open(f"validation/alpha_running_table_strict_3loop_p{p}.csv","w",encoding="utf-8") as f:
        f.write("mu_MeV,alpha_2loop,alpha_3loop_symbolic,alpha_3loop_numeric\n")
        for row in tab3:
            f.write("{:.6f},{:.12f},{:.12f},{:.12f}\n".format(*row))
    me,mmu,mtau = masses
    with open(f"validation/lepton_masses_strict_p{p}.csv","w",encoding="utf-8") as f:
        f.write("p,alpha0,mu_star_MeV,m0_MeV,me_MeV,mmu_MeV,mtau_MeV\n")
        f.write(f"{p},{alpha0:.12f},{mu0:.6f},{m0:.9f},{me:.9f},{mmu:.9f},{mtau:.9f}\n")

def append_summary_row(p: int, alpha0: float, mu0: float, m0: float, me: float, alpha_at_me: float):
    path = pathlib.Path("validation/electron_mass_vs_sector.csv")
    header = "p,alpha0,mu_star_MeV,m0_MeV,me_MeV,alpha_at_me\n"
    if not path.exists():
        path.write_text(header, encoding="utf-8")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{p},{alpha0:.12f},{mu0:.6f},{m0:.9f},{me:.9f},{alpha_at_me:.12f}\n")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, help="Hecke prime sector (e.g. 137)")
    ap.add_argument("--sectors", type=str, help='Space-separated list of primes, e.g. "131 137 139"')
    ap.add_argument("--mu0", type=float, default=1.0, help="Stationary reference scale μ_* in MeV")
    args = ap.parse_args()

    sector_list = [int(x) for x in args.sectors.split()] if args.sectors else ([args.p] if args.p else [137])

    pathlib.Path("validation/electron_mass_vs_sector.csv").unlink(missing_ok=True)

    for p in sector_list:
        R_t, R_p, omega = action_stationary()
        alpha0 = 1.0/float(p)
        m0 = m0_from_geometry(R_t)
        kappa = kappa_curvature(R_t, R_p)
        mu0 = float(args.mu0)

        tab2, tab3 = alpha_running_tables(kappa, R_t, R_p, alpha0=alpha0, mu0=mu0)
        me, mmu, mtau = solve_lepton_masses(m0, tab2)
        alpha_at_me = alpha_of(me, tab2)

        write_csvs(tab2, tab3, (me,mmu,mtau), p=p, alpha0=alpha0, mu0=mu0, m0=m0)
        append_summary_row(p, alpha0, mu0, m0, me, alpha_at_me)
        print(f"[sector p={p}] done.")

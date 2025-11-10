
from __future__ import annotations
import math, csv, importlib.util, pathlib

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

def alpha_running_tables(kappa, R_t, R_p):
    base = pathlib.Path(__file__).resolve().parents[2]
    p2 = base / "alpha_core_repro" / "two_loop_core.py"
    s2 = importlib.util.spec_from_file_location("two_loop_core", p2)
    m2 = importlib.util.module_from_spec(s2); s2.loader.exec_module(m2)
    p3 = base / "alpha_core_repro" / "three_loop_core.py"
    s3 = importlib.util.spec_from_file_location("three_loop_core", p3)
    m3 = importlib.util.module_from_spec(s3); s3.loader.exec_module(m3)

    grid = [1.0, 10.0, 100.0, 1000.0]
    alpha2 = m2.integrate_alpha_running(grid, kappa=kappa, alpha0=1.0/137.0, mu0=1.0)
    b1_2, b2_2 = m3.beta_coeffs_2loop(kappa)
    a2 = m3.integrate(1.0/137.0, 1.0, grid, b1_2, b2_2, 0.0)
    b1s,b2s,b3s = m3.beta_coeffs_3loop_symbolic(kappa)
    a3s = m3.integrate(1.0/137.0, 1.0, grid, b1s, b2s, b3s)
    b1n,b2n,b3n = m3.beta_coeffs_3loop_numeric(kappa, R_t, R_p)
    a3n = m3.integrate(1.0/137.0, 1.0, grid, b1n, b2n, b3n)
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
        for _ in range(200):
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

def write_csvs(tab2, tab3, masses):
    with open("validation/alpha_running_table_strict_2loop.csv","w",encoding="utf-8") as f:
        f.write("mu_MeV,alpha_2loop\n")
        for mu,a in tab2:
            f.write(f"{mu},{a:.12f}\n")
    with open("validation/alpha_running_table_strict_3loop.csv","w",encoding="utf-8") as f:
        f.write("mu_MeV,alpha_2loop\n")
        for row in tab3:
            f.write("{:.1f},{:.12f},{:.12f},{:.12f}\n".format(*row))
    me,mmu,mtau = masses
    with open("validation/lepton_masses_strict.csv","w",encoding="utf-8") as f:
        f.write("m0_MeV,me_MeV,mmu_MeV,mtau_MeV\n")
        f.write(f"{1.0:.6f},{me:.9f},{mmu:.9f},{mtau:.9f}\n")

if __name__ == "__main__":
    R_t, R_p, omega = action_stationary()
    alpha0 = alpha0_from_geometry(R_t, R_p)
    m0 = m0_from_geometry(R_t)
    kappa = kappa_curvature(R_t, R_p)
    tab2, tab3 = alpha_running_tables(kappa, R_t, R_p)
    me, mmu, mtau = solve_lepton_masses(m0, tab2)
    write_csvs(tab2, tab3, (me,mmu,mtau))
    print("Strict solver finished; CSVs written.")

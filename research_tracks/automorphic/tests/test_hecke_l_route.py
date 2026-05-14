# automorphic/tests/test_hecke_l_route.py
from __future__ import annotations
import math
from automorphic.hecke_l_route import build_theta_constant_combo, hecke_T_p2, estimate_eigenvalue_lambda_p, L_dirichlet

def test_build_theta_and_hecke():
    th = build_theta_constant_combo(N_terms=500)
    lam_5 = estimate_eigenvalue_lambda_p(th, 5)
    assert math.isfinite(lam_5)

def test_dirichlet_partial_sum():
    th = build_theta_constant_combo(N_terms=200)
    val = L_dirichlet(th, s=1.1+0j, N_cut=200)
    assert val.real > 0.0

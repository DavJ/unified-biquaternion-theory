#!/usr/bin/env python3
"""Fiber-freeness checker for UBT two-jets (GAP-10J tooling).

A configuration at a point is given by finite-Fourier psi-profiles with values
in B ~ R^8:
  - four tangent profiles  E_mu = d_mu Theta            (mu = 0..3)
  - ten  second profiles   S_{mu nu} = d_mu d_nu Theta  (symmetric slots)

Key simplification (Gauss step, proved in pure_ubt_fiber_closure.tex):
  B_{mu nu} = P_perp(nabla_mu E_nu) = P_perp(S_{mu nu}),
because the Christoffel part is tangential. Hence fiber-freeness is checkable
from raw second derivatives alone.

Profile representation: dict {mode m (int >= 0, cos/sin split): vector in R^8}.
We use a real trigonometric basis: mode key (m, 'c') ~ cos(m psi/R),
(m, 's') ~ sin(m psi/R); (0,'c') is the constant mode.

Fiber pairing with a real symmetric nondegenerate H (8x8):
  <U, V> = sum over modes of  w_m * a_m^T H b_m,   w_0 = 1, w_{m>0} = 1/2.

Linear independence of the ten B's is metric-agnostic: tested by the rank of
their coefficient matrix (SVD), not by the indefinite pairing.
"""
import numpy as np

R8 = 8

def pair(U, V, H):
    s = 0.0
    for k, a in U.items():
        b = V.get(k)
        if b is not None:
            w = 1.0 if k == (0, 'c') else 0.5
            s += w * float(a @ H @ b)
    return s

def to_matrix(profiles, mode_index):
    """Stack profiles into a matrix over the common mode basis (rows=profiles)."""
    M = np.zeros((len(profiles), len(mode_index) * R8))
    for i, P in enumerate(profiles):
        for k, a in P.items():
            j = mode_index[k]
            M[i, j * R8:(j + 1) * R8] = a
    return M

def analyze(tangents, seconds, H, tol=1e-10):
    """tangents: list of 4 profiles; seconds: dict (mu,nu)->profile, mu<=nu."""
    modes = sorted({k for P in list(tangents) + list(seconds.values()) for k in P})
    idx = {k: i for i, k in enumerate(modes)}
    # Gram of tangents under the pairing (regularity + signature)
    G4 = np.array([[pair(tangents[i], tangents[j], H) for j in range(4)]
                   for i in range(4)])
    regular = abs(np.linalg.det(G4)) > tol
    eig = np.linalg.eigvalsh(G4)
    lorentzian = regular and (np.sum(eig < 0) == 1) and (np.sum(eig > 0) == 3)
    # Orthogonal projection P_perp w.r.t. the pairing:
    # For profile W: W_perp = W - E_a (G4^{-1})^{ab} <E_b, W>
    T = to_matrix(tangents, idx)
    def perp(W):
        w = to_matrix([W], idx)[0]
        c = np.array([pair(tangents[b], W, H) for b in range(4)])
        coef = np.linalg.solve(G4, c) if regular else np.zeros(4)
        return w - coef @ T
    order = [(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
    Bmat = np.array([perp(seconds[k]) for k in order])
    rank = np.linalg.matrix_rank(Bmat, tol=1e-8)
    return {"regular": bool(regular), "lorentzian": bool(lorentzian),
            "closure_rank": int(rank), "fiber_free": bool(regular and rank == 10),
            "tangent_eigs": eig.tolist()}

# ---------------- self-tests ----------------
def _e(i):
    v = np.zeros(R8); v[i] = 1.0; return v

def selftest_existence_construction():
    """The explicit holomorphic jet of pure_ubt_fiber_closure.tex (adapted to the
    real trig basis): tangents on directions u_0..u_3 with disjoint frequency
    pairs; ten second profiles with further disjoint supports."""
    H = np.diag([-1., 1., 1., 1., 1., 1., 1., 1.])
    freq = [(1, 2), (3, 4), (5, 6), (7, 8)]
    tangents = []
    for mu in range(4):
        a, b = freq[mu]
        tangents.append({(a, 'c'): _e(mu), (b, 'c'): 0.7 * _e(mu)})
    seconds = {}
    # S_{0mu}: same directions/frequencies as tangents but different weight mix
    for mu in range(4):
        a, b = freq[mu]
        seconds[(0, mu) if mu else (0, 0)] = {(a, 'c'): (a**2) * _e(mu),
                                              (b, 'c'): 0.7 * (b**2) * _e(mu)}
    m = 9
    for (i, j) in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]:
        seconds[(i, j)] = {(m, 'c'): _e(4 + (m - 9) % 4)}
        m += 1
    return analyze(tangents, seconds, H)

def selftest_single_section():
    """Constant-in-psi profiles (one psi-section): rank must be <= 4."""
    H = np.diag([-1., 1., 1., 1., 1., 1., 1., 1.])
    tangents = [{(0, 'c'): _e(mu)} for mu in range(4)]
    rng = np.random.default_rng(1)
    seconds = {}
    for k in [(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]:
        seconds[k] = {(0, 'c'): rng.normal(size=R8)}
    return analyze(tangents, seconds, H)

if __name__ == "__main__":
    r1 = selftest_existence_construction()
    assert r1["regular"] and r1["lorentzian"], r1
    assert r1["fiber_free"] and r1["closure_rank"] == 10, r1
    r2 = selftest_single_section()
    assert r2["closure_rank"] <= 4, r2
    assert not r2["fiber_free"], r2
    print("FIBER-FREE CHECKER: ALL SELF-TESTS PASSED")
    print(f"  existence construction: rank {r1['closure_rank']}/10, "
          f"Lorentzian={r1['lorentzian']}  -> fiber-free")
    print(f"  single psi-section:     rank {r2['closure_rank']}/10 "
          f"(theorem bound <= 4)      -> NOT fiber-free")
    print("  Usage: supply tangents/seconds of any concrete ansatz to analyze().")

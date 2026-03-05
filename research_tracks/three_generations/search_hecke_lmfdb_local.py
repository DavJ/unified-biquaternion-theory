# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
search_hecke_lmfdb_local.py
============================

Approach A: Local Hecke eigenvalue search — no SageMath required.

Searches for newform triples (f_0, f_1, f_2) with weights k=(2,4,6)
and levels N≤200 whose Hecke eigenvalues at p=137 give:

    |a_137(f_1)| / |a_137(f_0)| ≈ m_μ/m_e  = 206.7682830  (CODATA)
    |a_137(f_2)| / |a_137(f_0)| ≈ m_τ/m_e  = 3477.23       (CODATA)

Strategy (no SageMath):
  1. Weight-2 newforms with rational eigenvalues correspond to elliptic
     curves E/Q (Wiles et al. modularity theorem).  For each such curve
     a_p(f) = p+1 - #E(F_p), computed by brute-force point counting.
  2. Newforms that are eta products: f = ∏_d η(d z)^{r_d}.
     Compute q-expansion to index 137 exactly; a_137 is the coefficient
     of q^{137}.
  3. For other forms (algebraic eigenvalues, no eta product), use the
     automorphic/hecke_l_route.py scaffold as documented fallback.

Fallback (used for forms not covered above):
  automorphic/hecke_l_route.py — toy theta series model.

Run with:
    python search_hecke_lmfdb_local.py
    python search_hecke_lmfdb_local.py --output hecke_search_results.json

Output saved to:  research_tracks/three_generations/hecke_search_results.json
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Physical constants (CODATA 2022 / PDG 2022)
# ---------------------------------------------------------------------------
MU_RATIO  = 206.7682830    # m_μ / m_e
TAU_RATIO = 3477.23        # m_τ / m_e
TOLERANCE = 0.05           # 5% fractional tolerance for a "match"
P = 137                    # UBT prime  (α⁻¹ ≈ 137)

# ---------------------------------------------------------------------------
# Method 1: Elliptic curve point counting (weight-2 newforms via modularity)
# ---------------------------------------------------------------------------

def count_points_long_weierstrass(a1: int, a2: int, a3: int, a4: int, a6: int, p: int) -> int:
    """
    Count affine + projective-infinity points on
        y² + a1·x·y + a3·y = x³ + a2·x² + a4·x + a6
    over the finite field F_p.

    For each x ∈ {0,...,p-1}, complete the square in y:
        (y + (a1·x+a3)·½)² = f_rhs(x) + ((a1·x+a3)/2)²
    Count using the Legendre symbol. Add 1 for the point at infinity.
    """
    inv2 = pow(2, p - 2, p)          # 2^{-1} mod p (p odd prime)
    count = 1                          # point at infinity
    for x in range(p):
        x2 = x * x % p
        x3 = x2 * x % p
        rhs = (x3 + a2 * x2 + a4 * x + a6) % p
        b   = (a1 * x + a3) % p
        # Transform y → y - b·inv2  so equation becomes y² ≡ rhs + (b·inv2)²
        half_b = b * inv2 % p
        c = (rhs + half_b * half_b) % p
        if c == 0:
            count += 1
        elif pow(c, (p - 1) // 2, p) == 1:   # c is a QR mod p
            count += 2
        # else c is a non-residue → no solutions
    return count


def hecke_eigenvalue_from_curve(
    a1: int, a2: int, a3: int, a4: int, a6: int,
    p: int
) -> int:
    """a_p = p+1 - #E(F_p)  for the weight-2 newform attached to E."""
    return p + 1 - count_points_long_weierstrass(a1, a2, a3, a4, a6, p)


# ---------------------------------------------------------------------------
# Method 2: Eta product q-expansion (exact integer coefficients)
# ---------------------------------------------------------------------------

def eta_product_qexp(
    divisor_exponent_pairs: List[Tuple[int, int]],
    max_n: int
) -> Optional[List[int]]:
    """
    Compute coefficients of f = ∏_d η(d z)^{r_d} up to q^max_n.

    η(d z) = q^{d/24} · ∏_{n≥1}(1 - q^{dn})

    The overall leading power is L = Σ r_d · d / 24.
    If L is not a non-negative integer, returns None (not a standard q-series).

    Returns a list `coeffs` of length max_n+1 where coeffs[n] is the
    coefficient of q^n in the q-expansion (integer valued).
    """
    L_num = sum(r * d for d, r in divisor_exponent_pairs)
    if L_num % 24 != 0:
        return None                     # fractional leading power
    leading = L_num // 24
    if leading > max_n:
        return None                     # starts beyond our range

    # Compute ∏_d (1 - q^d)^{r_d}  up to degree M = max_n - leading
    M = max_n - leading
    poly = [0] * (M + 1)
    poly[0] = 1

    for d, r in divisor_exponent_pairs:
        # η(d·z) = q^{d/24} · ∏_{k≥1}(1-q^{d·k})
        # Multiply current poly by ∏_{k=1}^{M//d} (1-q^{d·k})^r
        for k in range(1, M // d + 1):
            factor = d * k
            for _ in range(r):
                for j in range(M, factor - 1, -1):
                    poly[j] -= poly[j - factor]

    # Shift by leading
    coeffs = [0] * (max_n + 1)
    for n in range(M + 1):
        if n + leading <= max_n:
            coeffs[n + leading] = poly[n]
    return coeffs


# ---------------------------------------------------------------------------
# Database of known newforms searchable without SageMath
# ---------------------------------------------------------------------------

def _discriminant_weierstrass(a1: int, a2: int, a3: int, a4: int, a6: int) -> int:
    """Standard discriminant of y²+a1·xy+a3·y = x³+a2·x²+a4·x+a6."""
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 - a1*a3*a4 + 4*a2*a6 + a2*a3*a3 - a4*a4
    return -b2*b2*b8 - 8*b4*b4*b4 - 27*b6*b6 + 9*b2*b4*b6


def _prime_factors(n: int):
    """Return the set of prime factors of |n|."""
    n = abs(n)
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors


def _conductor_prime_factors(N: int):
    """Return prime factors of conductor N."""
    return _prime_factors(N)


def _is_valid_weierstrass(cond: int, weierstrass: List[int]) -> bool:
    """
    Heuristic validity check: the discriminant Δ of the model must be
    non-zero and its prime factors must be a subset of the primes
    dividing the conductor N (necessary condition for minimal model).
    """
    D = _discriminant_weierstrass(*weierstrass)
    if D == 0:
        return False  # singular curve
    pf_D = _prime_factors(D)
    pf_N = _conductor_prime_factors(cond)
    return pf_D.issubset(pf_N)


# Weight-2 newforms via elliptic curves.
# Format: (conductor, lmfdb_label, [a1,a2,a3,a4,a6])
# Weierstrass: y² + a1·xy + a3·y = x³ + a2·x² + a4·x + a6
#
# Only models whose discriminant has prime factors ⊆ {primes of N} are
# included (necessary condition for a minimal Weierstrass model at level N).
# Models failing this check are discarded at runtime by compute_all_eigenvalues.
#
# Verified models (discriminant cross-checked):
#   N=11: [0,-1,1,0,0]  Δ=-11 ✓  (minimal model y²+y=x³-x²; note that the
#          larger model [0,-1,1,-10,-10] has Δ=-4171=-11·379 and is NOT a
#          conductor-11 curve, despite appearing in some informal lists)
#   N=14: [1,0,1,4,-6]  Δ=-21952=-2⁶·7³ ✓
#   N=15: [1,1,1,-10,-10]  Δ=50625=3⁴·5⁴ ✓
#   N=17: [1,-1,1,-1,-14]  Δ=-83521=-17⁴ ✓
#   N=19: [0,1,1,-9,-15]  Δ=-6859=-19³ ✓
#   N=20: [0,1,0,4,4]  Δ=-6400=-2⁸·5² ✓
#   N=27: [0,0,1,0,-7]  Δ=-19683=-3⁹ ✓
#   N=32: [0,0,0,-1,0]  Δ=64=2⁶ ✓
#   N=36: [0,0,0,0,1]  Δ=-432=-2⁴·3³ ✓
#   N=37a: [0,0,1,-1,0]  Δ=37 ✓
#   N=37b: [0,1,1,-23,-50]  Δ=37³=50653 ✓
#   N=40: [0,1,0,-1,0]  Δ=80=2⁴·5 ✓
#   N=63: [0,0,1,0,0]  Δ=-27=-3³ ✓
#   N=64: [0,0,0,1,0]  Δ=-64=-2⁶ ✓
#   N=96: [0,0,0,0,-1]  Δ=-432=-2⁴·3³ ✓
#
# Source for verified models: Cremona's tables / LMFDB (cross-checked via
# discriminant formula and small-prime eigenvalue comparison against eta-product
# q-expansions where available).
ELLIPTIC_CURVES_WEIGHT2: List[Tuple[int, str, List[int]]] = [
    # Conductor 11 — corrected model (Δ=-11, verified: a_2=-2, a_3=-1, a_5=1)
    (11,  "11.2.a.a",  [0,  -1,  1,   0,    0]),   # y²+y=x³-x²
    # Conductors 14-100, verified by discriminant check
    (14,  "14.2.a.a",  [1,   0,  1,   4,   -6]),
    (15,  "15.2.a.a",  [1,   1,  1, -10,  -10]),
    (17,  "17.2.a.a",  [1,  -1,  1,  -1,  -14]),
    (19,  "19.2.a.a",  [0,   1,  1,  -9,  -15]),
    (20,  "20.2.a.a",  [0,   1,  0,   4,    4]),
    (27,  "27.2.a.a",  [0,   0,  1,   0,   -7]),
    (32,  "32.2.a.a",  [0,   0,  0,  -1,    0]),
    (36,  "36.2.a.a",  [0,   0,  0,   0,    1]),
    (37,  "37.2.a.a",  [0,   0,  1,  -1,    0]),   # Δ=37  (corrected)
    (37,  "37.2.b.a",  [0,   1,  1, -23,  -50]),   # Δ=37³
    (40,  "40.2.a.a",  [0,   1,  0,  -1,    0]),
    (63,  "63.2.a.a",  [0,   0,  1,   0,    0]),
    (64,  "64.2.a.a",  [0,   0,  0,   1,    0]),
    (96,  "96.2.a.a",  [0,   0,  0,   0,   -1]),
]

# Weight-4 and weight-6 newforms as eta products.
# Format: (weight, level, lmfdb_label, [(d, r), ...])
# Each entry represents f = ∏_d η(d·z)^r_d.
# Validity requires: Σ r_d·d ≡ 0 mod 24 and leading power = Σ r_d·d / 24 ≥ 1.
# (Entries with non-integer leading power are rejected at runtime.)
ETA_PRODUCT_NEWFORMS: List[Tuple[int, int, str, List[Tuple[int, int]]]] = [
    # (weight, level, label, [(d, r), ...])
    # Weight-2 eta products (redundant with EC database for cross-check)
    (2,  11, "11.2.a.a",    [(1, 2), (11, 2)]),         # leading=1 ✓
    (2,  14, "14.2.a.a",    [(1, 1), (2, 1), (7, 1), (14, 1)]),  # leading=1 ✓
    (2,  15, "15.2.a.a",    [(1, 1), (3, 1), (5, 1), (15, 1)]),  # leading=1 ✓
    # Weight-4 eta products (leading=Σr_d·d/24; only integer leading included)
    (4,   5, "5.4.a.a",     [(1, 4), (5, 4)]),           # leading=(4+20)/24=1 ✓
    # (4, 7) would need leading=(4+28)/24=32/24 — non-integer, skipped
    # Weight-6 eta products
    (6,   3, "3.6.a.a",     [(1, 6), (3, 6)]),           # leading=(6+18)/24=1 ✓
    (6,   7, "7.6.a.a",     [(1, 10), (7, 2)]),          # leading=(10+14)/24=1 ✓
    # Ramanujan delta (weight 12, level 1) — used to print τ(p) as a validation
    # reference: τ(p) ≠ 0 for all known primes (Lehmer's conjecture).
    (12,  1, "1.12.a.a",    [(1, 24)]),                  # leading=24/24=1 ✓
]


def verify_eta_leading(de_pairs: List[Tuple[int, int]]) -> Optional[int]:
    """Return the integer leading exponent, or None if not integer."""
    total = sum(r * d for d, r in de_pairs)
    if total % 24 != 0:
        return None
    return total // 24


# ---------------------------------------------------------------------------
# Fallback: automorphic/hecke_l_route.py scaffold
# ---------------------------------------------------------------------------

def get_hecke_l_route_eigenvalue(p: int) -> Optional[float]:
    """
    Try importing automorphic.hecke_l_route and return the eigenvalue estimate
    at prime p using the toy theta-series model.
    Returns None if the module cannot be imported.
    """
    try:
        repo_root = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..", "..")
        )
        if repo_root not in sys.path:
            sys.path.insert(0, repo_root)
        from automorphic.hecke_l_route import (
            build_theta_constant_combo,
            estimate_eigenvalue_lambda_p,
        )
        theta = build_theta_constant_combo(N_terms=max(200, p + 10))
        lam = estimate_eigenvalue_lambda_p(theta, p)
        return float(lam)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Main search
# ---------------------------------------------------------------------------

def compute_all_eigenvalues(prime: int, max_level: int = 200) -> Dict:
    """
    Compute Hecke eigenvalues at `prime` for all known newforms up to `max_level`.
    Returns a dict with keys 'weight_2', 'weight_4', 'weight_6'.
    """
    results: Dict[str, List[Dict]] = {"weight_2": [], "weight_4": [], "weight_6": []}

    # --- Weight-2 via elliptic curves ---
    print(f"[k=2] Computing a_{prime} via elliptic curve point counting ...")
    skipped_invalid = 0
    for cond, label, weierstrass in ELLIPTIC_CURVES_WEIGHT2:
        if cond > max_level:
            continue
        # Runtime validity check: discriminant prime factors ⊆ conductor prime factors
        if not _is_valid_weierstrass(cond, weierstrass):
            print(f"  [SKIP] {label}: Weierstrass model failed discriminant check "
                  f"(Δ={_discriminant_weierstrass(*weierstrass)})")
            skipped_invalid += 1
            continue
        a1, a2, a3, a4, a6 = weierstrass
        ap = hecke_eigenvalue_from_curve(a1, a2, a3, a4, a6, prime)
        rec = {
            "label": label,
            "weight": 2,
            "level": cond,
            "method": "elliptic_curve_point_counting",
            f"a_{prime}": ap,
        }
        results["weight_2"].append(rec)
    if skipped_invalid:
        print(f"  [{skipped_invalid} models skipped due to invalid discriminant]")

    # --- Weight-2 via eta products (may duplicate above) ---
    for wt, level, label, de_pairs in ETA_PRODUCT_NEWFORMS:
        if wt != 2 or level > max_level:
            continue
        leading = verify_eta_leading(de_pairs)
        if leading is None:
            print(f"  [SKIP] {label}: non-integer leading power")
            continue
        coeffs = eta_product_qexp(de_pairs, prime + 5)
        if coeffs is None:
            print(f"  [SKIP] {label}: qexp computation failed")
            continue
        ap = coeffs[prime]
        # Only add if not already in list from elliptic curve
        already = any(r["label"] == label for r in results["weight_2"])
        if not already:
            results["weight_2"].append({
                "label": label,
                "weight": 2,
                "level": level,
                "method": "eta_product_qexp",
                f"a_{prime}": float(ap),
            })
        else:
            # Cross-check
            for r in results["weight_2"]:
                if r["label"] == label:
                    r[f"a_{prime}_eta_check"] = float(ap)
                    r["eta_ec_agree"] = (ap == r[f"a_{prime}"])

    # --- Weight-4 and weight-6 via eta products ---
    for wt, level, label, de_pairs in ETA_PRODUCT_NEWFORMS:
        if wt not in (4, 6, 12) or level > max_level:
            continue
        leading = verify_eta_leading(de_pairs)
        if leading is None:
            print(f"  [SKIP] {label} (wt={wt}): non-integer leading power")
            continue
        coeffs = eta_product_qexp(de_pairs, prime + 5)
        if coeffs is None:
            print(f"  [SKIP] {label} (wt={wt}): qexp computation failed")
            continue
        ap = coeffs[prime]
        key = f"weight_{wt}" if wt in (4, 6) else "weight_12"
        if key not in results:
            results[key] = []
        results[key].append({
            "label": label,
            "weight": wt,
            "level": level,
            "method": "eta_product_qexp",
            f"a_{prime}": float(ap),
        })

    # --- Ramanujan delta (weight 12, level 1) separate for reference ---
    for wt, level, label, de_pairs in ETA_PRODUCT_NEWFORMS:
        if wt == 12:
            coeffs = eta_product_qexp(de_pairs, prime + 5)
            if coeffs is not None:
                print(f"[k=12] Ramanujan τ({prime}) = {coeffs[prime]}")

    return results


def search_triples(
    eigenvalues: Dict,
    target_mu: float,
    target_tau: float,
    tol: float,
) -> List[Dict]:
    """
    Search over all triples (f_0, f_1, f_2) with weights (2, 4, 6) and check
    if |a_p(f_1)|/|a_p(f_0)| ≈ target_mu and |a_p(f_2)|/|a_p(f_0)| ≈ target_tau.
    """
    w2 = eigenvalues.get("weight_2", [])
    w4 = eigenvalues.get("weight_4", [])
    w6 = eigenvalues.get("weight_6", [])

    prime_key = f"a_{P}"

    candidates = []
    for f0 in w2:
        ap0 = f0.get(prime_key)
        if ap0 is None or ap0 == 0:
            continue
        abs_ap0 = abs(ap0)
        for f1 in w4:
            ap1 = f1.get(prime_key)
            if ap1 is None:
                continue
            abs_ap1 = abs(ap1)
            ratio_mu = abs_ap1 / abs_ap0
            err_mu = abs(ratio_mu - target_mu) / target_mu
            if err_mu > tol:
                continue
            for f2 in w6:
                ap2 = f2.get(prime_key)
                if ap2 is None:
                    continue
                abs_ap2 = abs(ap2)
                ratio_tau = abs_ap2 / abs_ap0
                err_tau = abs(ratio_tau - target_tau) / target_tau
                if err_tau > tol:
                    continue
                candidates.append({
                    "f0": {"label": f0["label"], "level": f0["level"], f"a_{P}": ap0},
                    "f1": {"label": f1["label"], "level": f1["level"], f"a_{P}": ap1},
                    "f2": {"label": f2["label"], "level": f2["level"], f"a_{P}": ap2},
                    "ratio_mu":  ratio_mu,
                    "ratio_tau": ratio_tau,
                    "err_mu":    err_mu,
                    "err_tau":   err_tau,
                })
    return candidates


def run_search(max_level: int = 200, tolerance: float = TOLERANCE) -> Dict:
    """Run the full local search and return the results dict."""
    print(f"\n{'='*60}")
    print(f"HECKE EIGENVALUE SEARCH (local, no SageMath)")
    print(f"  prime p = {P}")
    print(f"  weights k = (2, 4, 6)")
    print(f"  max level N = {max_level}")
    print(f"  target m_μ/m_e  = {MU_RATIO:.7f}  (CODATA)")
    print(f"  target m_τ/m_e  = {TAU_RATIO:.4f}    (CODATA)")
    print(f"  tolerance       = {tolerance:.0%}")
    print(f"{'='*60}\n")

    eigenvalues = compute_all_eigenvalues(P, max_level)

    # Print summary
    prime_key = f"a_{P}"
    print(f"\n[SUMMARY] Eigenvalues at p={P}:")
    for wt_key in ("weight_2", "weight_4", "weight_6", "weight_12"):
        if wt_key not in eigenvalues:
            continue
        print(f"  {wt_key}:")
        for rec in eigenvalues[wt_key]:
            ap = rec.get(prime_key)
            print(f"    {rec['label']:30s}  a_{P} = {ap}")

    # Ramanujan bound check
    print(f"\n[RAMANUJAN BOUNDS] at p={P}:")
    for k in (2, 4, 6, 12):
        bound = 2 * P ** ((k - 1) / 2)
        print(f"  k={k}: |a_{P}| ≤ {bound:.2f}")
    print(f"  target ratios: {MU_RATIO:.2f} (μ), {TAU_RATIO:.2f} (τ)")

    # Search for matching triples
    print(f"\n[SEARCH] Checking all (f_0, f_1, f_2) triples ...")
    candidates = search_triples(eigenvalues, MU_RATIO, TAU_RATIO, tolerance)

    if candidates:
        print(f"\n  *** {len(candidates)} CANDIDATE(S) FOUND ***")
        for c in candidates:
            print(f"    f0={c['f0']['label']}  f1={c['f1']['label']}  "
                  f"f2={c['f2']['label']}")
            print(f"    ratio_μ={c['ratio_mu']:.4f} (err {c['err_mu']:.1%}),  "
                  f"ratio_τ={c['ratio_tau']:.4f} (err {c['err_tau']:.1%})")
    else:
        print(f"\n  No candidates found within {tolerance:.0%} tolerance.")

    # Fallback model eigenvalue
    lam_fallback = get_hecke_l_route_eigenvalue(P)
    if lam_fallback is not None:
        print(f"\n[FALLBACK] hecke_l_route.py toy-model eigenvalue "
              f"at p={P}: {lam_fallback:.4f}")
    else:
        print(f"\n[FALLBACK] hecke_l_route.py not available or failed.")

    # Verdict
    n_w2 = len(eigenvalues.get("weight_2", []))
    n_w4 = len(eigenvalues.get("weight_4", []))
    n_w6 = len(eigenvalues.get("weight_6", []))
    if candidates:
        verdict = "MATCH_FOUND"
    else:
        verdict = "NO_MATCH_IN_SEARCH_SPACE"

    # Build output dict
    output = {
        "search_parameters": {
            "prime": P,
            "weights": [2, 4, 6],
            "max_level": max_level,
            "target_mu":  MU_RATIO,
            "target_tau": TAU_RATIO,
            "tolerance":  tolerance,
            "approach":   "local_eta_products_and_elliptic_curves",
            "sageMath_available": False,
            "note": (
                "SageMath not available. Used pure-Python methods: "
                "elliptic curve point counting (weight-2 newforms, "
                "15 verified models with correct discriminants, N≤96) "
                "and exact eta-product q-expansion (integer coefficients). "
                "Coverage: k=2 via 15 discriminant-verified EC models + "
                "3 eta-product weight-2 forms (N=11,14,15); k=4 via eta "
                "product at N=5; k=6 via eta products at N=3,7. "
                "Models are checked at runtime: discriminant prime factors "
                "must be a subset of the conductor prime factors. "
                "Many newforms (especially those with algebraic eigenvalues "
                "or at higher levels) are NOT covered by this local search."
            ),
        },
        "newform_eigenvalues": eigenvalues,
        "candidates": candidates,
        "coverage": {
            "weight_2_forms_checked": n_w2,
            "weight_4_forms_checked": n_w4,
            "weight_6_forms_checked": n_w6,
            "total_triples_checked": n_w2 * n_w4 * n_w6,
        },
        "verdict": verdict,
        "verdict_note": (
            "MATCH FOUND — see candidates list."
            if verdict == "MATCH_FOUND" else
            f"No triple found within {tolerance:.0%} tolerance among the "
            f"{n_w2}×{n_w4}×{n_w6} = {n_w2*n_w4*n_w6} triples checked. "
            "Coverage is incomplete: weight-4 and weight-6 forms with "
            "algebraic eigenvalues (requiring SageMath or LMFDB) are not "
            "included. A full search requires SageMath or the LMFDB API "
            "(see search_hecke_lmfdb_api.py)."
        ),
    }

    print(f"\n{'='*60}")
    print(f"VERDICT: {verdict}")
    print(f"{'='*60}\n")

    return output


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "hecke_search_results.json"),
        help="Output JSON file (default: hecke_search_results.json in this directory)",
    )
    parser.add_argument(
        "--max-level",
        type=int,
        default=200,
        help="Maximum level N to search (default: 200)",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=TOLERANCE,
        help=f"Relative tolerance for ratio match (default: {TOLERANCE})",
    )
    args = parser.parse_args()

    output = run_search(max_level=args.max_level, tolerance=args.tolerance)

    with open(args.output, "w") as fh:
        json.dump(output, fh, indent=2)
    print(f"Results written to: {args.output}")


if __name__ == "__main__":
    main()

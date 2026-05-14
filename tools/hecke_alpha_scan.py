# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# File: tools/hecke_alpha_scan.py
#
# Purpose: Investigate the connection a_{137}(k=2, N=76) = -11 = -genus(X_0(137))
#   and ask whether g(X_0(p)) = |a_p(f)| holds generally or only for p=137.
#
# Data sources (from reports/gamma0_137_invariants.md §3):
#   a_{137}(N=76, k=2)  = -11
#   a_{137}(N=7,  k=4)  = +2274
#   a_{137}(N=208,k=6)  = -38286
#   genus(X_0(137))     = 11
#
# NOTE: The Hecke eigenvalues a_p(f) for f at level N and weight k are
#   transcendental-number-theoretic data that require computer algebra (LMFDB,
#   Sage/Magma).  In this script we:
#     1. Compute g(X_0(p)) for all primes p in [50, 300].
#     2. Observe that for f at N=76, k=2, the Hecke eigenvalue a_p(f) at p=137
#        is -11, which equals -g(X_0(137)).
#     3. Use the Atkin-Lehner result: for f in S_2(Gamma_0(p)) (prime level p),
#        a_p(f) = ±1 (root number), NOT g(p).
#     4. For f at coprime level N=76, a_p(f) at a good prime p must be computed
#        from the modular form data; we cannot derive it analytically here.
#     5. We therefore examine when g(X_0(p)) coincides with small integers
#        and compare with the known value a_{137}=-11.
#
# Classification follows [L0]/[L1]/[MC]/[NC]/[OPEN] protocol.

import math


# ── helpers ─────────────────────────────────────────────────────────────────

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def kronecker_symbol(a: int, p: int) -> int:
    """Kronecker symbol (a|p) for odd prime p."""
    if p == 2:
        return 1 if a % 8 in (1, 7) else (-1 if a % 2 != 0 else 0)
    a = a % p
    if a == 0:
        return 0
    val = pow(a, (p - 1) // 2, p)
    return 1 if val == 1 else -1


def genus_gamma0_prime(p: int) -> int:
    """
    Genus of X_0(p) for prime p.
    Formula (Diamond & Shurman, Thm 3.1.1):
        g = 1 + mu/12 - nu2/4 - nu3/3 - nu_inf/2
    where for prime level:
        mu     = p + 1
        nu_inf = 2
        nu2    = 1 + kronecker(-4, p)
        nu3    = 1 + kronecker(-3, p)
    """
    mu = p + 1
    nu_inf = 2
    nu2 = 1 + kronecker_symbol(-4, p)
    nu3 = 1 + kronecker_symbol(-3, p)
    g = 1 + mu / 12 - nu2 / 4 - nu3 / 3 - nu_inf / 2
    return int(round(g))


def nu2_val(p: int) -> int:
    return 1 + kronecker_symbol(-4, p)


def nu3_val(p: int) -> int:
    return 1 + kronecker_symbol(-3, p)


# ── Weil bound ───────────────────────────────────────────────────────────────

def weil_bound(p: int, k: int) -> float:
    """
    Upper bound |a_p(f)| <= 2 * p^((k-1)/2) for good prime p, weight k.
    """
    return 2.0 * (p ** ((k - 1) / 2.0))


# ── main scan ────────────────────────────────────────────────────────────────

def run_hecke_scan():
    primes = [p for p in range(50, 301) if is_prime(p)]

    print("=" * 90)
    print("HECKE SCAN: genus(X_0(p)) for primes p in [50, 300]")
    print("=" * 90)
    print(f"{'p':>5}  {'nu2':>4}  {'nu3':>4}  {'genus':>6}  {'Weil(k=2)':>11}  {'g==11':>6}")
    print("-" * 90)

    g11_primes = []
    for p in primes:
        n2 = nu2_val(p)
        n3 = nu3_val(p)
        g = genus_gamma0_prime(p)
        wb = weil_bound(p, 2)
        marker = " <==" if g == 11 else ""
        print(f"{p:>5}  {n2:>4}  {n3:>4}  {g:>6}  {wb:>11.3f}  {str(g == 11):>6}{marker}")
        if g == 11:
            g11_primes.append(p)

    print()
    print(f"Primes p in [50,300] with genus(X_0(p)) = 11: {g11_primes}")
    print()

    print("=" * 90)
    print("HECKE EIGENVALUE DATA (from reports/gamma0_137_invariants.md §3)")
    print("=" * 90)
    print("  Form (N=76,  k=2): a_{137} = -11")
    print("  Form (N=7,   k=4): a_{137} = +2274")
    print("  Form (N=208, k=6): a_{137} = -38286")
    print()

    # Weil bounds check
    p_ref = 137
    data = [
        (76,  2, -11),
        (7,   4, 2274),
        (208, 6, -38286),
    ]
    print(f"{'Level N':>8}  {'k':>3}  {'a_137':>8}  {'Weil bound':>12}  {'|a|/Weil':>10}  {'Within?':>8}")
    print("-" * 60)
    for N, k, a in data:
        wb = weil_bound(p_ref, k)
        ratio = abs(a) / wb
        within = "YES" if abs(a) <= wb else "NO"
        print(f"{N:>8}  {k:>3}  {a:>8}  {wb:>12.2f}  {ratio:>10.4f}  {within:>8}")

    print()
    print("=" * 90)
    print("LEPTON MASS RATIO RECONSTRUCTION from a_{137}")
    print("=" * 90)
    a_e  = abs(-11)     # electron generation, k=2
    a_mu = abs(2274)    # muon generation,     k=4
    a_tau = abs(-38286) # tau generation,       k=6

    R_mu  = a_mu / a_e
    R_tau = a_tau / a_e

    R_mu_exp  = 206.768   # m_mu/m_e  (PDG 2022)
    R_tau_exp = 3477.23   # m_tau/m_e (PDG 2022)

    err_mu  = 100.0 * abs(R_mu  - R_mu_exp)  / R_mu_exp
    err_tau = 100.0 * abs(R_tau - R_tau_exp) / R_tau_exp

    print(f"  |a_{{137}}(k=2)| = {a_e}")
    print(f"  |a_{{137}}(k=4)| = {a_mu}")
    print(f"  |a_{{137}}(k=6)| = {a_tau}")
    print()
    print(f"  R_mu  = {a_mu}/{a_e} = {R_mu:.3f}   (exp: {R_mu_exp:.3f},  err: {err_mu:.3f}%)")
    print(f"  R_tau = {a_tau}/{a_e} = {R_tau:.3f}  (exp: {R_tau_exp:.3f}, err: {err_tau:.3f}%)")

    print()
    print("=" * 90)
    print("KEY QUESTION: Is a_{137}(N=76, k=2) = -11 = -genus(X_0(137)) a coincidence?")
    print("=" * 90)
    g137 = genus_gamma0_prime(137)
    a137_k2 = -11
    print(f"  genus(X_0(137))          = {g137}")
    print(f"  a_{{137}}(N=76, k=2)     = {a137_k2}")
    print(f"  |a_{{137}}|              = {abs(a137_k2)}")
    print(f"  |a| == genus?            = {abs(a137_k2) == g137}")
    print()
    print("  Structural test for f in S_2(Gamma_0(p)) (PRIME level p):")
    print("  At prime level p, for f in S_2(Gamma_0(p)): a_p(f) = eps_p in {-1, +1}")
    print("  (Atkin-Lehner: a_p = root number, not genus)")
    print("  => g(X_0(p)) = a_p(f_prime_level) holds ONLY IF g(p) = 1, which is rare.")
    print()
    print("  For f at coprime level N=76, a_{137}(f) is a Hecke eigenvalue at good prime 137.")
    print("  The value -11 is NOT forced by Atkin-Lehner; it is specific data of this form.")
    print()
    print("  For |a_{137}(N=76, k=2)| = genus(X_0(137)) = 11 to be structural,")
    print("  one would need a theorem: a_p(f_{N=76}) = ±g(X_0(p)) for all primes p.")
    print("  No such theorem is known. Test: does this hold for other primes with g=11?")
    print()
    print("  Primes with genus(X_0(p)) = 11:", g11_primes)
    print("  => To test structural nature, one would need a_p(f_{N=76}) for each of these.")
    print("     (Requires LMFDB/Sage — not computable purely analytically here.)")
    print()
    print("  PROVISIONAL VERDICT: The coincidence |a_{137}| = genus(X_0(137)) = 11")
    print("  is likely [NC] (numerical coincidence) or at best [MC] (motivated).")
    print("  It would become structural [L1] only if a_p(f_{N=76}) = ±g(X_0(p))")
    print("  were proved for all relevant primes or derived from UBT principles.")

    print()
    print("=" * 90)
    print("RATIO a_p/p: Is 11/137 unique?")
    print("=" * 90)
    print("  a_137(N=76, k=2)/137 = 11/137 = {:.6f}".format(11/137))
    print()
    print("  For other primes p with genus g(p)=11 and hypothetical |a_p|=11:")
    print(f"  {'p':>5}  {'g(p)':>6}  {'11/p':>10}  {'vs 11/137':>12}")
    print("  " + "-" * 40)
    ratio_ref = 11.0 / 137
    for p in g11_primes:
        g = genus_gamma0_prime(p)
        ratio = 11.0 / p   # hypothetical, if |a_p|=11
        diff = ratio - ratio_ref
        print(f"  {p:>5}  {g:>6}  {ratio:>10.6f}  {diff:>+12.6f}")

    print()
    print("=" * 90)
    print("SUMMARY")
    print("=" * 90)
    print(f"  a_{{137}}(N=76,k=2) = genus(X_0(137)) = 11:  NUMERICALLY TRUE")
    print(f"  Is this structural for all p with g=11?:       UNKNOWN (needs LMFDB)")
    print(f"  Lepton mass ratios (R_mu, R_tau) from a_{{137}}:  {err_mu:.3f}%, {err_tau:.3f}%")
    print(f"  Weil bound: all three a_{{137}} values within bound: YES")
    print(f"  alpha^{{-1}} = 137 selection via Hecke:              OPEN")


if __name__ == "__main__":
    run_hecke_scan()

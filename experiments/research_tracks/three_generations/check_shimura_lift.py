# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
check_shimura_lift.py
=====================

SageMath script to test whether the weight-2 and weight-6 newforms in
the UBT Hecke triples are related by the Shimura correspondence.

The Shimura lift maps weight-k forms to weight-2k forms (for k even).
If the weight-2 form f₀ (k=2) and the weight-6 form f₂ (k=6) in the
same prime triple are Shimura-related, this is strong evidence that the
triple is not coincidental.

Formal statement of the test:
  For a newform f of weight k=2 and level N, the Shimura lift Sh(f)
  has weight 2k=4.  We are testing whether f₂ (weight 6) is related
  to Sh(Sh(f₀)) (weight 8 → 6 by some mechanism).

  More precisely: we test whether the L-function of f₂ factors through
  that of f₀ via the Rankin-Selberg or symmetric-square lift.

  Practical test (SageMath): compare Hecke eigenvalues a_p for many
  primes p between f₀ (k=2) and f₂ (k=6).  If a_p(f₂) = a_p(f₀)^3
  (or similar polynomial relation), this is a strong indicator.

Usage:
  sage check_shimura_lift.py

  Or interactively:
  sage -c "exec(open('check_shimura_lift.py').read()); test_triple_p137()"

References:
  research_tracks/three_generations/step6_hecke_matches.tex
  research_tracks/three_generations/identify_lmfdb_labels.py
  Shimura, G. (1973) "On modular forms of half integral weight"
"""

# ---------------------------------------------------------------------------
# Triple specifications (from step6_hecke_matches.tex)
# ---------------------------------------------------------------------------

TRIPLES = {
    "p137": {
        "prime": 137,
        "k2": dict(N=38,  k=2, a_p=-9,    label_hint="38.2.?.?"),
        "k4": dict(N=56,  k=4, a_p=-1854,  label_hint="56.4.?.?"),
        "k6": dict(N=50,  k=6, a_p=-32253, label_hint="50.6.?.?"),
    },
    "p139": {
        "prime": 139,
        "k2": dict(N=195, k=2, a_p=15,     label_hint="195.2.?.?"),
        "k4": dict(N=50,  k=4, a_p=3100,   label_hint="50.4.?.?"),
        "k6": dict(N=54,  k=6, a_p=53009,  label_hint="54.6.?.?"),
    },
}

# ---------------------------------------------------------------------------
# Helper: get newform matching target a_p
# ---------------------------------------------------------------------------

def get_matching_newform(N, k, p, target_ap, tol=1.0):
    """Return the first newform at (N, k) with a_p ≈ target_ap."""
    try:
        from sage.all import CuspForms, Gamma0
    except ImportError:
        print("ERROR: SageMath required.")
        return None

    from sage.all import CuspForms, Gamma0
    S = CuspForms(Gamma0(N), k)
    for f in S.newforms("a"):
        try:
            ap_val = float(f[p])
        except Exception:
            continue
        if abs(ap_val - target_ap) <= tol:
            return f
    return None


# ---------------------------------------------------------------------------
# Shimura lift test: compare Hecke eigenvalues at many primes
# ---------------------------------------------------------------------------

def test_shimura_lift(triple_key, n_primes=20, verbose=True):
    """
    For a given triple (k2, k4, k6), test whether the forms are
    related by checking polynomial relations between Hecke eigenvalues.

    Shimura lift f₀(k=2) → Sh(f₀)(k=4) satisfies:
      a_p(Sh(f₀)) = a_p(f₀)² - p^(k-1)   [one relation to check]

    For the full k=2 → k=6 Shimura-square:
      a_p(f₂) = a_p(f₀)³ - 3p a_p(f₀)    [Symmetric-cube / Langlands]

    These are heuristic checks; a full proof requires L-function comparison.
    """
    try:
        from sage.all import primes
    except ImportError:
        print("ERROR: SageMath required.")
        return {}

    from sage.all import primes

    triple = TRIPLES[triple_key]
    p_target = triple["prime"]

    if verbose:
        print(f"\n{'='*60}")
        print(f"Testing Shimura lift for triple {triple_key} (p={p_target})")

    # Get the three forms
    f0 = get_matching_newform(
        triple["k2"]["N"], 2, p_target, triple["k2"]["a_p"])
    f1 = get_matching_newform(
        triple["k4"]["N"], 4, p_target, triple["k4"]["a_p"])
    f2 = get_matching_newform(
        triple["k6"]["N"], 6, p_target, triple["k6"]["a_p"])

    if f0 is None or f2 is None:
        if verbose:
            print("  Could not retrieve forms — SageMath computation required")
        return {"status": "requires_sageMath"}

    # Test Hecke eigenvalue relations at small primes
    test_primes = [q for q in primes(3, 100) if q != p_target][:n_primes]

    relations_k2_k6 = []
    for q in test_primes:
        try:
            aq_f0 = float(f0[q])
            aq_f2 = float(f2[q])
            # Symmetric-cube: a_p(f₂) = a_p(f₀)^3 - 3q*a_p(f₀)
            sym_cube = aq_f0**3 - 3 * q * aq_f0
            diff = abs(aq_f2 - sym_cube)
            relations_k2_k6.append(dict(q=q, aq_f0=aq_f0, aq_f2=aq_f2,
                                         sym_cube=sym_cube, diff=diff))
            if verbose:
                ok = "≈" if diff < 1.0 else "≠"
                print(f"  q={q:3d}: a_q(f₀)={aq_f0:8.2f}, "
                      f"a_q(f₂)={aq_f2:10.2f}, "
                      f"sym_cube={sym_cube:10.2f}  {ok}")
        except Exception:
            continue

    # Summary
    if relations_k2_k6:
        n_match = sum(1 for r in relations_k2_k6 if r["diff"] < 1.0)
        n_total = len(relations_k2_k6)
        frac = n_match / n_total
        if verbose:
            print(f"\n  Symmetric-cube match: {n_match}/{n_total} primes "
                  f"({100*frac:.0f}%)")
            if frac > 0.9:
                print("  STRONG EVIDENCE: f₂ is a symmetric-cube lift of f₀")
            elif frac > 0.5:
                print("  PARTIAL EVIDENCE: possible Shimura relation")
            else:
                print("  NO EVIDENCE: not related by symmetric-cube lift")
        return {"n_match": n_match, "n_total": n_total, "fraction": frac,
                "relations": relations_k2_k6}
    return {"status": "no_data"}


def test_triple_p137():
    return test_shimura_lift("p137")


def test_triple_p139():
    return test_shimura_lift("p139")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("check_shimura_lift.py — UBT Hecke Shimura correspondence test")
    print("Task: UBT_v29_task4_hecke_lmfdb  |  Date: 2026-03-06")
    print("=" * 70)
    print()
    print("Testing whether UBT Hecke triples are related by Shimura lift.")
    print("This requires SageMath with modular forms support.")
    print()
    print("Hypothesis: if f₀ (k=2), f₁ (k=4), f₂ (k=6) satisfy")
    print("  a_p(f₁) = a_p(f₀)² - p  (Shimura lift k=2→k=4)")
    print("  a_p(f₂) = a_p(f₀)³ - 3p·a_p(f₀)  (sym-cube lift)")
    print("then the triple is structurally motivated, not accidental.")
    print()

    for key in ["p137", "p139"]:
        result = test_shimura_lift(key, verbose=True)
        if "fraction" in result:
            pct = 100 * result["fraction"]
            print(f"\n  Triple {key}: {pct:.0f}% match for sym-cube relation")
        else:
            print(f"\n  Triple {key}: {result.get('status', 'error')}")

    print("\n" + "=" * 70)
    print("NEXT STEPS:")
    print("  1. Run identify_lmfdb_labels.py to get LMFDB labels")
    print("  2. Check https://lmfdb.org for official labels and L-functions")
    print("  3. Use LMFDB's Galois representation data to check Shimura lift")
    print("  4. If sym-cube match > 90%: update DERIVATION_INDEX.md")
    print("     'Hecke conjecture: Numerical support → Shimura-supported'")

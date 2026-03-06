# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
identify_lmfdb_labels.py
========================

SageMath script to identify LMFDB labels for newforms matching the
UBT Hecke eigenvalue triples at p=137 and p=139.

Context:
  The three-generation mechanism in UBT predicts that lepton masses
  are related to Hecke eigenvalues a_p of modular forms at weights
  k=2, 4, 6.  Numerical search found:

  p=137 matches:
    k=2, N=38,  a_137 ≈ -9
    k=4, N=56,  a_137 ≈ -1854
    k=6, N=50,  a_137 ≈ -32253

  p=139 matches:
    k=2, N=195, a_139 ≈ 15
    k=4, N=50,  a_139 ≈ 3100
    k=6, N=54,  a_139 ≈ 53009

Usage:
  sage identify_lmfdb_labels.py

  Or to check a single triple:
  sage -c "exec(open('identify_lmfdb_labels.py').read()); check_triple(38, 2, 137, -9)"

Requirements:
  SageMath >= 9.0 with Modular Forms module

Output:
  For each (N, k, p, target_a_p) triple:
    - SageMath label (e.g. 38.2.a.a)
    - LMFDB-style label
    - Whether it is a genuine newform
    - Atkin-Lehner eigenvalue at N
    - CM status (if available)

References:
  research_tracks/three_generations/step6_hecke_matches.tex
  research_tracks/three_generations/step5_hecke_search_results.tex
  DERIVATION_INDEX.md §Hecke
"""

# ---------------------------------------------------------------------------
# Target triples: (N, k, p, target_a_p, label_hint)
# ---------------------------------------------------------------------------

TARGETS = [
    # p = 137
    dict(N=38,  k=2, p=137, target_ap=-9,    label_hint="38.2.?.?",  prime="p=137"),
    dict(N=56,  k=4, p=137, target_ap=-1854,  label_hint="56.4.?.?",  prime="p=137"),
    dict(N=50,  k=6, p=137, target_ap=-32253, label_hint="50.6.?.?",  prime="p=137"),
    # p = 139
    dict(N=195, k=2, p=139, target_ap=15,     label_hint="195.2.?.?", prime="p=139"),
    dict(N=50,  k=4, p=139, target_ap=3100,   label_hint="50.4.?.?",  prime="p=139"),
    dict(N=54,  k=6, p=139, target_ap=53009,  label_hint="54.6.?.?",  prime="p=139"),
]

TOLERANCE = 0.5  # Hecke eigenvalues are algebraic integers; allow small rounding

# ---------------------------------------------------------------------------
# Main identification function (SageMath required)
# ---------------------------------------------------------------------------

def identify_newform(N, k, p, target_ap, verbose=True):
    """
    Find the newform at level N, weight k with a_p ≈ target_ap.

    Returns list of dicts with:
      label, a_p, is_new, is_CM, atkin_lehner, lmfdb_label
    """
    try:
        from sage.all import CuspForms, Gamma0  # noqa: F401
    except ImportError:
        print("  ERROR: SageMath not available. Run with 'sage identify_lmfdb_labels.py'")
        return []

    from sage.all import CuspForms, Gamma0

    if verbose:
        print(f"\n  Computing newforms for N={N}, k={k}...")

    S = CuspForms(Gamma0(N), k)
    newforms = S.newforms("a")

    if verbose:
        print(f"  Found {len(newforms)} newform(s) at (N={N}, k={k})")

    matches = []
    for idx, f in enumerate(newforms):
        label_char = chr(ord("a") + idx)
        sage_label = f"{N}.{k}.a.{label_char}"

        try:
            ap_val = float(f[p])
        except Exception as e:
            if verbose:
                print(f"    {sage_label}: could not compute a_{p}: {e}")
            continue

        # Check CM
        try:
            is_cm = bool(f.has_cm())
            cm_disc = int(f.cm_discriminant()) if is_cm else None
        except Exception:
            is_cm = None
            cm_disc = None

        # Atkin-Lehner eigenvalue at N
        try:
            al_eigen = int(f.atkin_lehner_eigenvalue(N))
        except Exception:
            al_eigen = None

        # LMFDB-style label: N.k.chi.label  (chi=a for trivial character)
        lmfdb_label = sage_label  # same format for trivial character

        info = dict(
            sage_label=sage_label,
            lmfdb_label=lmfdb_label,
            a_p=ap_val,
            is_cm=is_cm,
            cm_disc=cm_disc,
            atkin_lehner=al_eigen,
        )

        diff = abs(ap_val - target_ap)
        if diff <= TOLERANCE:
            info["match"] = True
            matches.append(info)
            if verbose:
                print(f"    *** MATCH: {sage_label}: a_{p} = {ap_val:.2f} "
                      f"(target={target_ap})  CM={is_cm}  AL={al_eigen}")
        else:
            if verbose:
                print(f"    {sage_label}: a_{p} = {ap_val:.2f} "
                      f"(target={target_ap}, diff={diff:.1f})")

    return matches


def check_triple(N, k, p, target_ap):
    """Convenience function for interactive use from SageMath."""
    matches = identify_newform(N, k, p, target_ap, verbose=True)
    if matches:
        print(f"\nBest match: {matches[0]['lmfdb_label']}")
    else:
        print(f"\nNo match found for N={N}, k={k}, a_{p}={target_ap}")
    return matches


# ---------------------------------------------------------------------------
# Run all targets
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("identify_lmfdb_labels.py — UBT Hecke LMFDB label search")
    print("Task: UBT_v29_task4_hecke_lmfdb  |  Date: 2026-03-06")
    print("=" * 70)

    all_results = {}

    for spec in TARGETS:
        N, k, p, target_ap = spec["N"], spec["k"], spec["p"], spec["target_ap"]
        print(f"\n{'='*50}")
        print(f"Triple: N={N}, k={k}, p={p}, target a_p={target_ap}  [{spec['prime']}]")
        print(f"Hint:   {spec['label_hint']}")

        matches = identify_newform(N, k, p, target_ap, verbose=True)

        key = (N, k, p)
        all_results[key] = matches

        if matches:
            print(f"\n  LMFDB label(s) found:")
            for m in matches:
                print(f"    {m['lmfdb_label']}")
                print(f"      a_{p} = {m['a_p']:.2f}  CM={m['is_cm']}  "
                      f"AL_eigenvalue={m['atkin_lehner']}")
        else:
            print(f"\n  No match found at tolerance {TOLERANCE}.")
            print(f"  Possible causes:")
            print(f"    - Target a_p is approximate; try LMFDB web search at")
            print(f"      https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/{N}/{k}/")
            print(f"    - Form may be at a non-trivial nebentypus character")
            print(f"    - Form may require higher precision arithmetic")

    print("\n" + "=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print(f"{'Level':>6}  {'Weight':>6}  {'Prime':>5}  {'Target a_p':>12}  "
          f"{'LMFDB label':>20}  {'CM':>4}  {'AL':>4}")
    print("-" * 70)
    for spec in TARGETS:
        N, k, p, target_ap = spec["N"], spec["k"], spec["p"], spec["target_ap"]
        key = (N, k, p)
        matches = all_results.get(key, [])
        if matches:
            m = matches[0]
            print(f"{N:>6}  {k:>6}  {p:>5}  {target_ap:>12}  "
                  f"{m['lmfdb_label']:>20}  {str(m['is_cm']):>4}  {str(m['atkin_lehner']):>4}")
        else:
            print(f"{N:>6}  {k:>6}  {p:>5}  {target_ap:>12}  "
                  f"{'NOT FOUND':>20}  {'?':>4}  {'?':>4}")

    print("\nNext step: verify found labels at https://lmfdb.org")
    print("and check Shimura lift relations with check_shimura_lift.py")

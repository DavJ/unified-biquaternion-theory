# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
test_prime_specificity.sage
===========================

TASK 1 — Prime Specificity Test (PRIORITY 1) — Set A

Checks whether the Hecke eigenvalue ratios that approximate lepton mass
ratios are special to the UBT prime p = 137, or whether they match for
an arbitrary prime p.

Tests BOTH Set A (p=137 sector) and Set B (p=139 mirror sector)
in a single run.

Forms identified in the 2026-03-07 SageMath run — Set A:
  k=2, N=76  :  a_{137} = -11        (electron generation)
  k=4, N=7   :  a_{137} =  2274      (muon generation)
  k=6, N=208 :  a_{137} = -38286     (tau generation)

Forms identified in the 2026-03-06 SageMath run — Set B (mirror sector):
  k=2, N=195 :  a_{139} = +15        (gen 1, mirror)
  k=4, N=50  :  a_{139} = +3100      (gen 2, mirror)
  k=6, N=54  :  a_{139} = +53009     (gen 3, mirror)
  Sage indices: newforms('a')[2], newforms('a')[1], newforms('a')[1]

Strategy
--------
For each set of three forms, compute the Hecke eigenvalue a_p at every
prime p in TEST_PRIMES.  Then compute the ratios

    R_mu(p)  = |a_p(k=4)| / |a_p(k=2)|
    R_tau(p) = |a_p(k=6)| / |a_p(k=2)|

and compare to the experimental mass ratios.

Interpretation of output
------------------------
  * If errors are small ONLY at p = 137 (Set A) or p=139 (Set B)
    → strong signal; continue
  * If errors are small for MANY primes → coincidence; likely DEAD END
  * If a_p = 0 at some prime            → bad prime for that form (skip ratio)

How to run
----------
  Option A — SageMath online:
      Go to https://sagecell.sagemath.org/
      Paste the entire contents of this file and click Evaluate.

  Option B — SageMath local:
      sage test_prime_specificity.sage

  Option C — Jupyter notebook (SageMath kernel):
      %run test_prime_specificity.sage

Raw results are in:
    reports/hecke_lepton/prime_specificity_results.txt

Related files
-------------
  scripts/hecke/global_scan_set_b.sage               — global scan for Set B
  research_tracks/three_generations/run_hecke_sage.py — original search
  research_tracks/three_generations/hecke_sage_results.txt — 2026-03-06 results
  reports/hecke_lepton/sage_results_2026_03_07.md    — analysis report
  reports/hecke_lepton/mirror_world_139.md           — Set B analysis
"""

# ---------------------------------------------------------------------------
# Experimental targets  (CODATA 2022 / PDG 2022)  — DO NOT CHANGE
# ---------------------------------------------------------------------------
MU_RATIO  = 206.7682830   # m_μ / m_e
TAU_RATIO = 3477.23       # m_τ / m_e

# ---------------------------------------------------------------------------
# Set A: Forms identified in the 2026-03-07 SageMath run
#   KEY: (level N, weight k, known_a137, sage_index, generation_label)
#
# sage_index: index in CuspForms(Gamma0(N), k).newforms('a') list.
# Use None to auto-detect by matching known_a137.
# ---------------------------------------------------------------------------
SET_A_FORMS = [
    # (N,   k,  known_a137, sage_index, generation_label)
    (76,    2,  -11,        None,       "electron (gen 1)"),
    (7,     4,   2274,      0,          "muon     (gen 2)"),
    (208,   6,  -38286,     None,       "tau      (gen 3)"),
]

# ---------------------------------------------------------------------------
# Set B: Forms identified in the 2026-03-06 SageMath run (mirror sector)
#   sage_index: verified indices from the 2026-03-06 run
# ---------------------------------------------------------------------------
SET_B_FORMS = [
    # (N,   k,  known_a139, sage_index, generation_label)
    (195,   2,   15,        2,          "mirror gen 1"),
    (50,    4,   3100,      1,          "mirror gen 2"),
    (54,    6,   53009,     1,          "mirror gen 3"),
]

# ---------------------------------------------------------------------------
# Primes to test in local scan
# ---------------------------------------------------------------------------
TEST_PRIMES = [127, 131, 137, 139, 149, 151]

# ---------------------------------------------------------------------------
# Helper: extract a_p from a Sage newform object using f[p]
# Falls back to q_expansion_coefficients if f[p] is not available.
# ---------------------------------------------------------------------------

def _a_p_float(form, p):
    """Return a_p(form) as a float, or None if unavailable.

    Uses form[p] (preferred) which directly accesses the p-th Hecke
    eigenvalue.  Falls back to q_expansion_coefficients for compatibility.
    """
    # Primary method: direct eigenvalue access via f[p]
    try:
        val = form[p]
        return float(val)
    except (TypeError, AttributeError, KeyError):
        pass
    # Fallback: q-expansion coefficient (integer or algebraic)
    try:
        val = form.q_expansion_coefficients(p + 1)[p]
        try:
            return float(val)
        except TypeError:
            return float(val.complex_embeddings()[0].real())
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Helper: load a set of forms and return {label: {p: float}}
# ---------------------------------------------------------------------------

def _load_forms(form_specs, ref_prime):
    """Load newforms and collect a_p for TEST_PRIMES.

    form_specs: list of (N, k, known_a_ref, sage_index, label)
    ref_prime:  prime used to identify the correct newform

    Returns: a_p_table dict {label: {p: float}}
    """
    a_p_table = {}
    for N, k, known_a_ref, sage_index, label in form_specs:
        print(f"[{label}]  Level N={N}, weight k={k},  "
              f"known a_{{{ref_prime}}} = {known_a_ref}")
        try:
            S     = CuspForms(Gamma0(N), k)
            forms = S.newforms('a')
        except Exception as e:
            print(f"  ERROR computing newforms: {e}")
            a_p_table[label] = {}
            continue

        if len(forms) == 0:
            print(f"  WARNING: no cusp newforms at this level/weight.")
            a_p_table[label] = {}
            continue

        # Select by explicit sage_index if provided
        selected = None
        if sage_index is not None and sage_index < len(forms):
            selected = forms[sage_index]
            a_val = _a_p_float(selected, ref_prime)
            if a_val is not None and abs(a_val - known_a_ref) < 0.5:
                print(f"  Used index [{sage_index}]:  "
                      f"a_{ref_prime} = {a_val:.0f}  ✓")
            else:
                print(f"  Index [{sage_index}] gives a_{ref_prime} = {a_val}  "
                      f"(expected {known_a_ref}) — mismatch, searching all forms")
                selected = None

        # Auto-detect: search all forms for the matching eigenvalue
        if selected is None:
            for idx, f in enumerate(forms):
                a_val = _a_p_float(f, ref_prime)
                if a_val is None:
                    continue
                if abs(a_val - known_a_ref) < 0.5:
                    selected = f
                    print(f"  Auto-detected index [{idx}]:  "
                          f"a_{ref_prime} = {a_val:.0f}  ✓")
                    break

        if selected is None:
            if len(forms) == 1:
                selected = forms[0]
                a_val = _a_p_float(selected, ref_prime)
                print(f"  Only one newform; a_{ref_prime} = {a_val}  "
                      f"(expected {known_a_ref} — discrepancy)")
            else:
                print(f"  WARNING: could not match a_{ref_prime} = {known_a_ref} "
                      f"among {len(forms)} newforms.  Skipping.")
                a_p_table[label] = {}
                continue

        # Collect a_p for all test primes using f[p]
        row = {}
        for p in TEST_PRIMES:
            row[p] = _a_p_float(selected, p)
        a_p_table[label] = row

        eigen_str = "  a_p:  " + "  ".join(
            f"a_{p}={row[p]:+.0f}" if row[p] is not None else f"a_{p}=N/A"
            for p in TEST_PRIMES
        )
        print(eigen_str)
        print()

    return a_p_table


# ---------------------------------------------------------------------------
# Helper: print ratio table
# ---------------------------------------------------------------------------

def _print_ratio_table(a_p_table, labels, set_name, ref_prime):
    """Print ratio table for a set of three forms."""
    label_e, label_m, label_t = labels

    print()
    print("=" * 72)
    print(f"RATIO TABLE — {set_name}  (reference prime: p={ref_prime})")
    print(f"  Targets:  R_mu = {MU_RATIO:.5f}   R_tau = {TAU_RATIO:.2f}")
    print("=" * 72)
    print()
    hdr = (f"{'prime p':>8}  {'R_mu':>10}  {'err_mu':>8}  "
           f"{'R_tau':>10}  {'err_tau':>8}  note")
    print(hdr)
    print("-" * 72)

    any_other_hit = False
    for p in TEST_PRIMES:
        a2 = a_p_table.get(label_e, {}).get(p)
        a4 = a_p_table.get(label_m, {}).get(p)
        a6 = a_p_table.get(label_t, {}).get(p)

        if None in (a2, a4, a6):
            print(f"{p:>8}  {'N/A':>10}  {'N/A':>8}  {'N/A':>10}  "
                  f"{'N/A':>8}  (missing eigenvalue)")
            continue

        if abs(a2) < 0.5:
            print(f"{p:>8}  {'—':>10}  {'—':>8}  {'—':>10}  "
                  f"{'—':>8}  a_p(k=2)=0, ratio undefined")
            continue

        R_mu  = abs(a4) / abs(a2)
        R_tau = abs(a6) / abs(a2)
        err_mu  = abs(R_mu  - MU_RATIO)  / MU_RATIO  * 100.0
        err_tau = abs(R_tau - TAU_RATIO) / TAU_RATIO  * 100.0

        CLOSE = err_mu < 1.0 and err_tau < 2.0
        MATCH = err_mu < 5.0 and err_tau < 5.0

        if p != ref_prime and MATCH:
            any_other_hit = True

        flag = ""
        if CLOSE:
            flag = "  ← CLOSE (<1%/2%)"
        elif MATCH:
            flag = "  ← match (<5%)"

        print(f"{p:>8}  {R_mu:>10.4f}  {err_mu:>7.2f}%  "
              f"{R_tau:>10.4f}  {err_tau:>7.2f}%{flag}")

    return any_other_hit


# ===========================================================================
# MAIN
# ===========================================================================

print()
print("=" * 72)
print("Prime Specificity Test — UBT Hecke Lepton Mass Conjecture")
print("Sets A and B — 2026-03-07 (Set A) / 2026-03-06 (Set B)")
print("=" * 72)
print()

# ---------------------------------------------------------------------------
# SET A
# ---------------------------------------------------------------------------
print(">>> Loading Set A forms (reference prime p=137) ...")
print()
a_p_table_A = _load_forms(SET_A_FORMS, ref_prime=137)
labels_A = [spec[4] for spec in SET_A_FORMS]

other_hit_A = _print_ratio_table(a_p_table_A, labels_A, "Set A", ref_prime=137)

print()
print("SET A VERDICT:")
if other_hit_A:
    print("  INCONCLUSIVE — ratios close at primes other than p=137 too.")
else:
    print("  SIGNAL — ratios close ONLY at p=137 among tested primes.")
print()

# ---------------------------------------------------------------------------
# SET B (mirror sector)
# ---------------------------------------------------------------------------
print()
print("=" * 72)
print(">>> Loading Set B forms (mirror sector, reference prime p=139) ...")
print()
a_p_table_B = _load_forms(SET_B_FORMS, ref_prime=139)
labels_B = [spec[4] for spec in SET_B_FORMS]

other_hit_B = _print_ratio_table(a_p_table_B, labels_B, "Set B (mirror)", ref_prime=139)

print()
print("SET B VERDICT:")
if other_hit_B:
    print("  INCONCLUSIVE — ratios close at primes other than p=139 too.")
else:
    print("  SIGNAL — ratios close ONLY at p=139 among tested primes.")
print()

# ---------------------------------------------------------------------------
# Twin prime check
# ---------------------------------------------------------------------------
print()
print("=" * 72)
print("TWIN PRIME EXCLUSIVITY CHECK")
print("=" * 72)
print()

# Set A at p=139
a2_A_139 = a_p_table_A.get(labels_A[0], {}).get(139)
a4_A_139 = a_p_table_A.get(labels_A[1], {}).get(139)
a6_A_139 = a_p_table_A.get(labels_A[2], {}).get(139)
if None not in (a2_A_139, a4_A_139, a6_A_139) and abs(a2_A_139) > 0.5:
    r_mu  = abs(a4_A_139) / abs(a2_A_139)
    r_tau = abs(a6_A_139) / abs(a2_A_139)
    e_mu  = abs(r_mu  - MU_RATIO)  / MU_RATIO  * 100
    e_tau = abs(r_tau - TAU_RATIO) / TAU_RATIO * 100
    print(f"  Set A at p=139:  R_mu={r_mu:.3f} (err {e_mu:.1f}%),  "
          f"R_tau={r_tau:.1f} (err {e_tau:.1f}%)  "
          f"{'<-- blind to 139' if e_mu > 10 else '<-- UNEXPECTED HIT'}")

# Set B at p=137
a2_B_137 = a_p_table_B.get(labels_B[0], {}).get(137)
a4_B_137 = a_p_table_B.get(labels_B[1], {}).get(137)
a6_B_137 = a_p_table_B.get(labels_B[2], {}).get(137)
if None not in (a2_B_137, a4_B_137, a6_B_137) and abs(a2_B_137) > 0.5:
    r_mu  = abs(a4_B_137) / abs(a2_B_137)
    r_tau = abs(a6_B_137) / abs(a2_B_137)
    e_mu  = abs(r_mu  - MU_RATIO)  / MU_RATIO  * 100
    e_tau = abs(r_tau - TAU_RATIO) / TAU_RATIO * 100
    print(f"  Set B at p=137:  R_mu={r_mu:.3f} (err {e_mu:.1f}%),  "
          f"R_tau={r_tau:.1f} (err {e_tau:.1f}%)  "
          f"{'<-- blind to 137' if e_mu > 10 else '<-- UNEXPECTED HIT'}")

print()
print("Expected: Set A blind to p=139, Set B blind to p=137.")
print("Twin primes 137 and 139: |137-139|=2, both prime.")
print()
print("NOTE: This script tests NUMERICAL OBSERVATIONS only.")
print("  A positive verdict here is NOT a proof that fermion masses are derived.")
print("  See reports/hecke_lepton/ for full analysis.")
print("=" * 72)


# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
test_prime_specificity.sage
===========================

TASK 1 — Prime Specificity Test (PRIORITY 1)

Checks whether the Hecke eigenvalue ratios that approximate lepton mass
ratios are special to the UBT prime p = 137, or whether they match for
an arbitrary prime p.

Forms identified in the 2026-03-07 SageMath run:
  k=2, N=76  :  a_{137} = -11        (electron generation)
  k=4, N=7   :  a_{137} =  2274      (muon generation)
  k=6, N=208 :  a_{137} = -38286     (tau generation)

Strategy
--------
For each of the three forms, compute the Hecke eigenvalue a_p at every
prime p in TEST_PRIMES.  Then compute the ratios

    R_mu(p)  = |a_p(k=4)| / |a_p(k=2)|
    R_tau(p) = |a_p(k=6)| / |a_p(k=2)|

and compare to the experimental mass ratios.

Interpretation of output
------------------------
  * If errors are small ONLY at p = 137   → strong signal; continue
  * If errors are small for MANY primes   → coincidence; likely DEAD END
  * If a_p = 0 at some prime              → bad prime for that form (skip ratio)

How to run
----------
  Option A — SageMath online:
      Go to https://sagecell.sagemath.org/
      Paste the entire contents of this file and click Evaluate.

  Option B — SageMath local:
      sage test_prime_specificity.sage

  Option C — Jupyter notebook (SageMath kernel):
      %run test_prime_specificity.sage

After running, copy the printed table into the file
    reports/hecke_lepton/prime_specificity_results.txt
and update the status in  reports/hecke_lepton/sage_results_2026_03_07.md.

Related files
-------------
  research_tracks/three_generations/run_hecke_sage.py  — original search
  research_tracks/three_generations/hecke_sage_results.txt — 2026-03-06 results
  reports/hecke_lepton/sage_results_2026_03_07.md        — analysis report
"""

# ---------------------------------------------------------------------------
# Experimental targets  (CODATA 2022 / PDG 2022)  — DO NOT CHANGE
# ---------------------------------------------------------------------------
MU_RATIO  = 206.7682830   # m_μ / m_e
TAU_RATIO = 3477.23       # m_τ / m_e

# ---------------------------------------------------------------------------
# Forms identified in the 2026-03-07 SageMath run
#   KEY: (level N, weight k, known a_137 from that run)
#
# NOTE: At levels N=76 (k=2) and N=208 (k=6) there may be multiple newforms.
# The script selects the unique newform whose a_137 equals the known value;
# if the space is 1-dimensional there is no ambiguity.
# ---------------------------------------------------------------------------
FORMS_2026_03_07 = [
    # (N,   k,  known_a137,  generation_label)
    (76,    2,  -11,         "electron (gen 1)"),
    (7,     4,   2274,       "muon     (gen 2)"),
    (208,   6,  -38286,      "tau      (gen 3)"),
]

# ---------------------------------------------------------------------------
# Primes to test
# ---------------------------------------------------------------------------
TEST_PRIMES = [127, 131, 137, 139, 149, 151]

# ---------------------------------------------------------------------------
# Helper: extract a_p from a Sage newform object as a Python float
# ---------------------------------------------------------------------------

def _a_p_float(form, p):
    """Return a_p(form) as a float, or None if unavailable."""
    try:
        val = form.q_expansion_coefficients(p + 1)[p]
        return float(val)
    except (TypeError, AttributeError):
        pass
    try:
        return float(val.complex_embeddings()[0].real())
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Step 1: Find each form and collect eigenvalues
# ---------------------------------------------------------------------------

print("=" * 72)
print("Prime Specificity Test — UBT Hecke Lepton Mass Conjecture")
print("2026-03-07 forms  (N=76 k=2, N=7 k=4, N=208 k=6)")
print("=" * 72)
print()

# Dictionary: generation label → { p: a_p float }
found_forms  = {}   # label → sage form object
a_p_table    = {}   # label → { p: float }

for N, k, known_a137, label in FORMS_2026_03_07:
    print(f"[{label}]  Level N={N}, weight k={k},  known a_{{137}} = {known_a137}")
    try:
        S     = CuspForms(Gamma0(N), k)
        forms = S.newforms('a')
    except Exception as e:
        print(f"  ERROR computing newforms: {e}")
        a_p_table[label] = {}
        continue

    if len(forms) == 0:
        print(f"  WARNING: no cusp newforms at this level/weight — unexpected.")
        a_p_table[label] = {}
        continue

    # Select the newform matching the known a_137
    selected = None
    for f in forms:
        a_val = _a_p_float(f, 137)
        if a_val is None:
            continue
        if abs(a_val - known_a137) < 0.5:        # exact integer match
            selected = f
            print(f"  Found matching newform:  a_137 = {a_val:.0f}  ✓")
            break

    if selected is None:
        # Fallback: if there is exactly one form, use it regardless
        if len(forms) == 1:
            selected = forms[0]
            a_val = _a_p_float(selected, 137)
            print(f"  Only one newform; a_137 = {a_val}  "
                  f"(expected {known_a137} — discrepancy, see note below)")
        else:
            print(f"  WARNING: could not match a_137 = {known_a137} "
                  f"among {len(forms)} newforms.  Skipping.")
            a_p_table[label] = {}
            continue

    found_forms[label] = selected

    # Collect a_p for all test primes
    row = {}
    for p in TEST_PRIMES:
        row[p] = _a_p_float(selected, p)
    a_p_table[label] = row

    eigenvalue_str = "  a_p:  " + "  ".join(
        f"a_{p}={row[p]:+.0f}" if row[p] is not None else f"a_{p}=N/A"
        for p in TEST_PRIMES
    )
    print(eigenvalue_str)
    print()


# ---------------------------------------------------------------------------
# Step 2: Compute and print ratios table
# ---------------------------------------------------------------------------

label_e = "electron (gen 1)"
label_m = "muon     (gen 2)"
label_t = "tau      (gen 3)"

print()
print("=" * 72)
print("RATIO TABLE")
print(f"  Experimental targets:  R_mu = {MU_RATIO:.5f}   R_tau = {TAU_RATIO:.2f}")
print("=" * 72)
print()
print(f"{'prime p':>8}  {'a_p(k=2)':>12}  {'a_p(k=4)':>12}  {'a_p(k=6)':>14}"
      f"  {'R_mu':>10}  {'err_mu':>8}  {'R_tau':>10}  {'err_tau':>8}  note")
print("-" * 112)

good_at_p137_only = True   # will be set False if another prime also matches

for p in TEST_PRIMES:
    a2   = a_p_table.get(label_e, {}).get(p)
    a4   = a_p_table.get(label_m, {}).get(p)
    a6   = a_p_table.get(label_t, {}).get(p)

    if a2 is None or a4 is None or a6 is None:
        print(f"{p:>8}  {'N/A':>12}  {'N/A':>12}  {'N/A':>14}"
              f"  {'N/A':>10}  {'N/A':>8}  {'N/A':>10}  {'N/A':>8}  (missing eigenvalue)")
        continue

    abs2 = abs(a2)
    if abs2 < 0.5:
        print(f"{p:>8}  {a2:>12.1f}  {a4:>12.1f}  {a6:>14.1f}"
              f"  {'—':>10}  {'—':>8}  {'—':>10}  {'—':>8}  a_p(k=2)=0, ratio undefined")
        continue

    R_mu  = abs(a4) / abs2
    R_tau = abs(a6) / abs2
    err_mu  = abs(R_mu  - MU_RATIO)  / MU_RATIO  * 100.0
    err_tau = abs(R_tau - TAU_RATIO) / TAU_RATIO  * 100.0

    CLOSE = err_mu < 1.0 and err_tau < 1.0
    MATCH = err_mu < 5.0 and err_tau < 5.0

    if p != 137 and MATCH:
        good_at_p137_only = False

    flag = ""
    if CLOSE:
        flag = "  ← CLOSE MATCH (<1%)"
    elif MATCH:
        flag = "  ← match (<5%)"

    print(f"{p:>8}  {a2:>12.1f}  {a4:>12.1f}  {a6:>14.1f}"
          f"  {R_mu:>10.4f}  {err_mu:>7.2f}%  {R_tau:>10.4f}  {err_tau:>7.2f}%{flag}")


# ---------------------------------------------------------------------------
# Step 3: Verdict
# ---------------------------------------------------------------------------

print()
print("=" * 72)
print("VERDICT")
print("=" * 72)

a2_137 = a_p_table.get(label_e, {}).get(137)
a4_137 = a_p_table.get(label_m, {}).get(137)
a6_137 = a_p_table.get(label_t, {}).get(137)

if None not in (a2_137, a4_137, a6_137) and abs(a2_137) > 0.5:
    R_mu_137  = abs(a4_137) / abs(a2_137)
    R_tau_137 = abs(a6_137) / abs(a2_137)
    err_mu_137  = abs(R_mu_137  - MU_RATIO)  / MU_RATIO  * 100.0
    err_tau_137 = abs(R_tau_137 - TAU_RATIO) / TAU_RATIO * 100.0

    print(f"  At p=137:  R_mu = {R_mu_137:.4f} (err {err_mu_137:.2f}%),  "
          f"R_tau = {R_tau_137:.2f} (err {err_tau_137:.2f}%)")

if good_at_p137_only:
    verdict = "SIGNAL — ratios match ONLY at p=137 (within 5%)"
    verdict_detail = (
        "This is a positive result. The lepton mass ratios are not reproduced "
        "by these three forms at other nearby primes. This strengthens the "
        "conjecture that p=137 plays a special role."
    )
else:
    verdict = "INCONCLUSIVE / POSSIBLE DEAD END — ratios match at other primes too"
    verdict_detail = (
        "The lepton mass ratios are reproduced at primes other than p=137. "
        "This weakens the conjecture: the agreement at p=137 may be a "
        "coincidence. Document as dead end unless further algebraic "
        "motivation is found."
    )

print()
print(f"  {verdict}")
print()
print(f"  {verdict_detail}")
print()
print("Next steps:")
print("  1. Copy this output to reports/hecke_lepton/prime_specificity_results.txt")
print("  2. Update status in reports/hecke_lepton/sage_results_2026_03_07.md")
print("  3. If SIGNAL: proceed with LMFDB label identification")
print("  4. If DEAD END: document and archive")
print()
print("NOTE: This script tests NUMERICAL OBSERVATIONS only.")
print("  A positive verdict here is NOT a proof that fermion masses are derived.")
print("=" * 72)

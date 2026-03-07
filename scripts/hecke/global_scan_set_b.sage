# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
global_scan_set_b.sage
======================

Global Prime Scan for Set B (Mirror Sector, reference prime p=139)

Scans all primes p in SCAN_RANGE and computes lepton-like ratios for
Set B forms (N=195 k=2, N=50 k=4, N=54 k=6).

Set B was identified in the 2026-03-06 SageMath run as the "mirror sector"
triple that reproduces lepton mass ratios at p=139 rather than p=137.
Sets A and B are mutually exclusive: Set A hits only p=137, Set B only p=139.

Forms (Set B, mirror sector):
  k=2, N=195 : a_{139} = +15     [SageMath index 2]
  k=4, N=50  : a_{139} = +3100   [SageMath index 1]
  k=6, N=54  : a_{139} = +53009  [SageMath index 1]

How to run
----------
  sage global_scan_set_b.sage
  or paste at https://sagecell.sagemath.org/

Output is a table of all primes and their ratio errors.
Strong hits (both errors < threshold) are flagged.

Related files
-------------
  scripts/hecke/test_prime_specificity.sage — local scan, Sets A and B
  reports/hecke_lepton/prime_specificity_results.txt — confirmed results
  reports/hecke_lepton/mirror_world_139.md           — Set B analysis
  reports/hecke_lepton/sage_results_2026_03_07.md    — main report
"""

# ---------------------------------------------------------------------------
# Experimental targets (CODATA 2022 / PDG 2022) — DO NOT CHANGE
# ---------------------------------------------------------------------------
MU_RATIO  = 206.7682830   # m_μ / m_e
TAU_RATIO = 3477.23       # m_τ / m_e

# ---------------------------------------------------------------------------
# Set B forms (mirror sector, reference prime p=139)
# ---------------------------------------------------------------------------
SET_B_LEVEL_K2  = 195
SET_B_LEVEL_K4  = 50
SET_B_LEVEL_K6  = 54
SET_B_INDEX_K2  = 2    # CuspForms(Gamma0(195), 2).newforms('a')[2]
SET_B_INDEX_K4  = 1    # CuspForms(Gamma0(50),  4).newforms('a')[1]
SET_B_INDEX_K6  = 1    # CuspForms(Gamma0(54),  6).newforms('a')[1]
SET_B_A139_K2   = 15
SET_B_A139_K4   = 3100
SET_B_A139_K6   = 53009

# ---------------------------------------------------------------------------
# Scan range
# ---------------------------------------------------------------------------
SCAN_MIN   = 50
SCAN_MAX   = 300
HIT_THRESH_MU  = 0.5    # % threshold for μ-ratio to count as "hit"
HIT_THRESH_TAU = 5.0    # % threshold for τ-ratio to count as "hit"

# ---------------------------------------------------------------------------
# Helper: a_p via f[p] with fallback
# ---------------------------------------------------------------------------

def _a_p_float(form, p):
    """Return a_p(form) as a float, or None if unavailable.
    Uses form[p] (preferred), falls back to q_expansion_coefficients.
    """
    try:
        return float(form[p])
    except (TypeError, AttributeError, KeyError):
        pass
    try:
        val = form.q_expansion_coefficients(p + 1)[p]
        try:
            return float(val)
        except TypeError:
            return float(val.complex_embeddings()[0].real())
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Load forms
# ---------------------------------------------------------------------------

def _load_set_b_forms():
    """Load Set B forms and return (f_k2, f_k4, f_k6) or None on error."""
    print("Loading Set B forms ...")
    forms = []
    specs = [
        (SET_B_LEVEL_K2, 2, SET_B_INDEX_K2, SET_B_A139_K2, "k=2, N=195"),
        (SET_B_LEVEL_K4, 4, SET_B_INDEX_K4, SET_B_A139_K4, "k=4, N=50"),
        (SET_B_LEVEL_K6, 6, SET_B_INDEX_K6, SET_B_A139_K6, "k=6, N=54"),
    ]
    for N, k, idx, a139_expected, label in specs:
        try:
            S = CuspForms(Gamma0(N), k)
            nf = S.newforms('a')
        except Exception as e:
            print(f"  ERROR loading {label}: {e}")
            return None
        if idx >= len(nf):
            print(f"  ERROR: {label} index {idx} out of range "
                  f"(only {len(nf)} newforms)")
            return None
        f = nf[idx]
        a_val = _a_p_float(f, 139)
        if a_val is None or abs(a_val - a139_expected) > 0.5:
            print(f"  WARNING: {label} index [{idx}] gives a_139={a_val}, "
                  f"expected {a139_expected}. Proceeding anyway.")
        else:
            print(f"  {label} index [{idx}]: a_139 = {a_val:.0f}  ✓")
        forms.append(f)
    return tuple(forms)


# ---------------------------------------------------------------------------
# Main scan
# ---------------------------------------------------------------------------

print("=" * 72)
print("Global Prime Scan — Set B (Mirror Sector, reference prime p=139)")
print(f"Range: p = {SCAN_MIN}–{SCAN_MAX}")
print(f"Hit thresholds: err_mu < {HIT_THRESH_MU}%, err_tau < {HIT_THRESH_TAU}%")
print("=" * 72)
print()

loaded = _load_set_b_forms()
if loaded is None:
    print("FATAL: Could not load Set B forms. Aborting.")
else:
    f_k2, f_k4, f_k6 = loaded

    print()
    print(f"{'p':>6}  {'R_mu':>10}  {'err_mu':>8}  {'R_tau':>10}  {'err_tau':>8}  note")
    print("-" * 72)

    hits = []
    partial_hits = []

    for p in prime_range(SCAN_MIN, SCAN_MAX + 1):
        a2 = _a_p_float(f_k2, p)
        a4 = _a_p_float(f_k4, p)
        a6 = _a_p_float(f_k6, p)

        if None in (a2, a4, a6):
            print(f"{p:>6}  (missing eigenvalue)")
            continue
        if abs(a2) < 0.5:
            print(f"{p:>6}  (a_p(k=2)=0, ratio undefined)")
            continue

        R_mu  = abs(a4) / abs(a2)
        R_tau = abs(a6) / abs(a2)
        err_mu  = abs(R_mu  - MU_RATIO)  / MU_RATIO  * 100.0
        err_tau = abs(R_tau - TAU_RATIO) / TAU_RATIO  * 100.0

        is_hit     = err_mu < HIT_THRESH_MU  and err_tau < HIT_THRESH_TAU
        is_partial = err_mu < HIT_THRESH_MU  and err_tau >= HIT_THRESH_TAU

        flag = ""
        if is_hit:
            flag = "  *** HIT ***"
            hits.append((p, err_mu, err_tau))
        elif is_partial:
            flag = "  (partial — mu close)"
            partial_hits.append((p, err_mu, err_tau))

        if is_hit or is_partial or p == 139:
            print(f"{p:>6}  {R_mu:>10.4f}  {err_mu:>7.2f}%  "
                  f"{R_tau:>10.4f}  {err_tau:>7.2f}%{flag}")

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print()
    if hits:
        print(f"Strong hits (err_mu < {HIT_THRESH_MU}% AND err_tau < {HIT_THRESH_TAU}%):")
        for p, e_mu, e_tau in hits:
            print(f"  p={p}:  err_mu={e_mu:.2f}%,  err_tau={e_tau:.2f}%")
    else:
        print("  No strong hits found.")
    print()
    if partial_hits:
        print(f"Partial hits (err_mu < {HIT_THRESH_MU}%, tau further off):")
        for p, e_mu, e_tau in partial_hits:
            print(f"  p={p}:  err_mu={e_mu:.2f}%,  err_tau={e_tau:.2f}%")
    print()
    print("NOTE: These are NUMERICAL OBSERVATIONS only.")
    print("  A hit here is NOT a proof of any physical connection.")
    print("  See reports/hecke_lepton/mirror_world_139.md for interpretation.")
    print("=" * 72)

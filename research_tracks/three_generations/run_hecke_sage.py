#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
SageMath Hecke Eigenvalue Search for UBT Lepton Mass Ratios
============================================================

Run with:
    sage run_hecke_sage.py

Or paste the entire file at:
    https://sagecell.sagemath.org/

What this script does
---------------------
Searches for modular newform triples (f_0, f_1, f_2) with weights k=(2,4,6)
whose Hecke eigenvalues at the UBT prime p=137 reproduce the lepton mass ratios:

    |a_137(f_1)| / |a_137(f_0)|  ≈  m_μ / m_e  =  206.7682830  (CODATA 2022)
    |a_137(f_2)| / |a_137(f_0)|  ≈  m_τ / m_e  = 3477.23       (PDG 2022)

Prior results (from hecke_search_results.json / step5 analysis):
  - Best k=4 candidate: 4.4.a.a  with a_137 = 1626
  - Need k=2 form with |a_137| ≈ 7.86  → ratio 1626 / 7.86 ≈ 206.77  ✓
  - Need k=6 NON-CM form with |a_137| ∈ [500, 100000] at N ∈ [50, 500]
  - CM forms at N ≤ 4 are ruled out (|a_137| > 81400)

HOW TO RUN:

  Option A — SageMath online:
    Go to https://sagecell.sagemath.org/
    Paste the contents of this file and click Evaluate.

  Option B — SageMath local:
    sage run_hecke_sage.py

  Option C — LMFDB API (no SageMath needed):
    pip install requests
    python run_hecke_lmfdb_search.py

After running: commit hecke_lmfdb_results.json (or copy the printed output)
to the repository.  The verdict (MATCH_FOUND / NO_MATCH) is read next session.
"""

# ---------------------------------------------------------------------------
# Constants — CODATA 2022 / PDG 2022 — DO NOT CHANGE
# ---------------------------------------------------------------------------
P          = 137           # UBT prime (fixed by α⁻¹ = 137 + Δ_CT)
MU_RATIO   = 206.7682830   # m_μ / m_e
TAU_RATIO  = 3477.23       # m_τ / m_e
TOLERANCE  = 0.05          # 5%  — start here, tighten if hits found

# ---------------------------------------------------------------------------
# Known k=2 and k=4 eigenvalues from hecke_search_results.json
# (local-search results, verified by eta-products / elliptic curves)
# ---------------------------------------------------------------------------
KNOWN_K2 = [
    # (label, a_137)
    ("11.2.a.a",  -7),
    ("14.2.a.a",  18),
    ("15.2.a.a",  -6),
    ("17.2.a.a",  -6),
    ("19.2.a.a",  -3),
    ("20.2.a.a",  18),
    ("32.2.a.a",  -22),
    ("37.2.a.a",  -6),
    ("37.2.b.a",  -6),
    ("40.2.a.a",  18),
    ("64.2.a.a",  -22),
]

KNOWN_K4 = [
    # (label, a_137)
    ("4.4.a.a",   1626),
    ("5.4.a.a",  -2334),
    ("6.4.a.a",   -726),
]

# ---------------------------------------------------------------------------
# SageMath search
# ---------------------------------------------------------------------------

print("=" * 64)
print("SageMath Hecke Eigenvalue Search — UBT Lepton Mass Ratios")
print("=" * 64)
print(f"  prime p       = {P}")
print(f"  target μ      = {MU_RATIO}")
print(f"  target τ      = {TAU_RATIO}")
print(f"  tolerance     = {TOLERANCE:.0%}")
print()

# --- Step 1: Compute k=2 eigenvalues from scratch via SageMath ---
print("[STEP 1] Computing weight-2 newforms, N ∈ [1, 200] ...")
sage_k2 = []   # list of (label_str, level, a_137)

for N in range(1, 201):
    try:
        S = CuspForms(Gamma0(N), 2)
        for f in S.newforms('a'):
            a137 = f.q_expansion_coefficients(P + 1)[P]
            try:
                a_val = float(a137)
            except Exception:
                # Algebraic coefficient — take first real embedding
                try:
                    a_val = float(a137.complex_embeddings()[0].real())
                except Exception:
                    continue
            if abs(a_val) < 0.5:
                continue  # skip zero eigenvalue
            label = str(f)
            sage_k2.append((label, N, a_val))
    except Exception as err:
        pass  # empty space or computational error

print(f"  → {len(sage_k2)} weight-2 forms with non-zero a_{P}.")

# Supplement with known values from local search
known_k2_labels = {t[0] for t in sage_k2}
injected_k2 = 0
for lbl, a in KNOWN_K2:
    if lbl not in known_k2_labels and a != 0:
        N = int(lbl.split(".")[0])
        sage_k2.append((lbl, N, float(a)))
        known_k2_labels.add(lbl)
        injected_k2 += 1
if injected_k2:
    print(f"  + Injected {injected_k2} known k=2 form(s) from hecke_search_results.json.")

# --- Step 2: Compute k=4 eigenvalues ---
print(f"\n[STEP 2] Computing weight-4 newforms, N ∈ [1, 50] ...")
sage_k4 = []

for N in range(1, 51):
    try:
        S = CuspForms(Gamma0(N), 4)
        for f in S.newforms('a'):
            a137 = f.q_expansion_coefficients(P + 1)[P]
            try:
                a_val = float(a137)
            except Exception:
                try:
                    a_val = float(a137.complex_embeddings()[0].real())
                except Exception:
                    continue
            label = str(f)
            sage_k4.append((label, N, a_val))
    except Exception:
        pass

print(f"  → {len(sage_k4)} weight-4 forms computed.")

# Supplement with known values
known_k4_labels = {t[0] for t in sage_k4}
injected_k4 = 0
for lbl, a in KNOWN_K4:
    if lbl not in known_k4_labels:
        N = int(lbl.split(".")[0])
        sage_k4.append((lbl, N, float(a)))
        known_k4_labels.add(lbl)
        injected_k4 += 1
if injected_k4:
    print(f"  + Injected {injected_k4} known k=4 form(s) from hecke_search_results.json.")

# --- Step 3: Compute k=6 NON-CM eigenvalues, N ∈ [50, 500] ---
print(f"\n[STEP 3] Computing weight-6 NON-CM newforms, N ∈ [50, 500] ...")
print("  (This may take several minutes — estimated < 1 hour for N ≤ 200)")
print("  (Extend N range below if needed)")
sage_k6 = []

# Structural bound: a TAU-ratio match requires |a_137(f2)| ≤ max(|a_137(f0)|) * TAU_RATIO
# With Ramanujan bound |a_137(f0)| ≤ 2*137^{(k-1)/2} for k=2, we get ≤ 81400 roughly.
# We use a generous upper bound to avoid missing candidates.
K6_BOUND_LOW  =   500   # forms with |a_137| below this cannot give τ-ratio
K6_BOUND_HIGH = 100000  # structural upper bound (generous)

for N in range(50, 201):   # start with 50..200; extend to 501 by changing range(50, 501)
    try:
        S = CuspForms(Gamma0(N), 6)
        for f in S.newforms('a'):
            # Skip CM forms
            if f.has_cm():
                continue
            a137 = f.q_expansion_coefficients(P + 1)[P]
            try:
                a_val = float(a137)
            except Exception:
                try:
                    a_val = float(a137.complex_embeddings()[0].real())
                except Exception:
                    continue
            if abs(a_val) < K6_BOUND_LOW or abs(a_val) > K6_BOUND_HIGH:
                continue
            label = str(f)
            sage_k6.append((label, N, a_val))
            print(f"    N={N:4d}: {label:20s}  a_{P} = {a_val:12.1f}")
    except Exception:
        pass

print(f"  → {len(sage_k6)} non-CM k=6 forms with |a_{P}| ∈ [{K6_BOUND_LOW}, {K6_BOUND_HIGH}].")

# --- Step 4: Find matching triples ---
print(f"\n[STEP 4] Searching for matching triples (tolerance={TOLERANCE:.0%}) ...")

candidates = []

for lbl2, N2, a2 in sage_k6:
    abs2 = abs(a2)

    for lbl4, N4, a4 in sage_k4:
        abs4 = abs(a4)

        for lbl0, N0, a0 in sage_k2:
            abs0 = abs(a0)
            if abs0 < 0.5:
                continue

            ratio_mu  = abs4 / abs0
            ratio_tau = abs2 / abs0

            err_mu  = abs(ratio_mu  - MU_RATIO)  / MU_RATIO
            err_tau = abs(ratio_tau - TAU_RATIO) / TAU_RATIO

            if err_mu < TOLERANCE and err_tau < TOLERANCE:
                print(f"\n{'*'*56}")
                print(f"*** MATCH FOUND ***")
                print(f"  f0 (k=2): {lbl0}  a_{P} = {a0:.1f}  (N={N0})")
                print(f"  f1 (k=4): {lbl4}  a_{P} = {a4:.1f}  (N={N4})")
                print(f"  f2 (k=6): {lbl2}  a_{P} = {a2:.1f}  (N={N2})")
                print(f"  μ-ratio : {ratio_mu:.5f}  (target {MU_RATIO:.5f}, err {err_mu:.2%})")
                print(f"  τ-ratio : {ratio_tau:.4f}  (target {TAU_RATIO:.4f}, err {err_tau:.2%})")
                print(f"{'*'*56}")
                candidates.append({
                    "f0": {"label": lbl0, "level": N0, "a_137": a0},
                    "f1": {"label": lbl4, "level": N4, "a_137": a4},
                    "f2": {"label": lbl2, "level": N2, "a_137": a2},
                    "ratio_mu":  float(ratio_mu),
                    "ratio_tau": float(ratio_tau),
                    "error_mu":  float(err_mu),
                    "error_tau": float(err_tau),
                })

# --- Step 5: Print summary and save JSON ---
print()
print("=" * 64)
if candidates:
    verdict = "MATCH_FOUND"
    verdict_note = (
        f"Found {len(candidates)} matching triple(s). "
        "See 'candidates' list for details."
    )
elif not sage_k6:
    verdict = "INCONCLUSIVE"
    verdict_note = (
        "No k=6 non-CM forms found with |a_137| in the required range. "
        "Consider extending the level range above N=200."
    )
else:
    verdict = "NO_MATCH"
    verdict_note = (
        f"No matching triple within {TOLERANCE:.0%} tolerance. "
        f"Searched {len(sage_k2)} k=2 forms (N≤200), "
        f"{len(sage_k4)} k=4 forms (N≤50), "
        f"{len(sage_k6)} k=6 non-CM forms (N∈[50,200])."
    )

print(f"VERDICT: {verdict}")
print(f"  {verdict_note}")
print("=" * 64)

# Build JSON output (paste or redirect this into hecke_lmfdb_results.json)
import json as _json

results = {
    "search_parameters": {
        "prime":          P,
        "target_mu":      MU_RATIO,
        "target_tau":     TAU_RATIO,
        "tolerance":      TOLERANCE,
        "k2_level_range": "1..200",
        "k4_level_range": "1..50",
        "k6_level_range": "50..200  (extend range(50,501) to search higher levels)",
        "k6_nonCM_only":  True,
        "method":         "SageMath_CuspForms",
    },
    "candidates": candidates,
    "k6_nonCM_forms_found": [
        {"label": lbl, "level": N, "a_137": a}
        for lbl, N, a in sage_k6
    ],
    "verdict":      verdict,
    "verdict_note": verdict_note,
}

print("\n--- JSON OUTPUT (copy to hecke_lmfdb_results.json) ---")
print(_json.dumps(results, indent=2))

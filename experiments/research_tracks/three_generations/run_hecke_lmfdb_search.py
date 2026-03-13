#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
LMFDB Hecke Eigenvalue Search for UBT Lepton Mass Ratios
=========================================================
Run this script locally (requires internet access + requests library).

Usage:
    pip install requests
    python run_hecke_lmfdb_search.py

Results saved to: hecke_lmfdb_results.json

HOW TO RUN:

  Option A — LMFDB API (this script):
    pip install requests
    python run_hecke_lmfdb_search.py
    → saves hecke_lmfdb_results.json

  Option B — SageMath (run_hecke_sage.py):
    Online: go to https://sagecell.sagemath.org/
            paste the contents of run_hecke_sage.py
            click Evaluate
    Local:  sage run_hecke_sage.py

  After running: commit hecke_lmfdb_results.json to the repo.
  The verdict (MATCH_FOUND / NO_MATCH) will be read in the next session.

Theory context
--------------
We search for newform triples (f_0, f_1, f_2) with weights k=(2, 4, 6) whose
Hecke eigenvalues at the UBT prime p=137 reproduce the lepton mass ratios:

    |a_137(f_1)| / |a_137(f_0)|  ≈  m_μ / m_e  =  206.7682830  (CODATA 2022)
    |a_137(f_2)| / |a_137(f_0)|  ≈  m_τ / m_e  = 3477.23       (PDG 2022)

Prior results (from hecke_search_results.json):
  - Best k=4 candidate: 4.4.a.a  with a_137 = 1626
  - Need k=2 form with |a_137| ≈ 7.86  → ratio 1626 / 7.86 ≈ 206.77  ✓
  - Need k=6 NON-CM form with |a_137| ∈ [500, 100000] at N ∈ [50, 500]
  - CM forms at N ≤ 4 are ruled out (|a_137| > 81400)
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

try:
    import requests
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

# ---------------------------------------------------------------------------
# Physical constants — CODATA 2022 / PDG 2022 — DO NOT CHANGE
# ---------------------------------------------------------------------------
MU_RATIO  = 206.7682830   # m_μ / m_e
TAU_RATIO = 3477.23       # m_τ / m_e
P = 137                   # UBT prime (fixed by α⁻¹ = 137 + Δ_CT)
TOLERANCE = 0.05          # 5% — start here, tighten if hits found

# ---------------------------------------------------------------------------
# LMFDB API configuration
# ---------------------------------------------------------------------------
LMFDB_BASE = "https://www.lmfdb.org/api"
TIMEOUT    = 30           # seconds per HTTP request
PAGE_LIMIT = 500          # records per page (LMFDB max is typically 1000)
RETRY_MAX  = 3            # retries on transient network errors

# Known k=4 forms from local search (step4 analysis)
KNOWN_K4 = [
    {"label": "4.4.a.a",  "level": 4,  "a_137": 1626.0},
    {"label": "5.4.a.a",  "level": 5,  "a_137": -2334.0},
    {"label": "6.4.a.a",  "level": 6,  "a_137": -726.0},
]


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _primes_up_to(n: int) -> List[int]:
    """Sieve of Eratosthenes — return all primes ≤ n."""
    if n < 2:
        return []
    sieve = bytearray([1] * (n + 1))
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(2, n + 1) if sieve[i]]


PRIMES_TO_P = _primes_up_to(P)
P_INDEX     = PRIMES_TO_P.index(P)   # 0-based index of 137 in prime list (= 32)


def _extract_a_p_from_record(record: Dict[str, Any], p_idx: int) -> Optional[float]:
    """
    Extract the Hecke eigenvalue a_p from a mf_newforms or mf_hecke_nf record.

    LMFDB storage formats observed in the wild:
      'hecke_eigenvalues'   : list indexed by prime index (0-based), each entry
                              is int/float or a list [real_embedding, ...] for
                              algebraic eigenvalues.
      'an'                  : list a_1, a_2, ..., a_n (Dirichlet coefficients).
                              a_137 is at index 136 (0-based) if list is long enough.
      'hecke_eigs'          : same as 'hecke_eigenvalues' in mf_hecke_nf table.
      'eigenvalues'         : alternative name seen in some API versions.

    We try all known formats and return the float value if found.
    """
    # --- Format 1: hecke_eigenvalues / hecke_eigs / eigenvalues (prime-indexed) ---
    for field in ("hecke_eigenvalues", "hecke_eigs", "eigenvalues"):
        eigs = record.get(field)
        if isinstance(eigs, list) and p_idx < len(eigs):
            val = eigs[p_idx]
            if isinstance(val, (int, float)):
                return float(val)
            # Algebraic: first element is a real embedding in some LMFDB formats
            if isinstance(val, list) and val and isinstance(val[0], (int, float)):
                return float(val[0])

    # --- Format 2: 'an' — Dirichlet coefficients a_1..a_N (1-indexed) ---
    an = record.get("an")
    if isinstance(an, list) and P <= len(an):
        val = an[P - 1]  # 0-based
        if isinstance(val, (int, float)):
            return float(val)
        if isinstance(val, list) and val and isinstance(val[0], (int, float)):
            return float(val[0])

    return None


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _get(url: str, params: Dict[str, Any]) -> Optional[Dict]:
    """
    HTTP GET with retry logic.  Returns parsed JSON or None on failure.

    Note on LMFDB API URL syntax:
      https://www.lmfdb.org/api/mf_newforms/?weight=2&level=1..200&_fields=...
      Ranges use the format  field=low..high  (two dots).
      Boolean fields: is_cm=false  (literal string "false").
    """
    if not _HAS_REQUESTS:
        # Fallback: use stdlib urllib
        import urllib.parse, urllib.request, urllib.error
        full_url = url + "?" + urllib.parse.urlencode(params)
        for attempt in range(RETRY_MAX):
            try:
                with urllib.request.urlopen(full_url, timeout=TIMEOUT) as resp:
                    return json.loads(resp.read().decode())
            except Exception:
                if attempt < RETRY_MAX - 1:
                    time.sleep(2 ** attempt)
        return None

    for attempt in range(RETRY_MAX):
        try:
            resp = requests.get(url, params=params, timeout=TIMEOUT)
            if resp.status_code == 200:
                return resp.json()
            print(f"    [HTTP {resp.status_code}] {url}")
        except requests.RequestException as exc:
            print(f"    [Network error attempt {attempt+1}/{RETRY_MAX}] {exc}")
        if attempt < RETRY_MAX - 1:
            time.sleep(2 ** attempt)
    return None


def _paginate(
    endpoint: str,
    base_params: Dict[str, Any],
    max_pages: int = 20,
) -> Tuple[bool, List[Dict]]:
    """
    Paginate through all results at `endpoint` using _limit / _offset.
    Returns (network_ok, records).
    """
    records: List[Dict] = []
    offset = 0
    network_ok = False

    for page_num in range(max_pages):
        params = {**base_params, "_limit": PAGE_LIMIT, "_offset": offset, "_format": "json"}
        data = _get(endpoint, params)
        if data is None:
            print(f"    [WARN] No data at offset={offset} (network error or end of results).")
            break
        network_ok = True

        # LMFDB API wraps results in {"data": [...]} or {"results": [...]}
        page = data.get("data") or data.get("results") or []
        if not isinstance(page, list):
            break
        records.extend(page)

        # Check if there are more pages
        total = data.get("count") or data.get("total") or 0
        if len(page) < PAGE_LIMIT or (total and offset + PAGE_LIMIT >= total):
            break
        offset += PAGE_LIMIT

    return network_ok, records


# ---------------------------------------------------------------------------
# Hecke eigenvalue fetcher via mf_hecke_nf endpoint
# ---------------------------------------------------------------------------

def _fetch_a_p_from_hecke_nf(label: str) -> Optional[float]:
    """
    Fetch a_137 for a specific form via the mf_hecke_nf table.

    LMFDB endpoint:
      GET /api/mf_hecke_nf/?label=<label>&_fields=label,hecke_eigs

    This is used as a fallback when the mf_newforms record does not contain
    the 'hecke_eigenvalues' field (common for algebraic-coefficient forms).
    """
    endpoint = f"{LMFDB_BASE}/mf_hecke_nf/"
    params = {
        "label": label,
        "_fields": "label,hecke_eigs,hecke_eigenvalues,eigenvalues,an",
        "_format": "json",
        "_limit": 1,
    }
    data = _get(endpoint, params)
    if data is None:
        return None
    recs = data.get("data") or data.get("results") or []
    for rec in recs:
        val = _extract_a_p_from_record(rec, P_INDEX)
        if val is not None:
            return val
    return None


# ---------------------------------------------------------------------------
# Step 1: Fetch weight-2 newforms, level ≤ 200
# ---------------------------------------------------------------------------

def fetch_k2_forms() -> Tuple[bool, List[Dict]]:
    """
    Query LMFDB for weight-2 newforms at levels 1..200.

    Fields requested: label, level, weight, hecke_eigenvalues, an_normalization

    Note: Many weight-2 forms have rational (integer) Hecke eigenvalues and
    LMFDB stores them directly in 'hecke_eigenvalues'.  Algebraic eigenvalues
    (higher-dimensional Galois orbits) are stored as lists of embeddings.
    """
    print("\n[STEP 1] Fetching weight-2 newforms, N ≤ 200 ...")
    endpoint = f"{LMFDB_BASE}/mf_newforms/"
    params = {
        "weight": 2,
        "level": "1..200",
        "_fields": "label,level,weight,hecke_eigenvalues,an,an_normalization,is_cm,cm_disc",
    }
    ok, records = _paginate(endpoint, params)
    print(f"  → {len(records)} weight-2 records retrieved.")
    return ok, records


# ---------------------------------------------------------------------------
# Step 2: Fetch / verify weight-4 newforms, level ≤ 50
# ---------------------------------------------------------------------------

def fetch_k4_forms() -> Tuple[bool, List[Dict]]:
    """
    Query LMFDB for weight-4 newforms at levels 1..50.
    We already know 4.4.a.a, 5.4.a.a, 6.4.a.a from the local search;
    this call verifies them via the API and extends to the full level range.
    """
    print("\n[STEP 2] Fetching weight-4 newforms, N ≤ 50 ...")
    endpoint = f"{LMFDB_BASE}/mf_newforms/"
    params = {
        "weight": 4,
        "level": "1..50",
        "_fields": "label,level,weight,hecke_eigenvalues,an,an_normalization,is_cm,cm_disc",
    }
    ok, records = _paginate(endpoint, params)
    print(f"  → {len(records)} weight-4 records retrieved.")
    return ok, records


# ---------------------------------------------------------------------------
# Step 3: Fetch weight-6 NON-CM newforms, level 50–500
# ---------------------------------------------------------------------------

def fetch_k6_nonCM_forms() -> Tuple[bool, List[Dict]]:
    """
    Query LMFDB for weight-6 NON-CM newforms at levels 50..500.

    CM forms are ruled out by structural analysis (step5):
    all small-level CM forms have |a_137| >> 81400 = max consistent with
    the τ-ratio and the Ramanujan bound at k=2.

    LMFDB CM filter:
      is_cm=0   means NOT a CM form (cm_disc field is 0 or null)
      Depending on LMFDB API version, use is_cm=0 or is_cm=false or cm_disc=0.
      We try 'cm_disc=0' (integer) which is most stable across versions.

    Note: If is_cm / cm_disc filtering does not work via the API,
    we fall back to fetching all k=6 forms and filtering locally by
    checking record['is_cm'] == False or record['cm_disc'] == 0.
    """
    print("\n[STEP 3] Fetching weight-6 NON-CM newforms, N ∈ [50, 500] ...")
    endpoint = f"{LMFDB_BASE}/mf_newforms/"

    # Try with CM filter (preferred — reduces data transfer)
    params = {
        "weight": 6,
        "level": "50..500",
        "cm_disc": 0,           # 0 = not CM in LMFDB schema
        "_fields": "label,level,weight,hecke_eigenvalues,an,an_normalization,is_cm,cm_disc",
    }
    ok, records = _paginate(endpoint, params)

    if ok and records:
        print(f"  → {len(records)} weight-6 records (cm_disc=0 filter applied).")
    else:
        # Fallback: fetch all k=6 forms and filter locally
        print("  [FALLBACK] cm_disc=0 filter returned no results. "
              "Fetching all k=6 forms and filtering locally ...")
        params_nofilt = {
            "weight": 6,
            "level": "50..500",
            "_fields": "label,level,weight,hecke_eigenvalues,an,an_normalization,is_cm,cm_disc",
        }
        ok, all_records = _paginate(endpoint, params_nofilt)
        # Filter: keep only non-CM forms
        records = [
            r for r in all_records
            if not r.get("is_cm") and r.get("cm_disc", 0) in (0, None)
        ]
        print(f"  → {len(records)} non-CM weight-6 forms (out of {len(all_records)} total).")

    return ok, records


# ---------------------------------------------------------------------------
# Eigenvalue extraction with fallback to mf_hecke_nf
# ---------------------------------------------------------------------------

def get_a_p(record: Dict[str, Any]) -> Optional[float]:
    """
    Return a_137 for a newform record.

    Tries in order:
      1. 'hecke_eigenvalues' / 'hecke_eigs' / 'eigenvalues' (prime-indexed list)
      2. 'an' (Dirichlet coefficient list, index 136)
      3. mf_hecke_nf API endpoint (per-label fallback)
    """
    val = _extract_a_p_from_record(record, P_INDEX)
    if val is not None:
        return val

    # Fallback: fetch from dedicated Hecke table
    label = record.get("label")
    if label:
        val = _fetch_a_p_from_hecke_nf(label)
    return val


# ---------------------------------------------------------------------------
# Step 4: Find matching triples
# ---------------------------------------------------------------------------

def find_triples(
    k2_forms: List[Dict],
    k4_forms: List[Dict],
    k6_forms: List[Dict],
    tolerance: float = TOLERANCE,
) -> List[Dict]:
    """
    Search all (f0, f1, f2) triples for matching lepton mass ratios.

    Matching condition:
      err_mu  = |ratio_mu  - MU_RATIO|  / MU_RATIO  < tolerance
      err_tau = |ratio_tau - TAU_RATIO| / TAU_RATIO  < tolerance

    where
      ratio_mu  = |a_137(f1)| / |a_137(f0)|
      ratio_tau = |a_137(f2)| / |a_137(f0)|
    """
    print(f"\n[STEP 4] Searching for matching triples (tolerance={tolerance:.0%}) ...")

    # Pre-compute eigenvalues to avoid re-fetching
    def _enrich(forms: List[Dict], weight: int) -> List[Dict]:
        enriched = []
        missing = 0
        for r in forms:
            a = get_a_p(r)
            if a is None:
                missing += 1
                continue
            if a == 0.0:
                continue
            enriched.append({
                "label":  r.get("label", "?"),
                "level":  r.get("level"),
                "weight": weight,
                "a_137":  a,
            })
        if missing:
            print(f"  [k={weight}] {missing} form(s) skipped (eigenvalue not available in API).")
        return enriched

    e2 = _enrich(k2_forms, 2)
    e4 = _enrich(k4_forms, 4)
    e6 = _enrich(k6_forms, 6)

    print(f"  Forms with a_137: k=2:{len(e2)}, k=4:{len(e4)}, k=6:{len(e6)}")

    # Inject known k=4 values if not already present from API
    known_labels = {r["label"] for r in e4}
    injected = 0
    for kf in KNOWN_K4:
        if kf["label"] not in known_labels:
            e4.append(dict(kf, weight=4))
            known_labels.add(kf["label"])
            injected += 1
    if injected:
        print(f"  Injected {injected} known k=4 form(s) not returned by API.")

    candidates: List[Dict] = []

    for f0 in e2:
        abs0 = abs(f0["a_137"])
        if abs0 < 1.0:
            continue  # avoid near-zero denominators

        for f1 in e4:
            ratio_mu = abs(f1["a_137"]) / abs0
            err_mu   = abs(ratio_mu - MU_RATIO) / MU_RATIO
            if err_mu > tolerance:
                continue  # early exit

            for f2 in e6:
                ratio_tau = abs(f2["a_137"]) / abs0
                err_tau   = abs(ratio_tau - TAU_RATIO) / TAU_RATIO
                if err_tau > tolerance:
                    continue

                print(
                    f"  *** CANDIDATE FOUND ***\n"
                    f"    f0(k=2): {f0['label']}  a_137={f0['a_137']}\n"
                    f"    f1(k=4): {f1['label']}  a_137={f1['a_137']}\n"
                    f"    f2(k=6): {f2['label']}  a_137={f2['a_137']}\n"
                    f"    ratio_μ = {ratio_mu:.5f}  (target {MU_RATIO:.5f}, err {err_mu:.2%})\n"
                    f"    ratio_τ = {ratio_tau:.4f}  (target {TAU_RATIO:.4f}, err {err_tau:.2%})"
                )
                candidates.append({
                    "f0":        {"label": f0["label"], "level": f0["level"], "a_137": f0["a_137"]},
                    "f1":        {"label": f1["label"], "level": f1["level"], "a_137": f1["a_137"]},
                    "f2":        {"label": f2["label"], "level": f2["level"], "a_137": f2["a_137"]},
                    "ratio_mu":  ratio_mu,
                    "ratio_tau": ratio_tau,
                    "error_mu":  err_mu,
                    "error_tau": err_tau,
                })

    return candidates


# ---------------------------------------------------------------------------
# Step 5: Build results dict and save
# ---------------------------------------------------------------------------

def build_results(
    k2_forms: List[Dict],
    k4_forms: List[Dict],
    k6_forms: List[Dict],
    candidates: List[Dict],
    network_ok_k2: bool,
    network_ok_k4: bool,
    network_ok_k6: bool,
    tolerance: float,
) -> Dict:
    """Assemble the final results dictionary."""

    # All k=6 non-CM forms with their a_137 (for inspection)
    k6_nonCM_with_eig = []
    for r in k6_forms:
        a = get_a_p(r)
        if a is not None:
            k6_nonCM_with_eig.append({
                "label": r.get("label"),
                "level": r.get("level"),
                "a_137": a,
                "is_cm": r.get("is_cm", False),
                "cm_disc": r.get("cm_disc"),
            })

    # Levels actually searched
    k2_levels = sorted({r.get("level") for r in k2_forms if r.get("level")})
    k4_levels = sorted({r.get("level") for r in k4_forms if r.get("level")})
    k4_levels += sorted({kf["level"] for kf in KNOWN_K4 if kf["level"] not in k4_levels})
    k6_levels = sorted({r.get("level") for r in k6_forms if r.get("level")})

    if candidates:
        verdict = "MATCH_FOUND"
        verdict_note = (
            f"Found {len(candidates)} matching triple(s). "
            "See 'candidates' list for details."
        )
    elif not (network_ok_k2 or network_ok_k4 or network_ok_k6):
        verdict = "INCONCLUSIVE"
        verdict_note = (
            "Network unavailable — could not reach the LMFDB API. "
            "Run this script on a machine with internet access, or use "
            "run_hecke_sage.py instead."
        )
    elif not k6_nonCM_with_eig:
        verdict = "INCONCLUSIVE"
        verdict_note = (
            "No weight-6 non-CM forms with retrievable a_137 were found. "
            "The LMFDB may not yet store hecke_eigenvalues for all forms at "
            "these levels.  Consider using run_hecke_sage.py for local computation."
        )
    else:
        verdict = "NO_MATCH"
        verdict_note = (
            f"No matching triple found within {tolerance:.0%} tolerance. "
            f"Searched {len(k2_forms)} k=2 forms (N≤200), "
            f"{len(k4_forms)+len(KNOWN_K4)} k=4 forms (N≤50), "
            f"{len(k6_forms)} k=6 non-CM forms (N∈[50,500]).  "
            "If eigenvalue coverage was incomplete (many 'skipped' warnings), "
            "run run_hecke_sage.py for exhaustive local computation."
        )

    return {
        "search_parameters": {
            "prime":              P,
            "target_mu":          MU_RATIO,
            "target_tau":         TAU_RATIO,
            "tolerance":          tolerance,
            "k2_level_range":     "1..200",
            "k4_level_range":     "1..50",
            "k6_level_range":     "50..500",
            "k6_nonCM_only":      True,
            "k2_levels_searched": k2_levels,
            "k4_levels_searched": k4_levels,
            "k6_levels_searched": k6_levels,
            "lmfdb_endpoint":     LMFDB_BASE,
        },
        "candidates":            candidates,
        "k6_nonCM_forms_found":  k6_nonCM_with_eig,
        "verdict":               verdict,
        "verdict_note":          verdict_note,
    }


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Search LMFDB for Hecke eigenvalue triples matching UBT lepton mass ratios."
    )
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "hecke_lmfdb_results.json"),
        help="Output JSON file (default: hecke_lmfdb_results.json)",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=TOLERANCE,
        help=f"Relative tolerance for ratio matching (default: {TOLERANCE})",
    )
    args = parser.parse_args()

    if not _HAS_REQUESTS:
        print(
            "[WARNING] 'requests' library not installed.  "
            "Falling back to stdlib urllib.  "
            "Install with:  pip install requests"
        )

    print("=" * 64)
    print("LMFDB Hecke Eigenvalue Search — UBT Lepton Mass Ratios")
    print("=" * 64)
    print(f"  Prime p           = {P}")
    print(f"  Target m_μ/m_e    = {MU_RATIO}")
    print(f"  Target m_τ/m_e    = {TAU_RATIO}")
    print(f"  Tolerance         = {args.tolerance:.0%}")
    print(f"  LMFDB endpoint    = {LMFDB_BASE}")
    print(f"  p=137 prime index = {P_INDEX}  (0-based in prime list)")
    print()
    print("  LMFDB API note:")
    print("  Eigenvalue availability: LMFDB stores hecke_eigenvalues for many")
    print("  newforms, but coverage depends on dimension and level.  Forms")
    print("  with high-degree coefficient fields may only have partial data.")
    print("  If you see many 'eigenvalue not available' warnings, use")
    print("  run_hecke_sage.py for exact computation via SageMath.")
    print()

    # --- Fetch forms ---
    ok2, k2_forms = fetch_k2_forms()
    ok4, k4_forms = fetch_k4_forms()
    ok6, k6_forms = fetch_k6_nonCM_forms()

    # --- Verify known k=4 forms via API ---
    print("\n[STEP 2b] Verifying known k=4 forms via API ...")
    for kf in KNOWN_K4:
        api_rec = next((r for r in k4_forms if r.get("label") == kf["label"]), None)
        if api_rec:
            api_a = get_a_p(api_rec)
            if api_a is not None:
                agree = "✓ AGREE" if abs(api_a - kf["a_137"]) < 0.5 else "✗ DISAGREE"
                print(f"  {kf['label']:15s}  local={kf['a_137']:>8.0f}  api={api_a:>8.1f}  {agree}")
            else:
                print(f"  {kf['label']:15s}  local={kf['a_137']:>8.0f}  api=N/A (not in response)")
        else:
            print(f"  {kf['label']:15s}  local={kf['a_137']:>8.0f}  api=not returned by query")

    # --- Find triples ---
    candidates = find_triples(k2_forms, k4_forms, k6_forms, tolerance=args.tolerance)

    # --- Build results ---
    results = build_results(
        k2_forms, k4_forms, k6_forms,
        candidates,
        ok2, ok4, ok6,
        args.tolerance,
    )

    # --- Print summary ---
    print()
    print("=" * 64)
    print(f"VERDICT: {results['verdict']}")
    print(f"  {results['verdict_note']}")
    print("=" * 64)
    print(f"  k=2 forms retrieved  : {len(k2_forms)}")
    print(f"  k=4 forms retrieved  : {len(k4_forms)}  (+{len(KNOWN_K4)} known from local search)")
    print(f"  k=6 non-CM retrieved : {len(k6_forms)}")
    print(f"  k=6 with a_137       : {len(results['k6_nonCM_forms_found'])}")
    print(f"  Candidates           : {len(candidates)}")

    # --- Save ---
    out_path = args.output
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)
    print(f"\nResults written to: {out_path}")
    print("Commit this file to the repo when done.")


if __name__ == "__main__":
    main()

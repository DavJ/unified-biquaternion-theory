# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
search_hecke_lmfdb_api.py
==========================

Approach B: Query the LMFDB REST API for newform Hecke eigenvalues.

Searches for newform triples (f_0, f_1, f_2) with weights k=(2,4,6)
and levels N≤500 whose Hecke eigenvalue at p=137 gives:

    |a_137(f_1)| / |a_137(f_0)| ≈ m_μ/m_e  = 206.7682830  (CODATA)
    |a_137(f_2)| / |a_137(f_0)| ≈ m_τ/m_e  = 3477.23       (CODATA)

API:  https://www.lmfdb.org/api/mf_newforms
Docs: https://www.lmfdb.org/api/

If the LMFDB is unavailable (network blocked, timeout), falls back
automatically to Approach A (search_hecke_lmfdb_local.py).

Run with:
    python search_hecke_lmfdb_api.py
    python search_hecke_lmfdb_api.py --max-level 500 --output results.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Physical constants (CODATA 2022 / PDG 2022) — same as local script
# ---------------------------------------------------------------------------
MU_RATIO  = 206.7682830
TAU_RATIO = 3477.23
TOLERANCE = 0.05           # 5% fractional tolerance
P = 137                    # UBT prime

# LMFDB API base URL
LMFDB_API = "https://www.lmfdb.org/api/mf_newforms/"
TIMEOUT    = 15            # seconds per HTTP request


# ---------------------------------------------------------------------------
# LMFDB API helpers
# ---------------------------------------------------------------------------

def lmfdb_query(params: Dict[str, Any], timeout: int = TIMEOUT) -> Optional[Dict]:
    """
    Perform a GET request to the LMFDB mf_newforms API.
    Returns the parsed JSON response, or None on failure.
    """
    url = LMFDB_API + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
        return data
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, TimeoutError) as exc:
        return None
    except Exception:
        return None


def fetch_newforms_for_weight(weight: int, max_level: int) -> Tuple[bool, List[Dict]]:
    """
    Query LMFDB for all newforms with given weight and level ≤ max_level.
    Returns (network_ok, list_of_records).
    Each record is a LMFDB mf_newforms dict (or a minimal synthetic dict on failure).
    """
    params = {
        "weight": weight,
        "level": f"1..{max_level}",
        "_fields": "label,level,weight,hecke_eigenvalues,an_normalization,char_labels",
        "_format": "json",
        "_limit": 500,
    }
    data = lmfdb_query(params)
    if data is None:
        return False, []
    records = data.get("data", data.get("results", []))
    return True, records


def extract_a_p(record: Dict, p: int) -> Optional[float]:
    """
    Extract the Hecke eigenvalue a_p from an LMFDB mf_newforms record.

    The LMFDB stores eigenvalues in two possible fields:
      'hecke_eigenvalues': a list [..., a_2, a_3, a_5, ...] indexed by prime index
      'an_normalization': can be 'analytic' or 'arithmetic'

    For primes, the index k in hecke_eigenvalues corresponds to the k-th prime.
    p=137 is the 33rd prime (0-based index 32 in a 0-indexed list of primes).

    Eigenvalues may be rational (float) or algebraic (stored as a list
    representing the minimal polynomial or an embedding).  We return the
    real embedding if available, else None.
    """
    eigs = record.get("hecke_eigenvalues") or record.get("hecke_orbit_code")
    if eigs is None:
        return None

    # Build prime list up to p
    primes_up_to_p = _primes_up_to(p)
    try:
        idx = primes_up_to_p.index(p)
    except ValueError:
        return None

    if isinstance(eigs, list) and idx < len(eigs):
        val = eigs[idx]
        if isinstance(val, (int, float)):
            return float(val)
        # Algebraic: first element of list is a real embedding in some LMFDB formats
        if isinstance(val, list) and len(val) > 0 and isinstance(val[0], (int, float)):
            return float(val[0])
    return None


def _primes_up_to(n: int) -> List[int]:
    """Sieve of Eratosthenes up to n (inclusive)."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


# ---------------------------------------------------------------------------
# Ratio checker
# ---------------------------------------------------------------------------

def check_triple(
    f0: Dict,
    f1: Dict,
    f2: Dict,
    target_mu: float,
    target_tau: float,
    tol: float,
) -> Optional[Dict]:
    """Return a candidate dict if the triple matches, else None."""
    ap0 = extract_a_p(f0, P)
    ap1 = extract_a_p(f1, P)
    ap2 = extract_a_p(f2, P)
    if ap0 is None or ap1 is None or ap2 is None:
        return None
    if ap0 == 0:
        return None
    abs0, abs1, abs2 = abs(ap0), abs(ap1), abs(ap2)
    ratio_mu  = abs1 / abs0
    ratio_tau = abs2 / abs0
    err_mu    = abs(ratio_mu  - target_mu)  / target_mu
    err_tau   = abs(ratio_tau - target_tau) / target_tau
    if err_mu > tol or err_tau > tol:
        return None
    return {
        "f0": {"label": f0.get("label"), "level": f0.get("level"), f"a_{P}": ap0},
        "f1": {"label": f1.get("label"), "level": f1.get("level"), f"a_{P}": ap1},
        "f2": {"label": f2.get("label"), "level": f2.get("level"), f"a_{P}": ap2},
        "ratio_mu":  ratio_mu,
        "ratio_tau": ratio_tau,
        "err_mu":    err_mu,
        "err_tau":   err_tau,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_api_search(max_level: int = 500, tolerance: float = TOLERANCE) -> Dict:
    print(f"\n{'='*60}")
    print(f"HECKE EIGENVALUE SEARCH (LMFDB API)")
    print(f"  endpoint: {LMFDB_API}")
    print(f"  prime p = {P}")
    print(f"  weights k = (2, 4, 6)")
    print(f"  max level N = {max_level}")
    print(f"  target m_μ/m_e  = {MU_RATIO:.7f}  (CODATA)")
    print(f"  target m_τ/m_e  = {TAU_RATIO:.4f}    (CODATA)")
    print(f"  tolerance       = {tolerance:.0%}")
    print(f"{'='*60}\n")

    network_ok = True
    forms_by_weight: Dict[int, List[Dict]] = {}

    for weight in (2, 4, 6):
        print(f"[API] Querying weight-{weight} newforms (N≤{max_level}) ...")
        ok, records = fetch_newforms_for_weight(weight, max_level)
        if not ok:
            print(f"  ✗ Network failure or timeout for weight={weight}.")
            network_ok = False
            forms_by_weight[weight] = []
        else:
            print(f"  ✓ Received {len(records)} records.")
            forms_by_weight[weight] = records

    if not network_ok:
        print("\n[FALLBACK] Network unavailable — falling back to Approach A "
              "(search_hecke_lmfdb_local.py).")
        # Import and run local search
        local_dir = os.path.dirname(__file__)
        if local_dir not in sys.path:
            sys.path.insert(0, local_dir)
        try:
            from search_hecke_lmfdb_local import run_search as local_run
            local_results = local_run(max_level=min(max_level, 200), tolerance=tolerance)
        except Exception as exc:
            local_results = {"error": str(exc)}
        return {
            "approach": "B_api_with_fallback_to_A",
            "network_available": False,
            "api_endpoint": LMFDB_API,
            "fallback_used": True,
            "fallback_results": local_results,
            "candidates": local_results.get("candidates", []),
            "verdict": local_results.get("verdict", "ERROR"),
            "verdict_note": (
                "LMFDB API unavailable (network blocked or timed out). "
                "Fell back to local Approach A. "
                + local_results.get("verdict_note", "")
            ),
        }

    # Network available — search triples
    print(f"\n[SEARCH] Checking triples ...")
    w2 = forms_by_weight.get(2, [])
    w4 = forms_by_weight.get(4, [])
    w6 = forms_by_weight.get(6, [])

    candidates = []
    skipped_no_eig = 0
    total_checked = 0

    for f0 in w2:
        ap0 = extract_a_p(f0, P)
        if ap0 is None or ap0 == 0:
            skipped_no_eig += 1
            continue
        for f1 in w4:
            ap1 = extract_a_p(f1, P)
            if ap1 is None:
                continue
            if abs(abs(ap1) / abs(ap0) - MU_RATIO) / MU_RATIO > tolerance:
                continue
            for f2 in w6:
                total_checked += 1
                c = check_triple(f0, f1, f2, MU_RATIO, TAU_RATIO, tolerance)
                if c is not None:
                    candidates.append(c)

    verdict = "MATCH_FOUND" if candidates else "NO_MATCH_IN_SEARCH_SPACE"

    print(f"  Forms checked: k=2:{len(w2)}, k=4:{len(w4)}, k=6:{len(w6)}")
    print(f"  Triples fully evaluated: {total_checked}")
    if candidates:
        print(f"  *** {len(candidates)} CANDIDATE(S) FOUND ***")
        for c in candidates:
            print(f"    {c['f0']['label']} / {c['f1']['label']} / {c['f2']['label']}")
            print(f"    ratio_μ={c['ratio_mu']:.4f}  ratio_τ={c['ratio_tau']:.4f}")
    else:
        print(f"  No candidates found within {tolerance:.0%} tolerance.")

    output = {
        "approach": "B_lmfdb_api",
        "network_available": True,
        "api_endpoint": LMFDB_API,
        "fallback_used": False,
        "search_parameters": {
            "prime": P,
            "weights": [2, 4, 6],
            "max_level": max_level,
            "target_mu":  MU_RATIO,
            "target_tau": TAU_RATIO,
            "tolerance":  tolerance,
        },
        "forms_found": {
            "weight_2": len(w2),
            "weight_4": len(w4),
            "weight_6": len(w6),
        },
        "skipped_no_eigenvalue": skipped_no_eig,
        "candidates": candidates,
        "verdict": verdict,
        "verdict_note": (
            "MATCH FOUND — see candidates list."
            if verdict == "MATCH_FOUND" else
            f"No triple found among LMFDB data within {tolerance:.0%} tolerance. "
            "Note: LMFDB hecke_eigenvalues field may not include a_137 for all "
            "newforms; records with missing eigenvalue data were skipped."
        ),
    }

    print(f"\n{'='*60}")
    print(f"VERDICT: {verdict}")
    print(f"{'='*60}\n")

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "hecke_search_results_api.json"),
        help="Output JSON file",
    )
    parser.add_argument(
        "--max-level",
        type=int,
        default=500,
        help="Maximum level N (default: 500)",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=TOLERANCE,
        help=f"Relative tolerance (default: {TOLERANCE})",
    )
    args = parser.parse_args()

    output = run_api_search(max_level=args.max_level, tolerance=args.tolerance)

    with open(args.output, "w") as fh:
        json.dump(output, fh, indent=2)
    print(f"Results written to: {args.output}")


if __name__ == "__main__":
    main()

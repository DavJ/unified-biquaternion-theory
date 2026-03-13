#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
search_k8_forms.py — Search for weight-8 newforms at levels N=1..50 and
test whether their Hecke eigenvalues at p=137 and p=139 give a
"fourth-generation" lepton mass consistent with UBT predictions.

PURPOSE
-------
The UBT weight-generation correspondence (step7_theoretical_motivation.tex)
predicts k = 2n for generation n.  For three generations: k = 2, 4, 6.
If this pattern continues: k=8 for a hypothetical fourth generation.

This script searches k=8 newforms and computes Hecke eigenvalue ratios:
  m_4 / m_e = a_{p*}(f_4) / a_{p*}(f_1)

If m_4 >> m_tau (e.g., > 100 TeV), the fourth generation is too heavy
to observe, explaining why only three generations exist.

APPROACH
--------
Direct computation of Hecke eigenvalues for k=8 newforms requires
SageMath or LMFDB access.  This script:
  1. Lists known properties of k=8 spaces (dimension formula).
  2. Provides a stub for SageMath computation (to be run locally).
  3. Estimates expected a_{137} values using the Ramanujan bound.

RAMANUJAN BOUND
---------------
For a weight-k newform: |a_p| <= 2 * p^{(k-1)/2}
For k=8, p=137: |a_137| <= 2 * 137^{3.5} = 2 * 137^3 * sqrt(137)
  = 2 * 2571353 * 11.705 = ~60.2 million.

The required ratio for a 100 TeV fourth generation:
  m_4 / m_e = 100e6 MeV / 0.511 MeV ≈ 1.96e8.
  a_{137}(f_4) / a_{137}(f_1) ≈ 1.96e8.
  a_{137}(f_4) ≈ 1.96e8 * (-9) ≈ -1.76e9.

But the Ramanujan bound gives |a_{137}(f_4)| <= 6e7 << 1.76e9.
Therefore: IF the Hecke conjecture pattern holds for k=8, the fourth
generation mass is BOUNDED by the Ramanujan bound and cannot be > ~few TeV
(not > 100 TeV as required for invisibility at the LHC).

This is a partial dead end: the Ramanujan bound alone does NOT explain
why the fourth generation is unobservable.

USAGE
-----
    python research_tracks/three_generations/search_k8_forms.py

    For full SageMath search (requires local SageMath installation):
        sage: from sage.modular.modform.constructor import CuspForms
        sage: M = CuspForms(Gamma0(N), 8)
        sage: M.newforms('a')  # for N = 1..50

REFERENCES
----------
  - step7_theoretical_motivation.tex
  - step6_hecke_matches.tex
  - TASK_NEXT_HECKE.md
"""

import math
import sys


def dimension_formula_k8(N):
    """
    Dimension of S_8(Gamma0(N)) using the trace formula.
    For k >= 2 and N squarefree:
      dim = (k-1)/12 * N * prod(1 + 1/p) - corrections
    Rough estimate for prime N:
      dim ≈ (k-1)/12 * (N+1) = 7/12 * (N+1)
    """
    # This is a rough lower bound; actual computation needs full trace formula
    return max(0, int((8 - 1) / 12 * (N + 1) - 2))


def ramanujan_bound(p, k):
    """
    Ramanujan-Petersson bound: |a_p(f)| <= 2 * p^{(k-1)/2}
    for a weight-k newform f.
    """
    return 2 * (p ** ((k - 1) / 2))


def main():
    PI = math.pi
    p_star = 137
    p_star2 = 139

    # From Step 6: a_{137}(f_1) = -9 for the electron-generation k=2 form
    a_k2_p137 = -9
    a_k2_p139 = 9

    # Known lepton mass ratios
    r_mu_e = 206.768
    r_tau_e = 3477.23

    print("=" * 72)
    print("search_k8_forms.py — Weight-8 Newform Search for 4th Generation")
    print("=" * 72)
    print()

    print("─" * 72)
    print("DIMENSION ESTIMATES: dim S_8(Gamma_0(N)) for N = 1..20")
    print("─" * 72)
    print(f"  {'N':>4}  {'dim (rough)':>12}  {'Notes'}")
    print("  " + "-" * 40)
    for N in range(1, 21):
        d = dimension_formula_k8(N)
        notes = ""
        if N == 1:
            notes = "Only Delta (k=12 is first non-trivial)"
        if d > 0:
            print(f"  {N:>4}  {d:>12}  {notes}")
        else:
            print(f"  {N:>4}  {'(empty)':>12}  {notes}")

    print()
    print("  Note: Exact dimensions require SageMath; these are rough estimates.")
    print()

    print("─" * 72)
    print("RAMANUJAN BOUNDS for k=8 at p=137 and p=139")
    print("─" * 72)

    for k in [2, 4, 6, 8]:
        bound_137 = ramanujan_bound(p_star, k)
        bound_139 = ramanujan_bound(p_star2, k)
        print(f"  k={k}: |a_137| <= {bound_137:.2e}, |a_139| <= {bound_139:.2e}")

    print()

    print("─" * 72)
    print("FOURTH-GENERATION MASS ESTIMATE")
    print("─" * 72)
    print()

    # If k=2n pattern holds and a_137(f_4) saturates the Ramanujan bound:
    max_a137_k8 = ramanujan_bound(p_star, 8)
    max_ratio_k8 = max_a137_k8 / abs(a_k2_p137)
    max_mass_4th = max_ratio_k8 * 0.511  # in MeV

    print(f"  a_137(f_1) = {a_k2_p137}  (k=2, electron generation)")
    print(f"  Ramanujan bound |a_137(f_4)| <= {max_a137_k8:.3e}  (k=8)")
    print(f"  Maximum ratio |a_137(f_4) / a_137(f_1)| <= {max_ratio_k8:.3e}")
    print(f"  Maximum 4th-gen mass <= {max_mass_4th:.3e} MeV = {max_mass_4th/1e6:.3f} TeV")
    print()

    lhc_limit_mev = 1e6  # ~1 TeV in MeV, rough collider exclusion for 4th gen leptons
    print(f"  LHC exclusion for heavy leptons: m_4 > ~1 TeV = {lhc_limit_mev:.0e} MeV")
    print()

    if max_mass_4th > lhc_limit_mev:
        print("  STATUS: CONSISTENT — Ramanujan bound allows m_4 > LHC limit.")
        print("          Fourth generation CAN be heavy enough to be unobserved.")
    else:
        print("  STATUS: TENSION — Ramanujan bound gives m_4 < LHC limit.")
        print("          The k=2n pattern with Ramanujan bound does NOT explain")
        print("          why the 4th generation is unobservable.")
        print()
        print("  RESOLUTION CANDIDATES:")
        print("    (a) The actual a_137(f_4) is NOT close to the Ramanujan bound.")
        print("    (b) The k=2n pattern breaks at k=8 (only 3 generations).")
        print("    (c) The fourth generation is forbidden by a different mechanism.")

    print()
    print("─" * 72)
    print("SAGAMATH STUB (run locally)")
    print("─" * 72)
    print("""
  # In SageMath:
  from sage.modular.modform.constructor import CuspForms
  from sage.all import Gamma0

  results = []
  for N in range(1, 51):
      try:
          M = CuspForms(Gamma0(N), 8)
          nf = M.newforms('a')
          for f in nf:
              # Compute a_137 = f.q_eigenform(138)[137]
              q = f.q_expansion(200)
              a137 = q[137]
              a139 = q[139]
              results.append({'N': N, 'k': 8, 'a137': a137, 'a139': a139})
              print(f'N={N}: a_137={a137}, a_139={a139}')
      except Exception as e:
          pass

  # Check ratios
  a_k2_p137 = -9
  for r in results:
      ratio = r['a137'] / a_k2_p137
      print(f"N={r['N']}: ratio = {ratio:.1f}  (vs m_tau/m_e = 3477)")
""")

    print()
    print("─" * 72)
    print("SUMMARY")
    print("─" * 72)
    print()
    print("  The Ramanujan bound for k=8, p=137 gives |a_137| <= 6.02e7.")
    print(f"  Maximum 4th-gen mass from Ramanujan: {max_mass_4th/1e6:.1f} TeV")
    print()
    print("  Gap: Need SageMath to find actual a_137(f_{k=8})")
    print("  for N=1..50 and compare to collider bounds.")
    print()
    print("  See: search_k8_forms.py (this file) for SageMath stub.")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())

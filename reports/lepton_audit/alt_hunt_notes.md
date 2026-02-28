# Alternative Formula Hunt — Notes

**Date**: 2026-02-28  
**Goal**: Find any formula or derivation in the repository that could legitimately
produce m_μ/m_e ≈ 207.3 and m_τ/m_μ ≈ 16.9 with at most one calibration parameter.

---

## Search Coverage

Keywords searched across entire repo (`.tex`, `.py`, `.md`):
- Numeric values: `207.3`, `206.7`, `16.9`, `16.817`, `3477`
- Formulas: `E_{n,m}`, `n+delta`, `tau_*`, `y_*`, `modulus`, `rectangular torus`
- Mappings: `M(E)`, `mass mapping`, `nonlinear`, `power`, `exp`, `log`
- Topology: `degeneracy`, `multiplicity`, `3-torus`, `T^3`, `T³`, `Hopf`, `winding`
- Operators: `Dirac`, `Laplacian`, `squared eigenval`

Files with the numbers 207, 3477, or 16.9:
- `consolidation_project/appendix_W2_lepton_spectrum.tex` (now patched)
- `consolidation_project/masses/sum_rules_and_ratios.tex` (experimental reference only)
- `consolidation_project/old/appendix_N_mass_predictions_consolidated.tex`
- `original_release_of_ubt/solution_P5_dark_matter/ThetaM_MassHierarchy.tex`

---

## Candidate 1: Integer Mode Law

**Source**: `consolidation_project/old/appendix_N_mass_predictions_consolidated.tex`

**Claim**: "The leading (no-parameter) predictions are m_μ^(0) = 207 m_e and m_τ^(0) = 3477 m_e."

**Formula**:
```
m_lepton(n) = n × m_e
  n_e   = 1
  n_mu  = 207
  n_tau = 3477
```

**Parameters**:
- `m_e` — one calibration (overall scale)
- `n_mu = 207`, `n_tau = 3477` — are these derived or fitted?

**Analysis**:
- Experimental: `m_μ/m_e = 206.768283`, `m_τ/m_e = 3477.228`
- The integers 207 and 3477 are the nearest integers to the experimental ratios.
- **No formula in the file derives 207 or 3477 from first principles.**
  The file states "integer-mode leading values" but provides no calculation —
  it appears to round the experimental ratios to the nearest integer.
- This is a 0.11% fit to m_μ and a 0.0066% fit to m_τ — by construction.
- **Verdict: NOT a prediction under the 1-calibration rule. The "integers" 207 and 3477
  are themselves second and third calibration parameters, fitted to experiment.**

---

## Candidate 2: Hopf Charge Power Law

**Source**: `original_release_of_ubt/solution_P5_dark_matter/ThetaM_MassHierarchy.tex`

**Formula**:
```
S(n) = a × n^p     (mass of generation n)
  n=1 → electron, n=2 → muon, n=3 → tau
```

**Analysis** (p = 3/2 as stated in file):
```
m_mu/m_e = 2^(3/2) = 2.828   (exp: 206.77)   ← factor 73 off
m_tau/m_e = 3^(3/2) = 5.196  (exp: 3477.2)   ← factor 669 off
```

The file itself acknowledges: "a_μ ≠ a_τ, suggesting a single power law may not fit
all three values."  Indeed:
```
a_mu  = m_mu / 2^(3/2) = 37.36    (uses exp m_mu)
a_tau = m_tau / 3^(3/2) = 341.96  (uses exp m_tau)
a_e   = m_e / 1^(3/2)  = 0.511    (uses exp m_e)
```
a_mu/a_e ≈ 73 — not equal at all. No single `a` fits all three generations.

For any power p:
```
p=1:   m_mu/m_e = 2 → not 207
p=2:   m_mu/m_e = 4 → not 207  
p=7.9: m_mu/m_e = 2^7.9 ≈ 238 → closer but m_tau/m_e = 3^7.9 ≈ 2615 ≠ 3477
```
No single exponent p can fit both ratios simultaneously.

**Verdict: FAILS under the 1-calibration rule. Needs 2 free parameters (a and p, or
equivalently n_mu and n_tau separately), which reduces to Candidate 1.**

---

## Candidate 3: Rectangular Torus with Modulus y_*

**Source**: `consolidation_project/appendix_V2_emergent_alpha.tex` (references τ = iy_*)

**Formula**:
```
E_{n,m} = (1/R) √[ (n+δ)² + (m+δ')² y_*² ]   (rectangular torus)
```

**Analysis**:
```
E_{0,2}/E_{0,1} = √[ (0.25 + 4 y_*²) / (0.25 + y_*²) ]
```
- As y_* → ∞: ratio → √(4/1) = 2.000 (upper bound)
- At y_* = 100: ratio = 1.999981
- **Maximum possible ratio is 2.000 — cannot reach 207.**

For the τ/μ ratio with mode (1,0) vs (0,2):
```
E_{1,0}/E_{0,2} = √[ 2.25 / (0.25 + 4 y_*²) ]
```
- As y_* → ∞: ratio → 0 (goes to zero, not 16.9)

**Verdict: FAILS for any real y_*. The rectangular modulus formula is bounded above at
ratio = 2 for the μ/e candidate modes.**

---

## Candidate 4: Complex Modulus (General Torus)

**Formula**:
```
E_{n,m} = (1/R) | (n+δ) + (m+δ') τ_* |   with τ_* = x + iy_*
```

For τ_* = iy_* (purely imaginary, which is what Appendix V gives):
```
|(n+δ) + (m+δ') iy_*|² = (n+δ)² + (m+δ')² y_*²
```
This reduces to Candidate 3. Same upper bound of 2. **FAILS.**

For complex τ_* = x + iy_*:
The ratio E_{0,2}/E_{0,1} = |(0.5) + 2τ_*| / |(0.5) + τ_*|.
To reach 207, need |(0.5 + 2τ_*)| / |(0.5 + τ_*)| ≈ 207,
i.e. |0.5 + 2τ_*| ≈ 207 |0.5 + τ_*|.
This requires τ_* ≈ −0.5 + very small ε (near a zero of the denominator),
making the formula highly tuned and physically unmotivated.
**No physical argument in the repo selects such a τ_*.**

**Verdict: FAILS unless τ_* is fine-tuned to be near −½, which would require a
second calibration parameter and has no theoretical justification.**

---

## Candidate 5: Squared Eigenvalues / Laplacian vs Dirac

**Source**: `ubt/spectral/laplacian_torus.py`

**Idea**: Maybe mass ~ E² (squared Dirac eigenvalue = Laplacian eigenvalue)?

```
m_mu/m_e = (E_{0,2}/E_{0,1})² = 1.844² = 3.400   (not 207)
m_mu/m_e = (E_{0,2}/E_{0,1})^k = 1.844^k = 207 → k = log(207)/log(1.844) ≈ 8.97
```

With k ≈ 8.97: m_tau/m_mu = (E_{1,0}/E_{0,2})^8.97 = 0.728^8.97 ≈ 0.054 (wrong direction).

**Verdict: FAILS — no integer power k gives both ratios in the right direction.**

---

## Candidate 6: Degeneracy-Weighted Mode Index

**Idea**: On T², modes (n,m) with |n|²+|m|² = N have degeneracy d(N) = #{(n,m):...}.
Could cumulative degeneracy index reproduce 207?

Cumulative mode count up to level N (including Hosotani shift δ=½):
- Level (0,1): index 1 → electron
- Level (0,2): cumulative index... 

```python
# Modes with E_{n,m}·R ≤ E_{0,2}·R = 2.062:
# (0,1): √1.25 = 1.118 ✓
# (0,-1): √1.25 ✓ (if δ'=0; m shifts negative too)
# (1,0): √2.25=1.5 ✓; (-1,0): √2.25 ✓
# (0,2): √4.25=2.062 ✓; (0,-2) etc.
# Total: small number, not 207
```

**Verdict: FAILS. Degeneracy counting on T² gives small integers (~10–20), not 207.**

---

## Summary

| Candidate | Formula | Max μ/e ratio | Verdict |
|-----------|---------|---------------|---------|
| 1: Integer mode law | m = n·m_e | Arbitrary (n is free) | NOT a prediction (n_mu = 207 is 2nd calibration) |
| 2: Hopf power law | m = a·n^p | 2.83 (p=1.5) to arbitrary | FAILS or uses extra fit |
| 3: Rectangular torus modulus | E = √[(n+δ)²+(m·y_*)²]/R | max 2.000 | FAILS |
| 4: Complex modulus τ_* | E = \|(n+δ)+(m+δ')τ_*\|/R | requires fine-tuning | FAILS |
| 5: Squared eigenvalues | m ~ E^k | requires k≈9 | FAILS (wrong τ direction) |
| 6: Degeneracy counting | cumulative index | ~10–20 | FAILS |

**Conclusion**: No formula found in the repository can produce m_μ/m_e ≈ 207 and
m_τ/m_μ ≈ 16.9 simultaneously with at most one calibration parameter (the overall
mass scale R = 1/m_e).

The numbers 207.3 and 16.9 in Appendix W.5 (and its predecessors) are
experimental reference values presented without a closed derivation.

---

## What Would Be Needed

A genuine derivation must supply a formula F(mode indices, τ_*) such that:
1. F is derived from first principles (not fitted to 207 or 3477).
2. F(mode for μ) / F(mode for e) ≈ 207 using only one calibration (R = 1/m_e).
3. F(mode for τ) / F(mode for μ) ≈ 16.8 from the same formula.
4. The mode assignments follow from a physical principle (not post-hoc).

No such formula exists in this repository as of 2026-02-28.

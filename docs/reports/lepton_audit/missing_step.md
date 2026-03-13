# Lepton Ratios — Missing Step Analysis

**Question**: What is the minimal missing ingredient that would bridge the gap between
the formula `E_{n,m} = (1/R)√[(n+δ)²+(m+δ')²]` and the claimed ratios 207.3 / 16.9?

---

## Observed Gaps

| Ratio   | Formula | Claimed | Experimental | Gap factor |
|---------|---------|---------|--------------|------------|
| μ/e     | 1.844   | 207.3   | 206.768      | ≈ 112.4    |
| τ/μ (from E₁₀)| 0.728 | 16.9 | 16.817   | ≈ 23.2 (and wrong direction) |

---

## Hypotheses Tested

### Hypothesis 1: Missing torus modulus y_* (rectangular formula)

If the correct formula on a torus with modulus `τ = iy_*` is:

```
E_{n,m} = (1/R) √[ (n+δ)² + (m+δ')² y_*² ]
```

then for n=0:

```
E_{0,2}/E_{0,1} = √[ (0.5² + 4 y_*²) / (0.5² + y_*²) ]
```

Maximum value as `y_* → ∞`: approaches 2.  
**Conclusion**: This formula cannot give 207.3 for any real `y_*`. ✗

Verification:
```python
import math
for y in [1, 5, 10, 100, 1000]:
    r = math.sqrt((0.25 + 4*y**2)/(0.25 + y**2))
    print(f"y_* = {y:6}: ratio = {r:.6f}")
# y_* =      1: ratio = 1.844390
# y_* =      5: ratio = 1.990099
# y_* =     10: ratio = 1.997506
# y_* =    100: ratio = 1.999975
# y_* =   1000: ratio = 1.999999
```

### Hypothesis 2: Missing torus modulus (alternate orientation)

```
E_{n,m} = (1/R) √[ (n+δ)² y_*² + (m+δ')² ]
```

For n=0: independent of y_*; ratio still approaches 2. ✗  
For n=1: `E_{1,0}/E_{0,2}` can grow with y_*, but then `E_{0,2}/E_{0,1}` → 1. ✗

No choice of y_* simultaneously gives 207.3 for μ/e **and** 16.9 for τ/μ.

### Hypothesis 3: Nonlinear mass mapping  M(E) = f(E)

Could an exponential or power-law mapping `m = A · Eᵅ` help?

- The ratio `m_μ/m_e = (E₀₂/E₀₁)ᵅ = 1.844ᵅ` must equal 207.3.  
  → `α = log(207.3)/log(1.844) ≈ 8.97`
- Then `m_τ/m_μ = (E₁₀/E₀₂)ᵅ = 0.728^8.97 ≈ 0.054` — goes the **wrong way**.

No single power-law exponent gives the correct direction for both ratios. ✗

### Hypothesis 4: Different mode assignment (3D torus / degeneracy)

On a 3-torus `T³`, extra quantum numbers could be added.  
However, Appendix W is explicit about a 2-torus `T²(τ)` and the modes `(n,m) ∈ ℤ²`.  
No evidence in the appendix for a 3D mode assignment.

### Hypothesis 5: Wrong mode labelling in the table

The table in W.T assigns:
- (0,2) → muon, with `E_{0,2}·R = √4.25 ≈ 2.062`
- (1,0) → tau,  with `E_{1,0}·R = √2.25 = 1.500`

But `E_{1,0} < E_{0,2}`, so the "tau" is **lighter** than the "muon".  
The hierarchy `m_τ > m_μ > m_e` cannot be reproduced with these mode assignments
and the formula as written.

---

## Most Likely Explanation

The table column "Ratio to E_{0,1}" in Appendix W.T contains the **experimental values**
(207.3 ≈ m_μ/m_e, 3477 ≈ m_τ/m_e) rather than values derived from the formula.  
The formula column correctly evaluates `√(...)`, but the ratio column is not computed
from those values — it is an unacknowledged insertion of measured data.

**The derivation is circular**: the claimed predictions are the observations themselves,
entered as if they were derived.

---

## Minimum Required to Complete the Derivation

To legitimately obtain `m_μ/m_e ≈ 207.3` from a toroidal eigenmode formula, at least ONE
of the following must be added (while keeping max 1 calibration):

| Missing ingredient | What it would need to do |
|--------------------|--------------------------|
| A genuinely new formula (not eq. W.2 as written) that includes `τ_*` and produces the right gap | Replace the approximate W.2 with a correct torus spectral formula |
| An explicit derivation of `y_*` from Appendix V and a corrected eigenmode formula that produces 207.3 and 16.9 | Currently absent from the repository |
| An explicit nonlinear mass mapping `M(E)` with a physical justification that simultaneously gives the right ratios for **both** μ/e and τ/μ | Currently absent from the repository |

**Current status**: None of these ingredients are present. The numbers 207.3 and 16.9
in Appendix W are asserted without a closed derivation.

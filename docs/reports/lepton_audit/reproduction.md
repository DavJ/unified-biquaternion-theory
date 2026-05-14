# Lepton Ratios — Reproduction Report

**Script**: `tools/reproduce_lepton_ratios.py`  
**Run from repo root**: `python tools/reproduce_lepton_ratios.py`

---

## Result: MISMATCH

The formula in Appendix W, section W.2, evaluated **exactly as written** does NOT reproduce
the claimed ratios.

---

## Step-by-step Breakdown

### Formula used (Appendix W, eq. W.2)

```
E_{n,m} = (1/R) * sqrt( (n + δ)² + (m + δ')² )
```

Parameters (from Appendix W):

| Parameter | Value | Source |
|-----------|-------|--------|
| δ         | 0.5   | W.3: Q=−1, θ_H=π → shift ½ along ψ-cycle |
| δ'        | 0.0   | W.T table: implicit (formula uses bare m for φ-cycle) |
| R         | 1/m_e | One calibration (W.3), sets overall scale |

### Eigenvalues computed (in units of 1/R)

| Mode (n,m) | Formula | Value |
|------------|---------|-------|
| (0,1)      | √(0.25 + 1.00) | **1.11803** |
| (0,2)      | √(0.25 + 4.00) | **2.06155** |
| (1,0)      | √(2.25 + 0.00) | **1.50000** |
| (1,1)      | √(2.25 + 1.00) | **1.80278** |

### Ratios and comparison

| Ratio         | Formula value | Claimed (W.5) | Experimental | Rel. error |
|---------------|---------------|---------------|--------------|------------|
| E₀₂/E₀₁ (μ/e)| **1.8439**    | 207.3         | 206.768      | **99.1 %** |
| E₁₀/E₀₂ (τ/μ)| **0.7276**    | 16.9          | 16.817       | **95.7 %** |
| E₁₁/E₀₂ (τ/μ alt)| **0.8745** | 16.9         | 16.817       | **94.8 %** |
| E₁₀/E₀₁      | **1.3416**    | 3477          | 3477.15      | **99.96 %**|

---

## Where It Breaks

### Break point 1: μ/e ratio

- Formula gives `√4.25 / √1.25 = √3.4 ≈ 1.844`
- Claimed: 207.3
- Missing factor: **≈ 112.4**
- This is a 99.1 % relative error — the formula is off by two orders of magnitude.

### Break point 2: τ/μ ratio — wrong direction

- Candidate (1,0): `E_{1,0} = √2.25 = 1.500 < E_{0,2} = 2.062`  
  → ratio < 1 → this mode is **lighter** than the muon, contradicting the τ > μ hierarchy.
- Candidate (1,1): `E_{1,1} = √3.25 = 1.803 < E_{0,2}` — same problem.
- No simple mode assignment from the formula gives a ratio > 1 that would match 16.9.

---

## Conclusion

The numbers 207.3 and 16.9 in Appendix W, table W.T, do **not** follow from the eigenvalue
formula stated in the same appendix.  The table entry for the "Ratio to E_{0,1}" column
appears to copy the **experimental** values rather than computing them from the formula.

The derivation as written is **incomplete** (missing step) or **internally inconsistent**.
See `missing_step.md` for the minimal missing ingredient analysis.

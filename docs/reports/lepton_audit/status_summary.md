# Lepton Sector — Status Summary

**Date**: 2026-02-28  
**Script**: `tools/reproduce_lepton_ratios.py`  
**Appendix**: `consolidation_project/appendix_W2_lepton_spectrum.tex`

---

## Current Status: OPEN PROBLEM

The lepton mass ratios m_μ/m_e ≈ 206.77 and m_τ/m_μ ≈ 16.82 are **not derived** from any
formula in this repository under the one-calibration rule.

---

## Canonical Formula (Appendix W, eq. W.2)

```
E_{n,m} = (1/R) √[ (n+δ)² + (m+δ')² ]    δ=½, δ'=0
```

| Mode | E·R      | Ratio to E₀₁ | Experimental | Match? |
|------|----------|--------------|--------------|--------|
| (0,1)| 1.11803  | 1.000        | 1.000        | ✓ (by calibration) |
| (0,2)| 2.06155  | **1.844**    | 206.77       | ❌ 99% error |
| (1,0)| 1.50000  | 1.342        | < E_(0,2)    | ❌ wrong direction |

**One calibration**: R = 1/m_e (sets overall scale).  
**Result**: MISMATCH — formula gives 1.844, experiment is 206.77 (factor ~112 off).

---

## Candidate Variants Tried

### Candidate 1: Integer mode law (`--variant candidate_integer`)

```
m_lepton = n × m_e    (n_mu=207, n_tau=3477)
```

**Source**: `consolidation_project/old/appendix_N_mass_predictions_consolidated.tex`  
**Calibrations used**: 3 (m_e, n_mu, n_tau)  
**Result**: NOT_A_PREDICTION — n_mu=207 is just the experimental ratio rounded.  
The near-integer property is an observation, not a derivation.

---

### Candidate 2: Hopf charge power law (`--variant candidate_hopf`)

```
m(n) = a × n^(3/2)    (n=1,2,3 for e,μ,τ)
```

**Source**: `original_release_of_ubt/solution_P5_dark_matter/ThetaM_MassHierarchy.tex`  
**Calibrations used**: 1 (a = m_e) + p=3/2 fixed  
**Result**: MISMATCH — gives m_μ/m_e = 2^(3/2) ≈ 2.83 (not 207).  
No single p can simultaneously fit both ratios.

---

### Candidate 3: Rectangular torus modulus (analytical bound)

```
E_{n,m} = (1/R) √[ (n+δ)² + (m+δ')² y_*² ]
```

**Result**: FAILS — E_{0,2}/E_{0,1} is bounded above by 2.000 as y_*→∞.  
Cannot reach 207 for any real y_*.

---

### Candidates 4–6 (see `alt_hunt_notes.md`)

- Complex modulus τ_* → reduces to Candidate 3 (for iy_*) or requires fine-tuning.
- Squared eigenvalues (Laplacian) → ratio 1.844² = 3.40 (not 207); wrong direction for τ/μ.
- Degeneracy counting → small integers (~10–20), not 207.

---

## Downgraded Claims

The following statements in earlier versions of Appendix W have been corrected:

| Old statement | New status |
|---------------|------------|
| "E_{0,2}/E_{0,1} ≈ 207.3" (derived) | "experimental reference value; NOT derived from eq. W.2" |
| "E_{1,0}/E_{0,2} ≈ 16.9" (derived) | "experimental reference value; NOT derived from eq. W.2" |
| Mode (1,0) as τ candidate | Removed — E_{1,0} < E_{0,2} (lighter than μ mode) |
| "magic numbers follow from toroidal geometry" | Replaced with open-problem statement |

---

## What Would Be Needed

A genuine derivation of m_μ/m_e ≈ 207 from toroidal eigenmodes requires at least ONE of:

1. **Corrected eigenvalue formula** incorporating τ_* from Appendix V that produces
   a ratio ≈ 207 without additional free parameters. (Currently absent.)
2. **Nonlinear mass mapping M(E)** with a physical justification that maps
   E_{0,2}/E_{0,1} ≈ 1.844 → ratio ≈ 207 for μ AND E_{?}/E_{0,2} → ratio ≈ 16.8 for τ
   simultaneously from the same formula. (Currently absent.)
3. **Different mode assignment** with a physical argument that identifies the muon
   with a mode (n,m) such that the ratio is ~207 under eq. W.2. This would require
   very large m, e.g. (0, m) with √(0.25+m²)/√(1.25) ≈ 207 → m ≈ 231. No physical
   motivation for m=231 is present in the repository.

---

## Audit Artifacts

All evidence is preserved permanently:

| File | Content |
|------|---------|
| `reports/lepton_audit/inventory.md` | All files containing lepton ratio claims |
| `reports/lepton_audit/equations.md` | Extracted equations and parameter table |
| `reports/lepton_audit/parameter_table.csv` | All parameters with sources and roles |
| `reports/lepton_audit/reproduction.md` | Step-by-step where formula breaks |
| `reports/lepton_audit/missing_step.md` | Analysis of what structural change is needed |
| `reports/lepton_audit/alt_hunt_notes.md` | All candidate variants and why they fail |
| `reports/lepton_audit/canonical_derivation.md` | Locked formula values + cross-ref to appendix patch |
| `tools/reproduce_lepton_ratios.py` | Runnable script: `--variant canonical/candidate_integer/candidate_hopf/all` |
| `tests/test_reproduce_lepton_ratios.py` | Regression tests (25 tests) |
| `consolidation_project/appendix_W2_lepton_spectrum.tex` | Patched appendix (honest, with boxed audit notice) |

---

## Enforcement

`pytest tests/test_reproduce_lepton_ratios.py` guards against:
- Canonical formula values drifting from locked reference
- Mismatch being accidentally removed/hidden
- Any variant claiming to reproduce ratios without justification

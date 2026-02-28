# Lepton Mass Ratio Audit — Inventory

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

Forensic inventory of all claims about lepton mass ratios m_μ/m_e and m_τ/m_μ
in the UBT repository.

---

## Source Locations

| File | Lines | Claim | Status |
|------|-------|-------|--------|
| `consolidation_project/appendix_W2_lepton_spectrum.tex` | 41–44 | `E(0,2)/E(0,1) ≈ 207.3`, `E(1,0)/E(0,2) ≈ 16.9` | **INCORRECT** — see critical note below |
| `consolidation_project/appendix_W2_lepton_spectrum.tex` | 76 | Table row: `(0,2)` → ratio `≈ 207.3` | Same error |
| `consolidation_project/appendix_K2_fundamental_constants_consolidated.tex` | 39 | References "207 and 3477" as near-integers | **Sourced from W2** |
| `consolidation_project/appendix_V2_emergent_alpha.tex` | 95–97 | `m_μ/m_e ≈ 207.3 vs 206.77_exp` | **Sourced from W2** |
| `consolidation_project/masses/sum_rules_and_ratios.tex` | 39–50 | Experimental values only | OK (labeled as experimental) |

---

## Critical Finding: Formula Mismatch in Appendix W

The toroidal eigenvalue formula stated in Appendix W is:

```
E_{n,m} = (1/R) * sqrt((n + δ)² + (m + δ')²)
```

with δ = 1/2, δ' unspecified (assumed 0 from context).

**Actual computed ratios** (see `tools/reproduce_lepton_ratios.py`):

| Mode assignment | Formula ratio | Claimed ratio | Experimental |
|----------------|--------------|---------------|-------------|
| m_μ/m_e = E(0,2)/E(0,1) | **1.844** | 207.3 | 206.768 |
| m_τ/m_μ = E(1,0)/E(0,2) | **0.728** | 16.9 | 16.817 |

**The formula as written does NOT reproduce the claimed ratios.**

The ratios "207.3" and "16.9" in the text appear to be the **experimental values**, not
computed eigenvalue ratios. The formula produces dimensionless ratios of order 1, not 200+.

### Possible Explanations (All Require Verification)

1. **Missing overall scale factor**: A radius parameter R or additional scale factor
   could shift the ratios, but cannot change a ratio of eigenvalues for same R.
2. **Different formula**: The actual formula may involve R-dependent absolute energies
   compared to a fixed scale (e.g., Planck scale), not eigenvalue *ratios*.
3. **Different mode assignment**: Perhaps m_e is not E(0,1) but some other reference scale.
4. **Typographical error in appendix**: The claimed ratios 207.3 and 16.9 are simply
   copied from experimental data without a correct derivation.

### Current Status

- The claim "lepton mass ratios arise from toroidal eigenmodes" is a **conjecture**.
- The supporting numerical calculation in Appendix W is **not internally consistent**.
- The appendix must be labeled as a conjecture pending a corrected derivation.

---

## Single Canonical Formula Chain (T8)

The formula chain, as stated in Appendix W, is:

1. **Background**: Torus T²(τ) with modulus τ = τ_* from Appendix V, Wilson branch θ_H = π.
2. **Hosotani shift**: δ = 1/2 for Q = -1 charge along Wilson cycle.
3. **Dirac spectrum**: E_{n,m} = (1/R) sqrt((n+δ)² + (m+δ')²)
4. **Electron**: m_e = E(0,1) = (1/R) sqrt(0.25 + 1)
5. **Muon**: m_μ ~ E(0,2) = (1/R) sqrt(0.25 + 4)
6. **Tau**: m_τ ~ E(1,0) or E(1,1)
7. **Ratios**: m_μ/m_e = E(0,2)/E(0,1), m_τ/m_μ = E(1,0)/E(0,2)

**Critical gap**: Step 7 gives ratios ≈ 1.8, 0.7 — not 207, 16.9.

No calibration vs. prediction separation is possible until the formula is corrected.

---

## Required Actions

- [ ] Correct or retract the numerical claim in appendix_W2_lepton_spectrum.tex
- [ ] Label the toroidal eigenmode mechanism as a **conjecture pending derivation**
- [ ] Identify the actual formula needed to produce ratios ~207 and ~16.9
- [ ] Create corrected script in `tools/reproduce_lepton_ratios.py`

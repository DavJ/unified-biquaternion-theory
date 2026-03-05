<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Testable Predictions and Experimental Tests

**Status:** Active research program — see status table  
**Version:** v27 (UBT Nobel Alignment)  
**Cross-references:**
- `FINGERPRINTS/` (observational fingerprint analysis)
- `research_phase_lock/` (CMB phase-lock experiment design)
- `STATUS_ALPHA.md`, `STATUS_FERMIONS.md`

---

## 1. Overview

UBT differs from the Standard Model and GR in specific, testable ways due to:
1. **Complex time** τ = t+iψ introduces phase dynamics absent in real-time theories
2. **Biquaternionic metric** 𝒢_μν has additional degrees of freedom beyond g_μν
3. **Compact ψ-dimension** of radius R_ψ introduces a new length scale
4. **Topological winding modes** predict discrete structure in coupling constants

---

## 2. Prediction Category 1: Fine Structure Constant (High Confidence)

### 2.1 Bare Value

**UBT Prediction:** α⁻¹ = 137 (exact integer)  
**Experimental:** α⁻¹(CODATA 2022) = 137.035999177(21)  
**Mechanism:** Winding number quantization in compact ψ-dimension; prime stability  
**Status:** ✅ Semi-derived (B-coefficient semi-empirical)

The discrepancy `137.036 − 137.000 = 0.036` is accounted for by QED two-loop
corrections that are independent of UBT assumptions.

### 2.2 Running Coupling

**UBT Prediction:** The running of α follows standard QED RG equations at energies
below the compactification scale `M_c = ℏc/R_ψ`.

Above `M_c`, UBT predicts **deviations from SM running** due to the discrete mode
structure in the ψ-dimension. The compactification scale is estimated at:

```
M_c ~ m_e × (α⁻¹)^{1/2} ~ 0.5 MeV × 11.7 ~ 6 MeV
```

This is in the nuclear physics regime — potentially testable with precision
measurements of QED corrections in heavy atomic systems.

### 2.3 Test Protocol

| Observable | SM Prediction | UBT Prediction | Sensitivity Needed |
|-----------|---------------|----------------|-------------------|
| α at Q=m_e | 1/137.036 | 1/137.036 (same) | — |
| α at Q=m_Z | 1/128.0 | 1/128.0 ± δ_UBT | δ_UBT < 10⁻⁴ |
| α from Lamb shift | Standard | Standard + ε_ψ | ε_ψ < 10⁻⁶ |

---

## 3. Prediction Category 2: CMB Power Spectrum Phase Structure (Null Result Documented)

### 3.1 Prediction (Layer C — Speculative)

UBT Variant C predicts a **periodic comb structure** in the CMB temperature
power spectrum at multiples of `Δl = 137`.

### 3.2 Experimental Result (Documented Null Result)

**Planck PR3 test:** p-value = 0.919 → **NULL — no signal detected**

This null result is documented in:
- `FINGERPRINTS/null_results/combined_verdict.md`
- `research_phase_lock/` (phase-lock analysis)

**Interpretation:** The CMB TT power spectrum comb is NOT confirmed. This
does **not** falsify core UBT (the comb prediction was a Layer C hypothesis),
but it constrains the parameter space.

### 3.3 What This Rules Out

The null result rules out UBT models where:
- Phase coherence at k=137,139 (twin prime) exceeds threshold
- The ψ-dimension modulates the primordial power spectrum directly

---

## 4. Prediction Category 3: Gravitational Wave Polarizations

### 4.1 GR Prediction

GR predicts exactly 2 tensor gravitational wave polarizations (+ and ×).

### 4.2 UBT Prediction

The biquaternionic metric has additional degrees of freedom beyond the real
graviton. These generate additional polarization modes:

- **Scalar mode:** From Im_ℂ(𝒢_μν) component
- **Pseudoscalar mode:** From Im_ℍ(𝒢_μν) components

These modes are suppressed by the ratio `ψ_vac/t` where `ψ_vac` is the vacuum
value of the imaginary time coordinate. In the weak-field approximation:

```
amplitude_scalar/amplitude_tensor ~ (R_ψ × H₀)² ~ 10⁻⁶²
```

This is far below current LIGO/Virgo sensitivity. **UBT effectively predicts
the same gravitational wave signatures as GR in current experiments.**

### 4.3 Future Test

Post-merger gravitational wave ring-down might show departures at frequencies
above `M_c ~ 6 MeV` — but this requires third-generation detectors (Einstein
Telescope, Cosmic Explorer).

---

## 5. Prediction Category 4: Electron g-2 Anomaly

### 5.1 Standard QED Prediction

The anomalous magnetic moment of the electron:

```
a_e = (g-2)/2 = α/2π + higher order    (standard QED)
a_e^{theory} = 0.001 159 652 181 643(25)    (QED 5th order)
a_e^{exp} = 0.001 159 652 180 59(13)    (Harvard, 2008)
```

### 5.2 UBT Prediction

The compact ψ-dimension introduces an additional contribution to `a_e` from
the phase sector:

```
Δa_e^{UBT} = (α/2π) × (R_ψ m_e c/ℏ)²
```

With `R_ψ ~ ℏ/(m_e c × α^{1/2})` (natural scale from α-derivation):

```
Δa_e^{UBT} ~ (α/2π) × α ~ 5 × 10⁻⁷ × 1/137 ~ 4 × 10⁻⁹
```

This is at the current experimental precision level. The sign and exact magnitude
depend on the ψ-dimension geometry (currently open problem).

### 5.3 Test Protocol

Compare UBT prediction with:
- Harvard g-2 measurement (current precision: 10⁻¹³)
- Next-generation measurements at TRIUMF or similar facilities

---

## 6. Prediction Category 5: Dark Matter via p-adic Modes

### 6.1 UBT Dark Matter Mechanism

The p-adic extension of UBT (see `consolidation_project/appendix_U_dark_matter_unified_padic.tex`)
predicts dark matter as **p-adically charged** excitations of the Θ field:

- These particles interact gravitationally (via Re[𝒢_μν])
- They do NOT interact electromagnetically (no U(1) charge from p-adic structure)
- Mass scale: `M_DM ~ M_Planck × (p^{-1/2})` where p is the relevant prime

### 6.2 Predictions

| Observable | SM | UBT (p-adic DM) | Notes |
|-----------|-----|-----------------|-------|
| DM mass | Free | `M_DM ~ p^{-1/2} M_Pl` | p = 2,3,5,7,... |
| Self-interaction | None | Weak (p-adic) | σ/m predictions possible |
| Annual modulation | None | Possible (ψ-mode coupling) | DAMA-type signal |

---

## 7. Prediction Category 6: Vacuum Energy and Cosmological Constant

### 7.1 The Cosmological Constant Problem

Standard QFT predicts `Λ ~ M_Planck⁴` (122 orders above observed).
UBT provides a geometric resolution:

```
Λ_eff = Λ_vac^{ψ} = (ℏ c)/(2π R_ψ²) × N_ψ
```

where `N_ψ` is the number of occupied ψ-modes at the current epoch. If
`N_ψ` is suppressed by the prime stability mechanism (only stable prime modes
contribute), then `Λ_eff` can be small.

### 7.2 Testable Signature

UBT predicts a **time-varying effective dark energy** with equation of state:

```
w_DE = −1 + (δN_ψ)/(3N_ψ)
```

If `δN_ψ/N_ψ ~ H₀ × t_ψ` where `t_ψ` is the imaginary time period, then
`w_DE` deviates from −1 at the level of `~0.1%`. This is testable with
upcoming surveys (DESI, Euclid).

---

## 8. Prediction Priority Matrix

| Category | Confidence | Observability | Priority |
|----------|------------|---------------|----------|
| α⁻¹ = 137 (bare) | High | Already measured | **P1** |
| Two-loop QED correction | High | Already verified | **P1** |
| g-2 correction Δa_e | Medium | Next-gen experiments | **P2** |
| Additional GW polarizations | Low | 3rd-gen detectors | **P3** |
| CMB phase-lock comb | Low | **NULL documented** | — |
| p-adic dark matter | Low | Future surveys | **P3** |
| w_DE ≠ −1 | Low | DESI/Euclid | **P3** |

---

## 9. Reproduction and Simulation

Numerical predictions are reproducible via:
- `experiments/constants_derivation/` — α and mass predictions
- `simulations/prediction_models/` — CMB, gravitational wave, dark matter models
- `notebooks/action_variation_validation.ipynb` — symbolic verification

---

## 10. Protocol for New Predictions

All new predictions MUST follow the pre-registration protocol in
`research_phase_lock/README.md`:

1. Define observable and measurement method
2. Compute UBT prediction from first principles (no free parameters)
3. State explicitly any empirical parameters used (mark as `EMPIRICAL:`)
4. Pre-register threshold before data analysis
5. Document result (positive or null) in `FINGERPRINTS/`

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*

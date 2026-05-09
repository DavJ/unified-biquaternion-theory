<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Prediction Inventory v2 — UBT to Polariton Effective Model

**Track:** `research_tracks/polariton_supersolid/`  
**Status:** Draft (baseline + speculative split)  
**Important:** This document does **not** claim that UBT already predicts existing experiments.

---

## Separation Rule

- **Tier A (Established condensed-matter physics):** Predictions from GP/ddGP/CGL without UBT assumptions.
- **Tier B (SPECULATIVE UBT corrections):** Predictions contingent on deriving the reduction terms from `Theta(q, tau)`.

Only falsifiable statements are listed.

---

## Tier A — Established Condensed-Matter Predictions

### A1. Condensation threshold
- **Equation:** `P_th = Gamma_C * Gamma_R / R`
- **Observable:** PL intensity threshold vs pump power.
- **Falsifier:** No threshold onset despite calibrated nonzero `R` and finite cavity lifetime.

### A2. Effective-mass dispersion near k=0
- **Equation:** `E(k) = E_0 + hbar^2 k^2 / (2 m*)`
- **Observable:** Angle-resolved dispersion fit for `m*`.
- **Falsifier:** Persistent non-parabolic low-k branch in the nominal single-branch regime.

### A3. Nonlinear blueshift
- **Equation:** `Delta E ~ g * |psi|^2`
- **Observable:** Density-dependent resonance shift.
- **Falsifier:** No monotonic interaction shift in the mean-field density range.

### A4. Finite-k instability onset (when engineering supports it)
- **Equation form:** `Re[Lambda(k_c)] = 0` with `k_c != 0`
- **Observable:** Emergent side peaks at `±k_c` and real-space density modulation.
- **Falsifier:** No finite-k growth in the scanned instability window.

### A5. Phase locking under coherent drive
- **Equation form:** `dot(phi) = Delta_omega - K sin(phi)`
- **Observable:** Locking plateaus / Arnold tongues.
- **Falsifier:** Absence of locking region for nonzero coherent coupling.

### A6. Coherence stabilization condition
- **Criterion:** long-wave damping balance yields bounded phase fluctuations.
- **Observable:** Extended `g^(1)(r)` length when pump-loss balance is tuned.
- **Falsifier:** Coherence length remains unchanged across controlled gain/loss sweeps.

---

## Tier B — SPECULATIVE UBT-Correction Predictions

These require a derived low-energy mapping `Theta(q,tau) -> psi(r,t)` and validated coefficients.

### B1. Effective-mass correction channel
- **Hypothesis:** `m*_eff = m* + delta m_UBT` from projected biquaternionic sector.
- **Falsifiable test:** Joint fit to dispersion and density dynamics prefers `delta m_UBT != 0` over all baseline nuisance models.
- **Current gap:** `delta m_UBT` not derived from a closed UBT reduction.

### B2. Nonlinearity correction channel
- **Hypothesis:** `g_eff = g + delta g_UBT` with density-dependent deviation pattern.
- **Falsifiable test:** Residuals from baseline `Delta E vs |psi|^2` are explained by one stable `delta g_UBT` law across datasets.
- **Current gap:** no canonical expression for `delta g_UBT`.

### B3. Finite-k selector correction
- **Hypothesis:** higher-gradient term (`lambda_k nabla^4`) shifts `k_c` beyond ddGP expectation.
- **Falsifiable test:** measured `k_c(P,n)` trend rejects baseline model and matches one UBT-parameter family.
- **Current gap:** sign/magnitude of `lambda_k` uncomputed.

### B4. Phase-lock bandwidth correction
- **Hypothesis:** complex-time memory term (`eta_tau d_t^2`) renormalizes locking width.
- **Falsifiable test:** locking boundary shift persists after accounting for cavity detuning and thermal drifts.
- **Current gap:** mapping from UBT complex-time structure to `eta_tau` not derived.

### B5. Coherence-length correction
- **Hypothesis:** UBT correction modifies effective phase diffusion, changing asymptotic `g^(1)(r)` decay scale.
- **Falsifiable test:** one correction law explains coherence-length residuals vs baseline across independent pump powers.
- **Current gap:** no error-controlled effective theory linking UBT parameters to phase diffusion.

---

## Mathematical Gaps (Explicit)

1. Controlled elimination of fast UBT modes with quantified truncation error is missing.
2. Open-system (gain/loss/noise) derivation from UBT action is missing.
3. Parameter-identifiability analysis separating UBT corrections from standard cavity uncertainties is missing.

Until these are closed, Tier B remains speculative.

---

## Out-of-Scope Statements (Excluded)

- No TOE-level claim.
- No claim that existing polariton data confirms UBT.
- No consciousness interpretation.

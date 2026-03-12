<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Theta Functions, Modular Forms, and the Alpha Candidate Program
## UBT Research Track — Complex Time / Modular Extension

**Date:** 2026-03-10  
**Status:** Research track — NOT canonical theory  
**Author:** Ing. David Jaroš  
**Related files:**
- `research/theta_modular_geometry.tex` — torus formalization
- `AUDITS/complex_time_modular_audit.md` — full modular audit
- `consolidation_project/appendix_ALPHA_torus_theta.tex` — eta/torus calculation
- `STATUS_ALPHA.md` — B_base open problem

---

## Epistemic Notice

> ⚠️ **All mechanisms in this document are research proposals, not proofs.**
>
> No mechanism in this document currently gives a closed first-principles derivation
> of α⁻¹ = 137.036. The B_base derivation remains the central open hard problem.
> The label [SE] (semi-empirical) or [MC] (motivated conjecture) is applied to
> all speculative connections. No new physical claims are asserted beyond what is
> already documented in `STATUS_ALPHA.md`.

---

## 1. Theta Function Definition

The Jacobi theta function relevant to UBT is:
```
ϑ₃(z|τ) = Σ_{n∈ℤ} q^{n²} exp(2πi n z),    q = exp(iπτ)
```

At z = 0 (theta constant):
```
ϑ₃(0|τ) = Σ_{n∈ℤ} q^{n²} = 1 + 2q + 2q⁴ + 2q⁹ + ...
```

This is a modular form of **weight k = 1/2** for Γ₀(4).  
**Source:** Classical; `report/hecke_modular_structure.md` §2.2  
**Status:** [L0] — algebraic identity

---

## 2. Theta Heat Equation and Diffusion Connection

The Jacobi theta function satisfies the partial differential equation:
```
∂/∂τ [ϑ₃(z|τ)] = (1/4πi) ∂²/∂z² [ϑ₃(z|τ)]
```

This is a heat/diffusion equation in the modular time τ with diffusion coefficient
`D = 1/(4πi)`.

### 2.1 Relation to Fokker-Planck

Under the substitution τ = it (Wick rotation in modular time), the equation becomes:
```
∂/∂t [ϑ₃(z|it)] = -(1/4π) ∂²/∂z² [ϑ₃(z|it)]
```

This is a real diffusion (Fokker-Planck) equation. The theta function provides
the heat kernel on the torus T¹.

**Physical interpretation in UBT:** The diffusion in modular time corresponds
to the spreading of the Θ-field wavefunction in the imaginary direction ψ.
The spectral analysis of this diffusion yields KK mode masses m_n = n/R_ψ,
consistent with `report/theta_spectrum_analysis.md`.

**Status:** [L1] — follows from classical theta function theory; UBT identification
is [L1] given the theta constant = Θ zero mode identification.

---

## 3. Alpha Candidate Mechanisms

Six candidate mechanisms are assessed below. Each is rated by rigor level.

### 3.1 Im(τ) Fixed Point: τ* = i/α

**Idea:** If a dynamical or variational principle fixes Im(τ) = α (the fine-structure
constant), then τ* = i·α is the preferred modular parameter.

**Mathematical object:** τ* = i/137 (the imaginary axis value corresponding to α⁻¹ = 137)

**Connection to V_eff program:**
The effective potential V_eff(n) = An² - Bn ln(n) has a minimum at n* = 137
among primes. Identifying n* = 1/Im(τ*) gives:
```
Im(τ*) = 1/n* = 1/137 ≈ α₀
```

**Status:** [SE] — Structurally consistent with the V_eff minimum, but requires
derivation of B_base to be complete. The V_eff minimum is proved [L1] given B_base;
the modular interpretation is motivated but not derived.

**File:** `consolidation_project/appendix_ALPHA_torus_theta.tex` §4

### 3.2 Extremum of log ϑ₃

**Idea:** The effective coupling is proportional to log ϑ₃(0|τ), and a dynamical
extremum fixes τ.

**Mathematical object:** d/d(Im τ) [log ϑ₃(0|τ)] = 0 along the imaginary axis τ = iy

**Analysis:**
```
d/dy [log ϑ₃(0|iy)] = π · Σ_{n≠0} n² · (-1)^{n-1} · q^{n²} / ϑ₃  ≠ 0 for y > 0
```

The derivative along the imaginary axis is monotone (log ϑ₃ decreases as y increases
for the q = e^{-πy} parameterisation). There is no interior extremum on τ ∈ iℝ₊.

**Conclusion:** This mechanism does **not** fix τ on the imaginary axis.
**Status:** [O] — mechanism not viable for imaginary-axis τ.

### 3.3 Extremum of log η (Dedekind eta)

**Idea:** The Dedekind eta function η(τ) = q^{1/24} ∏_{n≥1}(1-q^{2n}) controls
the functional determinant of the torus Laplacian:
```
det'(-Δ_{T²}) ∝ (Im τ) |η(τ)|⁴
```
(see `consolidation_project/appendix_ALPHA_torus_theta.tex` §3)

**Special value:** η(i) = Γ(1/4) / (2π^{3/4}) ≈ 0.7682 (known closed form)

**Analysis along τ = iy:**
The function y → |η(iy)|⁴ is monotone in y and has no extremum on iℝ₊.
The self-dual point τ = i (y = 1) is the *fixed point of S: τ → -1/τ*, not a
minimum of |η|. Setting τ = i is thus a symmetry argument (self-duality), not
an extremum argument.

**Coupling renormalization:**
```
1/α_ren(τ) = A₀ + c₂(τ),    c₂(τ) ∝ (Im τ) |η(τ)|⁴
```
At τ = i: c₂(i) = |η(i)|⁴ = [Γ(1/4)/(2π^{3/4})]⁴ ≈ 0.348

**Status:** [SE] — The tau = i self-dual point gives a definite (computable)
coupling, but the proportionality coefficient A₀ requires derivation of B_base.
This is the same obstruction as in §3.1.

**File:** `consolidation_project/appendix_ALPHA_torus_theta.tex` §4

### 3.4 Modular Invariant j(τ)

**Idea:** The j-invariant j(τ) = 1/q + 744 + 196884q + ... is the unique modular
invariant of weight 0. Special values include j(i) = 1728, j(e^{2πi/3}) = 0.

**Connection to α:** No connection established. j(τ) = 1728 at τ = i, and
1728 = 12³ = (N_eff)³ for N_eff = 12 (the UBT effective mode count). This
numerical coincidence is noted but not interpreted as a derivation.

**Status:** [O] — No algebraic mechanism connecting j(τ) to α identified.

### 3.5 Spectral Gap from q-Suppression

**Idea:** The spectral gap (first KK mass above zero) is λ₁ = 1/R_ψ². In units
where R_ψ is expressed relative to the Planck scale, the spectral gap could
provide a dimensionless ratio related to α.

**Analysis:**
```
λ₁/m_Pl² = (ℓ_Pl/R_ψ)² = (ℓ_Pl/R_ψ)²
```
For R_ψ ∼ √α · ℓ_Pl, one gets λ₁/m_Pl² ∼ α. This is dimensional analysis,
not a derivation.

**Status:** [SE] — Dimensional analysis consistent; dimensional constant R_ψ
is the free parameter. Without fixing R_ψ, no prediction results.

### 3.6 Attractor Points in Moduli Space

**Idea:** The UBT field equations drive τ toward an attractor value τ* under
renormalization group (RG) flow. The attractor is an argument for why a
particular τ is physically selected.

**Connection to V_eff:** The effective potential V_eff(n) studied in the
alpha program is interpreted as a potential on the discrete moduli space n ∈ ℕ.
The minimum n* = 137 is then an attractor of this discrete system.

**Mathematical statement:**
```
∂V_eff/∂n|_{n=n*} = 0,    n* = 137 (first prime minimum for specific B values)
```
This is **proved [L1]** given B_base (see `STATUS_ALPHA.md`).

The continuous analog would be an attractor in the moduli space ℋ with τ* = i/n*.

**Status:** [MC] — The discrete attractor (V_eff minimum at n=137) is proved [L1].
The modular interpretation as a continuous attractor τ* = i/137 is a motivated
conjecture [MC].

---

## 4. Summary Table

| # | Mechanism | Object | Mathematical status | Gives α? |
|---|-----------|--------|---------------------|---------|
| 1 | Im(τ) = 1/n* | τ* = i/137 | [SE] — consistent with V_eff, not independent | No (B_base needed) |
| 2 | Extremum of log ϑ₃ | d/dτ log ϑ₃ = 0 | [O] — no extremum on iℝ₊ | No |
| 3 | Extremum of log η / self-dual point | τ = i | [SE] — self-duality argument; A₀ unknown | No (A₀ needed) |
| 4 | j(τ) invariant | j(i) = 1728 = 12³ | [O] — numerical coincidence only | No |
| 5 | Spectral gap q-suppression | λ₁ ∝ α | [SE] — dimensional analysis | No (R_ψ needed) |
| 6 | Attractor in moduli space | n* = 137 | [MC] — V_eff minimum proved; modular interpretation conjecture | No (B_base needed) |

**Central conclusion:** All six mechanisms point to n* = 137 or τ* = i/137 as
the preferred modular parameter, but none closes the derivation independently of
B_base. The B_base problem (exponent 3/2 in N_eff^{3/2}) is the universal
blocking factor.

---

## 5. What Would Constitute a Closed Derivation

A complete first-principles derivation of α⁻¹ = 137 would require:

1. A derivation of B_base = N_eff^{3/2} = 41.57 from the UBT field equations
   (or an alternative closed formula for B)
2. A proof that the minimum of V_eff among primes is at n = 137 (proved [L1]
   given B_base — this step would be complete)
3. A demonstration that the quantum correction +0.036 arises from two-loop QED
   (already documented in `STATUS_ALPHA.md` as [L1])

**Current status of Step 1:** 22 approaches tested; none succeeds. The B_base
problem is classified as an "open hard problem" in `STATUS_ALPHA.md`.

---

## 6. Connection to Existing Repository Work

| Topic | File | Status |
|-------|------|--------|
| V_eff(n) minimum at n=137 | `STATUS_ALPHA.md` | [L1] given B_base |
| B_base = N_eff^{3/2} open problem | `STATUS_ALPHA.md` | [O] |
| Torus/eta alpha calculation | `consolidation_project/appendix_ALPHA_torus_theta.tex` | [SE] |
| Hecke eigenvalues at p=137 | `reports/hecke_lepton/sage_results_2026_03_07.md` | [NO] |
| Theta spectrum (KK) | `report/theta_spectrum_analysis.md` | [L1] |
| Hecke modular structure | `report/hecke_modular_structure.md` | [L1] algebra; [NO] physics |
| Mirror sector at p=139 | `reports/hecke_lepton/mirror_world_139.md` | [NO] |

---

*This document is part of the complex-time modular extension program.*  
*Status of this document: Research proposal. Not canonical theory.*  
*License: CC BY-NC-ND 4.0 — Ing. David Jaroš, 2026*

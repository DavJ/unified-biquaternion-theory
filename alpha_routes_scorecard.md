<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# alpha_routes_scorecard.md — Alpha Derivation Routes: Final Offensive Scorecard

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Alpha Final Offensive  
**Companion**: `ALPHA_FINAL_OFFENSIVE.md`, `best_candidate_derivation.tex`  
**Hard rule**: No parameter may be chosen to fit α.  
Every constant must come from an independent UBT sector.

---

## Classification Key

| Code | Meaning |
|------|---------|
| **VIABLE** | All steps proved or have a clear proof path; no circular inputs |
| **BLOCKED** | Structural gap with no known resolution; route cannot deliver α |
| **NUMEROLOGY** | Route produces a number close to 137.036 without structural justification |
| **INCOMPLETE** | Route is internally consistent but cannot deliver α as stated; addresses a sub-problem only |
| **CONDITIONAL** | Could deliver α if one or more identified gaps are resolved |

---

## Scorecard

### Track A1 — GaugeNormalization

**File**: `canonical/alpha/gauge_normalization_attempt.tex`  
**Question**: Does the canonical A-field normalization in Tr[(D_μΘ)†(D^μΘ)] fix e and hence α?

| Step | Formula | Classification | Status |
|------|---------|----------------|--------|
| Covariant derivative | D_μ = ∂_μ + ig_s G + igW + ig'B | CLEAN | ✅ Proved |
| Photon after SSB | A_μ = sinθ_W W³ + cosθ_W B | CLEAN (algebra) | ✅ Proved |
| Charge relation | e = g sinθ_W | CLEAN (algebra) | ✅ Proved |
| Fix g from ℂ⊗ℍ | g from canonical Tr norm | **GAP EW-1a** | ❌ Open |
| Fix θ_W from Aut(ℂ⊗ℍ) | tan(θ_W) = g'/g | **GAP EW-1b** | ❌ Open |
| α = e²/(4π) | Final combination | Conditional on both gaps | ❌ Blocked |

**Route classification**: **CONDITIONAL** (would be viable if Gap EW-1 resolved)

**Blocking gap**: EW-1 — the hypercharge coupling g' is not constrained relative
to g by the biquaternion algebra.  The U(1)_Y generator Y commutes with su(2)_L
by Schur's lemma and its normalisation is free.

**What would resolve it**: Proof that Aut(ℂ⊗ℍ) restricts the normalisation
of Y relative to the SU(2)_L generators, or an embedding into a simple GUT group
that fixes sin²θ_W(GUT) algebraically.

**Numerical check** (conditional): If EW-1 were resolved with θ_W = θ_W^SM:
- α = g²(m_Z) sin²θ_W(m_Z) / (4π) ≈ 1/128 at m_Z pole (correct, but uses m_Z)
- This is not a prediction — it is a consistency check only.

---

### Track A2 — ElectroweakProjection

**File**: `canonical/alpha/symmetry_breaking_alpha_attempt.tex`  
**Question**: Does the SU(2)_L × U(1)_Y → U(1)_EM SSB in UBT fix θ_W from
the biquaternion vacuum structure?

| Step | Formula | Classification | Status |
|------|---------|----------------|--------|
| SSB pattern | SU(2)×U(1) → U(1)_EM | Adopted from SM | ⚠️ Gap EW-2 |
| Unbroken generator | Q = T₃ + Y/2 | CLEAN (algebra) | ✅ Proved |
| VEV as doublet | Θ₀ ↦ doublet | **GAP EW-2** | ❌ Open |
| g = g' at EW scale | sin²θ_W = 1/2 | **EXCLUDED** | ✗ Contradicts experiment |
| tan(θ_W) from Aut(ℂ⊗ℍ) | g'/g from algebra | **GAP EW-1** | ❌ Open |
| GUT embedding (SU(5)) | sin²θ_W(GUT) = 3/8 | **GAP GUT-UBT** | ❓ Unknown |
| α via GUT + RGE | α(m_Z) from GUT scale | GUT-scale free | ❌ Incomplete |

**Route classification**: **CONDITIONAL** (blocked by Gaps EW-1 + EW-2 + GUT-UBT)

**Key near-miss excluded**: g = g' at the EW scale gives sin²θ_W = 1/2,
hence α = g²/(8π) ≈ 1/97.  This prediction is incorrect and is definitively
excluded by experiment.  The EW norm-matching condition does not work.

**Most promising sub-route**: GUT embedding — if ℂ⊗ℍ algebraically forces a
specific grand-unified group G_GUT, then sin²θ_W(GUT) is fixed by Lie theory
(e.g., 3/8 for SU(5)).  After RGE running, α(m_Z) follows.  
**Status of Gap GUT-UBT**: dim_ℝ(ℂ⊗ℍ) = 8 ≠ dim(SU(5)) = 24; no natural
embedding is known; octonion-related exceptional algebra route is unexplored.

---

### Track A3 — ModularTheta

**Question**: Do modular invariants or Hecke eigenvalues of the UBT complex-time
torus partition function Ẑ(τ) = ϑ₃³(τ) determine α?

| Expression / Route | Value | Equals α⁻¹ = 137.036? | Assessment |
|-------------------|-------|------------------------|------------|
| j(i) / 1000 | 1.728 | No | Unrelated |
| e^π (Gelfond constant) | 23.140 | No | Unrelated |
| 16π³ | 4961 | No | Unrelated |
| τ(137) Ramanujan τ-function | −182213199 | No | Large integer |
| Hecke T₁₃₇ eigenvalue of Δ | Large integer | No | No match |
| V_eff min n* = 137 (prime attractor) | 137 | Yes (bare integer) | Already proved [L1]; not new to this route |
| Modular weight of Ẑ(τ) | 3/2 | — | Structural fact; not α |
| Modular bootstrap → k_KM | Unknown | Unknown | **NOT YET ATTEMPTED** |

**Modular bootstrap assessment**:
The partition function Ẑ(τ) = ϑ₃³(τ) has modular weight 3/2 under SL(2,ℤ).
Crossing symmetry constraints on the 4-point function of the torus CFT may
force the Kac-Moody level k_KM = 1 as a consistency condition.  If so:
k_KM = 1 → B_base = N_eff^{3/2} proved → α⁻¹_bare = 137 is a clean result.
This route has NOT been attempted; it is the single open direction in A3.

**Route classification**: **INCOMPLETE**

- **Incomplete (not failed)**: The modular bootstrap is genuinely untested.
- **The integer 137 as a modular/torus feature**: already proved [L1] via the
  prime attractor; this is NOT numerology — it has structural derivation.
  However, it does not independently belong to A3 as a new result.
- **The full 137.036 from modular invariants alone**: no modular expression
  of weight 0 (modular-invariant) has been found that equals 137.036.
  All explicit modular invariants produce unrelated values.

---

### Track A4 — RGFlow

**Question**: Does UBT predict α at a UV scale (GUT, Planck, or T-duality scale),
from which the IR value α(0) ≈ 1/137.036 can be obtained by RGE running?

| Sub-requirement | Status | Classification |
|----------------|--------|----------------|
| α(μ_UV) predicted by UBT structure | Only α⁻¹_bare = 137 from prime attractor (bare, UV) | CONDITIONAL on G3-k |
| UV scale μ_UV identified algebraically | R_ψ = ℏ/(m_e c) uses m_e — circular | SE/CIRC |
| SM RGE as bridge from UV to IR | External inputs: m_e, m_Z, SM matter content | External (not UBT) |
| α_GUT free even with GUT group | g_GUT is a free parameter in GUT + RGE approach | BLOCKED |

**Detailed analysis**:

The RGE formula connecting UV bare value to IR physical value:
```
α⁻¹(0) = α⁻¹_bare + (1/3π) ln(Λ/m_e) + O(α)
```
requires both Λ and m_e as inputs.  The UBT prediction α⁻¹_bare = 137 (if k=1
is proved) would enter as α⁻¹_bare.  But Λ cannot be fixed without m_e.

The T-duality scale R_ψ = ℏ/(m_e c) would provide Λ ≈ 1/R_ψ ∝ m_e — directly
circular.  No algebraic fixation of R_ψ in physical units is known without
importing m_e as external input.

**Route classification**: **BLOCKED**

The RG flow route is a relay leg, not an independent starting point.  It requires
a UV prediction from A1 or A2, plus a UV scale fixed algebraically — neither of
which is currently available.  Its role, once A1 or A2 succeeds, is to verify
consistency between the UV prediction and the observed low-energy α.

**Not numerology**: The structure is correct physics.  The route is blocked by
missing algebraic inputs, not by an error in the RGE logic.

---

### Track A5 — CodingSecondary

**Script**: `research_tracks/alpha/layer2_coding_alpha_scan.py`  
**Question**: Do Hamming (8,4,4), Gray transport, or 1⊕3⊕3̄⊕1 decomposition
constraints fix the U(1) coupling magnitude (not just the charge spectrum)?

| Coding result | Status | Fixes α? |
|--------------|--------|----------|
| ℂ⊗ℍ ≅ M_2(ℂ) — 8 real dimensions | CLEAN [L0] | No (structural fact) |
| 1⊕3⊕3̄⊕1 under SU(2) — 8 = 1+3+3+1 | CLEAN [L0] | No (structural fact) |
| ℤ₂×ℤ₂×ℤ₂ involutions → SU(3) | CLEAN [L0] | No |
| Hamming (8,4,4): minimum distance d_min = 4 | Structural [O] | No |
| Gray code adjacency on phase transitions | Hypothesis [MC] | No |
| Hamming parity → charge quantization (integer multiples) | Plausible [MC] | Partially (spectrum only) |
| Coding fixes magnitude of e = √(4πα) | **FAILED** | No |

**Scan result** (from `layer2_coding_alpha_scan.py`):
All combinations of the form α = (C_code / N_gray^k)² / (4π) with Hamming and
Gray parameters produce zero combinations within 5% of α⁻¹ = 137 with any
UBT-internal motivation.

**Structural boundary**:
The 1⊕3⊕3̄⊕1 decomposition contains no j=1/2 doublet irrep.  This means the
SM Higgs doublet VEV structure cannot be directly implemented on the fundamental
biquaternion representation — confirming that Gap EW-2 is a genuine structural gap.

**Route classification**: **INCOMPLETE**

- The coding layer correctly and cleanly constrains **charge quantisation** (spectrum).
- It does NOT constrain **coupling magnitude** (α value).
- This is a boundary identification, not a failure of the coding layer per se.
- The Layer2 coding paper (independent of B_base, publication-ready ≈6 weeks)
  is the appropriate scope for this result.

---

## Master Scorecard Table

| Track | Route | Classification | Gaps | Can deliver α? |
|-------|-------|----------------|------|----------------|
| A1 | GaugeNormalization | **CONDITIONAL** | EW-1 | Yes, if EW-1 resolved |
| A2 | ElectroweakProjection | **CONDITIONAL** | EW-1, EW-2, GUT-UBT | Yes, if EW-1+EW-2+GUT-UBT resolved |
| A3 | ModularTheta | **INCOMPLETE** | Modular bootstrap not yet attempted | Possibly yes (for α⁻¹_bare = 137) |
| A4 | RGFlow | **BLOCKED** | A10 (R_ψ uses m_e), α_GUT free | No (relay only; requires A1 or A2 first) |
| A5 | CodingSecondary | **INCOMPLETE** | Coding ≠ magnitude | No (spectrum only) |

---

## What Is Already Achieved (Zero-Parameter, No α Input)

| Result | Classification | Source |
|--------|----------------|--------|
| N_eff = 12 from ℂ⊗ℍ | CLEAN [L0] | `canonical/n_eff/` |
| B₀ = 8π one-loop baseline | CLEAN [L1] | `canonical/n_eff/step2_vacuum_polarization.tex` |
| V_eff(n) = n² − B·n·ln n | CLEAN [L1] given B | `canonical/alpha/veff_corrected.tex` |
| 2n* = B(ln n* + 1) stationarity | CLEAN [L1] given B | `canonical/alpha/veff_corrected_statement.tex` |
| Prime stability of n* = 137 | CLEAN [L1] | `canonical/appendices/appendix_alpha_geometry.tex §4` |
| α⁻¹_bare = 137 (given k=1) | CONDITIONAL [L1] — k=1 open | Above chain |
| Dirac charge quantisation | CLEAN [L0] | `canonical/appendices/appendix_alpha_geometry.tex §1` |

---

## What Is NOT Achieved (and Why)

| Claim | Status | Reason |
|-------|--------|--------|
| k=1 from CFT | NOT PROVED | Gap G3-k; modular bootstrap not yet attempted |
| B_base = N_eff^{3/2} | MOTIVATED CONJECTURE [MC] | Requires k=1 proof |
| α⁻¹_bare = 137 (zero-parameter) | CONDITIONAL | Requires k=1 |
| g'/g from ℂ⊗ℍ | NOT DERIVED | Gap EW-1; no algebraic constraint found |
| θ_W from UBT | NOT DERIVED | Same as EW-1 |
| α⁻¹ = 137.036 (full, zero-parameter) | NOT ACHIEVED | δ = 0.036 circular (uses α, m_e) |
| R_ψ in physical units from S[Θ] | OPEN HARD PROBLEM | Uses m_e — Gap A10 |

---

## Gap Priority Order

1. **G3-k** (k = 1 from modular bootstrap / CFT) — resolves A3 and enables A1/A2 prime-attractor chain
2. **EW-1** (g'/g from Aut(ℂ⊗ℍ)) — resolves A1 and A2 directly
3. **GUT-UBT** (ℂ⊗ℍ → specific GUT group) — alternative path to EW-1 resolution
4. **EW-2** (Θ₀ VEV as doublet from S[Θ]) — required for A2
5. **A9** (δ = 0.036 without α, m_e) — required for full 137.036 claim
6. **A10** (R_ψ without m_e) — required for A4, and for removing last SE input

---

## Strategic Recommendation

**Immediate actions**:
1. Attempt modular bootstrap for k=1 (A3 time-box, 4 weeks to 2026-05-26)
2. Begin Layer2 coding paper in parallel (A5 publication path, independent)

**If gate opens (k=1 proved)**:
3. Draft minimal "α⁻¹_bare = 137" paper using prime-attractor chain

**If gate stays closed (2026-05-26)**:
4. Declare T3_ALPHA time-boxed; redirect T3 effort to T1_GR + T2_GAUGE writing
5. Continue Layer2 paper as primary deliverable from T3

---

## References

| File | Content |
|------|---------|
| `ALPHA_FINAL_OFFENSIVE.md` | Full track analysis with derivation steps |
| `ALPHA_PROGRESS_REPORT.md` | Full progress report on 27+ exhausted approaches |
| `reports/alpha_no_fit_audit.md` | No-fit audit (previous pass) |
| `canonical/alpha/alpha_derivation_routes.md` | Four-route survey (previous pass) |
| `best_candidate_derivation.tex` | Best-candidate derivation document |
| `research_tracks/T3_ALPHA/` | Full T3_ALPHA track documentation |
| `DERIVATION_INDEX.md` | Full approach inventory |

<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T3_ALPHA — Progress Log: Fine Structure Constant Derivation

**Track**: T3_ALPHA — Fine Structure Constant  
**Date**: 2026-04-28  
**Purpose**: Chronological record of the derivation state, exhausted approaches,
current status, and next recommended actions.  
**Sources**: `alpha_status_report.md`, `assumptions_audit.md`,
`MODULAR_BOOTSTRAP_K1_PLAN.md`, `fallback_layer2_outline.md`,
`DERIVATION_INDEX.md`, `canonical/alpha/alpha_derivation_routes.md`,
`reports/alpha_no_fit_audit.md`

---

## Executive Summary (2026-04-28)

| What is proved | What is blocked | What is open-hard |
|----------------|-----------------|-------------------|
| α⁻¹_bare = 137 [L1] given B_base | B_base = N_eff^{3/2} = 41.57 (k=1 Kac-Moody level) | R_ψ in physical units from S[Θ] |
| N_eff = 12 from ℂ⊗ℍ [L0] | | δ = 0.036 without α,m_e as inputs |
| B₀ = 8π one-loop [L1] | | |
| V_eff(n) = n² − B ln n form [L1] | | |
| Prime stability of n* = 137 [L1] | | |
| Dirac charge quantisation [L0] | | |
| Toroidal compactification [L0] | | |

**Current status**: The derivation chain is complete from axioms down to a conditional
result: α⁻¹_bare = 137, assuming B_base = 41.57.  The single remaining gap is proving
k = 1 (Kac-Moody level) without circular input.  27+ approaches have been exhausted.

**New direction as of 2026-04-28**: The α problem has been **converted to the
electroweak mixing problem** — deriving tan(θ_W) = g'/g from UBT algebra.
If θ_W is derived, then α = g² sin²θ_W / (4π) follows without B_base.
See `canonical/alpha/weinberg_angle_derivation.md` and `reports/ew_mixing_status.md`.

---

## Chronological Progress Log

### Phase 1 — Foundations (2025)

| Date | Achievement | Status | Source |
|------|-------------|--------|--------|
| 2025-Q3 | N_eff = 12 derived from ℂ⊗ℍ mode counting | [L0] PROVED | `canonical/n_eff/step1_mode_decomposition.tex` |
| 2025-Q3 | B₀ = 8π from one-loop vacuum polarisation | [L1] PROVED | `canonical/n_eff/step2_vacuum_polarization.tex` |
| 2025-Q3 | V_eff(n) = n² − B ln n effective potential | [L1] PROVED | `canonical/appendices/appendix_alpha_geometry.tex §3` |
| 2025-Q4 | n* = √(B/2) stationarity condition | [L1] PROVED | `canonical/appendices/appendix_alpha_geometry.tex §4` |
| 2025-Q4 | Prime stability: n* = 137 (given B_base) | [L1] PROVED | `canonical/appendices/appendix_alpha_geometry.tex §4` |
| 2025-Q4 | Toroidal compactification and Dirac quantisation | [L0] PROVED | `canonical/appendices/appendix_alpha_geometry.tex §1` |
| 2025-Q4 | T-duality self-dual point (algebraic part) | [L0] PROVED | `canonical/geometry/Rpsi_dynamical_fix.tex` |

### Phase 2 — B_base Attack (27+ approaches, 2025–2026)

| Approach | Method | Result | Status |
|----------|--------|--------|--------|
| H1 | Direct N_eff counting | B₀ = 8π | Proved [L1] |
| H2 | CS-term absence → k=1 | k=1 motivated | [MC] only |
| H3 | Modular bootstrap ϑ₃³(τ) | k = 3/2 modular weight | Computed [L0]; disconnected |
| H4 | j(τ) = 1728 = 12³ | Numerical coincidence | Noted [O]; not a proof |
| H5 | Spectral gap q-suppression | R_ψ-dependent | [SE] — external input |
| H6 | RG attractor τ* = i/137 | Modular interpretation | [MC] — no derivation |
| H7–H27 | Variants of H2–H6 | No new closure | Documented in `DERIVATION_INDEX.md §α` |

**Outcome of Phase 2**: The B_base gap remains open.  No approach in H2–H27 has
produced a proof of k=1 from ℂ⊗ℍ axioms alone without circular use of α or m_e.

### Phase 3 — Modular Bootstrap (Active as of 2026-04-28)

**Plan**: `MODULAR_BOOTSTRAP_K1_PLAN.md`  
**Time-box**: 4 weeks (deadline 2026-05-26)  
**Goal**: Prove k=1 via crossing symmetry constraint on the partition function Ẑ(τ) of
the biquaternion field Θ on the torus T².  

| Step | Target | Status |
|------|--------|--------|
| M1 | Show S[Θ] restricted to T² is a 2D CFT with c = 3 | In progress — `research_tracks/T3_ALPHA/bootstrap_step_m1_conformal.tex` |
| M2 | Compute partition function Ẑ(τ) = ϑ₃³(τ) | Planned |
| M3 | Apply crossing symmetry to constrain k | Planned |
| M4 | Verify k = 1 is unique solution | Planned |

If all four steps succeed: k=1 is proved, B_base = 41.57 follows, α⁻¹_bare = 137
becomes a zero-parameter result.

### Phase 4 — EW Conversion (New, 2026-04-28)

**New strategy**: Convert the α problem to the electroweak mixing problem.

The key identity: $\alpha = \frac{g^2 \sin^2\theta_W}{4\pi}$

If tan(θ_W) = g'/g is derived from UBT algebra, then:
- α follows if g is also derived (or via the SM relation α(m_Z) = α_EM known from experiment).
- Alternatively, α itself may not be the target — **θ_W is the more fundamental quantity**.

See `canonical/alpha/weinberg_angle_derivation.md` for the three-workstream attack plan.

---

## Proved Results (No Qualifications)

These results are clean and can be stated without caveats in any paper.

### A-PR-1: N_eff = 12 [L0]

```
N_phases = dim_ℝ(Im ℍ) = 3
N_helicity = 2  (left/right helicity)
N_charge = 2   (charge conjugate pairs)
N_eff = 3 × 2 × 2 = 12
```

Zero free parameters.  
**Source**: `canonical/n_eff/step1_mode_decomposition.tex`

### A-PR-2: B₀ = 8π [L1]

```
B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π ≈ 25.133
```

One-loop vacuum polarisation of N_eff = 12 charged modes on S¹_ψ.  
**Source**: `canonical/n_eff/step2_vacuum_polarization.tex`

### A-PR-3: V_eff and Prime Attractor [L1, given B_base]

If B_base = 41.57 (i.e., R² = B_base / B₀ ≈ 1.241, R ≈ 1.114), then:
```
V_eff(n) = n² − B ln n  (B = B_base · R²)
n* = √(B/2) ≈ 137
```
α⁻¹_bare = n* = 137.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`

### A-PR-4: Dirac Charge Quantisation [L0]

The ψ-circle winding condition:
```
exp(iq ∮_ψ A_ψ dψ) = 1  ⟹  q ∈ ℤ · e_0
```
Electric charge is quantised in integer multiples of a unit e₀.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §1`

---

## Blocking Gaps (Ordered by Tractability)

### B-GAP-1: k=1 Kac-Moody Level [MC ONLY — BLOCKING]

**Description**: Prove that the Kac-Moody level of the current algebra of Θ
on T² is k = 1, without using α or m_e as inputs.

**Why it's hard**: Requires either:
- Rigorous 2D CFT treatment of ℂ⊗ℍ field theory on T²
- Heat-kernel / ζ-function regularisation of the one-loop determinant of ∇†∇
- Modular bootstrap crossing symmetry bound

**Approaches remaining**: Modular bootstrap (Step M1–M4, see `k_equals_1_attack_plan.md`).

**Time-box**: 4 weeks (2026-05-26 deadline).

### B-GAP-2: R_ψ in Physical Units [OPEN HARD]

**Description**: Derive the physical radius R_ψ of S¹_ψ from S[Θ] without using m_e.

**Why it's hard**: The T-duality self-dual point gives R_ψ = 1/√2 in string units,
but physical units require an additional scale input.

**Current status**: OPEN HARD PROBLEM — no known approach that avoids m_e.

### B-GAP-3: δ = 0.036 without circular input [OPEN]

**Description**: Derive the two-loop QED correction α⁻¹ − 137 ≈ 0.036 without using
α or m_e as inputs.

**Why it's hard**: The two-loop formula uses both α and m_e to specify the UV cutoff.

**Note**: If the EW conversion strategy succeeds (θ_W derived → α = g² sin²θ_W/(4π)),
this gap becomes irrelevant for the main derivation.

---

## EW Conversion: Why This is the Right Pivot

The original α problem:
```
α⁻¹_bare = 137 [L1, conditional on B_base]
          ↓
Need: B_base = 41.57 [MC only, 27 approaches exhausted]
```

The EW conversion problem:
```
α = g² sin²θ_W / (4π)
      ↓
Need: tan(θ_W) = g'/g from ℂ⊗ℍ algebra
      ↓
This is Gap EW-1 — fresh attack, 0 approaches exhausted
```

The EW approach has several advantages:
1. **Fresh problem**: Gap EW-1 has not been attacked. The original B_base gap had 27 exhausted approaches.
2. **Better target**: θ_W = 0.481 rad (sin²θ_W ≈ 0.231) is a dimensionless mixing angle — a more natural output from an algebraic construction.
3. **GUT anchor**: The SU(5) GUT prediction sin²θ_W(GUT) = 3/8 is algebraically clean. If ℂ⊗ℍ has an SU(5)-like structure, this gives a boundary condition.
4. **B_base bypass**: A derived θ_W gives α directly without needing k=1 at all.

---

## Current Recommendation

| Action | Timeline | Priority |
|--------|----------|----------|
| Continue modular bootstrap M1–M4 | 4 weeks | HIGH (time-boxed) |
| Attack Gap EW-1 via EW1/EW2/EW3 workstreams | Parallel | **CRITICAL (new)** |
| If bootstrap fails at M1: activate Layer2 coding paper | After 4 weeks | Fallback |
| Do NOT continue exhausting H2–H27 variants | — | FORBIDDEN |

---

## References

- `k_equals_1_attack_plan.md` — modular bootstrap attack plan (this track)
- `MODULAR_BOOTSTRAP_K1_PLAN.md` — root-level plan document
- `assumptions_audit.md` — complete circularity map
- `fallback_layer2_outline.md` — Layer2 coding paper alternative
- `canonical/alpha/weinberg_angle_derivation.md` — EW conversion workstreams
- `reports/ew_mixing_status.md` — EW mixing status
- `DERIVATION_INDEX.md §α` — all α-related proof entries

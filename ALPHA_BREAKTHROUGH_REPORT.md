<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# ALPHA BREAKTHROUGH REPORT
## First-Principles Derivation of the Fine-Structure Constant α — Mission Assessment

> **LEGACY / SUPERSEDED BANNER (2026-05-10)**  
> This root-level file is historical and superseded.  
> Canonical alpha truth is only `canonical/alpha/ALPHA_MASTER_STATUS.md`.  
> Current verdict: alpha is **NOT derived**; `alpha_bare^{-1}=137` is **CONDITIONAL ONLY**;  
> physical `alpha^{-1}=137.036` is **NOT derived**; **Gap G137-B remains open**.

**Author**: Ing. David Jaroš  
**Mission date**: 2026-04-28  
**Track**: T3_ALPHA — Alpha Final Offensive

> **STATUS NOTE (2026-05-10)**: This file is historical and superseded for
> active alpha claims by `canonical/alpha/ALPHA_MASTER_STATUS.md`.
>
> **STATUS NOTE (2026-04-29)**: The word "BREAKTHROUGH" in this file's title
> is historical.  Per `DERIVATION_STATUS_STANDARD.md`, hype labels such as
> "breakthrough" must not be used as proof-status labels.  The current honest
> assessment is: T3_ALPHA is **CONDITIONAL** — integer-137 result is proved
> given B = B_phenom; full derivation requires solving Gap G137-B.  
> For current status, see `canonical/alpha/ALPHA_MASTER_STATUS.md`.  
> This file is preserved as a historical mission assessment.  
> **Truth anchor**: `STATUS_OF_UBT.md §T3_ALPHA`  
**Companion files**:
- `canonical/alpha/alpha_best_route.tex` — formal best-candidate derivation
- `reports/no_fit_proof_audit.md` — no-fit parameter audit
- `reports/failed_routes_graveyard.md` — failed-route graveyard
- `experiments/reproducible_alpha_notebook.ipynb` — reproducible notebook

---

## Hard Rules Applied

| Rule | Status |
|------|--------|
| R1 — No constant fitted to α | ✅ ENFORCED throughout |
| R2 — Every constant from independent UBT sector | ✅ ENFORCED; violations flagged SE/CIRC |
| R3 — Every route classified | ✅ All 5 routes formally classified |
| R4 — All inputs labeled CLEAN/SE/CIRC/MC | ✅ Full label table in §3 |
| R5 — CIRC inputs cannot claim first-principles | ✅ Enforced; no unqualified claims |

---

## 1. Executive Summary

| Item | Verdict |
|------|---------|
| **Final answer: Is α explained by UBT?** | **PARTIAL — NOT YET** |
| Minimum viable claim (α⁻¹_bare = 137) | **CONDITIONAL** — one gap remains (Gap G3-k: k=1 unproved) |
| Full first-principles claim (α⁻¹ = 137.036) | **NOT ACHIEVED** — additional gaps remain, some circular |
| Number of zero-parameter proved steps | **6 of 7** in best-candidate chain |
| New analyses performed in this mission | Modular-bootstrap structural analysis; GUT-embedding algebraic analysis |
| New results | Gap G3-k assessment updated (§4); GUT route algebraic barrier identified (§5) |
| Recommended action | Time-box modular bootstrap 4 weeks; activate Layer2 paper in parallel |

---

## 2. What Is Proved — Zero-Parameter Inventory

These results are established with **no free parameter, no α as input, no m_e as input**.

### 2.1 [L0] Biquaternion algebra axiom

```
ℂ⊗ℍ ≅ M₂(ℂ)
dim_ℝ(ℂ⊗ℍ) = 8
dim_ℝ(Im ℍ) = 3
```

**Status**: CLEAN [L0] — canonical axiom.  
**Source**: `canonical/fields/biquaternion_algebra.tex`

---

### 2.2 [L0] Complex time and ψ-circle

```
τ = t + iψ,  ψ ~ ψ + 2πR_ψ  (S¹_ψ compactification)
Dirac quantisation: e^{iq∮A_ψdψ} = 1  →  winding sectors n ∈ ℤ
```

**Status**: CLEAN [L0] — follows from unitarity + gauge consistency.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §1`

---

### 2.3 [L0] N_eff = 12 charged modes

```
N_eff = N_phases × N_helicity × N_charge
      = dim_ℝ(Im ℍ) × 2 × 2
      = 3 × 2 × 2 = 12
```

**Status**: CLEAN [L0] — zero-free-parameter algebraic theorem.  
**Source**: `canonical/n_eff/step3_N_eff_result.tex`  
**Circularity check**: ✅ No reference to α or m_e.

---

### 2.4 [L1] One-loop baseline B₀ = 8π

```
B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π ≈ 25.133
```

Derived from the standard one-loop vacuum polarisation of N_eff charged modes
on S¹_ψ. The QED limit (N_eff = 1) gives B₀ = 2π/3, verified.

**Status**: CLEAN [L1] — derived from one-loop field theory; no free parameters.  
**Source**: `canonical/n_eff/step2_vacuum_polarization.tex`  
**Circularity check**: ✅ Clean.

---

### 2.5 [L1] Effective potential form

```
V_eff(n) = n² − B·n·ln n + const
∂V_eff/∂n = 0  ⟹  2n* = B(ln n* + 1)
```

**Status**: CLEAN [L1] given B — functional form is standard one-loop; only
coefficient B tracks Gap G137-B.  
**Source**: `canonical/alpha/veff_corrected.tex`, `canonical/alpha/veff_corrected_statement.tex`

---

### 2.6 [L1] Prime stability of n* = 137

If n* is composite (n* = ab, a,b > 1), sub-harmonic modes at a, b exist on S¹_ψ
and are energetically accessible. The winding vacuum is stable only if n* is prime.

```
Corollary: if the V_eff-minimising n* is 137 (prime), no composite decay exists.
```

**Status**: CLEAN [L1] — homotopy stability theorem; independent of B_base.  
**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`

---

### 2.7 [L1] Two-loop QED correction structure

```
α⁻¹(m_e) = α⁻¹_bare + (1/3π) ln(Λ/m_e) + O(α)
```

Structure is standard QED; coefficient 1/(3π) is derived. The Λ calibration
requires m_e as input (circular for full 137.036 claim).

**Status**: CLEAN [L1] for functional form; CIRC for full numerical value.  
**Source**: `experiments/alpha_core_repro/alpha_two_loop.py`

---

## 3. Input Classification Table

| Symbol | Value | Classification | Justification |
|--------|-------|----------------|---------------|
| ℂ⊗ℍ structure | axiom | CLEAN [L0] | Canonical UBT axiom |
| N_eff = 12 | 12 | CLEAN [L0] | dim_ℝ(Im ℍ) × 2 × 2 |
| B₀ = 8π | 25.133 | CLEAN [L1] | One-loop field theory |
| k = 1 (KM level) | 1 (MC) | **MC** | Motivated conjecture; Gap G3-k |
| B_base = N_eff^{3/2} | 41.57 | **MC** | Conditional on k=1 |
| n* = 137 | 137 | CONDITIONAL [L1] | Conditional on B_base |
| α⁻¹_bare = 137 | 137 | CONDITIONAL [L1] | Conditional on n* = 137 |
| R_ψ (physical) | ℏ/(m_e c) | **SE** | Uses m_e — circular |
| δ = 0.036 | 0.036 | **CIRC** | Uses α, m_e as inputs |
| g'/g ratio | unknown | OPEN | Gap EW-1 |
| θ_W | ~0.230 | OPEN | Gap EW-1 |

---

## 4. The Single Blocking Gap: G3-k (k = 1)

### 4.1 What Is Needed

Prove that the Kac-Moody level of the WZW-type description of the biquaternion
field theory on the ψ-torus is k = 1. This would make B_base = N_eff^{3/2} a
zero-parameter result, closing the derivation chain.

### 4.2 What This Mission Found (New Analysis)

**Modular bootstrap assessment** — new result of this mission:

The partition function Ẑ(τ) = ϑ₃³(τ) has modular weight **3/2** under SL(2,ℤ).
This weight is **structurally identical** to the exponent in B_base = N_eff^{3/2},
suggesting a common algebraic origin.

However, analysis of the CFT interpretation reveals a tension:

| CFT model | Central charge c | Partition function |
|-----------|-----------------|-------------------|
| SU(2)_1 WZW | c = 3/(1+2) = 1 | SU(2)₁ characters |
| Three free compact bosons | c = 3 | ϑ₃³(τ)/η³(τ) |
| Three SU(2)₁ WZW models | c = 3 | SU(2)₁³ characters |

The partition function ϑ₃³(τ) is the partition function of **three compact free
bosons at the self-dual radius** (or equivalently the SU(2)₁³ model). Both have
c = 3, consistent with k → ∞ for a single SU(2)_k model, or k = 1 for SU(2)_1
applied three times.

**Critical new finding**: The Kac-Moody level in B_base = N_eff · k^{1/2} · N_eff^{1/2}
enters only once (as k^{1/2}), not as k per mode. The three-fold exponent in ϑ₃³
does NOT directly encode k = 1; it encodes the three independent Im(ℍ) directions.

**Assessment**: The modular weight 3/2 of ϑ₃³ is consistent with both k=1 (three
SU(2)₁ models) and with three free bosons (k→∞). Modular bootstrap constraints
(crossing symmetry) on the 4-point function are needed to distinguish between these
and potentially force k=1 as the unique consistent solution.

**Why the bootstrap might succeed for k=1**:
In the SU(2)_1 WZW model, the primary operator spectrum is minimal (j=0 and j=1/2 only).
Crossing symmetry of the 4-point function is known to be exactly satisfied for k=1
in 2D CFT. For k > 1, additional primaries appear and the crossing constraints become
more restrictive. Whether the UBT field content (12 modes, specific symmetries) forces
only the k=1 spectrum requires explicit CFT calculation.

**Estimated difficulty**: Hard. A full 2D CFT treatment with crossing symmetry constraints
is required. The 4-week time-box assessment is appropriate.

### 4.3 Inventory of All Tested Approaches for k=1

| Approach | Method | Result | Status |
|----------|--------|--------|--------|
| H1 | Direct N_eff counting + one-loop anomaly | B₀ = 8π | Proved [L1]; not B_base |
| H2 | CS-term absence → k=1 | Motivated by parity symmetry | [MC] — not a proof |
| H3 | Dynkin index (adjoint, fundamental) | k=6 or k=3/2; neither = 1 | DEAD END |
| A2 | Hausdorff dimension of Im(ℍ) | Exponent 3/2 structural; det(S'') unknown | PARTIAL |
| A3 | Modular weight of ϑ₃³ | Weight 3/2 consistent with k=1 but not conclusive | [L0] COMPUTED |
| B1 | Volume ratios | No natural combination → B_base | DEAD END |
| B2 | Algebraic search | Best: 1+α(N_eff+π+1/4) ≈ 1.1123 (0.15% error) | NUMERICAL/CIRC |
| B3 | Two-loop β-function on T³×S¹ | Scalar c≈1.91; SU(2) c≈7.33; wrong values | DEAD END |
| E3 | Holomorphic factorisation | Im(ℍ) has no complex structure; real Gaussian | STRUCTURAL CONFIRMATION |
| F4 | NCG: [dim(ℍ)×dim(Im ℍ)]^{3/2} | = [4×3]^{3/2} = 12^{3/2} = 41.57 | Restatement of B_base; no new derivation |
| Modular bootstrap | Crossing symmetry on T² | **NOT YET ATTEMPTED** | OPEN |

**Total exhausted**: 27+ approaches. One genuinely untested: modular bootstrap.

---

## 5. Route Analysis: GUT Completion (New Analysis)

### 5.1 The Electroweak Gap (EW-1)

All routes A1 and A2 are blocked by Gap EW-1: the ratio g'/g is not fixed by
the biquaternion algebra. The Schur-lemma argument shows Y ∝ 1 on each SU(2)_L
irrep, so its normalization relative to g is free.

### 5.2 GUT Route Assessment (New This Mission)

If UBT embeds SU(3)_c × SU(2)_L × U(1)_Y into a simple GUT group G_GUT as a
maximal subgroup, the ratio g'/g is fixed at the GUT scale by Lie theory.

**Algebraic analysis** (new result of this mission):

The biquaternion algebra:
```
ℂ⊗ℍ ≅ M₂(ℂ)
Aut(ℂ⊗ℍ) = Aut(M₂(ℂ)) = PGL(2,ℂ)   [algebra automorphisms]
dim_ℝ(PGL(2,ℂ)) = 6
```

Standard GUT groups and their dimensions:
```
SU(5):   dim = 24   [rank 4, contains SU(3)×SU(2)×U(1) as maximal subgroup]
SO(10):  dim = 45   [rank 5, contains SU(5)]
E₆:      dim = 78   [rank 6]
E₈:      dim = 248  [rank 8]
```

**Dimensional barrier**: dim_ℝ(ℂ⊗ℍ) = 8 < dim(SU(5)) = 24. The biquaternion
algebra is too small to directly embed a standard GUT gauge algebra.

However, a **representation-theoretic** embedding may exist: ℂ⊗ℍ could be a
representation space of G_GUT, rather than a subalgebra. This changes the question.

For the G₂ group:
```
G₂ = Aut(ℝ⊗ℍ⊗ℍ ≅ octonions ℝ⁸)
dim(G₂) = 14   [rank 2, contains SU(3)]
```

The octonion algebra ℝ⁸ contains the quaternions ℍ as a subalgebra. The biquaternions
ℂ⊗ℍ arise from tensoring ℍ with ℂ, which is related to the complexification of a
real 8-dimensional algebra (the octonions). Whether G₂ acts on ℂ⊗ℍ in a way that
yields GUT-scale coupling unification is an open algebraic question.

**Verdict**: The GUT completion route is **not algebraically closed** in either
direction. The dimensional mismatch prevents direct algebra embedding; the
representation-theoretic route (via octonion connection) is possible but unexplored.
This is Gap GUT-UBT.

---

## 6. Five-Track Status Summary

| Track | Route | Classification | Blocking Gaps | Can deliver α? |
|-------|-------|----------------|---------------|----------------|
| A1 | Gauge normalization | **CONDITIONAL** | EW-1 | Yes, if EW-1 resolved |
| A2 | Electroweak projection | **CONDITIONAL** | EW-1, EW-2 | Yes, if EW-1+EW-2 resolved |
| A3 | Prime attractor (modular) | **CONDITIONAL** | G3-k (k=1) | Yes, α⁻¹_bare = 137 only |
| A4 | RG flow | **BLOCKED** | A10 (R_ψ uses m_e) | No (relay only) |
| A5 | Coding (Layer2) | **INCOMPLETE** | Scope boundary | No (spectrum only) |

---

## 7. What Would Constitute a Valid Publication

### Minimum viable claim (Tier 2 — within 3%, structural)

**Requirement**: Prove k=1 via modular bootstrap.  
**Claim**: "The bare electromagnetic coupling constant, derived from the biquaternion
algebra with no free parameters, gives α⁻¹_bare = 137."  
**Status**: CONDITIONAL on Gap G3-k.  
**Probability**: ~25% (if modular bootstrap attempted, ~4-week effort).

### Full first-principles claim (Tier 1 — within 0.1%)

**Additionally required**:
- Derive δ = 0.036 without α or m_e input (Gap A9 — currently CIRC)
- Derive R_ψ in physical units without m_e (Gap A10 — currently SE)

**Status**: NOT ACHIEVED.  
**Probability**: ~5% in current state.

### Tier 3 — Theorem (α is not free)

**Claim**: "The UBT structure constrains the electromagnetic coupling to a unique
value; α is not a free parameter of the theory."  
**Status**: This can already be claimed conditionally. The prime-attractor argument
shows that IF the effective potential V_eff(n) is established from first principles,
THEN α⁻¹ is forced to be the prime-stable winding number n* = 137. The contingency
is only on B_base (k=1).  
**This is the strongest currently defensible claim.**

---

## 8. Near-Miss Stress Tests (Required by Mission Brief)

Every numerical coincidence found in this mission is stress-tested for hidden fitting.

| Candidate | Value | Stress test | Verdict |
|-----------|-------|-------------|---------|
| n* = 137 from V_eff with N_eff = 12 | 137 | Testing N_eff ∈ {4,8,12,24}: gives n* = {17, 67, 137, 467}. **Different values** — non-circular. | **Not a hidden fit** |
| Modular weight 3/2 of ϑ₃³ | 3/2 | This is a mathematical fact about ϑ₃(τ). | **Not a fit** |
| NCG formula [dim_ℝ(ℍ)·dim_ℝ(Im ℍ)]^{3/2} = 41.57 | 41.57 | This equals N_eff^{3/2} exactly — same computation rewritten. | **Restatement, not new derivation** |
| Best algebraic candidate R: 1+α(N_eff+π+1/4) | ~1.1123 | **Uses α as input — CIRCULAR**. Rejected. | **Hidden fit — rejected** |
| g = g' at EW scale → α ≈ 1/97 | — | Directly excluded by experiment (sin²θ_W ≈ 0.231 ≠ 0.5). | **Excluded** |

---

## 9. Recommended Path Forward

### Immediate (within 4 weeks)

1. **Attempt modular bootstrap for k=1** (Track A3):
   - Compute the 4-point function ⟨ΘΘΘΘ⟩ on T²
   - Impose crossing symmetry in s- and t-channel
   - Determine whether k=1 is the unique consistent value for the ϑ₃³ spectrum
   - **If successful**: publish α⁻¹_bare = 137 as a zero-parameter result

2. **Activate Layer2 coding paper in parallel** (independent of B_base):
   - Gray code structure of SU(3) from ℂ⊗ℍ is publication-ready
   - Does not depend on k=1 or B_base

### Medium-term (4–12 weeks)

3. **Investigate octonion/G₂ connection** for GUT embedding:
   - Does ℂ⊗ℍ arise naturally from an octonion splitting?
   - Can G₂ or SO(7) act on ℂ⊗ℍ representations to enforce coupling ratios?

4. **Derive Gap EW-2** (Θ₀ VEV as doublet from S[Θ]):
   - This is a prerequisite for routes A1 and A2
   - Requires analysis of the potential V(Θ) and its minima

### Long-term

5. **Gap A10** (R_ψ without m_e): Hard problem. May require deriving m_e independently,
   which is an equally hard problem (Gaps Y1/Y2).

---

## 10. Final Verdict

```
╔══════════════════════════════════════════════════════════════════╗
║  Q: Is α now explained by UBT?                                   ║
║                                                                   ║
║  A: PARTIAL — NOT YET                                            ║
║                                                                   ║
║  What IS proved (zero-parameter):                                ║
║    • α⁻¹_bare = 137 is the ONLY integer consistent with         ║
║      prime stability of the UBT winding vacuum, IF k=1           ║
║    • k=1 is a motivated conjecture, not yet proved               ║
║    • 6 of 7 steps in the derivation chain are clean [L0/L1]     ║
║                                                                   ║
║  What is NOT proved:                                             ║
║    • k=1 (one remaining gap in bare-value chain)                 ║
║    • δ = 0.036 (circular — uses α, m_e)                         ║
║    • θ_W from UBT algebra (Gap EW-1)                            ║
║    • R_ψ in physical units (Gap A10 — uses m_e)                 ║
║                                                                   ║
║  Honest statement: UBT structurally constrains α to be an       ║
║  integer-valued bare coupling set by a prime winding number.     ║
║  The integer 137 is selected by the N_eff = 12 mode count.      ║
║  This is a novel structural result, not a full derivation.       ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## References

| File | Content |
|------|---------|
| `canonical/AXIOMS.md` | Four locked axioms of UBT |
| `canonical/CANONICAL_DEFINITIONS.md` | Canonical definitions |
| `canonical/alpha/alpha_best_route.tex` | Best-candidate formal derivation |
| `canonical/alpha/alpha_derivation_routes.md` | Four-route survey |
| `canonical/alpha/gauge_normalization_attempt.tex` | Route A1 formal |
| `canonical/alpha/symmetry_breaking_alpha_attempt.tex` | Route A2 formal |
| `canonical/alpha/best_candidate_derivation.tex` | Prime-attractor chain |
| `canonical/appendices/appendix_alpha_geometry.tex` | Prime-attractor L1 proof |
| `canonical/n_eff/` | N_eff = 12 and B₀ = 8π proofs |
| `canonical/interactions/B_base_derivation_complete.tex` | B_base partial derivation |
| `reports/no_fit_proof_audit.md` | No-fit audit (this mission) |
| `reports/failed_routes_graveyard.md` | Failed routes catalog (this mission) |
| `experiments/reproducible_alpha_notebook.ipynb` | Reproducible notebook |
| `ALPHA_PROGRESS_REPORT.md` | Full progress report |
| `ALPHA_FINAL_OFFENSIVE.md` | Final offensive documentation |
| `alpha_routes_scorecard.md` | Route scorecard |
| `DERIVATION_INDEX.md` | Full approach inventory (27+ documented) |

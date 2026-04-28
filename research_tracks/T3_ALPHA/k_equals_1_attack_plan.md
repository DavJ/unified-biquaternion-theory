<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T3_ALPHA — k=1 Attack Plan: Modular Bootstrap

**Track**: T3_ALPHA — Fine Structure Constant  
**Goal**: Prove k = 1 (Kac-Moody level of the current algebra of Θ on T²) from
ℂ⊗ℍ axioms alone, without circular use of α or m_e.  
**Method**: Modular bootstrap crossing symmetry  
**Time-box**: 4 weeks from 2026-04-28 (deadline: **2026-05-26**)  
**Date**: 2026-04-28  
**Parent plan**: `MODULAR_BOOTSTRAP_K1_PLAN.md` (root-level, full detail)  
**Sources**: `research_tracks/T3_ALPHA/bootstrap_step_m1_conformal.tex`,
`assumptions_audit.md §A5/A11`, `DERIVATION_INDEX.md §α`,
`canonical/alpha/alpha_derivation_routes.md`

---

## 1. Problem Statement

The single remaining gap in the minimum viable α derivation (α⁻¹_bare = 137) is:

> **Prove that the Kac-Moody level k of the current algebra of the biquaternion
> field Θ on the ψ-torus T² is k = 1.**

If k = 1:
```
B_base = N_eff^{3/2} = 12^{3/2} ≈ 41.569
  ↓
n* = √(B_base / 2) = √(N_eff^{3/2} / 2) ≈ 137.04
  ↓
α⁻¹_bare = 137  (zero-parameter result [L1])
```

If k ≠ 1 or k is not uniquely forced by the UBT field content:
B_base is not derived, and the α path via the prime attractor remains blocked.

---

## 2. Acceptance Criteria

A proof of k = 1 is accepted if and only if ALL five conditions hold:

| # | Criterion | Check |
|---|-----------|-------|
| 1 | **No fitting**: k = 1 forced by crossing symmetry or algebraic identity, not chosen to reproduce α | |
| 2 | **Unique value**: Argument must exclude k ≠ 1, not just show consistency | |
| 3 | **No circular input**: Proof must not use α, m_e, or any quantity calibrated to them | |
| 4 | **Explicit operator content**: Identifies which primary operators of the CFT are forced by UBT and shows inconsistency with k ≠ 1 | |
| 5 | **Reproducible**: Key computation is analytic or numerical script in `experiments/` | |

A result showing k = 1 is "most natural" or "simplest" without meeting condition 2
is [MC] only — this has already been achieved in v67 via the CS-absence argument.
A new result must go beyond [MC].

---

## 3. Circular Inputs Excluded

The following inputs are **forbidden** in the k=1 proof:

| Input | Label | Reason |
|-------|-------|--------|
| δ = 0.036 | **[CIRC]** | Uses α and m_e as input |
| R_ψ in SI units | **[SE]** | Uses electron mass m_e |
| Physical α correction | **[CIRC]** | UV cutoff Λ ≈ m_e/√α |
| sin²θ_W ≈ 0.231 | **[SE]** | Experimental value |

The proof must rest solely on ℂ⊗ℍ axiom, S¹_ψ compactification, N_eff = 12.

---

## 4. Four-Step Modular Bootstrap Plan

### Step M1: Conformal Invariance of S[Θ] on T²

**Goal**: Show that S[Θ] restricted to the torus T² = (S¹_ψ)² is a 2D CFT with
central charge c = 3.

**Why c = 3**: The ψ-circle compactification of ℂ⊗ℍ gives N_eff = 12 real bosonic
modes.  A free boson on a circle at radius R contributes c = 1.  The biquaternion
structure groups these into 3 complex bosons (N_eff/4 = 3), each contributing
c = 1, for a total c = 3.

**Proof requirements**:
- [ ] Show S[Θ] is Weyl-invariant on T² (conformal invariance)
- [ ] Compute the Virasoro central charge from the OPE of the stress tensor T(z)
- [ ] Show c = N_eff/4 = 3 follows from the mode decomposition

**Working document**: `research_tracks/T3_ALPHA/bootstrap_step_m1_conformal.tex`  
**Status**: IN PROGRESS

**Potential obstacle**: S[Θ] may not be Weyl-invariant without imposing a
conformal gauge — requires careful treatment of the T² metric.

---

### Step M2: Partition Function Ẑ(τ) = ϑ₃³(τ)

**Goal**: Compute the one-loop partition function of Θ on T² and show it is
$\hat{Z}(\tau) = |\vartheta_3(\tau)|^6$ (three complex free bosons).

**Strategy**:
- For a free complex boson on S¹ with radius R at Kac-Moody level k:
  the partition function is a Jacobi theta function ϑ₃(τ, z).
- For N_eff/4 = 3 independent complex bosons: Ẑ = ϑ₃³(τ) × [anti-holomorphic].
- The modular transformation τ → -1/τ exchanges winding and momentum modes.

**Proof requirements**:
- [ ] Write the Θ field mode expansion on T²: $\Theta = \sum_{m,n} \Theta_{m,n} e^{i(m t + n\psi)/R}$
- [ ] Compute the Hamiltonian H = L₀ + L̄₀ in terms of mode operators
- [ ] Show Z(τ) = Tr[e^{2πiτ(L₀ - c/24)}] factorizes as ϑ₃³(τ)
- [ ] Verify modular covariance under SL(2,ℤ)

**Status**: PLANNED

**Potential obstacle**: The biquaternion non-commutativity may generate cross-terms
in H beyond the free-boson form.

---

### Step M3: Crossing Symmetry Constraint on k

**Goal**: Apply modular bootstrap crossing symmetry to the four-point function of
current operators and show that k = 1 is the unique consistent value.

**Strategy**:
The Kac-Moody level k enters in the current-current OPE:
$$J^a(z) J^b(w) \sim \frac{k\,\delta^{ab}}{(z-w)^2} + \frac{if^{ab}{}_c J^c(w)}{z-w} + \ldots$$
Crossing symmetry of the four-point function $\langle J^{a_1} J^{a_2} J^{a_3} J^{a_4}\rangle$
gives a polynomial constraint on k.  For the specific representation content of the
UBT field Θ (which determines the operator spectrum), this constraint may fix k uniquely.

**Proof requirements**:
- [ ] Identify the current algebra of Θ on T²: which Kac-Moody algebra ĝ_k?
- [ ] For ĝ = ŝu(2), the spectrum of primary operators with dimension h = l(l+1)/(k+2)
  must be consistent with the UBT field content.
- [ ] UBT field content: N_eff = 12 modes → specific set of primary operators.
- [ ] Show that k = 1 is the unique level consistent with this set.

**Status**: PLANNED

**Potential obstacle**: If the current algebra of Θ is not ŝu(2) but a different
Kac-Moody algebra (e.g., ŝu(3) or ŝu(2)_L × ŝu(2)_R), the level structure is different.
The correct identification requires Step M1.

---

### Step M4: Uniqueness Verification

**Goal**: Verify computationally that k = 1 is the unique crossing-symmetric solution.

**Requirements**:
- [ ] Implement the crossing symmetry linear functional method (semidefinite programming
  or analytic bootstrap) for the specific CFT data from Step M3.
- [ ] Show the feasibility region for k reduces to a point (k = 1) or a discrete set.
- [ ] If discrete: show all k > 1 are ruled out by unitarity or by UBT operator content.
- [ ] Document in a reproducible script: `experiments/k1_bootstrap_verify.py`

**Status**: PLANNED — requires completion of M1–M3.

---

## 5. Alternative Proofs (If Bootstrap Fails)

If any step M1–M4 fails, these alternatives should be tested in order:

| Alternative | Description | Feasibility |
|-------------|-------------|-------------|
| **ALT-1**: WZW model embedding | Show Θ saturates the WZW level-rank duality at k = 1 | MEDIUM |
| **ALT-2**: Level-rank duality bound | SU(2)_k level-rank duality: k ≤ N_colors; with N_colors = 3, k ≤ 3; then k=1 from minimality | LOW–MEDIUM |
| **ALT-3**: Vertex algebra irreducibility | Show the Θ field VOA (vertex operator algebra) is irreducible only at k = 1 | MEDIUM |
| **ALT-4**: Modular discriminant | The η-function expansion of Ẑ(τ) gives η(τ)^{c/4}; at k=1, c is fixed by N_eff; check η identity | LOW |
| **ALT-5**: Lattice CFT | Realise Θ-CFT as a lattice model; k=1 follows from the minimal lattice | MEDIUM |

---

## 6. Decision Tree and Time-Boxing

```
Week 1: Attempt M1 (conformal invariance)
  ↓ Success → Week 2: M2
  ↓ Fail → ALT-1, ALT-2

Week 2: Attempt M2 (partition function)
  ↓ Success → Week 3: M3
  ↓ Fail → ALT-3

Week 3: Attempt M3 (crossing symmetry)
  ↓ Success → Week 4: M4
  ↓ Fail → ALT-4, ALT-5

Week 4: Verification M4 or ALT-5
  ↓ Success → k=1 proved; α⁻¹_bare = 137 [L1]
  ↓ Fail → Declare bootstrap blocked; pivot fully to EW conversion
```

**Hard deadline**: 2026-05-26.  After this date:
- If M1–M4 succeeded: write up k=1 proof.
- If M1–M4 failed: **activate Layer2 coding paper** (`fallback_layer2_outline.md`)
  AND continue EW conversion workstreams (`canonical/alpha/weinberg_angle_derivation.md`).

---

## 7. What the Publication Claims After a Successful Bootstrap

If k=1 is proved, the claim hierarchy is:

**Proved [L1]:**
```
ℂ⊗ℍ (AXIOM-A) + S¹_ψ compactification (AXIOM-B)
→ N_eff = 12
→ Kac-Moody level k = 1 [from crossing symmetry, this plan]
→ B_base = 12^{3/2} ≈ 41.569
→ V_eff minimum n* ≈ 137
→ Prime stability n* = 137
→ α⁻¹_bare = 137
```

**Stated as two-loop QED correction:**
```
α⁻¹(m_e) = 137 + (1/3π) ln(Λ/m_e) + O(α) ≈ 137.036
```
with Λ, m_e as SM/experimental inputs (stated explicitly, not derived).

**This is a publishable first-principles derivation** of α⁻¹_bare = 137 from
three axioms of UBT, with the 0.036 correction acknowledged as a known QED effect.

---

## 8. Cross-References

- `MODULAR_BOOTSTRAP_K1_PLAN.md` — full root-level plan (more detail on §2–§3)
- `bootstrap_step_m1_conformal.tex` — working document for Step M1
- `assumptions_audit.md` — complete circularity map (A1–A12)
- `alpha_progress_log.md` — progress log and phase history
- `fallback_layer2_outline.md` — Layer2 fallback (activate if bootstrap fails)
- `canonical/alpha/weinberg_angle_derivation.md` — EW conversion alternative
- `reports/ew_mixing_status.md` — EW mixing status

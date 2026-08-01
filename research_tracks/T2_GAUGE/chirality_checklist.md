<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# T2_GAUGE — Chirality Checklist: Closing Gap C1

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Gap**: C1 — Why SU(2)_L and not SU(2)_R  
**Current status**: MOTIVATED [SE] — physical argument given, no formal theorem  
**Target status**: [L1] PROVED — formal theorem from UBT axioms  
**Date**: 2026-04-28  
**Sources**: `missing_axioms.md §Gap C1`,
`canonical/chirality/step1_psi_parity.tex`,
`canonical/chirality/step2_chirality_result.tex`,
`canonical/chirality/step3_gap_C1_resolution.tex`,
`canonical/symmetry/chirality_and_parity_breaking.tex`

---

## What Gap C1 States

**Required theorem**: The complex-time structure $\tau = t + i\psi$ in UBT
selects **left-handed** weak couplings (SU(2)_L) over right-handed (SU(2)_R).
Formally: the UBT action $S[\Theta]$ is invariant under SU(2)_L gauge transformations
but not under SU(2)_R gauge transformations.

**Current status**: The ψ-parity argument is given in `canonical/chirality/`,
but it has not been elevated to a formal theorem with explicit proof steps.

---

## Proof Strategy (ψ-Parity Theorem)

The physical argument is:

1. Define the **ψ-parity** operation $P_\psi: \psi \mapsto -\psi$ acting on the
   imaginary time component of $\tau = t + i\psi$.
2. Under $P_\psi$, left-handed and right-handed field components transform differently.
3. Show that the UBT action $S[\Theta]$ is invariant under $P_\psi$ only for
   left-chiral couplings.
4. Therefore, the gauge symmetry preserved by $P_\psi$ is SU(2)_L, not SU(2)_R.

---

## Checklist: Steps to Formal Theorem

### Step C1.1 — Define ψ-Parity Formally

- [ ] **Define** $P_\psi: \tau = t + i\psi \mapsto t - i\psi$ as a map on the
  complex-time domain $\mathbb{C}_\tau$.
- [ ] **Specify** the induced action of $P_\psi$ on the Θ field:
  $P_\psi[\Theta(q,\tau)] = \Theta(q, \bar\tau)$.
- [ ] **Specify** the induced action of $P_\psi$ on the biquaternion algebra ℂ⊗ℍ:
  $P_\psi[z \otimes h] = \bar{z} \otimes h$ (complex conjugation of the ℂ factor).
- [ ] **Verify** that $P_\psi$ is an anti-involution of ℂ⊗ℍ:
  $P_\psi^2 = \mathrm{id}$, $P_\psi(ab) = P_\psi(b)P_\psi(a)$.

**Source**: `canonical/chirality/step1_psi_parity.tex`  
**Status**: Defined. Verification of anti-involution property — need to check.

---

### Step C1.2 — Decompose Θ into Chirality Components

- [ ] **Define** left-chiral component: $\Theta_L := \frac{1}{2}(\Theta + P_\psi[\Theta])$
- [ ] **Define** right-chiral component: $\Theta_R := \frac{1}{2}(\Theta - P_\psi[\Theta])$
- [ ] **Verify** that $\Theta = \Theta_L + \Theta_R$ is a direct sum decomposition.
- [ ] **Identify** which SU(2) subgroup of Aut(ℂ⊗ℍ) preserves $\Theta_L$ and which
  preserves $\Theta_R$.
- [ ] **Show** that $\Theta_L$ transforms under left multiplication (SU(2)_L sector)
  and $\Theta_R$ under right multiplication (SU(2)_R sector).

**Source**: `canonical/chirality/step2_chirality_result.tex`  
**Status**: Decomposition defined. Transformation properties — claim made but explicit
matrix computation not shown.

---

### Step C1.3 — Analyse the UBT Action under P_ψ

- [ ] **Write** the UBT kinetic action in terms of $\Theta_L$ and $\Theta_R$:
  $S[\Theta] = S[\Theta_L, \Theta_R]$.
- [ ] **Compute** $S[P_\psi[\Theta]] = S[\Theta_R + \Theta_L] = S[\Theta_L, \Theta_R]$
  (or show it is different, i.e., $S \neq S \circ P_\psi$).
- [ ] **Determine** whether $S[\Theta]$ changes under $P_\psi$.
- [ ] If $S[\Theta] \neq S[P_\psi[\Theta]]$: the theory is chiral and SU(2)_L is selected.
- [ ] If $S[\Theta] = S[P_\psi[\Theta]]$: the theory is vector-like and the argument fails
  — a new mechanism is needed.

**Key computation** (blocking the gap):  
The UBT kinetic term is $\mathrm{Tr}[\partial_\mu\Theta \cdot \partial^\mu\Theta^\dagger]$.
Under $P_\psi$: $\partial_\tau \Theta \to \partial_{\bar\tau}P_\psi[\Theta]$.
The question is whether the ψ-derivative $\partial_\psi\Theta$ contributes asymmetrically.

- [ ] **Compute** $\partial_\psi \Theta_L$ and $\partial_\psi \Theta_R$ explicitly.
- [ ] **Check** whether the cross-terms $\partial_\psi\Theta_L \cdot \partial_\psi\Theta_R^\dagger$
  vanish in the action.

**Source**: `canonical/chirality/step3_gap_C1_resolution.tex`  
**Status**: Computation not completed. This is the core missing step.

---

### Step C1.4 — Formal Gauge-Invariance Test

- [ ] **Perform** a gauge transformation under SU(2)_L: $\Theta \to U_L \Theta$,
  $U_L \in SU(2)_L$.
- [ ] **Verify** that $S[U_L\Theta] = S[\Theta]$ for all $U_L \in SU(2)_L$.
- [ ] **Perform** a gauge transformation under SU(2)_R: $\Theta \to \Theta U_R$,
  $U_R \in SU(2)_R$.
- [ ] **Verify** that $S[\Theta U_R] \neq S[\Theta]$ unless $U_R = \mathrm{const}$.
- [ ] If both hold: **Theorem C1** is proved.

**Subtlety**: SU(2)_L and SU(2)_R are not independent in ℂ⊗ℍ ≅ Mat(2,ℂ).
Left multiplication by SU(2) and right multiplication by SU(2) are both symmetries
of the Frobenius norm $\mathrm{Tr}[\Theta\Theta^\dagger]$.  The ψ-parity must break
this symmetry.

- [ ] **Show** explicitly that $\partial_\psi$ distinguishes left from right multiplication.

**Source**: `canonical/symmetry/chirality_and_parity_breaking.tex`  
**Status**: Argument given physically; algebraic verification not complete.

---

### Step C1.5 — Theorem Statement and Proof Write-Up

- [ ] **State** Theorem C1 formally with all hypotheses explicit.
- [ ] **Write** proof with explicit reference to Steps C1.1–C1.4.
- [ ] **Register** in `DERIVATION_INDEX.md` as [L1].
- [ ] **Update** `gauge_exactly_proved_vs_open.md` chirality entry from [MC] to [L1].

---

## Known Obstacles

| Obstacle | Description | Mitigation |
|----------|-------------|------------|
| Vector-like kinetic term | Tr[∂_μΘ ∂^μΘ†] is left-right symmetric under constant SU(2) | Must use ψ-derivative specifically |
| P_ψ does not flip chirality globally | Only ∂_ψ cross-terms break the symmetry | Must show non-vanishing contribution |
| AXIOM B ambiguity | AXIOM B sets timelike property of ∂_τ, but not chirality | Need P_ψ as additional derived property |
| Anti-involution vs. involution | P_ψ acts on the ℂ factor; whether it is an algebra automorphism needs verification | Explicit computation required |

---

## Alternative Approaches (If ψ-Parity Fails)

If Step C1.3 shows $S[\Theta] = S[P_\psi[\Theta]]$ (vector-like result), the following
alternatives should be investigated:

| Approach | Description | Source |
|----------|-------------|--------|
| ψ-winding parity | Odd/even ψ-winding numbers couple to SU(2)_L/SU(2)_R differently | `canonical/chirality/` |
| Complex-τ holomorphic sector | SU(2)_L = holomorphic sector under τ analyticity | Not yet explored |
| SSB chirality selection | SSB of SU(2)_L × SU(2)_R → SU(2)_L via VEV structure | `canonical/symmetry/effective_vs_fundamental_breaking.tex` |
| Index-theorem argument | Atiyah-Singer index theorem: net chirality = index of ∇ on S¹_ψ | Research track |

---

## Paper Impact Assessment

| Scenario | Impact on SM gauge paper |
|----------|--------------------------|
| Gap C1 closed before submission | Full claim: SU(2)_L chirality derived, zero free parameters including parity |
| Gap C1 open at submission | Paper covers all [L0] results; chirality stated as motivated-only gap with explicit proof strategy |
| Gap C1 closed after submission | Update in published erratum/addendum; prior submission priority protected |

**Recommended action**: Attempt Steps C1.1–C1.3 before paper submission.
Estimated time: 2–3 weeks.  If Step C1.3 fails to give a chiral result, switch
to alternative approaches and state C1 as open.

---

## Cross-References

- `missing_axioms.md §Gap C1` — registered gap with motivation
- `gauge_exactly_proved_vs_open.md §SU(2)_L` — entry to update when proved
- `canonical/chirality/step3_gap_C1_resolution.tex` — working document for the proof
- `canonical/symmetry/chirality_and_parity_breaking.tex` — symmetry analysis

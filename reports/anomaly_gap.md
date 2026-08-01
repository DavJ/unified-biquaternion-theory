<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# anomaly_gap.md — T2_GAUGE Anomaly Cancellation Status

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Purpose**: Per-anomaly audit of whether each Standard Model gauge anomaly
cancellation is proved, motivated, or open in UBT.  
**Date**: 2026-04-28  
**Location**: `reports/anomaly_gap.md` (promoted from `research_tracks/T2_GAUGE/`)  
**Sources**: `research_tracks/T2_GAUGE/gauge_exactly_proved_vs_open.md`,
`canonical/interactions/sm_gauge.tex`,
`canonical/algebra/involutions_Z2xZ2xZ2.tex`,
`canonical/chirality/`

---

## Background: Why Anomaly Cancellation Matters for the Gauge Paper

A gauge theory is only consistent if the quantum effective action is gauge-invariant —
i.e., all gauge anomalies cancel.  In the Standard Model, anomaly cancellation is a
non-trivial constraint that fixes fermion hypercharge assignments.  For UBT to claim
SM gauge structure from first principles, it must either:

1. **Derive** fermion representations and show anomaly cancellation follows, or
2. **State explicitly** which anomalies cancel as a consequence of derived results
   and which are assumed from the SM.

---

## Anomaly Classification

| Type | Symbol | Condition |
|------|--------|-----------|
| Pure non-Abelian | $[SU(3)]^3$, $[SU(2)]^3$ | Automatically zero for unitary groups |
| Mixed non-Abelian–U(1) | $[SU(3)]^2 U(1)_Y$ | Requires fermion rep content |
| Pure hypercharge | $[U(1)_Y]^3$ | Requires fermion rep content |
| Mixed hypercharge–gravity | $[\mathrm{grav}]^2 U(1)_Y$ | Requires fermion rep content |
| Witten global anomaly | $\pi_4(SU(2)) = \mathbb{Z}_2$ | Requires counting SU(2) doublets |

---

## Checklist: Per-Anomaly Status

### AN-1: $[SU(3)_c]^3$ — Pure Strong Anomaly

**Condition for cancellation**: Automatic for $\mathrm{SU}(3)$ in the standard
representation (since $d^{abc} = \mathrm{Tr}[T^a\{T^b,T^c\}] = 0$ for $\mathrm{SU}(3)$
in the adjoint representation).

- [x] **Status**: **[L0] AUTO** — the $\mathrm{SU}(3)$ cubic Casimir $d^{abc}$ vanishes
  identically in the fundamental and adjoint representations.
- **UBT note**: The SU(3) derivation (Theorems G.A–G.D) uses the standard representation;
  $d^{abc} = 0$ follows automatically.
- **Action needed**: None. State in paper.

---

### AN-2: $[SU(2)_L]^3$ — Pure Weak Anomaly

**Condition for cancellation**: Automatic for $\mathrm{SU}(2)$ since $\mathrm{Tr}[T^i\{T^j,T^k\}] = 0$
for $\mathrm{SU}(2)$ in any representation (all representations are pseudo-real).

- [x] **Status**: **[L0] AUTO** — $\mathrm{SU}(2)$ cubic anomaly vanishes automatically.
- **UBT note**: SU(2)_L is derived as the left-unitary subgroup of Mat(2,ℂ).
  The pseudo-reality of SU(2) representations is an algebraic fact about ℂ⊗ℍ.
- **Action needed**: None. State in paper.

---

### AN-3: $[SU(3)_c]^2 [U(1)_Y]$ — Mixed Strong–Hypercharge Anomaly

**Condition for cancellation** (per generation):
$$\sum_{\text{quarks}} Y(\text{left}) - Y(\text{right}) = 0$$
With SM assignments: $Y(Q_L) = 1/6$, $Y(u_R) = 2/3$, $Y(d_R) = -1/3$:
$$3 \times \frac{1}{6} - \frac{2}{3} - (-\frac{1}{3}) = \frac{1}{2} - \frac{2}{3} + \frac{1}{3} = 0\;\checkmark$$

- [ ] **Status**: **[MC] MOTIVATED** — cancellation follows if SM hypercharge
  assignments are derived from UBT.
- **What is proved**: The SU(3)_c and U(1)_Y sectors are separately derived [L0].
  The quark hypercharge assignments (Y = 1/6, 2/3, -1/3) are currently SM inputs.
- **What is needed**: Derive fermion hypercharge assignments from the ψ-winding
  representation theory of ℂ⊗ℍ.
- **Gap**: EW-2 (Θ₀ as SU(2)_L doublet with Y = 1/2 from S[Θ]); fermion Y assignments
  from representation theory.
- **Action**: State as motivated (follows from SM assignments adopted as input).

---

### AN-4: $[SU(2)_L]^2 [U(1)_Y]$ — Mixed Weak–Hypercharge Anomaly

**Condition for cancellation** (per generation):
$$\sum_{\text{SU(2) doublets}} Y = 0$$
With SM assignments (left doublets $Q_L$, $L_L$):
$$3 \times \frac{1}{6} + \frac{-1}{2} = \frac{1}{2} - \frac{1}{2} = 0\;\checkmark$$

- [ ] **Status**: **[MC] MOTIVATED** — same as AN-3; follows from SM hypercharge
  assignments.
- **Action**: State as motivated. Note the three-generation structure (N_gen = 3 proved [L0])
  is crucial — a single generation with SM assignments satisfies this; the ×3 factor
  cancels.

---

### AN-5: $[U(1)_Y]^3$ — Pure Hypercharge Anomaly

**Condition for cancellation** (per generation):
$$\sum_{\text{all fermions}} Y^3 = 0$$
With SM assignments:
$$3 \times \left(2Y_{Q_L}^3 - Y_{u_R}^3 - Y_{d_R}^3\right) + \left(2Y_{L_L}^3 - Y_{e_R}^3\right) = 0$$

Numerically: $3(2/216 - 8/27 - (-1/3)^3) + (2(-1/2)^3 - (-1)^3) = 0\;\checkmark$
(standard SM computation).

- [ ] **Status**: **[MC] MOTIVATED** — follows from SM hypercharge assignments, not
  yet derived from UBT.
- **What is needed**: The hypercharge values $Y = 1/6, 2/3, -1/3, -1/2, -1$ (one
  generation) must be derived from the ψ-winding representation content of ℂ⊗ℍ.
- **Difficulty**: HIGH — requires full fermion representation theory from UBT.
- **Action**: State as motivated. Mark as open problem requiring EW-2 + fermion
  representation derivation.

---

### AN-6: $[\mathrm{grav}]^2 [U(1)_Y]$ — Gravitational–Hypercharge Anomaly

**Condition for cancellation** (per generation):
$$\sum_{\text{all fermions}} Y = 0$$
With SM assignments: $2Y_{Q_L} + 3(-Y_{Q_L}) + Y_{L_L} + Y_{e_R} + Y_{\nu_R,\text{if exists}} = 0$

More explicitly: $3(2 \times 1/6 - 2/3 + 1/3) + 2 \times (-1/2) + 1 = 3(0) + (-1) + 1 = 0\;\checkmark$

- [ ] **Status**: **[MC] MOTIVATED** — as for AN-3 through AN-5.
- **UBT note**: The gravitational sector is derived [L1] independently. The mixed
  anomaly requires both the GR chain (proved) and the hypercharge assignments (open).
- **Action**: State as motivated.

---

### AN-7: Witten Global SU(2) Anomaly

**Condition for cancellation**: The total number of SU(2)_L doublets must be even
(equivalently, $\pi_4(SU(2)) = \mathbb{Z}_2$ anomaly vanishes when doublet count is even).

With SM assignments: 3 quark doublets × 3 colors + 3 lepton doublets = 12 doublets.
$12 \mod 2 = 0\;\checkmark$

- [x] **Status**: **[L0]+[MC]** — N_gen = 3 is proved [L0] from dim_ℝ(Im ℍ) = 3.
  With 3 quarks (×3 colors) + 3 leptons = 12 doublets (given SM assignment), the
  Witten anomaly cancels automatically.
- **UBT note**: The number of generations N_gen = 3 is proved. The doublet structure
  (quarks + leptons) needs fermion rep derivation.
- **Action**: State N_gen = 3 as derived; doublet counting as motivated.

---

### AN-8: Mixed $[SU(3)_c][SU(2)_L]$ — Would-be anomaly

**Condition**: This mixed anomaly does not exist as a quantum anomaly in the SM
(different gauge groups cannot mix in this way in a local anomaly). However,
decoupling of SU(3) and SU(2) sectors must be verified.

- [x] **Status**: **[L0] PROVED** — Theorem G.D establishes that the SU(3) and
  SU(2)_L sectors decouple algebraically from the ℂ⊗ℍ structure.
- **Action**: None. Cite Theorem G.D.

---

## Summary Table

| Anomaly | SM satisfied? | UBT status | Blocking gap |
|---------|--------------|------------|--------------|
| AN-1: $[SU(3)]^3$ | ✅ Auto | **[L0] PROVED** | None |
| AN-2: $[SU(2)]^3$ | ✅ Auto | **[L0] PROVED** | None |
| AN-3: $[SU(3)]^2 U(1)_Y$ | ✅ Hypercharge | **[MC] MOTIVATED** | Fermion Y assignments |
| AN-4: $[SU(2)]^2 U(1)_Y$ | ✅ Hypercharge | **[MC] MOTIVATED** | Fermion Y assignments |
| AN-5: $[U(1)_Y]^3$ | ✅ Hypercharge | **[MC] MOTIVATED** | Fermion Y assignments |
| AN-6: $[\text{grav}]^2 U(1)_Y$ | ✅ Hypercharge | **[MC] MOTIVATED** | Fermion Y assignments |
| AN-7: Witten SU(2) global | ✅ Doublet count | **[L0]+[MC]** | N_gen proved; doublets motivated |
| AN-8: SU(3)×SU(2) decoupling | ✅ Structure | **[L0] PROVED** (G.D) | None |

---

## What the Gauge Paper Can Claim About Anomalies

**Proved without qualification:**
- $[SU(3)]^3$ and $[SU(2)]^3$ anomalies cancel automatically — [L0].
- SU(3)/SU(2) sector decoupling (Theorem G.D) — [L0].
- N_gen = 3 (contributing to AN-7) — [L0].

**To state as motivated (following from SM hypercharge assignments):**
- AN-3 through AN-7 cancel in the SM; UBT inherits this by adopting SM hypercharge
  assignments for fermions (which are themselves an open derivation problem in UBT).

**To state as open:**
- First-principles derivation of fermion hypercharge assignments from ψ-winding
  representation theory — Gap EW-2 + fermion-rep gap.

**Impact**: The gauge structure paper can state that anomaly cancellation is ensured
for all pure non-Abelian anomalies from UBT algebraic structure, while the mixed
hypercharge anomalies inherit the SM result pending derivation of fermion hypercharge.
This is honest and does not block submission.

---

## Next Steps to Improve Anomaly Status

| Priority | Action | Estimated impact |
|----------|--------|-----------------|
| HIGH | Derive fermion Y assignments from ψ-winding representation theory | Would upgrade AN-3–AN-6 from [MC] to [L1] |
| MEDIUM | Show Witten anomaly cancellation directly from N_gen = 3 and doublet structure | Would upgrade AN-7 to [L1] |
| LOW | Investigate Green-Schwarz mechanism in UBT (if anomalies don't cancel) | Insurance |

---

## Update 2026-05-17 (P8 checkpoint)

- Added `research_tracks/EW/anomaly_cancellation.tex` as focused first-principles audit note.
- Direct numerical check on the currently used charge list gives:
  - \(\Sigma Q = 0\)
  - \(\Sigma Q^3 = -4/9\) (non-zero for this naive charge-only set)
- Therefore the first-principles anomaly closure remains **OPEN** pending full
  chiral representation-level derivation tied to the finalized C2 hypercharge theorem.

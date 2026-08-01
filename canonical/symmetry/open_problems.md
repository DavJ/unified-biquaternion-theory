<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# Open Problems in UBT Discrete Symmetry Sector

© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

This document lists unresolved problems in the discrete-symmetry architecture
of Unified Biquaternion Theory (UBT).  Each entry states what is known,
what is missing, and an honest assessment of difficulty.

---

## Legend

| Priority | Meaning |
|----------|---------|
| **CRITICAL** | Required for the framework to be internally consistent |
| **HIGH** | Important for physical predictions or reviewer acceptance |
| **MEDIUM** | Desirable; does not block core theory |
| **LOW** | Nice to have; long-term goal |

| Status | Meaning |
|--------|---------|
| Open | No clear path to resolution |
| Active | Being worked on |
| Gap | Known gap with a sketch toward resolution |
| Conjecture | A plausible claim with no proof |

---

## OP-S1 — Antiunitary Structure of Time Reversal

**Priority**: HIGH
**Status**: Gap

**What is known**: The canonical UBT time reversal $T_{\rm UBT}$ is defined as
$T_{\rm UBT}[\Theta](q,\tau) = \Theta(q,-\tau)$ (no complex conjugation of
field values; see `discrete_symmetries.tex`, Section 2.4).  In standard QFT,
time reversal is antiunitary (Wigner's theorem: any symmetry of the
$S$-matrix that reverses time is antiunitary).

**What is missing**: The canonical sesquilinear (inner product) form
$\langle\cdot,\cdot\rangle$ on the space of $\Theta$ fields has not been
fixed.  Without it, we cannot determine whether $T_{\rm UBT}$ or the
antiunitary variant $T_3 = P_1 \circ T_{\rm UBT}$ (complex conjugation
composed with time negation) is the physically correct operator.

**Impact**: If $T_{\rm UBT}$ should be antiunitary, the $CPT$ operator changes:
$CPT = C \circ P \circ T_3 = (P_1 \circ P_2) \circ (P_1 \circ T_{\rm UBT})
= P_2 \circ T_{\rm UBT}$ (the two $P_1$ factors cancel).
This would alter the algebra-level form of $CPT$.

**Toward resolution**: Define the Hilbert space of $\Theta$ modes via the
$L^2$ norm $\int d^4q\,|\mathrm{Tr}(\Theta^\dagger\Theta)|$, and determine
which $T$ operator is unitary vs.\ antiunitary with respect to this norm.

---

## OP-S2 — Equivalence of Grade and $\psi$-Mode Decompositions

**Priority**: HIGH
**Status**: Gap

**What is known**: Two definitions of the left/right chiral split are available:
(i) the algebraic grade decomposition $\Theta_L = \mathsf{P}_-\Theta$ via the
$P_2$ involution; (ii) the $\psi$-mode decomposition via odd/even Fourier
modes on the $\psi$-circle.  Both are used in the chirality derivation
(`canonical/chirality/step1_psi_parity.tex` and `chirality_and_parity_breaking.tex`).

**What is missing**: A proof that these two decompositions are equivalent, i.e.,
that the $P_2$-odd subspace of $\mathcal{B}$ maps exactly onto the odd-$n$
$\psi$-modes upon integration over the $\psi$-circle.

**Impact**: Without this equivalence, the claim that "UBT naturally produces
left-handed weak interactions" rests on two separate (possibly inconsistent)
arguments.

**Toward resolution**: Compute the $\psi$-mode profile of $\mathsf{P}_\pm\Theta$
for a generic $\Theta(q,t+i\psi)$ and verify odd/even $n$ selection.

---

## OP-S3 — Dynamical Origin of Chirality Selection

**Priority**: HIGH
**Status**: Conditional (gap partially addressed; see `step3_gap_C1_resolution.tex`)

**What is known**: The UBT framework provides an algebraic mechanism for
identifying left-handed modes (Section 3.2 of `chirality_and_parity_breaking.tex`).
`step3_gap_C1_resolution.tex` shows that under the no-$W_R$ selection rule,
$P_\psi(\mathcal{L}_W) \neq \mathcal{L}_W$, establishing parity violation
conditionally.

**What is still missing**: A derivation showing that the no-$W_R$ selection
rule is itself a theorem rather than a model axiom.  Without this, the
statement "the $W$-boson vertex is necessarily $P_\psi$-violating" is
conditional, not proved.  See OP-S4 for the open problem on $SU(2)_R$ absence.

**Toward resolution**: (a) Derive algebraically or via a symmetry argument
why gauging $SU(2)_R$ is forbidden or decoupled in UBT.  (b) Expand the full
covariant derivative $D_\mu = \partial_\mu + \Gamma_\mu + igW_\mu$ in
$\psi$-modes and confirm which vertex contains an odd power of $\partial_\psi$.

---

## OP-S4 — Exact Standard Model Gauge Group Recovery

**Priority**: CRITICAL
**Status**: Open

**What is known**: UBT contains $SU(2)$ from the quaternion sector and
$U(1)$ from the complex sector.  The $SU(3)_c$ sector is derived via
$\mathbb{Z}_2^3$ involutions in `canonical/su3_derivation/`.

**What is missing**:
- A proof that the UBT gauge group is exactly $SU(3)_c \times SU(2)_L \times U(1)_Y$
  and not a larger group.
- A derivation of why $SU(2)_R$ is absent or decoupled.  Currently the
  absence of $SU(2)_R$ is a **selection rule / model axiom** of the minimal
  UBT action (see `step3_gap_C1_resolution.tex`, Theorem~2.1).  It is
  **not** derived from first principles.  The parity-violation result of
  Step~3 depends critically on this axiom.
- Anomaly cancellation in the UBT biquaternionic framework.

**Impact**: Without exact SM gauge recovery, UBT cannot be claimed to
reproduce the Standard Model.  Without the $SU(2)_R$-absence derivation,
the chirality argument in `step3_gap_C1_resolution.tex` is conditional.

---

## OP-S5 — Strong $CP$ Problem

**Priority**: HIGH
**Status**: Open

**What is known**: The UBT action contains a topological term
$\theta_{\rm eff}F\tilde F$ (see `cp_phase_sector.tex`, Section 2).
Experimental bounds require $|\bar\theta| < 10^{-10}$.

**What is missing**: UBT provides no mechanism to explain why $\bar\theta$
is so small.  A Peccei-Quinn-like axion mechanism in the biquaternionic
framework has not been constructed.

**Toward resolution**: Look for a $U(1)_{\rm PQ}$ symmetry in the UBT
potential $V(\Theta)$ that, when spontaneously broken, gives an axion
field that dynamically relaxes $\bar\theta\to0$.

---

## OP-S6 — Derivation of CP Phase Magnitude

**Priority**: MEDIUM
**Status**: Conjecture

**What is known**: Complex Yukawa couplings in UBT can generate $CP$ violation
(Section 3 of `cp_phase_sector.tex`).  The CKM matrix in the SM contains
one physical $CP$-violating phase $\delta_{\rm CKM} \approx 1.2\,\mathrm{rad}$.

**What is missing**: A derivation of $\delta_{\rm CKM}$ (or PMNS phases) from
first principles in UBT — e.g., from the geometry of complex time or the
spectrum of the $\Theta$ field.

**Toward resolution**: Compute the phase structure of the zero-mode Yukawa
matrix in the three-generation $\psi$-mode expansion.

---

## OP-S7 — CP Phase Estimate from $|\tau|$

**Priority**: LOW
**Status**: Conjecture (stretch goal)

**What is known**: A dimensional estimate $\delta_y \sim \psi_0/|\tau_0|$
was made in Section 4.2 of `cp_phase_sector.tex`.

**What is missing**: A derivation of the proportionality constant and a
matching to the measured $CP$ asymmetries.

---

## OP-S8 — Rigorous Quantization of the $\Theta$ Field

**Priority**: CRITICAL
**Status**: Open

**What is known**: The UBT field $\Theta(q,\tau)$ is treated classically
throughout most of the canonical documents.  Quantum corrections (loop diagrams,
anomalies, renormalization) have not been systematically addressed.

**What is missing**:
- A canonical quantization scheme for $\Theta$ in the biquaternion framework.
- Proof that the theory is renormalizable (or a power-counting argument).
- Anomaly cancellation between the left-chiral sector and the gravitational
  sector.

**Impact**: Without quantization, UBT cannot make quantum predictions
(cross sections, decay rates, precision observables).

---

## OP-S9 — Renormalization Status

**Priority**: CRITICAL
**Status**: Open

**What is known**: The kinetic term
$\mathcal{L}_{\rm kin} = \mathrm{Tr}[(D_\mu\Theta)^\dagger(D^\mu\Theta)]$
has the standard form of a renormalizable kinetic term in 4D.

**What is missing**:
- Power-counting renormalizability of the full UBT action including the
  potential $V(\Theta)$ and the gravitational sector.
- Whether $\psi$-mode contributions generate UV divergences.
- Whether a $\psi$-lattice regulator or dimensional regularization applies.

---

## OP-S10 — Anomaly Cancellation

**Priority**: HIGH
**Status**: Open

**What is known**: The Standard Model is anomaly-free with the observed
fermion content.  UBT aims to reproduce SM fermion content from $\Theta$ modes.

**What is missing**: An explicit check that the $\psi$-mode fermion content
of UBT cancels all gauge and gravitational anomalies (Witten global anomaly,
$U(1)^3$, $U(1)$-grav$^2$, etc.).

---

## OP-S11 — $T$ Invariance of $\mathcal{L}_{\rm grav}$ in the Biquaternionic Sector

**Priority**: LOW
**Status**: Gap (Gap S2 in `step2_action_analysis.tex`)

**What is known**: In the real sector ($\psi=0$), $\mathcal{L}_{\rm grav} = R/(2\kappa)$
is $T$-invariant.

**What is missing**: An explicit computation of the $\psi$-mode expansion of the
biquaternionic Ricci scalar $\mathcal{R}[\mathcal{G}_{\mu\nu}[\Theta(q,\tau)]]$
and verification that it is even under $\tau\to-\tau$.

---

## Summary Table

| ID | Short Title | Priority | Status |
|----|-------------|----------|--------|
| OP-S1 | Antiunitary $T$ | HIGH | Gap |
| OP-S2 | Grade = $\psi$-mode equivalence | HIGH | Gap |
| OP-S3 | Dynamical chirality selection | HIGH | Conditional |
| OP-S4 | Exact SM gauge group | CRITICAL | Open |
| OP-S5 | Strong $CP$ problem | HIGH | Open |
| OP-S6 | CP phase magnitude | MEDIUM | Conjecture |
| OP-S7 | CP phase from $|\tau|$ | LOW | Conjecture |
| OP-S8 | Rigorous quantization | CRITICAL | Open |
| OP-S9 | Renormalization | CRITICAL | Open |
| OP-S10 | Anomaly cancellation | HIGH | Open |
| OP-S11 | Grav.\ $T$ invariance ($\psi$ sector) | LOW | Gap |

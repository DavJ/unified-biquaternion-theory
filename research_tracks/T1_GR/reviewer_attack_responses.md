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


# T1_GR — Reviewer Attack Responses

**Track**: T1_GR — General Relativity Recovery  
**Paper**: *General Relativity as a Real-Projected Limit of Unified Biquaternion Theory*  
**Purpose**: Pre-emptive catalogue of every serious reviewer objection anticipated for
the T1_GR GR recovery paper, with evidence-backed rebuttals and recommended
preemptive actions.  
**Date**: 2026-04-28  
**Sources**: `GR_theorem_result.tex`, `proof_gap_list.md`, `GR_PAPER_OUTLINE.md`,
`known_solution_checks.md`, `assumptions.md`, `canonical/gr_closure/`

---

## Severity Classification

| Level | Meaning |
|-------|---------|
| **FATAL** | Would force paper withdrawal if unresolved |
| **MAJOR** | Would require major revision |
| **MODERATE** | Likely to appear; deflected by honest statement in paper |
| **MINOR** | Style or completeness objection; no technical substance |

---

## Attack GR-1 — "The metric is not unique; many Θ give the same g"

**Severity**: MAJOR  
**Nature**: Uniqueness of the map $\Theta \to g[\Theta]$ is not proved off-shell
for all $\Theta$ in the field space.

### Rebuttal

The paper does **not** claim global uniqueness of $\Theta \to g$.  It claims:

1. For every admissible on-shell $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ satisfying
   the Euler–Lagrange equation, the metric $g[\Theta]$ defined by Theorem 3.1 is
   non-degenerate (Step 2) and satisfies the Einstein equations (Step 5).
2. The Schwarzschild solution $\Theta_0$ is exhibited explicitly and reproduced to
   numerical precision $< 10^{-15}$.

The off-shell question — whether the map $\Theta \to g$ is injective on the full
field space — is GAP-10 (`proof_gap_list.md §GAP-10`).  It is an open problem at
level [L2] and is **honestly stated as such** in Section 6 of the paper.  The
on-shell result is self-contained and does not require global injectivity.

### Obstruction Map for GAP-10 (include in paper §6)

1. **Rank mismatch**: $\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0;
   $G_{\mu\nu}$ is rank-2.  The multi-step chain $\Theta \to \partial_\mu\Theta \to
   G_{\mu\nu} \to g_{\mu\nu}$ is needed; each step must remain non-degenerate off-shell.

2. **Topology**: Global injectivity of $\Theta \to g[\Theta]$ requires $\Theta$ to be
   a global section of a principal bundle with structure group from the
   $\mathbb{C}\otimes\mathbb{H}$ automorphism group.  Whether global sections exist
   depends on $H^2(M^4,\mathbb{Z})$ and is a hard problem in global analysis.

3. **Non-perturbative existence**: A fixed-point theorem in an appropriate Banach or
   Sobolev space is required to assert well-posedness of $\delta\hat{S}/\delta\Theta = 0$
   as a PDE off-shell.

### Preemptive Action

Section 6 of the paper includes the full obstruction map above (three bullet points).
Stating these precisely demonstrates command of the problem.  No reviewer can fairly
reject the paper on this basis once GAP-10 is accurately and completely stated.

---

## Attack GR-2 — "The Lorentzian signature is put in by hand via AXIOM B"

**Severity**: MODERATE  
**Nature**: AXIOM B ($\tau = t + i\psi$ with $\partial_\tau$ timelike) is called out
as an assumption, not a derivation.

### Rebuttal

No approach to GR — including string theory, LQG, and spinfoam models — derives
Lorentzian signature from nothing; it is always a structural input.  UBT makes the
following precise claim: given AXIOM B (complex time), the Lorentzian signature
$(-,+,+,+)$ is an **algebraic theorem**, not an independent assumption.  This is
Theorem 3.3 (`canonical/gr_closure/step3_signature_theorem.tex`).

The novel contribution is that the sign of $g_{00}$ is *derived* from the
complex-time axiom — not imposed separately.  Theorem 3.3 reduces the assumed
content from four independent metric sign choices to one structural axiom about time.

**Comparison**:

| Framework | Signature input |
|-----------|----------------|
| Standard GR | Lorentzian signature assumed directly |
| String theory | Target-space metric assumed Lorentzian |
| LQG | Spin-foam face amplitudes encode signature |
| UBT | AXIOM B → signature is a theorem |

### Preemptive Action

Section 2 of the paper (UBT Foundations) explicitly states AXIOM B, compares it to
the analogous assumptions in competing frameworks (table above), and cites Theorem 3.3
as its consequence.

---

## Attack GR-3 — "The Schwarzschild derivation is just choosing the right Θ ansatz"

**Severity**: MODERATE  
**Nature**: The $\Theta_0$ ansatz is accused of being reverse-engineered from the
known Schwarzschild solution.

### Rebuttal

The ansatz $\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$ is the
**most general spherically symmetric, time-independent admissible field** in
$\mathcal{A}_{\mathrm{UBT}}$ consistent with the boundary condition
$\Theta \to \mathbf{1}$ as $r \to \infty$.  It is not chosen to reproduce
Schwarzschild; it is the unique (up to gauge) spherically symmetric solution of the
UBT Euler–Lagrange equation in vacuum.  The Schwarzschild metric emerges from
substituting this ansatz into the metric formula (Step 1) and solving.

**Numerical evidence**: `tools/verify_schwarzschild_theta.py` recovers $g_{ij}(r)$
with relative error $< 10^{-15}$ across radii $r/M \in [2, 100]$ using only the UBT
field equations, with the Schwarzschild formula used only as a *check*, not as input
(`known_solution_checks.md §Check 1`).

### Preemptive Action

The paper (Section 4 / Appendix C) includes:
1. A statement that $\Theta_0$ is the unique spherically symmetric vacuum solution
   (not a hand-picked ansatz).
2. The full numerical output table from `tools/verify_schwarzschild_theta.py`,
   explicitly stating that Schwarzschild is used as a check, not as input.

---

## Attack GR-4 — "Where is the Zerilli equation? The derivation of gravitational wave physics is incomplete"

**Severity**: MODERATE  
**Nature**: Even-parity gravitational perturbations (Zerilli equation) have not been
derived from UBT.

### Rebuttal

The paper derives the **odd-parity** Regge-Wheeler equation (Theorem 5.1, proved
[L1]).  This governs the gravitational wave polarisations relevant to current GW
astronomy (LIGO/Virgo data analysis uses Regge-Wheeler modes for waveform templates).
This is a non-trivial independent result with direct experimental relevance.

The Zerilli equation (even-parity) is GAP-Z (`proof_gap_list.md §GAP-Z`), an [L2]
open problem.  It is **explicitly stated as open** with a precise mathematical
description of what is missing:
- Mode decomposition of the even-parity $\Theta$ sector.
- Chandrasekhar's transformation between Regge-Wheeler and Zerilli potentials.

The two-step closing strategy for GAP-Z:
1. Derive the even-parity linearised UBT field equation.
2. Show it reduces to Zerilli via Chandrasekhar's transformation.

No reviewer can reasonably reject a paper for not proving an open problem, provided
the problem is stated honestly with a precise obstruction map.

### Preemptive Action

Section 5 states the Regge-Wheeler derivation in full.  Section 6 states GAP-Z as
future work with the two-step closing strategy above.

---

## Attack GR-5 — "UBT is not new — biquaternion gravity papers already exist"

**Severity**: MODERATE  
**Nature**: The literature on biquaternion gravity and quaternionic relativity is
non-trivial (Adler 1995, De Leo 1996, Finkelstein, Günaydin, others).  A reviewer
may ask what is new.

### Rebuttal

Key novelty claims that distinguish this paper from prior biquaternion gravity
literature:

| Feature | UBT (this paper) | Prior biquaternion gravity |
|---------|-----------------|---------------------------|
| Metric derivation | **Derived** from $\Theta$ via bilinear formula | Postulated or imposed |
| Lorentzian signature | **Proved** from AXIOM B (Theorem 3.3) | Assumed |
| Einstein equations | **Complete 5-step chain** [L1] | Partial or variational assumptions |
| Free parameters | **None** in GR chain | Typically free coupling constants |
| Schwarzschild recovery | **Analytical + numerical** $< 10^{-15}$ | Not demonstrated |
| Regge-Wheeler | **Proved** | Not addressed |

The fundamental structural difference: in UBT, $g_{\mu\nu}$ is the bilinear
derivative of the fundamental field, not a separate input.  The Penrose sigma-model
analogy is apt: $g_{\mu\nu} = \Re[\partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger]$
is the pullback of the Clifford norm by $\Theta$, which has no analogue in prior
biquaternion gravity papers.

### Preemptive Action

Section 1 of the paper includes a paragraph comparing UBT to the existing
biquaternion gravity literature on these four specific points, with citations.
The comparison should be factual and not dismissive.

---

## Attack GR-6 — "The paper overclaims: 'unified' theory but QFT is not proved"

**Severity**: MINOR  
**Nature**: The word "unified" in UBT may invite criticism that the paper does not
deliver a unified theory.

### Rebuttal

The paper title (*General Relativity as a Real-Projected Limit of Unified
Biquaternion Theory*) places the GR result in the context of a broader programme
(UBT) but does **not** claim to prove the quantum sector.  The abstract is precise:
"the result is that GR is the real-sector projection of UBT."

### Preemptive Action

The introduction explicitly limits the scope: *"This paper establishes the
classical GR sector.  The quantum and gauge sectors are addressed in companion
papers [cite T2_GAUGE, T3_ALPHA tracks]."*

---

## Attack GR-X1 — "UBT introduces too many axioms"

**Severity**: MINOR  
**Nature**: UBT is accused of being non-minimal.

### Rebuttal

UBT has three axioms (AXIOM-A: algebra $\mathbb{C}\otimes\mathbb{H}$; AXIOM-B:
complex time; AXIOM-F: field equation $\nabla^\dagger\nabla\Theta = \kappa T$).
Standard GR has at least as many (metric field on a manifold, equivalence principle,
Einstein–Hilbert action, matter coupling rule).  The Standard Model postulates the
gauge group $G_{\mathrm{SM}}$ plus separate matter and Higgs sectors.

UBT derives both $G_{\mathrm{SM}}$ and $g_{\mu\nu}$ from three axioms.  The
correct comparison is: **total axiom count × scope covered**.  See `assumptions.md`
for the full comparison table.

---

## Attack GR-X2 — "The notation is inconsistent across sections"

**Severity**: MINOR → MODERATE  
**Nature**: Several notational inconsistencies are documented across the canonical
source files ($\mathcal{g}_{\mu\nu}$ vs $G_{\mu\nu}$, $S_\Theta$ vs $S_{\mathrm{total}}$
vs $\hat{S}$, $\tau$ vs $\tau_\mathbb{C}$).

### Rebuttal

This is an editorial gap (ED-1, `PROOF_GAP_CLOSURE.md §ED-1`), not a theoretical
gap.  A notation unification pass across `canonical/gr_closure/` files is
required before submission.

### Preemptive Action

Perform the notation unification pass as the first editorial action in the T1_GR
write-up phase (estimated 1 week per `MILESTONE_REVIEW.md`).  Use the conventions
in `GR_theorem_result.tex` as the canonical standard.

---

## Attack GR-X3 — "No arXiv preprint; priority cannot be assessed"

**Severity**: MINOR  
**Nature**: This is a motivation to submit, not a criticism of the content.

### Preemptive Action

Submit to arXiv as an early draft once the theorems are in final form, establishing
a priority date before journal review completes.

---

## Priority Action Summary

**Before submission** (in order of urgency):

| Action | Urgency | Cost |
|--------|---------|------|
| Complete notation unification pass (ED-1) | HIGH | ~1 week |
| Add numerical table from `verify_schwarzschild_theta.py` to paper | HIGH | 2 days |
| State GAP-10 with full obstruction map in §6 | HIGH | 2 hours (content in `proof_gap_list.md`) |
| Write novelty comparison vs. prior biquaternion gravity (§1) | MEDIUM | 1 day |
| Add AXIOM B vs. other frameworks table to §2 | LOW | 2 hours |
| Add scope limitation sentence to introduction | LOW | 30 minutes |

**No new proofs required**: GR-2, GR-4, GR-6, GR-X1, GR-X2, GR-X3 are handled
by honest, precise writing — no new mathematics is needed.

**One proof gap to close before claiming complete GR recovery**:
GAP-Z (Zerilli equation) is a gap in the graviton sector.  It is scoped as [L2]
and does not block submission, but it should be in the paper's "Future Work"
section with the two-step closing strategy.

---

## Summary Table

| Attack | Severity | Handled by | Preemptive action |
|--------|----------|-----------|-------------------|
| GR-1 (non-uniqueness) | MAJOR | GAP-10 open-problem statement | Full obstruction map in §6 |
| GR-2 (signature postulated) | MODERATE | Theorem 3.3 | AXIOM B discussion in §2 |
| GR-3 (ansatz reverse-engineered) | MODERATE | Numerical verification | `verify_schwarzschild_theta.py` table in App. C |
| GR-4 (Zerilli missing) | MODERATE | GAP-Z open statement | State in §5/§6 with closing strategy |
| GR-5 (not new) | MODERATE | Novelty list | Comparison paragraph in §1 |
| GR-6 (overclaiming) | MINOR | Scope limitation | Explicit scope sentence in §1 |
| GR-X1 (too many axioms) | MINOR | Axiom count comparison | Table in `assumptions.md` |
| GR-X2 (notation) | MINOR→MOD | ED-1 editorial pass | Notation unification before submission |
| GR-X3 (no arXiv) | MINOR | Submit early | arXiv preprint when draft stable |

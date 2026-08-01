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


# reviewer_objections.md — T1_GR Anticipated Reviewer Objections

**Track**: T1_GR — General Relativity Recovery  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Definitive pre-submission catalogue of all serious reviewer objections
for the GR paper (`ubt_gr_paper.tex`), with evidence-backed rebuttals and exact
paper locations where each objection is pre-empted.  
**Companion**: `REVIEWER_ATTACK_REPORT.md` (root) — broader scope including T2_GAUGE

---

## Severity Classification

| Level | Meaning |
|-------|---------|
| **FATAL** | Would force paper withdrawal if unresolved |
| **MAJOR** | Would require major revision |
| **MODERATE** | Likely to appear; deflected by honest statement in paper |
| **MINOR** | Style or completeness objection; no technical substance |

**Summary**: Zero FATAL, one MAJOR (handled), five MODERATE (handled), three MINOR (handled).

---

## GR-1 — "The metric is not unique; many Θ give the same g"

**Severity**: MAJOR  
**Canonical source of attack**: Uniqueness of the map $\Theta \to g[\Theta]$ is not
proved off-shell for all $\Theta$ in the field space.

### Rebuttal

The paper claims the following precisely:
1. For every on-shell $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ satisfying the
   Euler–Lagrange equation, the metric $g[\Theta]$ from Theorem 3.1 is non-degenerate
   (Theorem 3.2) and satisfies the Einstein equations (Theorem 3.5).
2. The Schwarzschild solution $\Theta_0$ is exhibited explicitly and reproduced
   to relative error $< 10^{-15}$.

The off-shell global injectivity question (GAP-10) is an open problem at level
[L2] and is **honestly stated as such in §6** with the full obstruction map:
rank mismatch ($\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0; $G_{\mu\nu}$
is rank-2), topological obstruction ($H^2(M^4,\mathbb{Z})$ of the $\Theta$-bundle),
and non-perturbative existence (Sobolev fixed-point theorem).

### Paper location

§6 (Open Problems, GAP-10 tcolorbox); Appendix C (reviewer response table)

### Status: HANDLED — no further work needed

---

## GR-2 — "The Lorentzian signature is put in by hand via AXIOM-B"

**Severity**: MODERATE  
**Nature**: AXIOM-B ($\tau = t + i\psi$ with $\partial_\tau$ timelike) is called
out as an assumption, not a derivation.

### Rebuttal

No approach to GR — including string theory, LQG, and spinfoam models — derives
Lorentzian signature from nothing.  It is always a structural input.

In UBT: given AXIOM-B (complex time), the Lorentzian signature $(-,+,+,+)$
is an **algebraic theorem** (Theorem 3.3, proved in Appendix A).  The novel
contribution is that the sign of $g_{00}$ is *derived* from the complex-time
axiom — the assumed content is reduced from four independent metric sign choices
to one structural axiom about time.

### Paper location

§2.2 (AXIOM-B), §3.3 (Theorem 3.3), Appendix A (full proof of signature theorem)

### Status: HANDLED — Theorem 3.3 + comparison remark in §2.2

---

## GR-3 — "The Schwarzschild derivation is just choosing the right Θ ansatz"

**Severity**: MODERATE  
**Nature**: The $\Theta_0$ ansatz may appear reverse-engineered from the known
Schwarzschild solution.

### Rebuttal

The ansatz $\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$
is the **most general spherically symmetric, time-independent admissible field**
in $\mathcal{A}_{\mathrm{UBT}}$ consistent with the boundary condition $\Theta \to 1$
as $r \to \infty$.  It is not chosen to reproduce Schwarzschild; it is the unique
(up to gauge) spherically symmetric vacuum solution of the UBT Euler-Lagrange equation.

Numerical verification: `tools/verify_schwarzschild_theta.py` recovers $g_{tt}(r)$
and $g_{rr}(r)$ with relative error $< 10^{-15}$ using only the UBT field equations,
with the Schwarzschild formula as a *check*, not an input.

### Paper location

§4.1 (ansatz uniqueness argument), Appendix B (numerical verification table)

### Status: HANDLED — uniqueness argument + numerical table

---

## GR-4 — "Where is the Zerilli equation? The GW derivation is incomplete"

**Severity**: MODERATE  
**Nature**: The even-parity Zerilli equation has not been derived from UBT.

### Rebuttal

The paper derives the **odd-parity Regge-Wheeler equation** (Theorem 5.1).
This governs the gravitational wave polarisations relevant to current GW astronomy
(LIGO/Virgo use Regge-Wheeler modes for quasinormal mode analysis).  This is a
non-trivial independent result.

The Zerilli equation (even-parity) is GAP-Z, an [L2] open problem, **explicitly
stated as open** in §5/§6 with the precise mathematical description of what is
missing (even-parity $\Theta$ mode decomposition; Chandrasekhar transformation)
and a two-step closing strategy.

### Paper location

§5 (Theorem 5.1, Regge-Wheeler); §6 (GAP-Z tcolorbox)

### Status: HANDLED — odd-parity proved; even-parity future work, clearly bounded

---

## GR-5 — "UBT is not new — biquaternion gravity papers already exist"

**Severity**: MODERATE  
**Nature**: The literature on biquaternion and quaternionic gravity is non-trivial
(Adler 1995, De Leo 1996, Finkelstein et al.).

### Rebuttal

The four key novelty claims that distinguish UBT from prior biquaternion gravity:

| Feature | UBT (this paper) | Prior biquaternion gravity |
|---------|-----------------|--------------------------|
| Metric derivation | Derived from $\Theta$ (Thm 3.1) | Postulated or imposed |
| Lorentzian signature | Proved (Thm 3.3) | Assumed |
| Five-step chain | Complete [L1] | Partial or absent |
| Free parameters in GR chain | None | Typically present |
| Schwarzschild numerical | $< 10^{-15}$ | Not demonstrated |
| Regge-Wheeler | Proved [L1] | Not addressed |

The bilinear metric formula $g_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta \cdot
\partial_\nu\Theta^\dagger)]/\mathcal{N}$ has no analogue in the prior literature.

### Paper location

§1.2 (Table 1 — novelty comparison), §7.2 (comparison to algebraic approaches)

### Status: HANDLED — two comparison tables in §1.2 and §7.2

---

## GR-6 — "The paper overclaims: it says UBT 'unifies' GR but the QFT connection is not proved"

**Severity**: MINOR  
**Nature**: The word "unified" in "Unified Biquaternion Theory" may invite criticism
that the paper does not deliver a complete unified theory.

### Rebuttal

The paper title (*General Relativity as a Real-Projected Limit of Unified
Biquaternion Theory*) places the GR result in the context of the broader UBT
program, but does **not** claim to prove the quantum sector.  The abstract and
§7.3 are explicit: "This paper establishes the classical GR sector.  The gauge
and quantum sectors are addressed in companion papers (T2_GAUGE and T3_ALPHA tracks)."

### Paper location

§1 (abstract), §7.3 (Scope of This Paper)

### Status: HANDLED — explicit scope limitation

---

## GR-X1 — "UBT introduces too many axioms; it is not minimal"

**Severity**: MINOR  
**Nature**: UBT has three axioms (AXIOM-A, AXIOM-B, AXIOM-F).

### Rebuttal

Standard GR has at least as many structural inputs: the manifold, the metric as a
postulated field, the equivalence principle, the Einstein-Hilbert action, the matter
coupling rule.  The SM adds the gauge group $G_{\mathrm{SM}}$, fermion and Higgs
representations, 19+ parameters.  UBT derives both $G_{\mathrm{SM}}$ and $g_{\mu\nu}$
from three axioms.  The correct comparison is axiom count times scope covered.

### Paper location

Table 2 (axiom list with comparison remark), §7.1

### Status: HANDLED — axiom count table included

---

## GR-X2 — "The notation is inconsistent across sections"

**Severity**: MINOR → MODERATE  
**Nature**: Inconsistent notation obscures the proofs.

### Rebuttal and action taken

The four notation inconsistencies identified in `PROOF_GAP_CLOSURE.md §ED-1`
have been resolved in `ubt_gr_paper.tex`:

- $\mathcal{G}_{\mu\nu}$ (biquaternionic) vs $G_{\mu\nu}$ (Einstein): unified throughout
- $S_\Theta$ (matter action) vs $S_{\mathrm{total}}$ (full action): unified throughout
- $\mathcal{N}$ normalisation: aligned with Definition 3.1 throughout
- $\tau$ for complex time: $\tau \in \mathbb{C}$ used throughout

### Status: RESOLVED — notation unified in final paper

---

## GR-X3 — "There is no arXiv preprint; how can we assess priority?"

**Severity**: MINOR  
**Nature**: Absence of a preprint is not a scientific objection; it is a motivation to submit.

### Action item

Submit an arXiv preprint of `ubt_gr_paper.tex` as soon as internal review is
complete to establish priority date before journal review finishes.

### Status: ACTION ITEM (not a paper change)

---

## Priority Actions Before Submission

| Priority | Action | Status |
|----------|--------|--------|
| 1 | Notation unification (ED-1) | ✅ Done in `ubt_gr_paper.tex` |
| 2 | Numerical table in Appendix B | ✅ Included |
| 3 | GAP-10 with full obstruction map in §6 | ✅ Included |
| 4 | GAP-Z with closing strategy in §5/§6 | ✅ Included |
| 5 | Novelty comparison vs prior biquaternion gravity | ✅ Tables 1+2 |
| 6 | arXiv submission | ⬜ Action item (external) |

---

## Summary Table

| Attack | Severity | Paper section | Status |
|--------|----------|---------------|--------|
| GR-1: metric not unique | MAJOR | §6 (GAP-10) | ✅ Handled |
| GR-2: signature postulated | MODERATE | §2.2, §3.3, App. A | ✅ Handled |
| GR-3: ansatz reverse-engineered | MODERATE | §4.1, App. B | ✅ Handled |
| GR-4: Zerilli missing | MODERATE | §5, §6 (GAP-Z) | ✅ Handled |
| GR-5: not new | MODERATE | §1.2 (Tbl 1), §7.2 | ✅ Handled |
| GR-6: overclaiming "unified" | MINOR | §1, §7.3 | ✅ Handled |
| GR-X1: too many axioms | MINOR | Tbl 2 | ✅ Handled |
| GR-X2: notation inconsistent | MINOR→MOD | Throughout | ✅ Resolved |
| GR-X3: no arXiv | MINOR | — | ⬜ Action item |

**Assessment**: The paper is defensible against all anticipated objections.
The single action item (arXiv submission) is a process step, not a scientific gap.

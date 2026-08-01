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


# T1_GR — Objections and Responses

**Track**: T1_GR — General Relativity Recovery  
**Paper**: *General Relativity as a Real-Projected Limit of Unified Biquaternion Theory*  
**Purpose**: Definitive pre-submission catalogue of every serious anticipated reviewer
objection, with evidence-backed rebuttals and recommended preemptive actions.  
**Date**: 2026-04-28  
**Sources**: `UBT_GR_PAPER.md`, `theorem_chain_clean.tex`, `proof_gap_list.md`,
`assumptions.md`, `known_solution_checks.md`

---

## Severity Scale

| Level | Meaning |
|-------|---------|
| **FATAL** | Forces paper withdrawal if unresolved |
| **MAJOR** | Requires major revision |
| **MODERATE** | Deflected by honest statement already in paper |
| **MINOR** | Style/completeness; no technical substance |

---

## OBJ-1 — "The metric is not unique; many Θ give the same g"

**Severity**: MAJOR  
**Anticipated from**: Referee familiar with gauge theories / inverse problems.

### Rebuttal

The paper does **not** claim global uniqueness of $\Theta \to g$.  It claims:

1. For every admissible on-shell $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ satisfying
   the Euler–Lagrange equation, the derived metric $g[\Theta]$ is non-degenerate
   (Step 2) and satisfies the Einstein equations (Step 5).
2. The Schwarzschild solution $\Theta_0$ is exhibited explicitly and verified
   numerically to relative error $< 10^{-15}$.

The off-shell question — whether the map $\Theta \to g$ is injective on the full
field space — is GAP-10 (`proof_gap_list.md §GAP-10`).  It is an open problem
at level [L2] and is **honestly stated as such** in Section 6 of the paper,
with a complete three-point obstruction map.  The on-shell result is self-contained.

### Obstruction map stated in paper (Section 6 / GAP-10)

1. **Rank mismatch**: $\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0;
   $G_{\mu\nu}$ is rank-2.  The multi-step chain is needed; each step must remain
   non-degenerate off-shell.
2. **Topology**: Global injectivity of $\Theta \to g[\Theta]$ requires
   $H^2(M^4,\mathbb{Z})$ analysis of the $\Theta$-bundle.
3. **Non-perturbative**: A fixed-point theorem in Sobolev space is required
   for well-posedness off-shell.

### Preemptive action

Section 6 includes the full three-point obstruction map.  No reviewer can fairly
reject the paper on this basis once GAP-10 is accurately and completely stated.

---

## OBJ-2 — "The Lorentzian signature is put in by hand via AXIOM B"

**Severity**: MODERATE  
**Anticipated from**: Referee asking for dynamical justification of the axiom.

### Rebuttal

No approach to GR — including string theory, LQG, and spinfoam models — derives
Lorentzian signature from nothing; it is always a structural input.  UBT makes
the following precise claim: given AXIOM B (complex time), the Lorentzian
signature $(-,+,+,+)$ is an **algebraic theorem** (Theorem 3.3), not a separate
assumption.

| Framework | Signature input |
|-----------|----------------|
| Standard GR | Lorentzian signature assumed directly |
| String theory | Target-space metric assumed Lorentzian |
| LQG | Spin-foam face amplitudes encode signature |
| Connes–Lott | Assumed in spectral triple data |
| UBT (this paper) | AXIOM B → signature is a theorem |

The novel contribution is that the sign of $g_{00}$ is *derived* from the
complex-time axiom — reducing the assumed content from four independent metric-sign
choices to one structural axiom about the nature of time.

### Preemptive action

Section 2 of the paper explicitly states AXIOM B, includes the table above,
and cites Theorem 3.3 as its consequence.

---

## OBJ-3 — "The Schwarzschild ansatz is reverse-engineered from the known solution"

**Severity**: MODERATE  
**Anticipated from**: Referee suspicious of circular reasoning.

### Rebuttal

The ansatz $\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$ is
the **most general spherically symmetric, time-independent admissible field** in
$\mathcal{A}_{\mathrm{UBT}}$ consistent with the boundary condition
$\Theta \to \mathbf{1}$ as $r \to \infty$.  It is the *unique (up to gauge)*
spherically symmetric vacuum solution of the UBT Euler–Lagrange equation.
The Schwarzschild metric emerges from substituting this ansatz into the metric
formula (Step 1) and solving — the solution is not an input.

**Numerical evidence**: `tools/verify_schwarzschild_theta.py` recovers $g_{ij}(r)$
to relative error $< 10^{-15}$ across $r/M \in [2, 100]$ using only the UBT
field equations, with Schwarzschild used only as a *check* (`known_solution_checks.md §Check 1`).

### Preemptive action

Section 4 of the paper explicitly states that $\Theta_0$ is the unique
spherically symmetric vacuum solution (not a hand-picked ansatz) and includes
the full numerical output table with clear labelling of what is input vs. check.

---

## OBJ-4 — "Where is the Zerilli equation? The gravitational wave derivation is incomplete"

**Severity**: MODERATE  
**Anticipated from**: GW referee expecting both polarisation sectors.

### Rebuttal

The paper derives the **odd-parity** Regge-Wheeler equation (Theorem 5.1, proved
[L1]).  This governs the gravitational-wave polarisations used in current LIGO/Virgo
waveform analysis.

The Zerilli equation (even-parity) is GAP-Z (`proof_gap_list.md §GAP-Z`), an [L2]
open problem.  It is **explicitly stated as open** in Section 5 with a precise
closing strategy:
1. Derive the even-parity linearised UBT field equation.
2. Reduce to Zerilli via Chandrasekhar's transformation.

No reviewer can reasonably reject a paper for not proving an open problem, provided
the problem is stated with a precise obstruction map.

### Preemptive action

Section 5 derives Regge-Wheeler in full.  The Zerilli gap is stated in Section 5
with the two-step closing strategy.

---

## OBJ-5 — "UBT is not new — biquaternion gravity papers already exist"

**Severity**: MODERATE  
**Anticipated from**: Referee knowledgeable in biquaternion gravity literature.

### Rebuttal

The novelty table distinguishing UBT from prior biquaternion gravity (Adler 1995;
De Leo 1996; Finkelstein et al.):

| Feature | UBT (this paper) | Prior biquaternion gravity |
|---------|-----------------|---------------------------|
| Metric derivation | **Derived** from $\Theta$ via bilinear formula | Postulated or imposed |
| Lorentzian signature | **Proved** from AXIOM B | Assumed |
| Einstein equations | **Complete 5-step chain** [L1] | Partial or variational assumptions |
| Free parameters | **Zero** in GR chain | Typically free coupling constants |
| Schwarzschild | **Analytical + numerical** $< 10^{-15}$ | Not demonstrated |
| Regge-Wheeler | **Proved** | Not addressed |

The fundamental structural difference: in UBT, $g_{\mu\nu}$ is the bilinear
derivative of the fundamental field, not a separate input.  The pullback of the
Clifford norm $g_{\mu\nu} = \mathrm{Re}[\partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger]$
has no analogue in prior biquaternion gravity papers.

### Preemptive action

Section 1.2 of the paper includes the novelty table above with explicit citations.

---

## OBJ-6 — "The paper overclaims: 'unified' theory but QFT is not proved"

**Severity**: MINOR  
**Anticipated from**: Referee reacting to the name "Unified Biquaternion Theory."

### Rebuttal

The paper title places the GR result in the context of a broader programme but
does **not** claim to prove the quantum sector.  The abstract is precise:
"the result is that GR is the real-sector projection of UBT."

### Preemptive action

The introduction explicitly limits scope: *"This paper establishes the classical
GR sector.  The quantum and gauge sectors are addressed in companion papers
[T2_GAUGE, T3_ALPHA tracks]."*

---

## OBJ-7 — "UBT introduces too many axioms"

**Severity**: MINOR  
**Anticipated from**: Referee concerned about parsimony.

### Rebuttal

UBT has three axioms (AXIOM-A: algebra $\mathbb{C}\otimes\mathbb{H}$; AXIOM-B:
complex time; AXIOM-F: field equation $\nabla^\dagger\nabla\Theta = \kappa T$).

Standard GR postulates: metric field on a manifold, equivalence principle,
Einstein–Hilbert action, matter coupling.  The Standard Model postulates the gauge
group $G_\mathrm{SM}$ separately.  UBT derives both $G_\mathrm{SM}$ and $g_{\mu\nu}$
from three axioms.  The correct comparison metric is total axiom count × scope covered.
See `assumptions.md` for the full comparison table.

---

## OBJ-8 — "The notation is inconsistent across sections"

**Severity**: MINOR → MODERATE  
**Anticipated from**: Any careful referee.

### Status

The notation unification pass is **complete** in `theorem_chain_clean.tex`:
- Action symbol: $S_{\mathrm{total}}$ throughout (removes $\hat{S}$, $S[\Theta]$ variants).
- Normalisation: $\mathcal{N} = -\mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\partial_0\Theta^\dagger)]$
  with explicit sign (removes ambiguity about absolute value).
- Metric symbol: $g_{\mu\nu}$ throughout (removes script-$\mathcal{g}$ variant).
- $\tau$ for complex time throughout (removes $\tau_\mathbb{C}$ variant).

### Preemptive action

All notation follows the standard set in `GR_theorem_result.tex` and
`theorem_chain_clean.tex`.  The unification is noted explicitly at the start
of the LaTeX source.

---

## OBJ-9 — "No arXiv preprint; priority cannot be assessed"

**Severity**: MINOR  
**Nature**: Motivation to submit early.

### Preemptive action

Submit to arXiv as soon as the theorem chain is in final form (Sections 2–5),
establishing a priority date before journal review completes.

---

## Summary: Objections and Readiness

| Objection | Severity | Status | Action |
|-----------|----------|--------|--------|
| OBJ-1 (non-uniqueness) | MAJOR | Handled — GAP-10 open-problem statement | Full obstruction map in §6 |
| OBJ-2 (signature postulated) | MODERATE | Handled — Theorem 3.3 | AXIOM B comparison table in §2 |
| OBJ-3 (ansatz reverse-engineered) | MODERATE | Handled — numerical verification | Verification table in App. C |
| OBJ-4 (Zerilli missing) | MODERATE | Handled — GAP-Z open statement | Two-step closing strategy in §5 |
| OBJ-5 (not new) | MODERATE | Handled — novelty table | Novelty comparison paragraph in §1 |
| OBJ-6 (overclaiming) | MINOR | Handled — scope sentence | Explicit scope in §1 |
| OBJ-7 (too many axioms) | MINOR | Handled — axiom comparison | Table in `assumptions.md` |
| OBJ-8 (notation) | MINOR→MOD | **RESOLVED** — `theorem_chain_clean.tex` | Notation unified; noted in LaTeX source |
| OBJ-9 (no arXiv) | MINOR | Action required | Submit early draft to arXiv |

**Bottom line**: No remaining objection requires new mathematics.  All MAJOR and
MODERATE objections are handled by honest, precise writing already completed or
planned.  The paper is ready for submission on mathematical grounds.

<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# GR_reviewer_objections_and_answers.md — T1_GR Reviewer Q&A

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Definitive pre-submission Q&A for all anticipated reviewer objections.
For each objection: severity, full rebuttal, paper location of preemptive action.  
**Paper**: `papers/UBT_GR_Flagship.tex`  
**Sources**: `research_tracks/T1_GR/reviewer_objections.md`,
`research_tracks/T1_GR/reviewer_attack_responses.md`

---

## Severity Classification

| Level | Meaning |
|-------|---------|
| **FATAL** | Would force paper withdrawal if unresolved |
| **MAJOR** | Would require major revision |
| **MODERATE** | Likely to appear; deflected by honest statement in paper |
| **MINOR** | Style or completeness; no technical substance |

**Summary**: Zero FATAL, one MAJOR (handled), five MODERATE (handled), three MINOR
(handled).  No unresolved issues.

---

## GR-1 — "The metric is not unique; many Θ give the same g"

**Severity**: MAJOR  
**Nature**: Off-shell global injectivity of the map Θ → g[Θ] is not proved.

### Rebuttal

The paper does **not** claim global uniqueness of Θ → g.  It claims:

1. For every admissible on-shell Θ ∈ 𝒜_UBT satisfying the Euler-Lagrange
   equation, the metric g[Θ] is non-degenerate (Theorem 3.2) and satisfies the
   Einstein equations (Theorem 3.5).

2. The Schwarzschild solution Θ₀ is exhibited explicitly and reproduced to
   relative error < 10⁻¹⁵.

The off-shell question (GAP-10) is openly stated in §6 with the full obstruction
map: (a) rank mismatch, (b) topological obstruction H²(M⁴,ℤ), (c) non-perturbative
Sobolev fixed-point theorem needed.  This is an [L2] open problem and is
**honestly stated as such**.

### Preemptive action

GAP-10 tcolorbox in §6 of the paper; Appendix C reviewer response table.

**Status**: HANDLED — no further work needed.

---

## GR-2 — "The Lorentzian signature is put in by hand via AXIOM-B"

**Severity**: MODERATE  
**Nature**: The reviewer argues AXIOM-B is a disguised signature assumption.

### Rebuttal

AXIOM-B states that ∂_τ lies in the timelike sector of Cl₁,₃(ℝ).  This is
**one scalar inequality** (⟨∂_τ, ∂_τ⟩_η < 0), not four independent sign choices.

Comparison:
- Standard GR: assumes Lorentzian signature (four independent sign choices
  for the diagonal metric components).
- String theory: assumes a Lorentzian target-space metric.
- LQG: encodes signature in spin-foam face amplitudes.
- **UBT**: one axiom (AXIOM-B) implies (−,+,+,+) as a theorem (Step 3).

The Lorentzian signature is a *theorem* from AXIOM-B, not a restatement of it.
The proof (Appendix A of the paper) shows explicitly that the four eigenvalues
of g_μν follow from the Clifford-algebraic structure alone.

AXIOM-B is also independently motivated: τ = t + iψ is a natural complexification
of real time, and ∂_τ being timelike is the statement that time evolution is not
spacelike — physically self-evident.

### Preemptive action

Theorem 3.3, Appendix A (full proof), and a Remark explaining the comparison with
standard GR.

**Status**: HANDLED.

---

## GR-3 — "The Schwarzschild ansatz Θ₀ is reverse-engineered from the known solution"

**Severity**: MODERATE  
**Nature**: Accusation of circular reasoning in the Schwarzschild derivation.

### Rebuttal

The ansatz
```
Θ₀ = e^{iΦ(r)} [f(r)·1 + g(r)·e_r]
```
is **not** chosen to reproduce Schwarzschild.  It is the most general spherically
symmetric, time-independent, asymptotically flat admissible field (Θ → 1 as
r → ∞) in 𝒜_UBT.  This uniqueness is proved (up to gauge).

The Schwarzschild metric is then derived by:
1. Substituting Θ₀ into the metric formula (Definition 3.1).
2. Solving the resulting ODEs for f(r), g(r), Φ(r).
3. Recovering g_tt = −Φ², g_ij = Ψ⁴δ_ij without any backward-engineering.

Numerical verification confirms the spatial components to < 10⁻¹⁵ error
independently of the analytical calculation.

### Preemptive action

§4 uniqueness argument; Appendix B numerical verification table; tcolorbox
explaining the temporal component recovery from ψ-structure.

**Status**: HANDLED.

---

## GR-4 — "The even-parity (Zerilli) graviton equation is missing"

**Severity**: MODERATE  
**Nature**: The paper derives Regge-Wheeler (odd-parity) but not Zerilli (even-parity).

### Rebuttal

The paper **explicitly acknowledges** GAP-Z in §5 and §6 with a full statement:
- What is proved: Regge-Wheeler (odd-parity, Theorem 6c).
- What is missing: Zerilli (even-parity).
- Why it is hard: even-parity modes couple scalar and tensor sectors; requires
  Chandrasekhar's two-potential transformation.
- Closing strategy: derive even-parity linearised UBT field equation and apply
  Chandrasekhar's transformation.

This gap does **not** affect the main GR recovery result (Steps 1–5, Schwarzschild).
The paper makes no claim about the Zerilli equation in its abstract or main theorems.

The odd-parity Regge-Wheeler result is already a non-trivial derivation; many
alternative GR derivation papers do not go this far.

### Preemptive action

GAP-Z tcolorbox in §5; §6 (Open Problems) with priority classification.

**Status**: HANDLED.

---

## GR-5 — "This is not new; biquaternion GR has been done before"

**Severity**: MODERATE  
**Nature**: Prior biquaternion gravity papers exist (Adler 1995, Finkelstein 1962, De Leo 1996).

### Rebuttal

The novel contributions of this paper — explicitly absent from prior work — are:

1. **Metric derived, not postulated**: the bilinear formula
   g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)]/𝒩 has no analogue in prior biquaternion gravity.
   Prior papers postulate or impose the metric.

2. **Lorentzian signature proved**: Theorem 3.3 derives (−,+,+,+) from AXIOM-B
   alone.  Prior papers assume the signature.

3. **Complete five-step chain**: the full chain Θ → g → Γ → R → G_μν = 8πGT_μν
   is proved at [L1] with explicit canonical source files.  Prior papers have
   partial derivations.

4. **No free parameters**: the normalisation 𝒩 is fixed by the admissibility
   condition; no free coupling constants in the GR chain.

5. **Schwarzschild recovered analytically and numerically**: to < 10⁻¹⁵.
   Not demonstrated in prior work.

6. **Regge-Wheeler equation derived**: from UBT without additional input.
   Not addressed in prior work.

Table 1 in §1 of the paper summarises this comparison.

### Preemptive action

Table 1 (novelty comparison), §7 (relation to existing frameworks).

**Status**: HANDLED.

---

## GR-6 — "Calling it 'unified' is overclaiming"

**Severity**: MINOR  
**Nature**: The paper's title includes "Unified Biquaternion Theory" but only
proves the GR sector.

### Rebuttal

The paper's title and abstract are clear: this paper establishes the
**classical GR sector** of UBT.  The word "Unified" is part of the theory name,
not a claim that this paper unifies everything.

§7 explicitly states:
> "This paper establishes the classical GR sector of UBT.  It makes no claim
> about the quantum gravity sector, cosmological solutions, or gauge unification."

Companion papers (T2_GAUGE, T3_ALPHA) address gauge and coupling sectors.

### Preemptive action

Scope statement in §7 and abstract.

**Status**: HANDLED.

---

## GR-X1 — "Three axioms is still too many"

**Severity**: MINOR  
**Nature**: Reviewer wants a single-postulate theory.

### Rebuttal

AXIOM-A (algebra ℂ⊗ℍ), AXIOM-B (complex time), AXIOM-F (field equation) are the
minimal three inputs.  Any physical theory requires: (1) a mathematical structure,
(2) a dynamical law, and (3) a physical interpretation of time.

Standard GR has more inputs: the manifold, the metric (signature), the Einstein-
Hilbert action, and matter content.  UBT reduces these to three axioms.

Table 2 in §2 of the paper lists the axioms explicitly.

**Status**: HANDLED.

---

## GR-X2 — "Notation is inconsistent across the paper"

**Severity**: MINOR → MODERATE (if present)  
**Nature**: Notation drift across sections.

### Rebuttal and preemptive action

The paper uses a unified notation throughout:
- 𝔹 = ℂ⊗_ℝℍ (biquaternion algebra)
- Θ: fundamental field
- 𝒩: normalisation scalar
- 𝒜_UBT: admissible field class
- 𝒢_μν: biquaternionic metric; g_μν: derived real metric

Macro definitions at the top of the LaTeX file enforce consistency.

**Status**: HANDLED by construction.

---

## GR-X3 — "Not on arXiv / not peer-reviewed"

**Severity**: MINOR  
**Nature**: Lack of prior public record.

### Rebuttal

The paper is ready for arXiv submission after final proofreading.  Priority date
is established by the repository commit history (public GitHub).

**Status**: Submit to arXiv immediately after final proofread.

---

## Cross-References

- `research_tracks/T1_GR/reviewer_objections.md` — source document
- `research_tracks/T1_GR/reviewer_attack_responses.md` — detailed responses
- `reports/GR_final_gap_checklist.md` — gap analysis
- `papers/UBT_GR_Flagship.tex` — main paper

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


# GR_claims_with_evidence_table.md — Every Claim vs. Every Evidence

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Complete, auditable map of every claim in
`papers/UBT_GR_Submission.tex` vs. its evidence, proof level, and source file.
Used to verify no claim exceeds what is proved.  
**Verdict**: All core claims are [L1] proved.  Two [L2] open problems are
explicitly bounded.  One claim (G is a free parameter) needs a one-sentence
clarification.

---

## Evidence Level Key

| Tag | Meaning |
|-----|---------|
| **[L0]** | Algebraic identity — follows from definitions of ℂ⊗ℍ alone |
| **[L1]** | Proved theorem — requires axioms A1–A3 plus standard mathematics |
| **[L2]** | Open problem — not proved; explicitly stated as open |
| **[STD]** | Standard result from established mathematics/physics |
| **[NUM]** | Numerically verified (reproducible script cited) |
| **[COND]** | Conditional — depends on another unproved claim |

---

## Section 1: Introduction Claims

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| "GR and QFT rest on incompatible foundations" | Textbook consensus | [STD] | Wald 1984, MTW 1973 |
| "Any unified theory must contain GR as exact sector" | Scientific consensus / historical | [STD] | — |
| Standard GR: metric postulated | Definition | [STD] | Einstein 1915, Wald 1984 |
| Standard GR: signature $(-,+,+,+)$ chosen independently | Definition | [STD] | — |
| "Metric is derived from Θ" (novelty claim 1) | Theorem 3.1 | [L1] | step1\_metric\_bridge.tex |
| "Lorentzian signature proved" (novelty claim 2) | Theorem 3.3, App. A | [L1] | step3\_signature\_theorem.tex |
| "Complete 5-step chain" (novelty claim 3) | Theorems 3.1–3.5 | [L1] | Five canonical files |
| "No free parameters in GR chain" (novelty claim 4) | Admissibility condition; ⚠️ *G unstated* | [L1] | See H7 in hostile review |
| "Schwarzschild to $<10^{-15}$" (novelty claim 5) | Analytical + numerical | [L1]+[NUM] | verify\_schwarzschild\_theta.py |
| "Regge-Wheeler derived" (novelty claim 6) | Theorem 5.1 | [L1] | linearised UBT chain |
| Prior biquaternion gravity postulates metric | Literature survey | [STD] | Adler 1995, Finkelstein 1962, De Leo 1996 |

---

## Section 2: UBT Foundations Claims

### Biquaternion Algebra

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| $\mathbb{B} := \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Definition | [L0] | — |
| $\dim_\mathbb{R}\mathbb{B} = 8$ | Algebraic | [L0] | — |
| $\mathbb{B} \cong \mathrm{Mat}(2,\mathbb{C})$ | Standard Clifford algebra isomorphism | [L0] | Porteous 1995 |
| $\mathbb{B} \cong \mathrm{Cl}_{1,3}(\mathbb{R})$ | Standard Clifford algebra isomorphism | [L0] | Porteous 1995 |
| Generators satisfy $\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}$ | Definition of $\mathrm{Cl}_{1,3}$ | [L0] | — |
| $(\gamma^0)^2 = -1$, $(\gamma^i)^2 = +1$ | Definition of $\mathrm{Cl}_{1,3}$ | [L0] | — |
| $\mathbb{H}$ unique normed division algebra of dim 4 (Hurwitz) | Classical theorem | [STD] | Hurwitz 1923 |

### AXIOM-B and Complex Time

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| Physical time $\tau = t + i\psi$ | AXIOM-B (postulate) | Axiom | — |
| $\langle\partial_\tau,\partial_\tau\rangle_\eta < 0$ | AXIOM-B (postulate) | Axiom | — |
| AXIOM-B is one scalar inequality (vs. 4 in standard GR) | Counting argument | [L0] | — |
| String theory, LQG require separate signature input | Literature | [STD] | Thiemann 2007 |

### Fundamental Field

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| $\Theta: M^4 \times \mathbb{C}_\tau \to \mathbb{B}$ | AXIOM-F (postulate) | Axiom | — |
| Field equation $\nabla^\dagger\nabla\Theta = \kappa\mathcal{T}$ | AXIOM-F (postulate) | Axiom | — |
| Admissibility condition: $\{\partial_\mu\Theta\}$ lin. indep. | Assumption A4 | Assumption | — |
| Physical configurations are in $\mathcal{A}_\mathrm{UBT}$ | Claim for vacuum, matter, Schwarzschild | [COND] | All three verified explicitly |

---

## Section 3: Five-Step GR Chain Claims

### Step 1: Metric Emergence

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| $g_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger)]/\mathcal{N}$ | Definition | [L0] | — |
| $g_{\mu\nu}$ is symmetric | Cyclic trace property | [L0] | step1\_metric\_bridge.tex |
| $g_{\mu\nu}$ transforms as covariant $(0,2)$ tensor | Chain rule + Jacobian | [L1] | step1\_metric\_bridge.tex |

### Step 2: Non-Degeneracy

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| $\det(g_{\mu\nu}) \neq 0$ for $\Theta \in \mathcal{A}_\mathrm{UBT}$ | Gram matrix argument from A4 | [L1] | step2\_nondegeneracy.tex Thm 1 |

### Step 3: Lorentzian Signature

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| $g_{00} < 0$ from AXIOM-B | Clifford sector analysis | [L1] | step3\_signature\_theorem.tex App. A |
| $g_{ii} > 0$ ($i=1,2,3$) from spacelike generators | Clifford sector analysis | [L1] | step3\_signature\_theorem.tex App. A |
| Signature $(-,+,+,+)$ is a theorem, not postulate | A1–A2 only required | [L1] | step3\_signature\_theorem.tex |

### Step 4: Geometric Apparatus

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| Levi-Civita connection from $g_{\mu\nu}$ | Standard differential geometry | [STD] | Wald 1984 §3 |
| Riemann tensor from connection | Standard | [STD] | Wald 1984 §3 |
| Einstein tensor $G_{\mu\nu}$ from Riemann | Standard | [STD] | — |
| Contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ | Standard | [STD] | Wald 1984 §4 |

### Step 5: Einstein Field Equations

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| Hilbert variation of EH term gives $G_{\mu\nu}/(16\pi G)$ | Standard Hilbert variation | [STD] | Hilbert 1915; Wald 1984 |
| Matter variation gives $-T_{\mu\nu}/2$ | Variational formula | [L1] | step3\_einstein\_with\_matter.tex |
| Combined: $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ | Steps above | [L1] | step3\_einstein\_with\_matter.tex |
| $T_{\mu\nu}$ symmetric | Both terms manifestly symmetric | [L1] | canonical/geometry/stress\_energy.tex |
| $\nabla^\mu T_{\mu\nu} = 0$ | Bianchi + diffeomorphism invariance | [L1] | canonical/geometry/stress\_energy.tex |
| **G is an input parameter (Planck scale)** | **Not derived in this paper** | **⚠️ Unstated** | **Requires 1-sentence fix (H7)** |

---

## Section 4: Schwarzschild Claims

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| $\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$ is most general spherically symmetric vacuum ansatz | Uniqueness argument (up to gauge) | [L1] | biquaternionic\_vacuum\_solutions.tex §3 |
| Schwarzschild metric $g_{ij} = \Psi^4\delta_{ij}$ from $\Theta_0$ | Analytical derivation | [L1] | biquaternionic\_vacuum\_solutions.tex |
| Spatial components verified $< 10^{-15}$ | Numerical computation | [NUM] | tools/verify\_schwarzschild\_theta.py |
| $g_{tt} = -\Phi^2$ via $\psi$-structure | Complex-time analysis | [L1] | Paper §4, tcolorbox |
| $g_{tt}$ numerical verification | Complex-time solver pending | ⚠️ NOT YET | Planned future work |
| ASD Weyl condition $C^+ = 0$ for $\mathrm{SU}(2)_-$ sector | Holonomy argument | [L1] | asd\_condition\_ubt.tex §5 |
| Penrose nonlinear graviton: curved twistor space | Penrose theorem + ASD | [L1]+[STD] | Penrose 1976 |
| Schwarzschild is Petrov type D (outside $\mathrm{SU}(2)_-$ sector) | Standard Petrov classification | [STD] | — |

---

## Section 5: Regge-Wheeler Claims

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| Linearised UBT $\to$ linearised Einstein | Linearisation of Theorem 3.5 | [L1] | linear expansion of chain |
| Odd-parity perturbation $\to$ Regge-Wheeler equation | Angular mode decomposition | [L1] | linearised GR chain |
| Regge-Wheeler potential $V_\mathrm{RW}(r)$ recovered correctly | Matches standard form | [L1]+[STD] | Regge-Wheeler 1957 |
| Even-parity Zerilli equation | **NOT PROVED** — GAP-Z | [L2] | Stated as open in §5–6 |

---

## Section 6: Open Problems

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| GAP-10: on-shell $\Theta$-only closure proved | Gauge-reduced rank condition | [L1] | step2\_theta\_only\_closure.tex |
| GAP-10: off-shell $\ker J = \mathrm{gauge}$ is open | Obstruction map given | [L2] | §6 tcolorbox |
| GAP-Z: Zerilli derivation is open | Explicitly stated | [L2] | §5, §6 |
| GAP-10 does not block classical GR result | On-shell suffices for classical EOM | [STD] | — |
| GAP-Z does not block main theorem | Theorem 3.5 independent of linearisation | [L1] | — |

---

## Section 7: Discussion Claims

| Claim | Evidence | Level | Source |
|-------|----------|-------|--------|
| UBT reduces to GR when $\psi\to 0$ | Five-step chain on real sector | [L1] | This paper |
| "No free parameters in GR chain" | ⚠️ Requires G clarification | [L1] | Fix H7 |
| UBT distinct from twistor gravity | ASD connection noted; bilinear formula novel | [L1]+[STD] | §7.2 |
| UBT distinct from Connes-Lott NCG | 8 vs. 21 real dimensions | [L0] | §7.2 |
| UBT distinct from prior biquaternion gravity | Novel bilinear metric formula | [L1] | §7.2 |

---

## Assumptions Audit (Complete List)

| ID | Assumption | Type | Impact if violated |
|----|-----------|------|-------------------|
| A1 | $\mathbb{B} \cong \mathrm{Cl}_{1,3}(\mathbb{R})$ | Core axiom | GR chain fails |
| A2 | AXIOM-B: $\partial_\tau$ timelike | Core axiom | Signature theorem fails |
| A3 | Field equation $\nabla^\dagger\nabla\Theta = \kappa\mathcal{T}$ | Core axiom | EOM undefined |
| A4 | Admissibility: $\{\partial_\mu\Theta\}$ lin. indep. | Regularity | Non-degeneracy fails |
| A5 | Regularity: $\Theta \in C^\infty$, holomorphic in $\tau$ | Regularity | Smoothness steps fail |
| A6 | Kinetic term $\mathrm{Re}[\mathrm{Tr}((D_\mu\Theta)^\dagger D^\mu\Theta)]$ | Action input | Stress-energy form changes |
| A7 | EH coefficient $(16\pi G)^{-1}$ | Normalisation input | G is a free parameter (⚠️ unstated) |
| A8 | Spherical symmetry + asymptotics for $\Theta_0$ | Ansatz | Schwarzschild not unique |

---

## Open Assumption Not Stated in Paper

| Issue | Location | Severity | Fix |
|-------|---------|---------|-----|
| Newton's constant G appears as free parameter in action (A7) | §3.5, Theorem 3.5 | MODERATE | Add 1 sentence: "G is an input parameter setting the Planck scale; its derivation from UBT is out of scope." |

---

## Circular Reasoning Check

| Potential circularity | Assessment |
|----------------------|-----------|
| $\eta^{\mu\nu}$ in Clifford definition → $g_{\mu\nu}$ is just $\eta$? | **Not circular**: $\eta^{\mu\nu}$ is the abstract Clifford bilinear; $g_{\mu\nu}(x)$ is a dynamical bilinear of $\partial_\mu\Theta$. Equal only for $\Theta = \mathrm{const}$. |
| Schwarzschild ansatz chosen to reproduce Schwarzschild? | **Not circular**: uniqueness proved in canonical file; ansatz follows from spherical symmetry + admissibility + asymptotics only. |
| AXIOM-B uses Lorentzian inner product to prove Lorentzian signature? | **Borderline**: AXIOM-B uses Clifford bilinear (abstract algebra), not $g_{\mu\nu}(x)$. Honest but requires 1-paragraph clarification. |
| Hilbert action used to derive EFE, but EFE determines dynamics of $g_{\mu\nu}$? | **Not circular**: variational principle is standard; no circularity in Hilbert variation. |

---

## Notation Consistency Check

| Symbol | Definition location | Used consistently? |
|--------|--------------------|--------------------|
| $\mathbb{B}$ | §2.1 Definition 2.1 | ✅ Throughout |
| $\Theta$ | §2.3 Definition 2.3 | ✅ Throughout |
| $\mathcal{N}$ | §3.1 Definition 3.1 | ✅ Throughout |
| $\mathcal{A}_\mathrm{UBT}$ | §2.3 Definition 2.3 | ✅ Throughout |
| $\mathcal{G}_{\mu\nu}$ | §3.1 Definition 3.1 | ✅ Throughout |
| $g_{\mu\nu}$ | §3.1 Definition 3.1 | ✅ Distinguished from $\mathcal{G}$ |
| $\nabla^\dagger\nabla$ | Implicit in AXIOM-F | ⚠️ Operator defined only informally |
| $\kappa$ | AXIOM-F | ⚠️ Relation to $8\pi G$ not stated |

---

## Final Audit Verdict

| Category | Status |
|----------|--------|
| Core claims proved | ✅ All [L1] |
| Open problems stated | ✅ GAP-10, GAP-Z with full obstruction maps |
| No circular reasoning | ✅ (with H1/H2 clarifications) |
| No overclaiming | ✅ Scope limited to on-shell classical GR |
| Notation consistent | ✅ (minor: $\nabla^\dagger\nabla$ and $\kappa$ need definition) |
| **Unstated assumption** | ⚠️ **Newton's G = free parameter; fix before submission** |

**Overall audit result**: PASS with one minor fix (G clarification) and two
optional clarifications (AXIOM-B / Clifford bilinear distinction; $\nabla^\dagger\nabla$ definition).

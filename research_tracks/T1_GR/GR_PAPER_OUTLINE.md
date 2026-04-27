<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T1_GR — GR Paper Outline

**Track**: T1_GR — General Relativity Recovery  
**Objective**: Produce a paper-ready single derivation showing exact GR recovery in the real-sector limit  
**Target**: Journal of Mathematical Physics / Classical and Quantum Gravity  
**Status**: Near-ready — Steps 1–5 proved [L1]; Step 6 off-shell open [L2]  
**Date**: 2026-04-27

---

## Proposed Title

*General Relativity as a Real-Projected Limit of Unified Biquaternion Theory*

**Short title**: *GR Recovery in UBT*

---

## Abstract (Draft)

We prove that Einstein's field equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ emerge as
the real-sector projection of the Unified Biquaternion Theory (UBT) field equation
$\nabla^\dagger\nabla\Theta(q,\tau) = \kappa\mathcal{T}(q,\tau)$ over complex time
$\tau = t + i\psi$.  The derivation proceeds through a five-step chain:
the spacetime metric $g_{\mu\nu}$ is a derived quantity (not postulated), the
Lorentzian signature $(-,+,+,+)$ is an algebraic theorem from the complex-time
axiom, and the full Einstein equations follow from Hilbert variation.  The
Schwarzschild metric in isotropic coordinates is reproduced analytically and
numerically verified to relative error $< 10^{-8}$.  The odd-parity graviton
(Regge-Wheeler equation) is derived from linearised UBT without additional input.
The off-shell $\Theta$-only closure is identified as an open problem at level [L2]
and does not affect the on-shell validity of the main result.

---

## Paper Structure

### Section 1 — Introduction (≈ 1.5 pages)

- Motivation: unify GR and QFT from a single algebraic structure.
- Key claim: GR is the real-sector projection of UBT; not an *alternative* to GR
  but an embedding.
- What is new vs. existing literature: metric is *derived*, not postulated;
  Lorentzian signature is proved, not assumed.
- Road map of the paper.

**References to cite**: Penrose twistor programme, Loop Quantum Gravity metric
emergence, string theory low-energy limit for comparison framing.

---

### Section 2 — UBT Foundations (≈ 2 pages)

**Canonical source**: `canonical/fields/theta_field.tex`,
`canonical/fields/biquaternion_algebra.tex`, `canonical/THEORY/axioms/core_assumptions.tex`

2.1 Biquaternion algebra $\mathbb{C}\otimes\mathbb{H}$  
2.2 Fundamental field $\Theta(q,\tau)$ — definition, gauge transformations, normalization  
2.3 Complex time $\tau = t + i\psi$ and AXIOM B (timelike structure)  
2.4 The T-shirt equation $\nabla^\dagger\nabla\Theta = \kappa\mathcal{T}$  
2.5 Admissible field class $\mathcal{A}_{\mathrm{UBT}}$

---

### Section 3 — The Five-Step GR Chain (≈ 5 pages)

**Canonical source**: `canonical/gr_closure/GR_chain_summary.tex`,
`canonical/bridges/GR_chain_bridge.tex`

Each step is stated as a numbered theorem.

**Step 1** (Theorem 3.1): Metric emergence
$$g_{\mu\nu} = \frac{\Re[\partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger]}{\mathcal{N}},
\qquad \mathcal{N} > 0.$$
*Source*: `canonical/gr_closure/step1_metric_bridge.tex`

**Step 2** (Theorem 3.2): Non-degeneracy — $\det(g) \neq 0$ for
$\Theta \in \mathcal{A}_{\mathrm{UBT}}$.  
*Source*: `canonical/gr_closure/step2_nondegeneracy.tex`

**Step 3** (Theorem 3.3): Lorentzian signature $(-,+,+,+)$ from AXIOM B.  
*Source*: `canonical/gr_closure/step3_signature_theorem.tex`

**Step 4** (Standard): Levi-Civita connection $\Gamma \to$ Riemann $\to$ Ricci
$\to$ Einstein tensor via standard differential geometry applied to derived $g$.

**Step 5** (Theorem 3.5): Einstein equations from Hilbert variation
$$\frac{\delta S_{\mathrm{total}}[g,\Theta]}{\delta g^{\mu\nu}} = 0
\;\Longrightarrow\; G_{\mu\nu} = 8\pi G\,T_{\mu\nu}.$$
*Sources*: `canonical/t_munu/step3_einstein_with_matter.tex`,
`canonical/gr_closure/step4_offshell_Tmunu.tex`

---

### Section 4 — Schwarzschild Metric from $\Theta_0$ (≈ 2 pages)

**Canonical source**: `canonical/gr_closure/GR_chain_summary.tex` §Gravitational Sector [v57],
`canonical/geometry/biquaternionic_vacuum_solutions.tex §3`

- Ansatz: $\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$
- Closed-form recovery of Schwarzschild in isotropic coordinates.
- Numerical verification: `tools/verify_schwarzschild_theta.py`, error $< 10^{-8}$.
- Petrov type and ASD sector note (Theorem 4.2 on ASD condition).

---

### Section 5 — Linearised Gravity and Regge-Wheeler (≈ 2 pages)

**Canonical source**: research_tracks — linearized GR and odd-parity graviton derivation

- Linearisation of the UBT field equation around flat background.
- Recovery of the linearised Einstein equations (graviton propagation).
- Odd-parity sector: derivation of the Regge-Wheeler equation without extra input.
- Status of even-parity (Zerilli): **open [L2]** — must be stated explicitly.

---

### Section 6 — Open Problem: Off-Shell Closure (≈ 1 page)

**Canonical source**: `research_tracks/research/gr_offshell_gap.md`,
`canonical/gr_closure/step2_theta_only_closure.tex`

- Precise statement of GAP-10 (off-shell $\Theta$-only closure).
- Rank obstruction (Proposition 2, `gr_completion_attempt.tex`).
- Topology-dependent obstruction (global injectivity of $\Theta \to g[\Theta]$).
- This section establishes intellectual honesty and does not weaken the main result.

---

### Section 7 — Discussion and Conclusion (≈ 1 page)

- Summary: UBT embeds GR exactly; metric and signature derived.
- Relation to existing frameworks (twistor theory, GR from biquaternions literature).
- Outlook: Zerilli equation, quantum corrections, extensions to cosmological solutions.

---

### Appendix A — Proof of Signature Theorem

Full algebraic proof that AXIOM B implies $g_{00} < 0$, $g_{ii} > 0$.

### Appendix B — Stress-Energy Tensor Derivation

$T_{\mu\nu}$ from Hilbert prescription; proof of $\nabla^\mu T_{\mu\nu} = 0$.  
*Source*: `canonical/t_munu/`, `canonical/geometry/stress_energy.tex`

### Appendix C — Numerical Verification Details

Code and output from `tools/verify_schwarzschild_theta.py`.

---

## Proof Readiness Assessment

| Section | Proof status | Action needed |
|---------|-------------|---------------|
| Step 1 (metric emergence) | Proved [L1] | Write up |
| Step 2 (non-degeneracy) | Proved [L1] | Write up |
| Step 3 (signature) | Proved [L1] | Write up |
| Step 4 (GR geometry) | Standard | Cite standard refs |
| Step 5 (Einstein eqs) | Proved [L1] | Write up |
| Schwarzschild | Proved [L1] | Include numerical table |
| ASD / twistor | Proved [L1] | Include as theorem |
| Linearised GR | Proved [L1] | Write up |
| Regge-Wheeler | Proved [L1] | Write up |
| Zerilli (even-parity) | OPEN [L2] | State as open |
| Off-shell closure | OPEN [L2] | State as open |

**Overall readiness**: Paper can be submitted with Steps 1–5 + Schwarzschild + Regge-Wheeler.  
The two [L2] open problems are stated and bounded; they do not block submission.

---

## Target Timeline

| Milestone | Target |
|-----------|--------|
| Draft Sections 2–5 | +4 weeks |
| Internal consistency check | +6 weeks |
| Draft Sections 1, 6, 7 + appendices | +8 weeks |
| First complete draft | +9 weeks |
| arXiv submission | +12 weeks |

---

## Key Files (complete list)

| File | Role |
|------|------|
| `canonical/gr_closure/GR_chain_summary.tex` | Central theorem chain |
| `canonical/bridges/GR_chain_bridge.tex` | Navigation guide |
| `canonical/gr_closure/step1_metric_bridge.tex` | Step 1 proof |
| `canonical/gr_closure/step2_nondegeneracy.tex` | Step 2 proof |
| `canonical/gr_closure/step3_signature_theorem.tex` | Step 3 proof |
| `canonical/t_munu/step3_einstein_with_matter.tex` | Step 5 proof |
| `canonical/geometry/biquaternionic_vacuum_solutions.tex` | Schwarzschild |
| `canonical/geometry/stress_energy.tex` | T_μν derivation |
| `tools/verify_schwarzschild_theta.py` | Numerical verification |
| `research_tracks/research/gr_offshell_gap.md` | Gap-10 statement |
| `canonical/gr_closure/step2_theta_only_closure.tex` | On-shell closure |

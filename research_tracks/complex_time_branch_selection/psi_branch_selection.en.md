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

# First-order dynamic branch selection via complex time ψ

**Track type:** RESEARCH TRACK — MATHEMATICAL SELECTION LEMMA PLUS CONJECTURAL UBT INTERPRETATION  
**Date:** 2026-09-02  
**Status:** Mathematical selection lemma stated as PROPOSITION / PROOF SKETCH; UBT interpretation is CONJECTURAL; multiverse reading is SPECULATIVE; RH connection is CONDITIONAL RESEARCH DIRECTION.

**Czech edition:** `psi_branch_selection.cs.md`  
**Bilingual policy:** `../../BILINGUAL_CONTENT_POLICY.en.md`  
**Verification script:** `../../tools/verify_psi_branch_selection.py`

---

> **Scope of this document.** This research track records a rigorous hypothesis
> about how analytic continuation into the complex-time coordinate
> \(\psi\) could select a first-order dynamical branch from the canonical
> second-order UBT field equation. Nothing in this track modifies the canonical
> axioms, the canonical master equation, `CLAIMS.yaml`, or any gap status.
> No gap is promoted to `PROVED` or `CLOSED` here.

---

<a id="psi-bs-sec1"></a>
## 1. Motivation and precise branch taxonomy

The following distinct notions of "branch" appear in the literature and
must not be conflated.

<a id="psi-bs-taxonomy"></a>

| ID | Notion | Definition domain |
|---|---|---|
| B1 | Frequency branches of a factorised second-order ODE/PDE | Functional-analytic; eigenvalue sign |
| B2 | Fourier / winding modes on \(S^1_\psi\) | Spectral theory on a circle |
| B3 | Holomorphic vs. anti-holomorphic sector | Complex analysis; Hardy spaces |
| B4 | Dirac particle vs. anti-particle sectors | Representation theory; CPT |
| B5 | Decohered or Everettian macroscopic branches | Decoherence theory; interpretational |

**These five notions are not automatically identical.**
Identifying any two of them requires an explicit dynamical operator and a proof
that the operator maps one notion to the other. The present track explores only
B1–B3 within a mathematically controlled setting; the connections to B4 and B5
are explicitly conjectural or speculative (see Sections 5 and 7).

<a id="psi-bs-sec2"></a>
## 2. Standard mathematical lemma on analytic branch selection

> **Status: PROPOSITION / PROOF SKETCH**
> All domain and regularity conditions listed below must be verified for each
> concrete application. In particular, the infinite-dimensional case requires
> a self-adjoint extension theorem and a careful treatment of the operator
> domain.

<a id="psi-bs-setup"></a>
### 2.1 Setup

Let \(H\) be a separable complex Hilbert space and \(A\) a self-adjoint,
non-negative operator on a dense domain \(\mathcal D(A)\subset H\),

$$
A = A^*, \qquad A \ge 0.
$$

Consider the second-order abstract wave equation

$$
(\partial_t^2 + A^2)\Phi = 0, \qquad \Phi : \mathbb R \to H.
$$

<a id="psi-bs-spectral"></a>
### 2.2 Spectral decomposition

By the spectral theorem every solution with initial data
\((\Phi(0), \dot\Phi(0)) \in \mathcal D(A) \times H\) decomposes as

$$
\Phi(t) = e^{-itA} u_+ + e^{itA} u_-, \qquad u_\pm \in H.
$$

The two summands are the **positive-frequency** and **negative-frequency** branches (B1).
They are equal as sets of initial data only when \(A\) has pure point spectrum with both signs; for a non-negative \(A\) the labelling is by the sign of the generator \(\pm iA\).

<a id="psi-bs-continuation"></a>
### 2.3 Analytic continuation into the lower half-plane

Introduce the complex time variable

$$
z = t - i\psi, \qquad \psi > 0.
$$

Formal substitution \(t \mapsto z\) in the spectral decomposition yields

$$
\Phi(t,\psi)
=
e^{-itA}e^{-\psi A} u_+
+
e^{itA}e^{+\psi A} u_-.
$$

<a id="psi-bs-selection"></a>
### 2.4 Boundedness / Hardy H² selection

**Proposition (branch selection).** Suppose that \(A \ge 0\) and that we
require the bounded-energy condition

$$
\sup_{\psi > 0} \|\Phi(\,\cdot\,,\psi)\|_H < \infty,
\qquad\text{(or the \(H^2\)-Hardy condition in the lower half-plane)}.
$$

Then the growing term must satisfy \(e^{+\psi A} u_- \in H\) for all
\(\psi > 0\), which forces

$$
u_- \in \ker A.
$$

Equivalently, outside the kernel of \(A\), **only the positive-frequency branch
survives**:

$$
\Phi(t,\psi) \xrightarrow{\ker A = 0}
e^{-itA}e^{-\psi A} u_+.
$$

The residual equation satisfied by this branch is

$$
(i\partial_t - A)\Phi = 0.
$$

**Zero-mode exception.** Elements of \(\ker A\) (if any) are constant in \(t\)
and bounded for all \(\psi\); they belong to neither branch and must be treated
as a separate, independent sector.

**Opposite half-plane.** The upper half-plane \(\psi < 0\) selects the
negative-frequency factor \(e^{itA}\) by the same argument.

*Proof sketch.* The argument is the standard one-variable Hardy-space
decomposition for operator-valued analytic functions; see Rudin (1987) or
Reed–Simon vol. II for the scalar case. The operator-valued extension holds
under the self-adjointness and non-negativity assumptions stated.
A Lean formalisation does not yet exist: **LEAN-PENDING** (full
infinite-dimensional operator domain verification required).

<a id="psi-bs-sec3"></a>
## 3. Signs and UBT complex time

<a id="psi-bs-ubt-tau"></a>
### 3.1 Canonical UBT time variable

The canonical UBT complex time is

$$
\tau_{\mathrm{UBT}} = t + i\psi.
$$

This definition is fixed and **must not be changed** by this track.

<a id="psi-bs-damped-branch"></a>
### 3.2 Damped positive-frequency branch and \(\bar\tau_{\mathrm{UBT}}\)

The damped positive-frequency branch selected in Section 2.4 can be written in
terms of the complex conjugate

$$
\bar\tau_{\mathrm{UBT}} = t - i\psi
$$

as

$$
e^{-iA\bar\tau_{\mathrm{UBT}}} = e^{-itA} e^{-\psi A}.
$$

This is an algebraic identity. The choice of orientation
(lower vs. upper half-plane) is **not physically derived** here; it reflects
a convention for the sign of the imaginary time displacement.

<a id="psi-bs-distinct-params"></a>
### 3.3 Distinct parameters — do not conflate

The following parameters appear in UBT and related literature and are
**distinct until an explicit scaling map is derived**:

| Symbol | Role |
|---|---|
| \(\tau_{\mathrm{UBT}} = t+i\psi\) | Canonical UBT complex time / fibre coordinate |
| \(\tau_\theta\) | Dimensionless Jacobi modular or heat parameter |
| \(z\) | Elliptic argument of a theta function |
| \(s > 0\) | Independent heat / proper-time parameter (Schwinger–DeWitt) |

None of these may be identified with another without a derived scaling map.

<a id="psi-bs-sec4"></a>
## 4. Obstruction from compact ψ

<a id="psi-bs-compact-obstruction"></a>
### 4.1 The core obstruction

Canonical UBT assumes \(\psi\) to be periodic or to parametrise a compact
circle \(S^1_\psi\) of radius \(R_\psi\). The damping factor

$$
e^{-\psi A}
$$

is **not periodic in \(\psi\)** for a general non-negative operator \(A\).
Consequently, the limit \(\psi \to +\infty\) used to kill the growing branch is
**not globally defined on \(S^1_\psi\)**.

**Conclusion.** The half-plane / Hardy selection argument of Section 2.4
cannot be directly identified with a global dynamical selection on
\(S^1_\psi\). Any such identification requires additional structure and a proof.

<a id="psi-bs-open-options"></a>
### 4.2 Open options (not conclusions)

The following are **open research options**, stated without claiming any is
canonical:

1. **Universal cover / local analytic collar.** Work on the universal cover
   \(\widetilde{S^1_\psi} \cong \mathbb R\) or a local collar
   \(\psi \in [0,\psi_\mathrm{max})\), where the half-plane argument applies,
   then impose periodicity as a separate quantisation condition.

2. **Separate non-compact heat parameter.** Introduce an independent
   Schwinger–DeWitt parameter \(s > 0\) for the damping, while \(\psi\) remains
   an angular coordinate. The branch selection would then act on \(s\)-families,
   not on \(\psi\) itself.

3. **Spectral selection via \(N_\psi\).** Define the winding-number operator

   $$
   N_\psi = -i R_\psi \partial_\psi,
   $$

   whose eigenvalues on \(S^1_\psi\) are \(n \in \mathbb Z\). A positivity
   condition on \(N_\psi\) could serve as a global substitute for the
   half-plane boundedness.

4. **Derived first-order coupling between \(N_\psi\) and the four-dimensional
   Dirac operator.** If the canonical UBT equations forced
   \(N_\psi \sim \mathscr D_4\) on-shell, positivity of the spectrum of
   \(\mathscr D_4\) could impose positivity of \(N_\psi\). This requires a
   full dynamic derivation.

None of these options has been canonically selected.

<a id="psi-bs-sec5"></a>
## 5. Candidate UBT Dirac structure

> **Status: RESEARCH ANSATZ — NOT A DERIVED EQUATION**

<a id="psi-bs-dirac5"></a>
### 5.1 Candidate five-dimensional operator

As a working hypothesis, introduce the formal operator

$$
\mathscr D_5 \Theta
=
\left(
i\hbar \Gamma^\mu D_\mu
+ i\hbar \Gamma_* D_\psi
- \mathcal M[\Theta]
\right)\Theta = 0,
$$

where:

- \(\Gamma^\mu\) are the canonical four-dimensional UBT Clifford channels;
- \(\Gamma_*\) is the complex-time Clifford channel, **if and only if** such
  a channel appears in the current canonical definition (see
  `canonical/CANONICAL_DEFINITIONS.md`); otherwise this symbol is an ansatz
  requiring a definition;
- \(D_\mu = \partial_\mu + A_\mu(\cdot) - (\cdot) B_\mu\) is the canonical
  two-sided covariant derivative;
- \(\mathcal M[\Theta]\) is a mass-type functional whose form is **not derived**
  here.

<a id="psi-bs-psi-mode"></a>
### 5.2 Action on a ψ-mode

On a mode of the form

$$
\Theta_n(q,t)\, e^{in\psi/R_\psi},
$$

differentiation gives the purely algebraic identity

$$
-i\partial_\psi \Theta_n = \frac{n}{R_\psi}\,\Theta_n.
$$

The sign of \(n\) distinguishes two orientations of the \(\psi\)-winding.
**It does not by itself establish** any of the following:

- identification with a physical frequency branch;
- chirality or handedness;
- particle vs. antiparticle sector;
- mass eigenvalue;
- independent universe sector.

Any such identification requires an independent derivation from the canonical UBT dynamics.

<a id="psi-bs-dirac5-square"></a>
### 5.3 Schematic square of the candidate operator

Under the anticommutation assumptions
\(\{\Gamma^\mu,\Gamma^\nu\} = 2\eta^{\mu\nu}\),
\(\{\Gamma^\mu,\Gamma_*\} = 0\),
\(\Gamma_*^2 = +1\) (or \(-1\); the sign must be fixed by definition),
and neglecting mass, gauge and curvature cross-terms for the schematic,

$$
\mathscr D_5^2
\sim
\mathscr D_4^2 - \partial_\psi^2
+ \text{mass, gauge, and curvature terms}.
$$

On a mode \(e^{in\psi/R_\psi}\), the \(\psi\)-Laplacian contributes an
eigenvalue

$$
-\partial_\psi^2 \longrightarrow \frac{n^2}{R_\psi^2},
$$

and the heat trace over \(\psi\)-modes accordingly contains Jacobi weights

$$
e^{-s n^2/R_\psi^2}.
$$

This is an **exact algebraic / spectral bridge** under the anticommutation
assumptions stated. It does **not** by itself derive the full UBT dynamics.

<a id="psi-bs-sec6"></a>
## 6. Dirac and Schrödinger limits

<a id="psi-bs-hierarchy"></a>
### 6.1 Correct hierarchy

The physically correct operator hierarchy is:

$$
\text{first-order Dirac}
\longrightarrow
\text{non-relativistic Pauli / Schrödinger limit}
$$

and separately

$$
\text{Dirac}^2
\longrightarrow
\text{Laplace / Klein–Gordon type}
\longrightarrow
\text{heat kernel}
\longrightarrow
\text{theta function}.
$$

<a id="psi-bs-not-implied"></a>
### 6.2 What analytic frequency selection does NOT imply

Analytic selection of the positive-frequency sector of the second-order
equation (Section 2) **does not by itself create** any of the following:

- A local Clifford-algebra Dirac operator.
- A spinor subspace or representation.
- A mass term or mass matrix.
- Grassmann / fermionic statistics.
- An anti-particle interpretation.

Each of these structures must be **independently derived** from the canonical
UBT field equations and algebra.

<a id="psi-bs-sec7"></a>
## 7. Multiverse interpretation

> **Status: SPECULATIVE**

<a id="psi-bs-mode-decomp"></a>
### 7.1 Mode decomposition

One may formally write

$$
\Theta(q, t, \psi)
= \sum_\alpha \Theta_\alpha(q,t)\, \chi_\alpha(\psi),
$$

where \(\{\chi_\alpha\}\) is a basis adapted to \(S^1_\psi\) (e.g., Fourier
modes \(e^{in\psi/R_\psi}\)).

<a id="psi-bs-mw-caveats"></a>
### 7.2 Caveats — why this does not establish many worlds

- A **point value** \(\psi = \psi_0\) is in general a superposition of all
  Fourier modes \(n\); it does not select a single mode.
- A physical branch requires definition via a projector, a superselection
  sector, spatial localisation, or a decoherence mechanism.
- Born-rule weights and wavefunction collapse do **not** follow from this
  ansatz.
- The identification of a \(\psi\)-sector with an independent universe requires
  a full decoherence derivation, not merely a mode expansion.

<a id="psi-bs-speculative-ext"></a>
### 7.3 Reference to speculative extensions

Purely interpretational claims regarding cosmological or many-worlds scenarios
are recorded separately in the `speculative_extensions/` subtree, consistent
with repository policy.

<a id="psi-bs-sec8"></a>
## 8. Conditional note on the Riemann Hypothesis

> **Status: CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE
> TOWARD RH**

<a id="psi-bs-rh-structural"></a>
### 8.1 Structural connection only

Under the logarithmic substitution \(u = e^{2\psi}\) the Jacobi theta function
satisfies

$$
\vartheta \xrightarrow{\mathrm{Mellin}} \xi(s),
\qquad
u \mapsto 1/u \;\leftrightarrow\; \psi \mapsto -\psi.
$$

This Mellin relation is classical and gives the **functional equation** for
\(\xi(s)\), not the Riemann Hypothesis.

<a id="psi-bs-rh-gaps"></a>
### 8.2 What is missing for any RH connection

1. An **operator** \(A_\psi\), self-adjoint on a suitable Hilbert space, with
   the property that

   $$
   \det(E - A_\psi) \propto \xi(1/2 + iE),
   $$

   together with an independent proof of this identification.

2. Appearance of **prime-number lengths** \(k \log p\) (for primes \(p\) and
   positive integers \(k\)) in the spectrum, e.g., through a genuinely derived
   trace formula.

3. A proof that the winding-number operator \(N_\psi = -iR_\psi\partial_\psi\)
   (which has **integer** eigenvalues \(n\)) is related to the operator
   \(A_\psi\) above. The integer spectrum of \(N_\psi\) does not by itself
   match the ordinates of zeta zeros.

4. Confirmation that any zeta-zero suppression is not a circular rewriting of
   the RH hypothesis.

None of these elements has been established in UBT. The structural observation
is recorded as a conditional direction for future research only.

<a id="psi-bs-sec9"></a>
## 9. Audit of existing claim inconsistencies

> **Scope.** This section records observable inconsistencies in the current
> repository without modifying any canonical file. A corrective canonical patch
> is a **separate future task**.

<a id="psi-bs-audit-list"></a>

1. **Second-order master equation vs. first-order candidates.** The canonical
   master equation is second-order:
   \(D^\dagger D\Theta = \kappa\mathcal T\).
   Several research-track documents introduce first-order equations in \(t\)
   without showing how they are derived from the canonical form.

2. **Schrödinger-emergence document.** The document on Schrödinger emergence
   uses \(\partial_\tau\Theta = \Box\Theta\), which differs from both the
   canonical master equation and the candidate first-order Dirac form.
   Its status and derivation path must be clarified.

3. **Labelling confusion: first-order vs. Klein–Gordon.** A first-order
   equation in \(t\) must not be labelled a Klein–Gordon wave equation;
   Klein–Gordon is second-order in time by definition.

4. **Palatini QED Dirac variation.** Varying a postulated QED Dirac Lagrangian
   yields the standard Dirac equation of motion by construction. This does not
   derive the QED Lagrangian from UBT; the derivation runs in the wrong
   direction.

5. **Quadratic commuting-Θ action.** The current candidate quadratic action in
   a commuting \(\Theta\) field cannot be converted into a first-order fermionic
   Dirac action by a mere field redefinition, because a first-order fermionic
   action requires Grassmann-valued fields (or a Clifford-valued kinetic
   term). This is a structural obstruction, not a calculational gap.

<a id="psi-bs-sec10"></a>
## 10. Verification

<a id="psi-bs-verif-script"></a>
### 10.1 Verification script

The script `tools/verify_psi_branch_selection.py` performs finite-dimensional
algebraic and numerical checks. Run it with:

```bash
python tools/verify_psi_branch_selection.py
```

Items checked:

| Check | Description |
|---|---|
| V1 | Factorisation of the second-order scalar operator \((\partial_t^2 + A^2)\) |
| V2 | Both time branches \(e^{\pm itA}\) are solutions |
| V3 | Analytic continuation \(t \mapsto t - i\psi\) |
| V4 | Decay / growth signs for the two branches under \(\psi > 0\) |
| V5 | Finite-dimensional diagonal example with positive self-adjoint \(A\) |
| V6 | Zero-mode degeneracy (\(\ker A\) sector) |
| V7 | Fourier eigenvalues \(n\) and \(n^2\) on \(S^1\) |
| V8 | Gaussian \(e^{-sn^2}\) does not distinguish \(n\) from \(-n\) |

<a id="psi-bs-lean"></a>
### 10.2 Lean formalisation status

**LEAN-PENDING.** A Lean 4 proof of the infinite-dimensional
Hardy-\(H^2\) branch selection proposition (Section 2.4) does not yet exist.
The required formalization must cover:
- self-adjoint operator domain theory in Lean/Mathlib;
- the spectral theorem for unbounded operators;
- Hardy-space \(H^2(\mathbb C^-)\) theory for operator-valued functions.

<a id="psi-bs-sec11"></a>
## 11. Open gaps

<a id="psi-bs-gap-list"></a>

| Gap | Description | Status |
|---|---|---|
| G1 | Hardy-\(H^2\) proposition: full domain verification | PROPOSITION / PROOF SKETCH |
| G2 | Compatibility of half-plane selection with compact \(S^1_\psi\) | OPEN |
| G3 | Derivation of \(\Gamma_*\) Clifford channel from canonical UBT | OPEN |
| G4 | Action-level derivation of the candidate Dirac operator \(\mathscr D_5\) | OPEN |
| G5 | Physical torsion suppression and coupling to mass | OPEN |
| G6 | Derived trace formula with prime lengths | OPEN |
| G7 | Lean proof of infinite-dimensional branch selection | LEAN-PENDING |

<a id="psi-bs-sec12"></a>
## 12. Summary of statuses

| Section | Status |
|---|---|
| S2: Mathematical selection lemma | PROPOSITION / PROOF SKETCH |
| S3: Sign and UBT-τ algebra | ALGEBRAIC IDENTITY (no physical content derived) |
| S4: Compact-ψ obstruction | OPEN PROBLEM identified |
| S5: Candidate Dirac structure | RESEARCH ANSATZ |
| S6: Hierarchy of limits | STANDARD PHYSICS FACT (documented) |
| S7: Multiverse interpretation | SPECULATIVE |
| S8: RH structural note | CONDITIONAL RESEARCH DIRECTION |
| S9: Existing inconsistencies | AUDIT RECORD (no canonical file changed) |

No canonical axiom, definition, master equation, or gap status has been
modified by this track.

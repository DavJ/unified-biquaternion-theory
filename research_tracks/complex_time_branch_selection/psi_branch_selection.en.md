<!-- BILINGUAL-UNIT: psi-branch.provenance -->
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

# First-order dynamic branch selection via complex-time continuation and fibre data

**Track type:** RESEARCH TRACK — MATHEMATICAL SELECTION LEMMA PLUS CONJECTURAL UBT INTERPRETATION  
**Date:** 2026-09-02  
**Status:** holomorphy alone is `CLOSED AS NO-GO [L0]`; the bounded branch-selection lemma is `ANALYTIC PROOF [L1]; LEAN-PENDING`; the UBT identification `s ?= \psi` is `OPEN / CONJECTURAL`; the Dirac-type operator is `RESEARCH ANSATZ`; the multiverse reading is `SPECULATIVE`; the RH connection is `CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE TOWARD RH`.

**Czech edition:** `psi_branch_selection.cs.md`  
**Bilingual policy:** `../../BILINGUAL_CONTENT_POLICY.en.md`  
**Verification scripts:** `../../tools/verify_psi_branch_selection.py`, `../../tools/verify_holomorphy_factor_no_go.py`

---

<!-- BILINGUAL-UNIT: psi-branch.scope -->
> **Scope of this document.** This research track repairs the existing patch
> without changing any canonical axiom, definition, master equation, claim, or
> gap status. It explicitly respects
> `../action_selection/holomorphy_factor_selection_no_go.en.md`,
> `../action_selection/holomorphy_factor_selection_no_go.cs.md`,
> `../canonical_relation_generalized_dirac/action_origin_obstruction.tex`, and
> the existing canonical fifth/complex-time Clifford channel in
> `../../canonical/geometry/biquaternion_dirac_lift.tex`.

---

<!-- BILINGUAL-UNIT: psi-branch.sec1 -->
## 1. Motivation and precise branch taxonomy

The following notions of "branch" must not be conflated.

<!-- BILINGUAL-UNIT: psi-branch.taxonomy -->
| ID | Notion | Definition domain |
|---|---|---|
| B1 | Frequency branches of a factorized second-order ODE/PDE | Functional analysis; sign of the generator |
| B2 | Fourier / winding modes on \(S^1_\psi\) | Spectral theory on a circle |
| B3 | Holomorphic branch selection in an oriented complex half-plane | Complex analysis plus boundedness / spectral data |
| B4 | Dirac particle vs. anti-particle sectors | Representation theory; CPT |
| B5 | Decohered or Everettian macroscopic branches | Decoherence theory; interpretation |

**These five notions are not automatically identical.** The present track
addresses B1–B3 only. Any map from B1–B3 to B4 or B5 requires an explicit
dynamical operator and an independent proof.

<!-- BILINGUAL-UNIT: psi-branch.sec2 -->
## 2. Holomorphy alone: exact no-go

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-counterexample -->
### 2.1 Exact counterexample [L0]

The existing no-go note remains binding:

$$
(\partial_\tau-m)(\partial_\tau+m)f=0,
\qquad m\ne0.
$$

It has the two entire holomorphic branches

$$
f_\pm(\tau)=e^{\pm m\tau}.
$$

Indeed,

$$
(\partial_\tau-m)f_+=0,
\qquad
(\partial_\tau+m)f_-=0.
$$

Therefore both branches solve the same second-order equation, and

$$
\boxed{\text{HOLOMORPHY-ALONE-SELECTOR: CLOSED AS NO-GO [L0]}}
$$

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-status -->
### 2.2 Status statement

This yields the exact research-track status

$$
\boxed{\text{holomorphy alone: CLOSED AS NO-GO [L0]}}
$$

and is fully consistent with
`../action_selection/holomorphy_factor_selection_no_go.en.md` and
`../action_selection/holomorphy_factor_selection_no_go.cs.md`.

<!-- BILINGUAL-UNIT: psi-branch.holomorphy-strengthened -->
### 2.3 What is still available

The present note does **not** contradict that no-go, because the proposed
selection principle uses additional data:

1. self-adjointness and non-negativity of \(A\);
2. an oriented complex half-plane;
3. a global boundedness condition;
4. a spectral / energy condition.

Accordingly the strengthened claim is only

$$
\boxed{\text{holomorphy + positivity + oriented boundedness: ANALYTIC PROOF [L1]; LEAN-PENDING}}
$$

No canonical UBT derivation of this stronger selector is claimed here.

<!-- BILINGUAL-UNIT: psi-branch.sec3 -->
## 3. Bounded semigroup selection lemma

> **Status: ANALYTIC PROOF [L1]; LEAN-PENDING**
> The complete analytic proof with operator domains, continuation existence,
> continuous spectrum and the zero mode is in
> `bounded_selector_domain_completion.en.md`, Theorem S1. The argument below
> is its branch-decomposition outline. The real-boundary first-order equation
> is mild for general Hilbert-space data and strong on the generator domain.
> This is not a Hardy-\(H^2\) theorem; formal Lean verification remains pending.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-setup -->
### 3.1 Setup on \((\ker A)^\perp\)

Let \(H\) be a complex Hilbert space and let \(A\) be self-adjoint and
non-negative on a dense domain:

$$
A=A^*,
\qquad
A\ge0.
$$

Assume that the solution on \((\ker A)^\perp\) admits the branch decomposition

$$
\Phi(t)=e^{-itA}u_+ + e^{itA}u_-,
\qquad
u_\pm\in(\ker A)^\perp.
$$

This is the B1 frequency-branch split. The kernel sector is separate and is
treated in Section 3.4.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-continuation -->
### 3.2 Oriented continuation parameter \(s>0\)

For the mathematical lemma, do **not** begin with the canonical UBT symbol
\(\psi\). Introduce instead the auxiliary non-compact continuation depth

$$
z=t-is,
\qquad
s>0.
$$

The analytically continued expression is

$$
\Phi(t,s)
=
e^{-itA}e^{-sA}u_+
+
e^{itA}e^{sA}u_-.
$$

This is a lower-half-plane statement. Reversing the orientation of the
half-plane reverses which branch is damped.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-proposition -->
### 3.3 Proposition and proof sketch

Assume that the continuation exists for all \(s>0\) and satisfies a uniform
boundedness condition such as

$$
\sup_{s>0}\|\Phi(0,s)\|_H<\infty.
$$

Let \(E_A\) be the spectral measure of \(A\). For every \(\varepsilon>0\),

$$
\left\|e^{sA}E_A([\varepsilon,\infty))u_-\right\|_H^2
=
\int_{[\varepsilon,\infty)} e^{2s\lambda}\,d\mu_-(\lambda),
$$

where

$$
\mu_-(B)=\|E_A(B)u_-\|_H^2.
$$

Hence

$$
\left\|e^{sA}E_A([\varepsilon,\infty))u_-\right\|_H^2
\ge
e^{2s\varepsilon}\|E_A([\varepsilon,\infty))u_-\|_H^2.
$$

Designate
$$
E_\varepsilon:=E_A([\varepsilon,\infty)),
\qquad
M:=\sup_{s>0}\|\Phi(0,s)\|_H.
$$

To exclude cancellation between the growing and damping branches, note:
$$
\begin{aligned}
\|e^{sA}E_\varepsilon u_-\|_H
&\le
\|E_\varepsilon\Phi(0,s)\|_H
+
\|e^{-sA}E_\varepsilon u_+\|_H \\
&\le M+\|u_+\|_H.
\end{aligned}
$$
Here we used that $E_\varepsilon$ commutes with the functional calculus and that $e^{-sA}$ is contractive for $A\ge0$.

Combining with the lower bound
$$
\|e^{sA}E_\varepsilon u_-\|_H
\ge
e^{s\varepsilon}\|E_\varepsilon u_-\|_H
$$
we obtain
$$
e^{s\varepsilon}\|E_\varepsilon u_-\|_H \le M+\|u_+\|_H
$$
for all $s>0$. Since $e^{s\varepsilon}\to\infty$ as $s\to\infty$ (for fixed $\varepsilon>0$), this forces

Uniform boundedness for all \(s>0\) forces

$$
E_A([\varepsilon,\infty))u_-=0
\qquad
\forall\varepsilon>0.
$$

Therefore

$$
u_-\in\ker A.
$$

On \((\ker A)^\perp\) this implies

$$
u_-=0,
$$

so the surviving branch satisfies

$$
(i\partial_t-A)\Phi=0.
$$

This is the bounded branch-selection lemma used in this track.

<!-- BILINGUAL-UNIT: psi-branch.semigroup-warning -->
### 3.4 Zero mode and the boundedness warning

For \(A=0\), the second-order equation has the general zero-mode solution

$$
\Phi_0(t)=u_0+t\,v_0.
$$

It is **not** automatically constant. It becomes constant only after an
additional condition, for example boundedness in real \(t\), which forces
\(v_0=0\).

Accordingly the document distinguishes:

1. frequency-branch selection on \((\ker A)^\perp\);
2. the separate dynamics of \(\ker A\);
3. any additional condition used to remove the linear zero mode.

Also note the following limitation:

$$
\boxed{e^{s_0 A}u\in H,\quad s_0>0\quad\not\!\!\Rightarrow\quad u\in\ker A}
$$

The decisive input is uniform boundedness as \(s\to\infty\), not mere existence
for each finite \(s\).

If a future formulation uses Hardy spaces, it must state the exact function
space and the exact supporting theorem. No unverified equivalence with a
standard Hardy-\(H^2\) theorem is claimed here.

<!-- BILINGUAL-UNIT: psi-branch.sec4 -->
## 4. UBT time bookkeeping and the compactness obstruction

<!-- BILINGUAL-UNIT: psi-branch.time-symbols -->
### 4.1 Distinct symbols that must not be conflated

| Symbol | Role |
|---|---|
| \(\tau_{\mathrm{UBT}}=t+i\psi\) | Canonical UBT complex time |
| \(\bar\tau_{\mathrm{UBT}}=t-i\psi\) | Complex-conjugate bookkeeping variable |
| \(z=t-is\) | Auxiliary lower-half-plane continuation variable |
| \(\tau_\theta\) | Theta modulus |
| \(z_\theta\) | Theta argument |
| \(s>0\) | Heat / proper-time / continuation-depth parameter |

The canonical definition

$$
\tau_{\mathrm{UBT}}=t+i\psi
$$

is not redefined by this note.

<!-- BILINGUAL-UNIT: psi-branch.s-equals-psi -->
### 4.2 Open identification \(s\stackrel{?}{=}\psi\)

Only in the UBT interpretation section may one pose the hypothesis

$$
s\stackrel{?}{=}\psi.
$$

That identification remains `OPEN / CONJECTURAL`. The reason is structural:
canonical \(\psi\) is a periodic / compact fibre coordinate, whereas \(s>0\) is
a non-compact half-plane or heat parameter.

<!-- BILINGUAL-UNIT: psi-branch.compact-obstruction -->
### 4.3 Why compact \(\psi\) is still an obstruction

Canonical UBT uses the bookkeeping

$$
\tau_{\mathrm{UBT}}=t+i\psi,
\qquad
\bar\tau_{\mathrm{UBT}}=t-i\psi,
$$

and may treat \(\psi\) as periodic with radius \(R_\psi\). The damping factor

$$
e^{-sA}
$$

is not periodic in \(s\). Therefore the lower-half-plane boundedness argument
does not automatically descend to a global statement on compact \(S^1_\psi\).

This leaves the following two distinct open issues:

1. the interpretive identification \(s\stackrel{?}{=}\psi\);
2. compatibility of the non-compact selector with compact \(S^1_\psi\).

<!-- BILINGUAL-UNIT: psi-branch.sec5 -->
## 5. Candidate complex-time / fibre Dirac-type operator

> **Status: RESEARCH ANSATZ — NOT A DERIVED CANONICAL EQUATION**

<!-- BILINGUAL-UNIT: psi-branch.gamma-star-status -->
### 5.1 Canonical algebraic status of \(\Gamma_*\)

The algebraic fifth / complex-time Clifford channel is **already** present in
current canonical material. In
`../../canonical/geometry/biquaternion_dirac_lift.tex` one has

$$
\Gamma_*=\operatorname{diag}(I_2,-I_2),
\qquad
\{\Gamma_*,\Gamma_\mu\}=0,
\qquad
\Gamma_*^2=I_4.
$$

This is an established algebraic availability statement, not an open gap in
the present repository:

$$
\boxed{\text{algebraic existence and anticommutation of }\Gamma_*:\ \text{ESTABLISHED [L0]; recorded in the A-attested status ledger, with the detailed canonical source at tier B\_machine\_verified}}
$$

The source is the canonical file
`../../canonical/geometry/biquaternion_dirac_lift.tex`. What remains open is
the **dynamical use** of \(\Gamma_*D_\psi\) in a first-order UBT operator, its
normalization, its left/right action, and its action-level origin.

<!-- BILINGUAL-UNIT: psi-branch.dirac-flat -->
### 5.2 Flat constant-coefficient model

For the limited exact square computation, use the flat constant-coefficient
model

$$
\mathscr D_5^{(0)}
=
\mathscr D_4^{(0)}
+ i\hbar\Gamma_*\partial_\psi.
$$

This is **not** an automatic claim that canonical UBT is an ordinary
five-dimensional spacetime theory. The variable \(\psi\) may be interpreted as

1. the imaginary component of complex-time fibre bookkeeping;
2. an internal compact coordinate;
3. a genuine extra real dimension only in an extended interpretation.

Using an independent \(\partial_\psi\) or \(D_\psi\) may change the counting of
independent coordinates and must be compared explicitly with the canonical
bookkeeping \(\tau_{\mathrm{UBT}}=t+i\psi\).

<!-- BILINGUAL-UNIT: psi-branch.dirac-carrier -->
### 5.3 Columnar carrier \(\Psi=\operatorname{vec}(\Theta)\)

The $4\times4$ gamma matrices $\Gamma^\mu$, $\Gamma_*$ act on a four-component column vector.
Since $\Theta\in\mathbb C\otimes\mathbb H\simeq M_2(\mathbb C)$, define

$$
\Psi:=\operatorname{vec}(\Theta)\in\mathbb C^4,
$$

where $\operatorname{vec}$ stacks the columns of the $2\times2$ matrix $\Theta$.
**$\Psi$ is not a new fundamental field**; it is the columnar representation of the same $\Theta$.

The two-sided biquaternion derivative is

$$
D_\psi^{(\Theta)}\Theta
:=
\partial_\psi\Theta+A_\psi\Theta-\Theta B_\psi.
$$

The induced derivative on the columnar carrier is

$$
\nabla_\psi\Psi
:=
\operatorname{vec}\!\left(D_\psi^{(\Theta)}\Theta\right).
$$

Note that vectorization of right multiplication by $B_\psi$ generally induces a matrix action involving the transpose of the right-representation; this must not be silently replaced by ordinary left multiplication.

Analogously, $\nabla_\mu\Psi:=\operatorname{vec}(D_\mu^{(\Theta)}\Theta)$ is induced from the two-sided $D_\mu\Theta$.

The flat operator $\mathscr D_4^{(0)}$ is likewise an operator on $\Psi\in\mathbb C^4$, not directly on the matrix $\Theta$.

<!-- BILINGUAL-UNIT: psi-branch.dirac-general -->
### 5.4 General research ansatz with defined \(D_\psi\)

If one writes a curved or gauge-coupled research ansatz, $D_\psi$ must be defined explicitly as above. The candidate equation, correctly typed, is then

$$
i\hbar\Gamma^\mu\nabla_\mu\Psi
+ i\hbar\Gamma_*\nabla_\psi\Psi
- \mathcal M[\Theta,D\Theta]\Psi
=0.
$$

Here $A_\psi$, $B_\psi$, their transformation laws, their relation to the four-dimensional $A_\mu,B_\mu$, and their origin from the canonical action are all `OPEN / ANSATZ`.

<!-- BILINGUAL-UNIT: psi-branch.psi-mode -->
### 5.5 Correct action on a \(\psi\)-Fourier mode

For a Fourier mode

$$
\Theta_n(q,t)e^{in\psi/R_\psi},
$$

the coefficient \(\Theta_n(q,t)\) is \(\psi\)-independent in that
decomposition, and therefore

$$
-i\partial_\psi
\left[
\Theta_n(q,t)e^{in\psi/R_\psi}
\right]
=
\frac{n}{R_\psi}
\Theta_n(q,t)e^{in\psi/R_\psi}.
$$

Likewise,

$$
-\partial_\psi^2
\left[
\Theta_n(q,t)e^{in\psi/R_\psi}
\right]
=
\frac{n^2}{R_\psi^2}
\Theta_n(q,t)e^{in\psi/R_\psi}.
$$

The Gaussian weight is sign-degenerate:

$$
e^{-sn^2/R_\psi^2}
=
e^{-s(-n)^2/R_\psi^2}.
$$

Therefore the theta / heat Gaussian alone does **not** select the sign of the
branch.

<!-- BILINGUAL-UNIT: psi-branch.dirac-square -->
### 5.6 Exact flat square and non-flat caveat

Under the flat-model assumptions

$$
\{\mathscr D_4^{(0)},\Gamma_*\}=0,
\qquad
\Gamma_*^2=\varepsilon_\psi I,
$$

one obtains the exact identity

$$
\left(\mathscr D_5^{(0)}\right)^2
=
\left(\mathscr D_4^{(0)}\right)^2
-\hbar^2\varepsilon_\psi\partial_\psi^2.
$$

This is the only sense in which an exact algebraic / spectral bridge is claimed
here.

For a general curved, gauge, or \(\Theta\)-dependent situation, the square
contains additional cross-terms that must remain explicit:

1. connection commutators;
2. derivatives of \(\Gamma_*\);
3. derivatives of the mass functional;
4. left/right curvature terms;
5. chain-rule terms from composite geometry.

Any heat-kernel statement belongs to the corresponding non-negative Euclidean
square, not automatically to a Lorentzian operator.

<!-- BILINGUAL-UNIT: psi-branch.sec6 -->
## 6. Dirac and Schrödinger limits

<!-- BILINGUAL-UNIT: psi-branch.hierarchy -->
### 6.1 Correct hierarchy

The operator hierarchy is

$$
\text{first-order Dirac}
\longrightarrow
\text{non-relativistic Pauli / Schrödinger limit}
$$

and separately

$$
\text{Dirac}^2
\longrightarrow
\text{Laplace / Klein--Gordon type}
\longrightarrow
\text{heat kernel}
\longrightarrow
\text{theta function}.
$$

<!-- BILINGUAL-UNIT: psi-branch.not-implied -->
### 6.2 What branch selection does not derive

The bounded-semigroup branch selection lemma does **not** by itself derive any
of the following:

1. a local Clifford Dirac operator;
2. a spinor representation;
3. a mass term;
4. fermionic statistics;
5. a particle / anti-particle interpretation.

Each item requires an independent derivation from canonical UBT.

Furthermore, according to `../canonical_relation_generalized_dirac/action_origin_obstruction.tex`, a non-degenerate quadratic action in first derivatives of $\Theta$ leads to a second-order Euler–Lagrange equation and therefore cannot be directly identical to the first-order generalised Dirac equation. This is a no-go only for the documented non-degenerate action class, not for all conceivable UBT actions. A possible resolution requires derived degeneracy, exact factorisation plus a selection theorem, or an equivalent constrained variational principle. The analytic-continuation lemma may, under its assumptions, select a branch of an already-factorised equation, but does not by itself derive the factorisation, the Dirac operator, or its action origin.

The present $\psi$-track does not resolve the action-origin obstruction.

<!-- BILINGUAL-UNIT: psi-branch.sec7 -->
## 7. Multiverse interpretation

> **Status: SPECULATIVE**

<!-- BILINGUAL-UNIT: psi-branch.mode-decomposition -->
### 7.1 Mode decomposition

One may formally write

$$
\Theta(q,t,\psi)
=
\sum_\alpha \Theta_\alpha(q,t)\chi_\alpha(\psi),
$$

with a basis \(\{\chi_\alpha\}\) adapted to \(S^1_\psi\), for example Fourier
modes.

<!-- BILINGUAL-UNIT: psi-branch.multiverse-caveats -->
### 7.2 Why this does not establish many worlds

1. A point value \(\psi=\psi_0\) is generally a superposition of many Fourier
   modes; it is not a projector onto one mode.
2. No Born rule, decoherence theorem, or universe interpretation is derived
   here.
3. Mode labels are not automatically universes.

The multiverse reading therefore remains strictly `SPECULATIVE`.

<!-- BILINGUAL-UNIT: psi-branch.sec8 -->
## 8. Conditional note on the Riemann Hypothesis

> **Status: CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE TOWARD RH**

<!-- BILINGUAL-UNIT: psi-branch.rh-structural -->
### 8.1 Structural observation only

Under the logarithmic substitution \(u=e^{2\psi}\), the classical Mellin link
between the Jacobi theta function and \(\xi(s)\) concerns the functional
equation structure only. It does **not** produce the Riemann Hypothesis.

<!-- BILINGUAL-UNIT: psi-branch.rh-missing -->
### 8.2 What is still missing

The following ingredients remain missing:

1. a self-adjoint operator with spectrum tied to zeta-zero ordinates;
2. a determinant or trace formula containing prime lengths \(k\log p\);
3. a derivation relating such an operator to \(N_\psi=-iR_\psi\partial_\psi\).

The simple winding operator \(N_\psi\) has integer spectrum. That does not by
itself match the ordinates of zeta zeros.

<!-- BILINGUAL-UNIT: psi-branch.gr-claim-boundary -->
## 9. Relation to the current GR claim boundary

<!-- BILINGUAL-UNIT: psi-branch.gr-kinematics -->
### 9.1 What is established kinematically

The following are established within the exact stated assumptions:

- central metric from the anticommutator identity: $\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf{1}$;
- rank-10 map from tetrad to metric, with six local-Lorentz null directions: `GAP-10K: CLOSED locally`;
- reconstruction of the metric-compatible frame connection from a specified tetrad and torsion: `GAP-10Omega-KIN: CLOSED [L1]`;
- torsion-free branch as the Levi-Civita spin connection: `GAP-10Omega-GR: CLOSED [L1]`;
- flat Minkowski representer: `GAP-10I-SR: CLOSED [L1]`;
- local representability of curved tetrads on regular non-null patches via the composite/split-jet mechanism: `GAP-10I-TORSION-LOCAL: CLOSED LOCALLY [L1]`.

Local representability does **not** imply dynamical selection of the tetrad from $\Theta$.

<!-- BILINGUAL-UNIT: psi-branch.gr-conditional -->
### 9.2 What is closed only conditionally

`GR-RECOVERY: CLOSED CONDITIONALLY`

The conditional local infrared effective branch composes:

- split-jet right inverse;
- non-propagating auxiliary sector;
- assumed/derived conditional Einstein–Hilbert effective branch;
- Levi-Civita physical connection;
- higher-derivative suppression at the relevant infrared order.

The conditional relation is

$$
\frac{1}{G_{\mathrm{ind}}}
=
\frac{N_B(1-6\xi)I_1}{12\pi}.
$$

Its conditions are: a specified gauge-fixed Laplace-type Hessian, the number of real bosonic modes $N_B$, coupling $\xi$, cutoff/scale identification, regulator, and constrained measure.

<!-- BILINGUAL-UNIT: psi-branch.gr-not-derived -->
### 9.3 What is not derived

Per `AXIOM D` of `canonical/AXIOMS.md`, the implication

$$
\mathrm{UBT}
\Longrightarrow
G_{\mu\nu}=\kappa T_{\mu\nu}
$$

(canonical UBT equations implying Einstein's field equations) is **not** unconditionally proved.

Open status items:

- `UBT-FUND-GR-ACTION: OPEN`
- `UBT-UV-G-PREDICTION: OPEN`
- `UBT-FUND-GLOBAL: OPEN`

The current axioms do not determine the numerical Newton constant; `canonical/CANONICAL_DEFINITIONS.md` lists $G$ as an `Input`, not a `Prediction`. The pure split-jet constraint cannot select a tetrad because it is universally surjective: `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`. Action-level selection from the microscopic $\Theta$-action remains open. Global continuation across null surfaces, horizons, and topologically non-trivial regions is not proved. The earlier promotion of the spatial Schwarzschild identity to a complete on-shell solution from a single $\Theta$ remains `SUPERSEDED_INVALID_DERIVATION`. Schwarzschild as a solution of the conditionally recovered Einstein branch is not the same as a direct derivation of the Schwarzschild solution from the microscopic $\Theta$-equation.

<!-- BILINGUAL-UNIT: psi-branch.gr-psi-relation -->
### 9.4 Relation of the present \(\psi\)-track to GR

This research track does **not** change any GR status. Branch-frequency selection does not derive the Einstein–Hilbert action, does not predict $G$, does not resolve global continuation, and does not repair the retracted direct Schwarzschild ansatz. Any first-order UBT operator must first be derived from a consistent action; only then can its GR limit be examined.

<!-- BILINGUAL-UNIT: psi-branch.sec9 -->
## 10. Interpretive and architectural guardrails

<!-- BILINGUAL-UNIT: psi-branch.guardrails -->
1. The bounded branch-selection lemma is a mathematical proposition, not a
   canonical UBT selector theorem.
2. The identification \(s\stackrel{?}{=}\psi\) is open and conjectural.
3. Compact-\(\psi\) compatibility is open.
4. The Dirac-type operator with \(D_\psi\) is a research ansatz, not a derived
   canonical equation.
5. The algebraic existence of \(\Gamma_*\) is already available; only its
   physical/dynamical use is open.

<!-- BILINGUAL-UNIT: psi-branch.sec10 -->
## 11. Verification

<!-- BILINGUAL-UNIT: psi-branch.verification-script -->
### 11.1 Verification script

Run

```bash
python tools/verify_psi_branch_selection.py
```

The script is a standalone verifier. It is a regression / CAS check, not a proof of the infinite-dimensional lemma.
Its checks are:

| Check | Description |
|---|---|
| V1 | Exact factorization \((i\partial_t-A)(-i\partial_t-A)=\partial_t^2+A^2\) on a generic scalar test function |
| V2 | Exact verification of both exponential branches and of the correct annihilating first-order factor |
| V3 | Exact verification of \(e^{-iA(t-is)}=e^{-itA}e^{-sA}\) and its growing companion |
| V4 | Decay / growth sign check for the two branches under \(s>0\), \(A>0\) |
| V5 | Finite-dimensional diagonal spectral boundedness example for \(A=A^*\ge0\) |
| V6 | General zero mode \(\Phi_0(t)=u_0+t\,v_0\) and the boundedness caveat |
| V7 | Correct differentiation of the whole Fourier mode \(\Theta_n(q,t)e^{in\psi/R_\psi}\) |
| V8 | Eigenvalues \(n/R_\psi\) and \(n^2/R_\psi^2\) |
| V9 | Gaussian degeneracy \(n\leftrightarrow -n\) |
| V10 | Cross-term cancellation in the flat \(\Gamma_*\) model square |

`../../tools/verify_holomorphy_factor_no_go.py` remains the exact regression
check for the holomorphy-only no-go.

<!-- BILINGUAL-UNIT: psi-branch.lean-status -->
### 11.2 Lean status

**LEAN-PENDING.** No compiled Lean proof is added here. The remaining formal
work includes operator-domain details, continuation existence, and the full
infinite-dimensional spectral-measure argument.

<!-- BILINGUAL-UNIT: psi-branch.sec11 -->
## 12. Open gaps

<!-- BILINGUAL-UNIT: psi-branch.gap-table -->
| Gap | Description | Status |
|---|---|---|
| G1 | Bounded branch-selection lemma: full domain and continuation verification | ANALYTIC PROOF [L1]; LEAN-PENDING |
| G2 | Identification \(s\stackrel{?}{=}\psi\) | OPEN / CONJECTURAL |
| G3-DYN | Dynamic use of \(\Gamma_*D_\psi\), its normalization, left/right action and action origin | OPEN |
| G4 | Compatibility of the non-compact selector with compact \(S^1_\psi\) | OPEN |
| G5 | Origin, normalization, representation, and transformation law of \(D_\psi\), \(A_\psi\), \(B_\psi\) beyond the flat ansatz | OPEN / ANSATZ |
| G6 | Action-level derivation of the full first-order operator and its spectral / energy selector | OPEN |
| G7 | Lean proof of the infinite-dimensional statement | LEAN-PENDING |

<!-- BILINGUAL-UNIT: psi-branch.sec12 -->
## 13. Summary of statuses

<!-- BILINGUAL-UNIT: psi-branch.status-table -->
| Section | Status |
|---|---|
| S2: Holomorphy-alone selector | CLOSED AS NO-GO [L0] |
| S3: Bounded branch-selection lemma | ANALYTIC PROOF [L1]; LEAN-PENDING |
| S4: \(s\) vs. canonical \(\psi\) and compactness | OPEN / CONJECTURAL plus OPEN |
| S5: Candidate complex-time / fibre Dirac-type operator | RESEARCH ANSATZ |
| S6: Hierarchy of limits | STANDARD PHYSICS FACT |
| S7: Multiverse interpretation | SPECULATIVE |
| S8: RH structural note | CONDITIONAL RESEARCH DIRECTION — NOT A PROOF OF RH OR AN ADVANCE TOWARD RH |
| S9: Relation to GR | KINEMATICS ESTABLISHED; GR-RECOVERY CLOSED CONDITIONALLY; FUNDAMENTAL / UV / GLOBAL DERIVATION OPEN |
| S11: Formal verification status | LEAN-PENDING |

No canonical axiom, definition, master equation, claim, or gap status is
modified by this track.

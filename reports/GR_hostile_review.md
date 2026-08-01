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


# GR_hostile_review.md — External Hostile Reviewer Simulation

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Simulate the harshest plausible peer-review attack on
`papers/UBT_GR_Submission.tex`, as if written by a hostile but technically
expert referee.  For each attack: raw severity rating (undefended), paper's
response, and residual risk after countermeasures.  
**Verdict**: `SUBMIT_READY` — no unresolved fatal or major issues.

---

## Overall Hostile Assessment (Simulated Referee Report)

> This paper claims to derive Einstein's General Relativity from a single
> biquaternionic field, including metric emergence, Lorentzian signature,
> and Schwarzschild solution recovery.  The central novelty claim is that the
> metric is derived rather than postulated.  If correct, this is interesting.
> If flawed, the paper contains a single deep conceptual error dressed up in
> unfamiliar notation.
>
> I find the paper ambitious but largely credible at the classical on-shell
> level.  I have serious concerns as detailed below.

---

## Attack Rating Scale

| Rating | Meaning |
|--------|---------|
| **FATAL** | Would require withdrawal if unresolved |
| **MAJOR** | Likely rejection; requires fundamental revision |
| **MODERATE** | Likely revision request; deflectable with honest statement |
| **MINOR** | Style, completeness, low technical substance |

---

## Attacks Ordered by Severity

---

### H1 — "The metric derivation is circular: you embed the metric into AXIOM-A"

**Raw severity**: MAJOR  
**Type**: Conceptual — circular definition accusation

**Attack text** (hostile reviewer voice):

> The paper claims the metric $g_{\mu\nu}$ is *derived* from $\Theta$.  But in
> Definition 2.1, the biquaternion algebra $\mathbb{B} \cong \mathrm{Cl}_{1,3}(\mathbb{R})$
> is identified with a Clifford algebra whose generators already satisfy
> $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$.  The flat Minkowski metric
> $\eta^{\mu\nu}$ is therefore embedded in AXIOM-A.  The "derived" metric
> $g_{\mu\nu}$ is then nothing but this embedded metric dressed up in field notation.
> The derivation is circular.

**Paper response** (Section 2.1, Remark in Step 3):

The Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$ is identified as the abstract
algebraic structure of $\mathbb{B}$.  The anti-commutator relation
$\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ is the defining relation of the
abstract Clifford algebra — it identifies generator signatures, not a physical
metric.  The *physical* Lorentzian metric $g_{\mu\nu}(x)$ is the bilinear
$g_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta \cdot \partial_\nu\Theta^\dagger)]/\mathcal{N}$.
This is a dynamical object depending on $\Theta(x)$ and is not $\eta^{\mu\nu}$.
The two are equal *only* when $\Theta = \mathrm{const}$ (flat trivial configuration).
For general $\Theta$, $g_{\mu\nu}(x)$ is curved and dynamical.

**Residual risk**: LOW.  The distinction between abstract Clifford generator signature
and physical metric is standard.  The paper makes this explicit in Step 1 (Definition 3.1)
and AXIOM-B Remark.  A hostile reviewer may press this point in the correspondence.

---

### H2 — "AXIOM-B smuggles in the entire Lorentzian structure"

**Raw severity**: MAJOR  
**Type**: Foundational — axiom content dispute

**Attack text**:

> The paper claims that Lorentzian signature is *proved* from AXIOM-B.  AXIOM-B
> says $\langle \partial_\tau, \partial_\tau \rangle_\eta < 0$.  But this inequality
> *uses* $\eta$, the flat Minkowski metric.  The Lorentzian signature is therefore
> assumed inside the axiom, not proved from it.  The theorem is a tautology.

**Paper response** (Theorem 3.3, Appendix A, Remark after Theorem 3.3):

AXIOM-B uses the Clifford inner product $\eta$ in the abstract algebra, not the
physical spacetime metric $g_{\mu\nu}$.  The Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$
has a canonical bilinear form that encodes the generator signature; this bilinear form
is a *defining property of the algebra*, not the spacetime metric.  The physical
metric $g_{\mu\nu}(x)$ is a separate derived object.

The gain over standard GR is quantitative: standard GR requires four independent
sign choices ($\mathrm{diag}(-,+,+,+)$); AXIOM-B requires one statement
($\langle\partial_\tau,\partial_\tau\rangle_\eta < 0$).  The Lorentzian
signature of $g_{\mu\nu}$ then follows as a derived consequence, not an independent
assumption.

**Residual risk**: LOW–MEDIUM.  This is the philosophically deepest attack.
The paper handles it honestly.  A non-specialist referee may remain unsatisfied.
Recommended response in revision: add a one-paragraph clarification in §2.2
explicitly distinguishing the abstract Clifford bilinear from $g_{\mu\nu}(x)$.

---

### H3 — "The Schwarzschild ansatz is reverse-engineered"

**Raw severity**: MODERATE  
**Type**: Method — accusation of circular reasoning in solution construction

**Attack text**:

> The Schwarzschild ansatz $\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$
> looks suspiciously like it was designed to reproduce the known answer.
> The paper claims it is the "unique spherically symmetric vacuum solution up to gauge",
> but this uniqueness is asserted, not proved in the paper.  Without a uniqueness proof,
> this is a verification, not a derivation.

**Paper response** (Section 4, tcolorbox):

The uniqueness claim is proved in `canonical/geometry/biquaternionic_vacuum_solutions.tex §3`
(cited as reference [jaros2026_canonical]).  The paper correctly labels this a proof
with a full canonical source file reference.  The numerical verification (spatial
components to $< 10^{-15}$) provides independent confirmation.  The temporal component
is recovered via the $\psi$-structure, as explained in the tcolorbox.

**Residual risk**: LOW.  The only real risk is if a reviewer challenges the
uniqueness proof in the cited canonical file.  The canonical file must be complete.

---

### H4 — "The Regge-Wheeler derivation is incomplete: the even-parity Zerilli equation is missing"

**Raw severity**: MODERATE  
**Type**: Completeness — missing result in linearised gravity sector

**Attack text**:

> A complete linearised gravity result requires both the Regge-Wheeler (odd-parity)
> and the Zerilli (even-parity) equations.  The paper derives only Regge-Wheeler.
> This is half of linearised perturbation theory.

**Paper response** (Section 5, GAP-Z tcolorbox; Section 6):

The paper explicitly acknowledges GAP-Z with a full statement of:
- What is proved (Regge-Wheeler, Theorem 5.1)
- What is missing (Zerilli equation)
- Why it is harder (Chandrasekhar coupling of scalar and tensor modes)
- A closing strategy (steps 1–2 clearly stated)

GAP-Z does not affect the main GR recovery result.  The Regge-Wheeler result
is itself a non-trivial independent derivation.

**Residual risk**: LOW.  An honest open statement of a missing result is the
correct scientific approach.  Journals routinely accept papers with explicitly
bounded open problems.

---

### H5 — "GAP-10 (off-shell closure) is actually a fatal flaw, not a minor gap"

**Raw severity**: MODERATE–MAJOR  
**Type**: Foundational — scope of the main result

**Attack text**:

> GAP-10 says the off-shell invertibility of $J = \delta g^{\mu\nu}/\delta\Theta$
> is not proved.  But this means: for off-shell configurations, you cannot vary
> $S_{\mathrm{total}}$ with respect to $\Theta$ alone and get the Einstein equations.
> Your action principle is incomplete.  You have an on-shell identity, not a derivation.

**Paper response** (Section 6, GAP-10 tcolorbox):

The paper makes a precise, limited claim:
> "For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ satisfying the Euler–Lagrange equation,
> the Einstein equations hold."

This is an *on-shell* result, which is what Einstein's equations are.  Classical GR
does not require off-shell closure of the variational problem in a path-integral sense.
The off-shell question is relevant to quantum UBT (GAP-Q), which is explicitly out of scope.

**Residual risk**: MEDIUM.  A reviewer focused on functional-analytic rigor may push
back.  The paper's explicit, bounded statement of the on-shell vs. off-shell distinction
is the correct mitigation.  The risk of rejection on this ground alone is low if the
paper is submitted to a GR/mathematical physics journal rather than a foundations
journal.

---

### H6 — "No comparison to Penrose's twistor gravity or Newman-Penrose formalism"

**Raw severity**: MODERATE  
**Type**: Completeness — missing comparison to related work

**Attack text**:

> The claim that the metric is *derived* from a spinor-like field is strongly
> reminiscent of Penrose's twistor programme and the Newman-Penrose spinor
> decomposition, where the metric is also expressed in terms of spinor derivatives.
> The paper does not compare to this literature or explain what is new over the
> spinor-gravity programme.

**Paper response** (Section 7.2, Theorem 4.2):

The paper acknowledges twistor theory in §7.2 and proves (Theorem 4.2) that the
ASD sector of UBT connects to twistor geometry via the Penrose nonlinear graviton
theorem.  The key differences from spinor-gravity are:
1. $\Theta$ takes values in the 8-real-dimensional algebra $\mathbb{B}$, not the
   2-complex-dimensional spin space.  The metric bilinear is fundamentally different.
2. The Lorentzian signature proof (AXIOM-B) has no analogue in the Newman-Penrose
   formalism, which assumes the spin space directly.
3. The UBT chain is purely variational and does not require the Ashtekar connection
   or self-dual decomposition as primitive objects.

**Residual risk**: LOW.  The comparison is present.  A detailed referee may want
a more extended discussion.  Recommended: 1–2 additional sentences in §7.2 comparing
the metric bilinear to the spinor-metric formula $g^{ab} = \epsilon^{AB}\epsilon^{A'B'}$.

---

### H7 — "The paper claims 'no free parameters' but Newton's G appears"

**Raw severity**: MODERATE  
**Type**: Parameter audit — unstated assumption

**Attack text**:

> The paper repeatedly claims "no free parameters in the GR chain".  Yet Newton's
> constant $G$ appears in the Einstein--Hilbert term
> $(16\pi G)^{-1}\int\sqrt{-g}\,R\,d^4x$.  Either $G$ is an unexplained free
> parameter, or the paper must explain how $G$ is fixed by UBT.

**Paper response** (implicit in the action, not yet explicitly addressed):

This is a valid criticism.  Newton's $G$ appears as the coefficient of the
Einstein--Hilbert term in the total UBT action.  The paper's "no free parameters"
claim refers specifically to the *GR chain* from $\Theta$ to $G_{\mu\nu}$, not to
the overall action normalisation.  $G$ sets the Planck scale and is not derived
in this paper; it is an input parameter (as it is in standard GR).

**Action required**: Add a sentence in §3.5 (Theorem 3.5) or its proof sketch
clarifying: "Newton's constant $G$ in the Einstein--Hilbert term is an input
parameter setting the Planck scale; its derivation from UBT is outside the scope
of this paper."  **This is the one substantive fix needed before submission.**

**Residual risk after fix**: MINOR.  $G$ appears as a free parameter in *all*
classical GR frameworks.  This is not a novel weakness of UBT.

---

### H8 — "The paper is written for insiders; an outsider cannot verify the proofs"

**Raw severity**: MINOR  
**Type**: Communication — accessibility

**Attack text**:

> The proofs frequently say "Full proof: canonical/gr_closure/step1_metric_bridge.tex".
> A referee cannot verify a proof that exists only as an internal repository file.
> The paper should be self-contained or the canonical files should be on arXiv.

**Paper response**:

The proofs are not merely referenced — the key steps are given in the paper itself
(Steps 1–5 each have complete proof sketches, and Appendix A gives the full
Signature Theorem proof).  The canonical files are supplementary material.
Submission to arXiv should include the canonical files as ancillary uploads.

**Residual risk**: MINOR.  Resolved by including canonical files as arXiv ancillary
material on submission.

---

### H9 — "The abstract overclaims with 'relative error < 10^{-15}'"

**Raw severity**: MINOR  
**Type**: Precision — numerical claim accuracy

**Attack text**:

> The claim of $10^{-15}$ relative error is unrealistic for a double-precision
> floating-point computation, which has machine epsilon $\approx 2.2 \times 10^{-16}$.
> The paper cannot meaningfully claim $10^{-15}$ without a more careful error analysis.

**Paper response** (Appendix B):

The tables show errors ranging from 0 to $4.3 \times 10^{-16}$, which is at
machine epsilon.  The $< 10^{-15}$ claim is a loose upper bound (verified by the
tables; all errors are comfortably below it).  A more precise statement would be
"verified to relative error $< 10^{-15}$ (typical values $< 5 \times 10^{-16}$)."

**Action required**: Tighten the numerical claim in the abstract and Appendix B
to "relative error $< 5 \times 10^{-15}$" to give explicit headroom above machine
epsilon.  **Minor editorial fix.**

---

### H10 — "UBT is not falsifiable in the GR sector"

**Raw severity**: MINOR  
**Type**: Philosophy of science — falsifiability

**Attack text**:

> The paper claims UBT "contains GR as an exact sector".  But since GR is also
> the limit, there is no prediction that UBT makes in the GR regime that differs
> from GR.  The theory is unfalsifiable in this sector.

**Paper response**:

This is a category confusion.  The paper does not claim UBT *replaces* GR —
it claims UBT *contains* GR.  This is not a weakness but a requirement for any
unified theory.  Falsifiable predictions from UBT come from sectors *beyond* GR
(companion T2_GAUGE and T3_ALPHA papers).  The contribution of this paper is
proof of GR containment, which is a necessary pre-condition for a consistent
unification attempt.

**Residual risk**: MINIMAL.  This is a philosophical objection, not a technical one.

---

## Residual Risk Summary After Paper Countermeasures

| ID | Attack | Pre-response severity | Post-response severity | Action needed |
|----|--------|----------------------|----------------------|---------------|
| H1 | Circular metric | MAJOR | LOW | None (addressed in paper) |
| H2 | AXIOM-B smuggles Lorentz | MAJOR | LOW–MED | Optional §2.2 clarification |
| H3 | Ansatz reverse-engineered | MODERATE | LOW | Verify canonical file |
| H4 | Zerilli missing | MODERATE | LOW | None (GAP-Z stated) |
| H5 | GAP-10 is fatal | MOD–MAJOR | MEDIUM | None (on-shell claim stands) |
| H6 | Missing twistor comparison | MODERATE | LOW | Optional 1–2 sentences §7.2 |
| **H7** | **G is a free parameter** | **MODERATE** | **LOW (after fix)** | **Add 1 sentence §3.5 — REQUIRED** |
| H8 | Proofs not self-contained | MINOR | MINOR | Include canonical files in arXiv submission |
| H9 | 10⁻¹⁵ overclaim | MINOR | MINOR | Tighten to 5×10⁻¹⁵ |
| H10 | Unfalsifiable | MINOR | MINIMAL | None |

---

## Verdict

**SUBMIT_READY** with one mandatory fix (H7) and two optional improvements (H2, H6).

The paper is technically sound at the on-shell classical level.  The two [L2] gaps
(GAP-10, GAP-Z) are honestly stated and do not block submission.  The primary
competitive risk is reviewer H5 (GAP-10 framing) but the on-shell vs. off-shell
distinction is clearly made in the paper.

---

## Required Pre-Submission Action

1. **H7 (mandatory)**: Add 1 sentence in §3.5 clarifying that $G$ is an input
   parameter setting the Planck scale, not derived in this paper.

2. **H9 (recommended)**: Tighten numerical claim in abstract to
   "$< 5\times10^{-15}$" or "at floating-point precision".

3. **H8 (on submission)**: Include canonical files as arXiv ancillary uploads.

---

## References

- `papers/UBT_GR_Submission.tex` — main paper
- `reports/GR_claims_with_evidence_table.md` — claims × evidence table
- `reports/GR_final_gap_checklist.md` — gap analysis
- `reports/GR_reviewer_objections_and_answers.md` — structured Q&A responses

<!-- BILINGUAL-UNIT: legacy-action.provenance -->
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

# Legacy Appendix-AA action as a GR selector: decision audit

<!-- BILINGUAL-UNIT: legacy-action.question -->
## Question and scope

This note tests whether the archived `appendix_AA_theta_action.tex` can supply
the missing microscopic single-$\Theta$ action, functional-integral measure,
and Hessian required for unconditional GR recovery. The source is historical;
it is tested, not reactivated. This audit does not classify every possible
single-$\Theta$ action.

<!-- BILINGUAL-UNIT: legacy-action.dependencies -->
## Dependency test

The archived functional depends explicitly on a metric $G_{\mu\nu}$, spin
connection $\Omega_\mu$, gauge connection $A_\mu$, gauge curvature
$F_{\mu\nu}$, an unspecified interaction potential, and a boundary curvature
term. It does not define all of these objects as functionals of $\Theta$ and
does not perform the chain-rule variation required by the locked composite
tetrad architecture. It is therefore an action $S[\Theta,G,\Omega,A,\ldots]$,
not the required finalized action $S[\Theta]$.

If its kinetic metric is instead locked to
$g_{\mu\nu}[\Theta]=\mathcal N_0^{-1}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp$,
the exact contraction already proved in the canonical audit turns that kinetic
scalar into $4\mathcal N_0$ (or $2\mathcal N_0$ with the displayed one-half).
It becomes a volume term and supplies no Einstein--Hilbert selector.

<!-- BILINGUAL-UNIT: legacy-action.measure -->
## Measure and pairing test

The source declares four coordinates $q^\mu\in\mathbb B$, each with eight real
components, and also $(t,\psi)\in\mathbb R^2$, but integrates only
$d^4q\,dt\,d\psi$. The declared real coordinate count is therefore
$4\cdot8+2=34$, whereas the displayed differential has six factors. No map,
constraint, Jacobian, or induced submanifold measure reducing 34 to 6 is given.

The functional measure $\mathcal D\Theta$ is only named. Its gauge quotient,
Jacobian from $\Theta$ to composite variables, constraints, ghosts,
regularization, and normalization are not constructed. Consequently it cannot
fix the physical mode count or the finite Einstein--Hilbert coefficient.

The stated pairing is also internally incompatible as written: it is declared
real-valued through `Re`, yet is claimed to be complex sesquilinear. For a
nonzero value $z$ that is real, conjugate-linearity at $\lambda=i$ requires
$-iz$, which is not real. The only value satisfying both requirements for all
arguments is zero, contradicting positive definiteness.

<!-- BILINGUAL-UNIT: legacy-action.verification -->
## Verification

Lean file `formal/lean/UBT/GR/LegacyActionObstructions.lean` kernel-checks the
coordinate-count mismatch and the exact complex-number lemma underlying the
pairing conflict. The earlier Lean theorem
`CompositeKinetic.compositeKineticCollapse` covers the metric-lock collapse.
These formal results verify only the encoded obstructions; they do not prove
that no different microscopic action can work.

<!-- BILINGUAL-UNIT: legacy-action.verdict -->
## Verdict and next candidate

**REJECTED AS A CLOSURE INPUT.** The archived Appendix-AA functional does not
close `UBT-FUND-GR-ACTION`, `UBT-UV-G-PREDICTION`, or
`UBT-UV-PSI-STABILITY`, and it must not be cited as the missing microscopic
measure. GR recovery remains `CLOSED_CONDITIONALLY`.

The next admissible candidate must start directly from the frozen covariant
tetrad architecture, declare a non-surjective $\Theta$-only invariant beyond
the collapsed quadratic first-jet scalar, and specify its configuration space
and gauge quotient before its Hessian or induced Newton coefficient is used.

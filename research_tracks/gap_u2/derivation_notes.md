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

# GAP-U2 / GAP-B / pure-Theta closure notes

Date: 2026-07-14

## Correct Abelian current

For `D_mu Theta = nabla_mu Theta - i q A_mu Theta`, the real current is

\[
J^\mu=q\,\operatorname{ReTr}\left[i\left(\Theta^\dagger D^\mu\Theta-(D^\mu\Theta)^\dagger\Theta\right)\right]
=-2q\,\operatorname{ImTr}(\Theta^\dagger D^\mu\Theta),
\]

up to the overall sign convention for `D_mu`. The old formula with the factor `i` outside `ReTr` vanishes identically and is withdrawn.

## Schwarzschild lapse

The exact lapse is closed only in the static-vacuum GR branch:

\[
\Delta_hN=0,
\quad h_{ij}=\Psi^4\delta_{ij},
\quad N(\infty)=1,
\quad N(M/2)=0
\]

imply

\[
N=(1-M/(2r))/(1+M/(2r)).
\]

This does not derive the lapse from a Maxwell field or from the canonical Theta equation.

- `GAP-U2S`: closed conditionally on static vacuum GR + spatial branch + boundary data.
- `GAP-U2Theta`: open.

## GAP-B

The first metric variation is now based on the constant-normalized compact-psi metric:

\[
\delta g_{\mu\nu}=\frac{2}{\mathcal N_0}\left\langle
\partial_{(\mu}\Theta,\partial_{\nu)}\delta\Theta
\right\rangle_\psi.
\]

The perturbation bridge

\[
\delta(\nabla^\dagger\nabla\Theta)\longrightarrow\delta G_{\mu\nu}
\]

remains open. Regge–Wheeler and Zerilli results remain conditional on GAP-B.

## GAP-10 split

See `canonical/gr_closure/pure_ubt_fiber_closure.tex`:

- fixed-psi generic closure: rank no-go;
- full compact-psi fiber-free local vacuum closure: proved;
- matter closure: conditional on the direct internal equation;
- single-action separation, selected Jacobi sector, and global closure: open.

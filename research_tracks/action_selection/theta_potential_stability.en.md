<!-- BILINGUAL-UNIT: theta-potential-stability.provenance -->
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

# Stability boundary of the classified Theta potential

<!-- BILINGUAL-UNIT: theta-potential-stability.scope -->
## Scope

For the exact invariant family already classified in
`theta_potential_invariants.en.md`, write

\[
V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2D(X),
\qquad D(X):=|\det X|^2,
\]

with

\[
H(X)=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2,
\qquad
X=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

This note determines exactly when this polynomial is bounded below on
`Mat(2,C)` and whether it can by itself select an isolated vacuum.

<!-- BILINGUAL-UNIT: theta-potential-stability.inequality -->
## Universal inequality

For every complex `2 x 2` matrix,

\[
\boxed{H(X)\le 2|\det X|=2\sqrt{D(X)}.}
\]

Indeed,

\[
\begin{aligned}
H
&=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2\\
&\le 2|a||d|-2|b||c|\\
&\le 2\bigl||a||d|-|b||c|\bigr|\\
&\le 2|ad-bc|.
\end{aligned}
\]

The first line uses `Re(z) <= |z|`, the second uses
`|b|^2+|c|^2 >= 2|b||c|`, and the last is the reverse triangle inequality.

<!-- BILINGUAL-UNIT: theta-potential-stability.boundedness -->
## Exact boundedness theorem [L1]

The potential `V` is bounded below on all of `Mat(2,C)` if and only if one of
the following mutually compatible cases holds:

1. `lambda1 > 0` and `lambda2 >= 0`, with arbitrary real `m^2`;
2. `lambda1 = 0`, `lambda2 > 0`, and `m^2 <= 0`;
3. `lambda1 = lambda2 = m^2 = 0`.

### Sufficiency

If `lambda1 > 0` and `lambda2 >= 0`, completing the square gives

\[
\lambda_1H^2+m^2H
\ge -\frac{(m^2)^2}{4\lambda_1},
\]

so `V` is bounded below.

If `lambda1 = 0`, `lambda2 > 0`, and `m^2=-mu <= 0`, then for `H <= 0`

\[
-\mu H+\lambda_2D\ge0.
\]

For `H>0`, the universal inequality gives `H <= 2 sqrt(D)`. With
`y=sqrt(D)` this implies

\[
-\mu H+\lambda_2D
\ge \lambda_2y^2-2\mu y
\ge -\frac{\mu^2}{\lambda_2}.
\]

The third case is the constant potential.

### Necessity

Exact one-parameter witnesses exclude every remaining sign choice:

- `X=t [[0,1],[0,0]]` has `H=-t^2`, `D=0`; hence `lambda1<0` is unbounded,
  and with `lambda1=0` it also excludes `m^2>0`;
- `X=t diag(1,i)` has `H=0`, `D=t^4`; hence `lambda2<0` is unbounded;
- if `lambda1=lambda2=0` and `m^2<0`, `X=t I_2` has `H=2t^2` and is
  unbounded below; the first witness handles `m^2>0`.

These cases exhaust the complement of the stated region.

<!-- BILINGUAL-UNIT: theta-potential-stability.flat -->
## Exact noncompact flat direction [L0]

For every real `t`,

\[
X_t=t\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]

obeys

\[
H(X_t)=0,
\qquad
D(X_t)=0,
\qquad
V(X_t)=V_0.
\]

Therefore **no member of the complete connected-symmetry invariant quartic
potential family is coercive on the generic field space, and none can select
an isolated vacuum by the derivative-free potential alone**. This statement
is coefficient-independent.

This is not a proof of an instability of the complete UBT action: derivative
terms, gauge quotienting, constraints, or a smaller physical configuration
space can remove a flat direction. It is a no-go for solving action selection
by tuning only `m^2`, `lambda1`, and `lambda2` inside the already classified
potential.

<!-- BILINGUAL-UNIT: theta-potential-stability.verification -->
## Verification

`tools/verify_theta_potential_stability.py` evaluates all exact witness rays
with Gaussian-rational arithmetic and checks the coefficient-case logic used
above. `tests/test_theta_potential_stability.py` keeps the witnesses and the
flat direction under CI.

The universal inequality and the sufficiency proof are elementary analytic
inequalities written explicitly above. A complete Lean formalization of the
complex absolute-value inequality chain is `LEAN-PENDING`; no formal proof is
claimed for that part.

<!-- BILINGUAL-UNIT: theta-potential-stability.consequence -->
## Consequence for the single-action programme

Potential classification has now reached its natural boundary:

- the invariant basis is exact;
- boundedness gives exact sign regions;
- the entire family retains a noncompact coefficient-independent flat
  direction.

Thus the next theorem-critical selector is not another potential coefficient.
It must come from the derivative/gauge/constraint structure of the same single
action. In particular, a proposed microscopic action must show how its
configuration-space quotient and Hessian remove or render gauge the flat
`H=D=0` orbit while retaining the covariant-tetrad GR sector.

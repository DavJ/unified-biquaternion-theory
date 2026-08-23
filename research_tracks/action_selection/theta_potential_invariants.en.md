<!-- BILINGUAL-UNIT: theta-potential.provenance -->
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

# Local polynomial invariants of the Theta potential

<!-- BILINGUAL-UNIT: theta-potential.scope -->
## Scope and assumptions

This note classifies the derivative-free real polynomial terms available to
the local potential of the already declared action family. It uses the generic
field-value realization

\[
 X=\rho(\Theta)=
 \begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{Mat}(2,\mathbb C)
\]

and exactly the connected action

\[
 X\longmapsto e^{i\alpha}SXS^\dagger,
 \qquad S\in SL(2,\mathbb C),\quad e^{i\alpha}\in U(1).
\]

The first factor is the declared scalar phase and the second is the declared
gravitational spin lift. The result concerns real polynomials in the eight real
components of a generic `X`, of total degree at most four, with no derivatives
and no explicit coordinate dependence. It does not assume the Lorentz-real
classical slice for the field value.

<!-- BILINGUAL-UNIT: theta-potential.theorem -->
## Classification theorem [L1, computer-assisted exact]

Let matrix sharp be the adjugate involution

\[
 X^\sharp=\begin{pmatrix}d&-b\\-c&a\end{pmatrix},
\]

and define the real quadratic form

\[
 H(X):=\operatorname{Tr}(X^\sharp X^\dagger)
 =2\operatorname{Re}(a\bar d)-|b|^2-|c|^2.
\]

For the group action stated above:

1. the space of real homogeneous quadratic invariants is one-dimensional and
   is spanned by `H`;
2. the space of real homogeneous quartic invariants is two-dimensional and is
   spanned by `H^2` and `|det X|^2`;
3. homogeneous invariants of odd degree vanish.

Consequently every invariant real local polynomial potential of degree at most
four has the unique form

\[
 \boxed{V(X)=V_0+m^2H(X)+\lambda_1H(X)^2
                 +\lambda_2|\det X|^2,}
 \qquad V_0,m^2,\lambda_1,\lambda_2\in\mathbb R.
\]

“Unique form” means a unique basis expansion after the normalization of `H`
has been fixed. It does not determine the four real coefficients.

<!-- BILINGUAL-UNIT: theta-potential.proof -->
## Proof and exact rank certificate

For an infinitesimal spin transformation, write

\[
 \delta_A X=AX+XA^\dagger,
 \qquad
 A\in\left\{\frac{\sigma_i}{2},\frac{i\sigma_i}{2}\right\}_{i=1}^3,
\]

and add the phase generator `delta X=iX`. Realification gives seven rational
`8 x 8` generators. Their induced derivations act linearly on each homogeneous
monomial space.

There are 36 degree-two monomials. The stacked infinitesimal constraint matrix
has exact rational rank 35, so its kernel has dimension one. Direct expansion
puts `H` in that kernel.

There are 330 degree-four monomials. After multiplying all generators by two,
the constraint matrix is integral. Its rank is 328 over each of the finite
fields with primes `1000003` and `1000033`. A nonzero 328-minor modulo either
prime is a nonzero integer minor, hence the rational rank is at least 328.
The two explicitly verified independent kernel elements `H^2` and `|det X|^2`
give rational rank at most 328. Therefore the characteristic-zero rank is
exactly 328 and the kernel dimension is exactly two.

The groups `SL(2,C)` and `U(1)` are connected, so annihilation by all seven Lie
algebra generators is equivalent here to invariance under the stated connected
group. Finally the phase element with `alpha=pi` sends `X` to `-X`, excluding
all odd homogeneous degrees.

Finite invariance also follows analytically. Since `det S=1`,

\[
 (SXS^\dagger)^\sharp=(S^\dagger)^{-1}X^\sharp S^{-1}.
\]

Cyclicity of the trace proves invariance of `H`; determinant multiplicativity
proves Lorentz invariance of `det X`, and the phase charge of `det X` is two,
so `|det X|^2` is phase neutral.

<!-- BILINGUAL-UNIT: theta-potential.counterexample -->
## Why the former positive mass term is not admissible

The positive Hilbert--Schmidt expression is not the quadratic invariant. Take

\[
 S=\operatorname{diag}(2,1/2),\qquad X=I_2.
\]

Then `det S=1`, while

\[
 \operatorname{Tr}(X^\dagger X)=2,
 \qquad
 \operatorname{Tr}[(SXS^\dagger)^\dagger(SXS^\dagger)]
 =16+\frac1{16}=\frac{257}{16}.
\]

Thus `Tr(X^dagger X)` fails a nonunitary Lorentz boost. The admissible
quadratic form `H` is indefinite; symmetry alone does not prove stability.

<!-- BILINGUAL-UNIT: theta-potential.verification -->
## Verification record

| Claim | Tool and artifact | Result | Limitation | Lean status |
|---|---|---|---|---|
| Degree-two and degree-four invariant-space dimensions | SymPy 1.14.0 plus exact finite-field elimination, `tools/verify_theta_potential_invariants.py` | PASS: dimensions `1` and `2` | Only the stated field representation, group and degree bound | `LEAN-PENDING` for the 330-monomial completeness certificate |
| Finite transformation invariance and Hilbert--Schmidt counterexample | Python standard-library `Fraction`, `tools/verify_theta_potential_invariants_independent.py` | PASS with exact rational and complex-rational representatives | Spot checks do not prove completeness | `PARTIAL` |
| Spin and phase invariance of `H`, determinant spin invariance, determinant-norm phase invariance, and the boost counterexample | Lean 4.33.1 with mathlib, `formal/lean/UBT/Action/PotentialInvariants.lean` | PASS; the module and root `UBT` target compile | Does not prove the invariant-space dimensions | `PROVED` for the encoded claims |

Both scripts state the excluded physics explicitly. The first is an exact
classification, not a numerical sample; the second uses an independent matrix
implementation and no SymPy. Lean checks the candidate identities without
`sorry` or new axioms; completeness of the 330-monomial classification remains
explicitly `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: theta-potential.consequence -->
## Consequence for the single-action programme

This result removes the unrestricted function `V[Theta]` from the
renormalizable derivative-free ansatz and replaces it by three nonconstant
coefficients. It does not select `m^2`, `lambda_1`, or `lambda_2`, fix the
kinetic normalization or sign, derive the microscopic measure, or derive an
Einstein--Hilbert coefficient. Therefore it narrows
`UBT-FUND-GR-ACTION` but does not close it and does not upgrade GR recovery.

Additional declared internal-carrier actions, discrete involutions,
boundedness, the vacuum, the gauge-fixed Hessian, and physical `psi`-sector
stability must be imposed and checked next. Any of them may reduce the
three-parameter nonconstant family further or rule it out.

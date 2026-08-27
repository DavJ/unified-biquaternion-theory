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

# Two-sided renormalized Euler product and the prime nonlocality gate

**Track:** `research_tracks/prime_fock_operator`
**Status:** classical two-chart factorization proved; critical-line boundary operator and UBT origin open
**Proof level:** standard analytic mathematics plus deterministic finite/numerical checks; `LEAN-PENDING`
**Scope:** research audit; no canonical UBT status change and no RH claim

<a id="tre-purpose"></a>
## 1. Purpose and decision boundary

The adelic valuation audit identifies the radial finite-place trace with the Euler product in its convergent half-plane. This note asks whether the formal equation

\[
\prod_p\left(\sum_{m\geq0}p^{-ms}\right)=0
\]

can become a route to the nontrivial zeros. The answer is precise. The raw product is nonzero where it converges absolutely, while in the critical strip it is not a justified definition of zeta. A useful continuation must first remove finitely many divergent prime-power layers and must treat the two sides of the critical line as separate charts related by the functional equation.

The resulting construction is informative but not an RH proof. It isolates the only genuinely difficult term: the first prime layer

\[
P(s)=\sum_p p^{-s}.
\]

All higher local layers can be represented by a norm-convergent nonlocal translation operator arbitrarily close to the critical line. The unrenormalized first layer cannot.

<a id="tre-raw-product"></a>
## 2. The raw product cannot vanish in its trace domain

For every fixed prime and \(\Re s>0\),

\[
Z_p(s)=\sum_{m\geq0}p^{-ms}=\frac{1}{1-p^{-s}}.
\]

For \(\Re s>1\),

\[
Z_{\mathrm{fin}}(s)
=\prod_p Z_p(s)
=\prod_p\frac{1}{1-p^{-s}}
=\zeta(s).
\]

Every local factor is nonzero and the logarithm of the product converges absolutely. Hence

\[
\boxed{Z_{\mathrm{fin}}(s)\neq0\qquad(\Re s>1).}
\]

Finite-prime truncations are also never zero. Outside the absolute-convergence half-plane, those truncations do not canonically define the analytic continuation. Therefore a nontrivial zeta zero is a global obstruction to a holomorphic logarithm, not the vanishing of a single local geometric sum.

<a id="tre-maclaurin-subtraction"></a>
## 3. Finite Maclaurin subtraction

For an integer \(M\geq1\), define

\[
R_M(s)=
\prod_p
\frac{1}{1-p^{-s}}
\exp\left(-\sum_{m=1}^{M}\frac{p^{-ms}}{m}\right).
\]

Its logarithm is

\[
\log R_M(s)
=\sum_p\sum_{m=M+1}^{\infty}\frac{p^{-ms}}{m}.
\]

This double series converges absolutely and locally uniformly when

\[
\Re s>\frac{1}{M+1}.
\]

Consequently \(R_M\) is holomorphic and nonvanishing in that half-plane. Initially for \(\Re s>1\),

\[
\boxed{
\zeta(s)=R_M(s)
\exp\left(\sum_{m=1}^{M}\frac{P(ms)}{m}\right).
}
\]

Increasing \(M\) pushes the absolutely convergent remainder toward \(\Re s=0\), but it does not remove the need to continue the finitely many prime-zeta terms \(P(ms)\). This is the exact content of the infinite Maclaurin idea: it separates convergent local tails from global singular layers, but it does not prove that those layers are regular.

<a id="tre-right-chart"></a>
## 4. The right chart

The first useful case is

\[
R_1(s)=\prod_p\frac{e^{-p^{-s}}}{1-p^{-s}},
\qquad
\log R_1(s)=\sum_p\sum_{m\geq2}\frac{p^{-ms}}{m}.
\]

Thus \(R_1\) is holomorphic and nonzero for \(\Re s>1/2\). On every simply connected domain \(U\) in that half-plane avoiding \(s=1\) and the zeros of zeta, with a consistent logarithm branch,

\[
\zeta(s)=R_1(s)e^{P(s)}.
\]

The identity

\[
\log\zeta(s)=P(s)+\sum_{m\geq2}\frac{P(ms)}{m}
\]

shows that the tail is holomorphic for \(\Re s>1/2\). Therefore, in a neighborhood \(V_\rho\) of a zero \(\rho\) of multiplicity \(m_\rho\) in this open half-plane,

\[
P(s)=m_\rho\log(s-\rho)+h_\rho(s),
\qquad h_\rho\in\mathcal O(V_\rho),
\]

The prime-zeta function also has the pole-induced logarithmic singularity at \(s=1\). Hence RH is equivalently reformulated as the absence of any other logarithmic branch point of \(P(s)\) in \(\Re s>1/2\). This equivalence is a classical reformulation, not progress toward proving the required absence.

<a id="tre-left-chart"></a>
## 5. The left chart is not omitted

Use the entire completed function

\[
\xi(s)=C(s)\zeta(s),
\qquad
C(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
\qquad
\xi(s)=\xi(1-s).
\]

The two chart expressions are

\[
\boxed{
\xi(s)=C(s)R_1(s)e^{P(s)},
\qquad \Re s>\frac12,
}
\]

and

\[
\boxed{
\xi(s)=C(1-s)R_1(1-s)e^{P(1-s)},
\qquad \Re s<\frac12.
}
\]

The second remainder converges absolutely because \(\Re(1-s)>1/2\). For \(\Re s<0\), even \(P(1-s)\) is represented by its ordinary convergent prime series. In the left half of the critical strip, \(0<\Re s<1/2\), the only continuation problem is the reflected prime layer \(P(1-s)\).

This formulation also avoids treating the trivial zeros of zeta as spectral zeros: the gamma factor cancels them in \(\xi\). A nontrivial zero off the critical line occurs in the reflected quartet

\[
\{\rho,\overline\rho,1-\rho,1-\overline\rho\}.
\]

Thus controlling the right open half-strip controls the left one through a proved symmetry, but the left chart remains explicit in the construction.

<a id="tre-boundary"></a>
## 6. The critical line as a common regulated boundary

For real \(t\) and \(\varepsilon>0\), put

\[
s_+(\varepsilon,t)=\frac12+\varepsilon+it,
\qquad
s_-(\varepsilon,t)=\frac12-\varepsilon+it.
\]

Then

\[
1-s_-(\varepsilon,t)
=\frac12+\varepsilon-it
=\overline{s_+(\varepsilon,t)},
\]

and the functional equation plus real analyticity gives

\[
\boxed{
\xi(s_-(\varepsilon,t))
=\overline{\xi(s_+(\varepsilon,t))}.
}
\]

The two sides therefore have equal modulus and opposite phase. The limit \(\varepsilon\downarrow0\) is not supplied by absolute convergence of \(R_1\): its leading remaining layer has exponent \(2\Re s=1\) on the boundary. Any boundary operator must specify a regulator, topology of convergence, and subtraction prescription.

<a id="tre-nonlocal-operator"></a>
## 7. Exact nonlocal-operator split

Let \(U_a\) be the unitary translation on \(L^2(\mathbb R)\),

\[
(U_af)(x)=f(x+a).
\]

For \(\varepsilon>0\), the higher-layer operator

\[
B_\varepsilon
=\sum_p\sum_{m\geq2}
\frac{p^{-m(1/2+\varepsilon)}}{m}
U_{m\log p}
\]

converges in operator norm, because the sum of coefficient norms is finite. Its Fourier multiplier is the higher-layer logarithm \(\log R_1\), up to the Fourier-sign convention.

The first layer has finite cutoffs

\[
A_{\varepsilon,X}
=\sum_{p\leq X}p^{-1/2-\varepsilon}U_{\log p}.
\]

All coefficients align at zero Fourier frequency, so

\[
\boxed{
\|A_{\varepsilon,X}\|
=\sum_{p\leq X}p^{-1/2-\varepsilon}.
}
\]

Therefore the uncentered first layer converges in operator norm only in the safe region \(\varepsilon>1/2\), equivalent to \(\Re s>1\). For \(0<\varepsilon\leq1/2\), its norms diverge. Merely writing all prime translations as an operator does not analytically continue them.

A valid UBT/nonlocal step must consequently provide a canonical centering or renormalization of the first layer and prove a topology strong enough to control its resolvent. It may not insert zeta zeros into a spectral multiplier.

<a id="tre-chebyshev-gate"></a>
## 8. The Chebyshev remainder exposes the RH-strength gate

Let

\[
\psi(x)=\sum_{n\leq x}\Lambda(n).
\]

For \(\Re s>1\),

\[
-\frac{\zeta'}{\zeta}(s)
=\int_1^\infty x^{-s}\,d\psi(x)
=s\int_1^\infty\psi(x)x^{-s-1}\,dx.
\]

After subtracting the main term,

\[
\boxed{
-\frac{\zeta'}{\zeta}(s)-\frac{s}{s-1}
=s\int_1^\infty(\psi(x)-x)x^{-s-1}\,dx.
}
\]

If one proves

\[
\psi(x)-x=O_\delta(x^{1/2+\delta})
\qquad(\delta>0),
\]

then the centered transform continues with the required control throughout \(\Re s>1/2\). Conversely, this square-root prime-number-theorem error is RH-strength. The desired first-layer renormalization is therefore not a harmless regularization detail; its decisive bound contains the central difficulty.

<a id="tre-ledger"></a>
## 9. Theorem and gap ledger

| ID | Statement | Status |
|---|---|---|
| TRE-1 | the raw radial Euler product is nonzero for \(\Re s>1\) | **[STD/PROVED]** |
| TRE-2 | \(R_M\) is holomorphic and nonvanishing for \(\Re s>1/(M+1)\) | **[STD/PROVED]** |
| TRE-3 | right and left \(\xi\)-charts are related exactly by \(s\leftrightarrow1-s\) | **[STD/PROVED]** |
| TRE-4 | \(B_\varepsilon\) converges in norm for every \(\varepsilon>0\) | **[STD/PROVED]** |
| TRE-5 | the uncentered first-layer norms diverge for \(0<\varepsilon\leq1/2\) | **[STD/PROVED NO-GO]** |
| TRE-RH | construct a canonical centered first-layer operator with square-root control | **[OPEN; RH-strength]** |
| TRE-UBT | derive the prime translations, centering, and doubled involution from the canonical UBT action | **[OPEN]** |
| TRE-HP | obtain a self-adjoint operator whose spectral or resolvent singularities are exactly the nontrivial zeros | **[OPEN]** |

<a id="tre-next"></a>
## 10. Next admissible experiment

The next experiment should not evaluate larger raw Euler products. It should:

1. construct finite centered prime-translation operators from \(\psi(x)-x\);
2. compare cutoff schemes and test whether a regulator-independent strong or resolvent limit exists away from the critical line;
3. double the construction with the involution \(s\leftrightarrow1-s\), rather than adding the left side afterward;
4. use the argument principle for \(\xi\) to test winding, not zeros of finite Euler products;
5. stop if the centering is defined through \(\zeta'/\zeta\), a table of zeros, or an assumed square-root prime error.

Passing finite numerical tests will only validate normalization and symmetry. The decisive theorem must be an analytic bound independent of RH-equivalent input.

<a id="tre-verification"></a>
## 11. Verification

| Claim | Artifact/tool | Result | Scope | Limitation | Lean status |
|---|---|---|---|---|---|
| TRE-1 and finite Maclaurin identity | `tools/verify_two_sided_renormalized_euler.py`, Python 3.12 | pass | complex finite-prime products and logarithmic layers | finite products do not establish analytic continuation | `LEAN-PENDING` — Lean is unavailable in the runtime |
| TRE-2 convergence threshold | same artifact | pass | deterministic cutoff comparison above and below selected thresholds | numerical convergence is not the locally uniform analytic proof | `LEAN-PENDING` |
| TRE-3 reflection | same artifact | pass | exact affine reflection and the known values \(\xi(2)=\xi(-1)=\pi/6\) | one checkpoint does not prove the functional equation | `LEAN-PENDING` |
| TRE-4 and TRE-5 | same artifact | pass | coefficient norm bounds and sampled translation multipliers | finite Fourier samples supplement the analytic norm argument | `LEAN-PENDING` |
| prime-power logarithmic derivative | same artifact | exact pass | finite von Mangoldt sum versus prime-power enumeration | no continuation or zero location is tested | `LEAN-PENDING` |

No verifier result derives a UBT prime operator, a critical-line boundary value, or RH.

<a id="tre-references"></a>
## 12. Primary references

- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer, 2000.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed., Oxford University Press, 2008.
- C.-E. Fröberg, [*On the prime zeta function*](https://doi.org/10.1007/BF01933420), *BIT* **8** (1968), 187--202.

<!-- BILINGUAL-UNIT: selector-completion.header -->
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


# Domain-complete bounded branch selection and the remaining RH bridge

**Date:** 2026-09-08. **Status:** ANALYTIC PROOF [L1]; LEAN-PENDING.
This research companion completes the analytic domain argument of G1 in
`psi_branch_selection.en.md`. It also supplies the elementary operator-domain
proof requested as F5 in `../prime_fock_operator/gap_inventory.md`.
Neither result derives a canonical UBT generator or proves RH. These are
applications of classical spectral theory, with no claim of mathematical
priority. Their explicit proofs are retained for learning and verification.

<!-- BILINGUAL-UNIT: selector-completion.assumptions -->
## 1. Exact hypotheses

Let \(H\) be a complex Hilbert space, with inner product linear in the first
argument, and let \(A\) be a densely defined nonnegative self-adjoint
operator. No discrete spectrum or positive spectral gap is assumed.

\[
A=A^*\ge0,\qquad \mathbb C_-:=\{z\in\mathbb C:\operatorname{Im}z<0\}.
\]

Let \(F:\mathbb C_-\to H\) be norm-holomorphic and a weak solution of the
second-order equation, in the following precise sense:

\[
\langle F''(z),h\rangle+\langle F(z),A^2h\rangle=0
\quad(h\in D(A^2),\ z\in\mathbb C_-).
\]

Require a strong boundary value on the vertical ray and a bound on that ray:

\[
u=\lim_{s\downarrow0}F(-is)\in H,\qquad
M=\sup_{s>0}\|F(-is)\|_H<\infty.
\]

The parameter \(s\) is an auxiliary continuation depth. No identification
with a periodic realization of the UBT coordinate \(\psi\) is made.

<!-- BILINGUAL-UNIT: selector-completion.theorem -->
## 2. Bounded selection without a spectral gap

**Theorem S1 [L1].** Under precisely these hypotheses,

\[
F(z)=e^{-izA}u\quad(z\in\mathbb C_-).
\]

Conversely this formula defines the unique function satisfying the hypotheses
for every \(u\in H\). In the open half-plane it belongs to every power
domain and satisfies a strong first-order equation:

\[
F(z)\in\bigcap_{k\ge1}D(A^k),\qquad
iF'(z)=AF(z),\qquad
\sup_{z\in\mathbb C_-}\|F(z)\|=\|u\|.
\]

**Proof.** Write \(E_A\) for the spectral measure. For positive integers use
the bounded spectral windows and the zero-mode projection

\[
P_n=E_A([1/n,n]),\quad H_n=P_nH,\quad
A_n=A|_{H_n},\quad P_0=E_A(\{0\}).
\]

The weak equation tested against \(H_n\subset D(A^2)\) gives an ordinary
bounded-operator equation for \(w_n(s)=P_nF(-is)\):

\[
w_n''(s)=A_n^2w_n(s),\qquad
w_n(s)=e^{-sA_n}a_n+e^{sA_n}b_n.
\]

For completeness, these constants exist without differentiating the boundary
value: choose any \(s_0>0\) and set

\[
a_n=\tfrac12e^{s_0A_n}(w_n(s_0)-A_n^{-1}w_n'(s_0)),\qquad
b_n=\tfrac12e^{-s_0A_n}(w_n(s_0)+A_n^{-1}w_n'(s_0)).
\]

The bounded-operator initial-value problem is unique. The spectral lower bound
and the triangle inequality now give

\[
e^{s/n}\|b_n\|\le\|e^{sA_n}b_n\|
 \le M+\|a_n\|\qquad(s>0).
\]

Thus \(b_n=0\). Taking the strong boundary limit shows \(a_n=P_nu\).
In the kernel the equation is affine:

\[
P_0F(-is)=a_0+s b_0.
\]

The same vertical bound forces \(b_0=0\) and the boundary limit fixes
\(a_0=P_0u\). No extra real-time boundedness condition is needed under
the present hypotheses. Because

\[
\|(I-P_0-P_n)v\|\longrightarrow0\quad(\forall v\in H),
\]

the spectral calculus yields \(F(-is)=e^{-sA}u\). This step includes
continuous spectrum accumulating at zero.

Define \(G(z)=e^{-izA}u\) directly by the spectral calculus. It exists for
every \(u\in H\) and \(z=t-is\), since the spectral multiplier has modulus
\(e^{-s\lambda}\). Its derivatives are controlled locally by

\[
\sup_{\lambda\ge0}\lambda^k e^{-s\lambda}
 =\left(\frac{k}{es}\right)^k\quad(k\ge1).
\]

This proves norm holomorphy, membership in the power domains and the strong
equations in the interior. The scalar identity theorem, applied after taking
inner products with arbitrary vectors, extends \(F=G\) from the vertical ray
to the entire connected half-plane. Contractivity and the strong boundary
limit give the stated norm equality and also prove the converse.

<!-- BILINGUAL-UNIT: selector-completion.boundaries -->
## 3. Boundary regularity and what was not assumed

The boundary orbit is the strongly continuous unitary orbit

\[
F(t)=e^{-itA}u.
\]

It satisfies the first-order equation in the mild sense for arbitrary
\(u\in H\). Strong differentiability on the real boundary requires and is
equivalent to \(u\in D(A)\); a strong second-order boundary equation
requires \(u\in D(A^2)\). Interior smoothing does not remove these boundary
domain requirements.

An arbitrary growing branch need not admit continuation at all. Its exact
domain at depth \(s\) is

\[
\mu_v(B):=\|E_A(B)v\|^2,\qquad
D(e^{sA})=\left\{v\in H:
 \int_{[0,\infty)}e^{2s\lambda}\,d\mu_v(\lambda)<\infty\right\}.
\]

S1 does not assume that every real-time wave solution has a bounded analytic
continuation. It classifies those that do and constructs the surviving branch.
Holomorphy alone still permits both exponential branches.

This is a bounded Hilbert-space-valued analytic function statement, not a
Hardy square-integrability theorem on the real line. For nonzero \(u\),

\[
\int_{\mathbb R}\|e^{-itA}e^{-sA}u\|^2\,dt=\infty.
\]

The integrand is a positive constant in \(t\). Calling this orbit an element
of the usual vector-valued \(H^2(\mathbb C_-)\) would be incorrect.

<!-- BILINGUAL-UNIT: selector-completion.period -->
## 4. Exact limitation of periodic continuation

**Corollary S2 [L1].** If the selected continuation is additionally periodic
in the damping depth with period \(L>0\), then it is supported in the kernel:

\[
e^{-(s+L)A}u=e^{-sA}u\quad(s>0)
\quad\Longrightarrow\quad u\in\ker A.
\]

**Proof.** The spectral norm of the difference is

\[
\int_{[0,\infty)}e^{-2s\lambda}(1-e^{-L\lambda})^2
 \,d\mu_u(\lambda)=0.
\]

Its integrand is strictly positive for every positive spectral value, so the
spectral measure is supported at zero. The converse is immediate.

Therefore direct periodic identification of this damping depth with a compact
\(S^1_\psi\) cannot retain a nonzero-frequency selected orbit. This excludes
only that direct identification under S1. It does not exclude other periodic psi
constructions, thermal correlation functions or twisted data. Deriving any
alternative from UBT is still open; its existence is not asserted here.

<!-- BILINGUAL-UNIT: selector-completion.prime -->
## 5. The prime operator: explicit closure and trace domain

**Theorem S3 [L1].** On the Hilbert space with orthonormal basis indexed by
positive integers, initially define

\[
H_{\rm p}|n\rangle=(\log n)|n\rangle,\qquad
D_0=\operatorname{span}_{\rm fin}\{|n\rangle:n\ge1\}.
\]

This operator is essentially self-adjoint. Its self-adjoint closure has domain

\[
D(H_{\rm p})=\left\{a\in\ell^2(\mathbb N):
 \sum_{n\ge1}(\log n)^2|a_n|^2<\infty\right\}.
\]

**Proof.** Testing the adjoint against basis vectors identifies it as
multiplication by \(\log n\) on exactly the displayed domain. Conversely
that condition makes the adjoint pairing bounded, proving the domain equality.
Truncating a vector in this domain to finite support converges in graph norm,
so \(D_0\) is a core. The maximal multiplication operator is self-adjoint;
equivalently its deficiency equations give

\[
(\log n\mp i)a_n=0\quad\Longrightarrow\quad a_n=0\quad(\forall n).
\]

Unique prime factorization identifies this with the occupation-basis operator
\(\sum_p(\log p)N_p\); it does not derive that operator from UBT.
For a complex parameter \(\omega\), the heat operator is trace class exactly
when \(\operatorname{Re}\omega>1\), with

\[
\operatorname{Tr}(e^{-\omega H_{\rm p}})
 =\sum_{n\ge1}n^{-\omega}=\zeta(\omega),\qquad
\|e^{-\omega H_{\rm p}}\|_1=\sum_{n\ge1}n^{-\operatorname{Re}\omega}.
\]

These assertions follow directly from its diagonal singular values. The
analytic continuation of the scalar zeta function into the critical strip is
not a trace-class heat operator there. This completes the analytic part of
the older inventory's F5, while the UBT operator origin and interpretation of
zeta zeros remain open. The old unpaired inventory is not silently promoted
or rewritten by this companion.

<!-- BILINGUAL-UNIT: selector-completion.resolvent -->
### 5.1 The direct prime resolvent has no finite Schatten order

**Proposition S4 [L1].** For every real shift \(a>0\),
\(R_a=(H_{\rm p}+aI)^{-1}\) is compact but belongs to no finite Schatten
class. Its singular values tend to zero, but for every \(r>0\),

\[
s_n(R_a)=(a+\log n)^{-1},\qquad
\sum_{n\ge1}s_n(R_a)^r=\infty.
\]

**Proof.** Compactness follows from the diagonal entries tending to zero.
For positive integers \(m\), the block of integers between \(e^m\) and
\(e^{m+1}\) gives the lower bound

\[
\sum_{e^m\le n<e^{m+1}}(a+\log n)^{-r}
\ge\frac{\lfloor e^{m+1}\rfloor-\lceil e^m\rceil}{(a+m+1)^r}
\longrightarrow\infty.
\]

Thus no standard finite-order regularized Fredholm determinant of
\(I-zR_a\) applies. Likewise the usual spectral-zeta trace series for
\(H_{\rm p}+aI\) has no half-plane of absolute convergence to start from.
This does not rule out every alternative regularization; none is constructed
or identified with the completed Riemann zeta function here.

<!-- BILINGUAL-UNIT: selector-completion.heatdet -->
### 5.2 A valid heat determinant, with an exactly different zero set

**Proposition S5 [L1].** A fixed real damping parameter \(\beta>1\) does give
a trace-class operator and an ordinary Fredholm determinant:

\[
K_\beta=e^{-\beta H_{\rm p}},\qquad
D_\beta(z)=\det(I-zK_\beta)=\prod_{n\ge1}(1-z n^{-\beta}).
\]

**Proof.** The sum of the diagonal eigenvalues converges, so the product
converges locally uniformly. Its zeros are exactly \(z=n^\beta\), each
simple. For \(|z|<1\), absolute convergence also permits the logarithmic
expansion

\[
\log D_\beta(z)=-\sum_{k\ge1}\frac{z^k}{k}\zeta(\beta k).
\]

In particular Euler's sine product gives the exact closed form

\[
D_2(z)=\frac{\sin(\pi\sqrt z)}{\pi\sqrt z}
=\sum_{j\ge0}\frac{(-1)^j\pi^{2j}z^j}{(2j+1)!},\qquad D_2(0)=1.
\]

The power series makes its entire nature and independence of a square-root
branch explicit. There is also an exact symmetry obstruction: the determinant
vanishes at the positive unit argument and does not vanish at the negative
unit argument, whereas the target completed zeta function is even:

\[
D_\beta(1)=0,\quad D_\beta(-1)=\prod_{n\ge1}(1+n^{-\beta})>0,
\qquad \xi(1/2+iz)=\xi(1/2-iz).
\]

No everywhere nonvanishing multiplier can repair that zero-set mismatch.
This obstruction concerns this determinant, not all possible modifications.
Therefore the step from a prime heat trace to a determinant
can be performed exactly, but this determinant has the known integer-power
zeros, not the required zeros of the completed zeta function. Obtaining a
determinant is not sufficient; its exact identity with the target is the
missing step. The sine product is standard; see
[DLMF, infinite products](https://dlmf.nist.gov/4.22).
For the operator determinant conventions see
[Bornemann, Fredholm determinants](https://arxiv.org/abs/0804.2543).

<!-- BILINGUAL-UNIT: selector-completion.rh -->
## 6. What would actually establish RH

The classical theta–Mellin link and the functional equation are exact, but
they do not force the zeros onto the critical line. A positive self-adjoint
generator and its complex heat trace are also insufficient. For example,

\[
A_{\rm ex}=\operatorname{diag}(0,1,1),\qquad
Z_{\rm ex}(\omega)=1+2e^{-\omega},\qquad
Z_{\rm ex}(\log2+i\pi)=0.
\]

This exact counterexample concerns the proposed implication, not the Riemann
zeta function. It shows why selection for arbitrary positive generators cannot
be substituted for identification of the zeta zeros.

One sufficient spectral target would be an independently constructed
self-adjoint operator \(T\) with nonzero discrete real eigenvalues
\(\lambda_j\), repeated with multiplicity, satisfying

\[
\sum_j|\lambda_j|^{-2}<\infty,
\qquad
D_T(z)=\prod_j(1-z/\lambda_j)e^{z/\lambda_j}.
\]

The product converges locally uniformly and its zeros are exactly the real
eigenvalues. What is missing is the exact identity, for all complex \(z\),

\[
\xi(1/2+iz)=\xi(1/2)e^{h(z)}D_T(z),
\qquad h\in\mathcal O(\mathbb C),
\qquad
\xi(\omega)=\tfrac12\omega(\omega-1)
 \pi^{-\omega/2}\Gamma(\omega/2)\zeta(\omega).
\]

Because the exponential factor never vanishes, this identity would place all
zeros of \(\xi\) on the critical line. Constructing \(T\) from the zeta
zeros themselves would assume the missing answer. Matching finitely many
zeros, matching only their density, or obtaining a heat trace is not this
identity. This is a sufficient research target, not an achieved construction
and not the only possible route to RH.

Neither S1 nor S3 constructs \(T\) or establishes this determinant identity.
The branch-selection and prime-operator domain proofs close mathematical
bookkeeping gaps; the RH proof gap remains open.

<!-- BILINGUAL-UNIT: selector-completion.verification -->
## 7. Verification, sources and status boundary

Run `python tools/verify_bounded_spectral_gap_steps.py`. Its report is
`../../reports/bounded_spectral_gap_steps_2026_09_08.json`.
Exact SymPy checks cover branch signs, scalar window constants, kernel slopes,
periodicity, the heat-trace counterexample, resolvent block growth and the
sine determinant's series. A separate product-versus-sine calculation checks
truncation errors. Independent SciPy quadrature
tests a continuous multiplication spectrum reaching zero; a separate matrix
exponential calculation tests non-diagonal generators. Finite computations do
not prove S1 or the infinite-dimensional domain statement in S3.

**LEAN-PENDING:** neither Lean nor Lake is installed in the inspected runtime.
No unchecked Lean source is presented as a formal proof. Analytic proofs are
provided above; provenance stays `C_working`. Human semantic review of the
paired editions remains required before merge.

The underlying spectral calculus is standard; see Gerald Teschl's
[Mathematical Methods in Quantum Mechanics](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/).
For the completed zeta convention see
[DLMF, reflection formulas](https://dlmf.nist.gov/25.4).
For the RH problem and spectral motivation see
[Bombieri's official problem description](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).
These sources support the background, not a claim that UBT has supplied the
missing spectral determinant.

Research G1 has an analytic domain-complete theorem; its formal verification
G7 remains pending. The direct periodic interpretation has the restricted
no-go S2. The operator-domain part of prime F5 has the analytic proof S3.
The origins of the UBT action and generator, the compact-coordinate bridge,
the determinant identity, `UBT-FUND-GR-ACTION: OPEN`,
`UBT-UV-G-PREDICTION: OPEN` and `UBT-FUND-GLOBAL: OPEN` are unchanged.
No canonical claim or editorial attestation is promoted.

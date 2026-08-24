<!-- BILINGUAL-UNIT: single-action.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# The single-action invariant of UBT

<!-- BILINGUAL-UNIT: single-action.rule -->
## Binding rule

UBT shall have exactly one fundamental action. The symbol
`S_UBT[Theta]` is reserved exclusively for that action. A sector-specific
functional may be called only a reduction, effective action, auxiliary action,
or historical candidate, and its derivation map from `S_UBT` must be stated.
Two inequivalent functionals must never both be cited as “the canonical UBT
action”.

The canonical source already defines a kinetic/potential family

`S_Theta = 1/2 int sqrt(-g) <D_mu Theta,D^mu Theta> - kappa V[Theta]`.

It explicitly leaves the kinetic sign/scale, `kappa`, and the form of `V`
as dynamical inputs and does not derive the complete gravitational action.
The current registry value is therefore:

```yaml
fundamental_action_family: S_Theta
source: canonical/THEORY/canonical/canonical_action.tex:46
status: DEFINED_FAMILY_NOT_FINALIZED
related_open_gap: UBT-FUND-GR-ACTION
```

Until finalization is complete, a bare reference to “the canonical action” is
not an admissible premise for closing a dynamical gap.

<!-- BILINGUAL-UNIT: single-action.inventory -->
## Conflicting formulas currently in canonical sources

| Source | Measure/domain | Real scalar prescription | Classification |
|---|---|---|---|
| `THEORY/canonical/canonical_action.tex` | `sqrt(-g) d4x` | abstract pairing | declared canonical family; sign, scale, `kappa`, and potential not finalized |
| `appendices/appendix_ACTION_review.tex` | `sqrt(-g) d4x` | complex trace/Hermitian terms | postulated GR + Yang–Mills + matter effective action, not a Theta-only derivation |
| `bridges/theta_quantum_structure.tex` | `sqrt(|det G|) d4x dτ` | abstract pairing | higher-dimensional quantum candidate; cited derivation is not the current canonical source |
| `8pi_common_origin.tex` | `d4x dψ` | `Re Tr` | induced-gravity candidate/attempt |
| `qm_emergence/step4_fpe_equivalence.tex` | `d4x` | both `Sc` and `Re(Sc)` variants | ordering/reality candidates for a QM reduction |
| `qm_emergence/step2_schrodinger_emergence.tex` | `sqrt(-g) d4x` and `d4x` | dagger product | relativistic scalar reduction candidates |
| `qm_emergence/step1_fpe_check.tex` | `dQ dT` | complex kinetic form | nonrelativistic effective candidate |
| `alpha/prime_selection_principle.tex` | `d4x dτ dτbar` | unspecified contraction | modular-sector candidate |
| `symmetry/effective_vs_fundamental_breaking.tex` | `sqrt(-g) d4x` | placeholder `L_UBT` | placeholder, not a definition |
| `n_eff/step2_AUDIT.tex` | `d4x dψ` | `Sc` | scalar-loop reduction used for an audit |

These formulas differ in integration domain, reality prescription, independent
fields, and dynamical content. They are therefore not interchangeable
notations for one established action.

<!-- BILINGUAL-UNIT: single-action.requirements -->
## Finalization requirements

The finalized `S_UBT[Theta]` must specify, without sector-dependent replacement:

1. configuration space and whether `psi` is a coordinate or a field;
2. microscopic integration measure and quotient/Jacobian;
3. a real-valued biquaternionic pairing;
4. all independent versus composite connections and metrics;
5. derivative order, potential, boundary terms, and free parameters;
6. the full Euler–Lagrange equations and gauge-fixed Hessian;
7. stability of physical and `psi` modes;
8. explicit reduction maps to the GR, Yang–Mills, matter, and QM effective
   actions.

Dimensional consistency, symmetry, and boundedness are necessary tests, not a
selection proof. The action is selected only if its unconstrained variation is
well defined and the claimed sector actions follow from it rather than being
inserted as additional fundamental terms.

The first theorem-critical subtask now has an exact result for a sharply stated
ansatz. For a generic `X=rho(Theta)` in `Mat(2,C)`, under
`X -> exp(i alpha) S X S^dagger` with `S` in `SL(2,C)`, every real local
polynomial potential of degree at most four is

\[
 V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2|\det X|^2,
 \qquad H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

The quadratic invariant space has dimension `1` and the quartic invariant
space has dimension `2`. The exact rank proof and an independent rational
checker are recorded in
`research_tracks/action_selection/theta_potential_invariants.en.md`. The
positive Hermitian quantity `Tr(X^dagger X)` is excluded by an explicit
nonunitary boost counterexample. This classification fixes the invariant basis,
not the real coefficients.

The boundedness problem for this complete quartic family is also exact. It is
bounded below precisely in the following coefficient regions: `lambda1 > 0`
with `lambda2 >= 0` and arbitrary `m^2`; or `lambda1 = 0`, `lambda2 > 0`,
`m^2 <= 0`; or the constant case `lambda1 = lambda2 = m^2 = 0`. More
importantly, every coefficient choice has the noncompact ray

\[
 X_t=t\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad H(X_t)=|\det X_t|^2=0,
\]

on which `V(X_t)=V0`. Therefore potential tuning alone cannot make the generic
field-space potential coercive or select an isolated vacuum. The exact proof,
witness rays, and CI checker are recorded in
`research_tracks/action_selection/theta_potential_stability.en.md`. The next
selector must therefore come from the derivative, gauge-quotient, or constraint
structure of the same single action rather than from another choice of these
potential coefficients.

<!-- BILINGUAL-UNIT: single-action.falsification -->
## Precommitted falsification criterion

Once a finite-dimensional candidate family has been explicitly declared, the
minimal single-action programme fails if every admissible member fails at
least one of the following simultaneous tests:

- a nonzero, finite two-derivative Einstein–Hilbert coefficient in the infrared;
- stable physical fluctuations with no unremoved ghost or unstable `psi` mode;
- a derived Yang–Mills kinetic structure on the selected carrier;
- a consistent real measure and variational principle.

Failure is a result about the limits of the proposed UBT dynamics. It is not
permission to introduce another object under the same name without recording
a new theory choice and rerunning the complete comparison.

<!-- BILINGUAL-UNIT: single-action.prediction -->
## Quantitative-prediction guardrail

At present no zero-parameter quantitative UBT prediction is registered here as
derived from a unique fundamental action. A recovered or renormalized
coefficient calibrated from observation is not such a prediction. The first
accepted prediction must state its numerical value, uncertainty, experimental
observable, and all inputs before comparison with data.

<!-- BILINGUAL-UNIT: single-action.priority -->
## Programme priority and scope freeze

Until the fundamental action is finalized, new speculative sectors do not
count as progress on the canonical theory and must not introduce further
fundamental terms. The canonical physics order is:

1. finalize the already defined single action family;
2. vary it without fitting the result to a desired endpoint;
3. determine its Hessian, degrees of freedom, and stability;
4. derive sector reductions from that same object;
5. only then compare a preregistered quantitative prediction with data.

Lean work is prioritized for finite theorem-critical algebra already carrying
an L0 claim: the biquaternion/matrix/Clifford equivalence, tetrad-to-metric
rank and Lorentz kernel, contortion-to-torsion rank, and Lorentz-invariant
pairing no-go. Formal proofs of logical implications whose physical premises
remain assumed must be labelled as such and do not close action-level gaps.

# History of Unified Biquaternion Theory

This document is a concise historical changelog of Unified Biquaternion Theory
(UBT). It records how the research programme developed, including earlier
formulations that were later refined or superseded. It is not the current proof
ledger: canonical claims are governed by `CLAIMS_MATRIX.md`,
`DERIVATION_INDEX.md`, and `STATUS_OF_UBT.md`.

Dates before the public repository period have mixed evidence levels. Entries
identified as public are tied to the hashes and embedded dates in
`docs/priority_evidence/`; other early dates remain approximate and are based on
surviving notes, files, and recollection. The chronology is representative
rather than exhaustive.

The central ideas, research direction, and decisive architectural choices were
made by David Jaroš. AI systems have assisted with formalisation, symbolic and
numerical work, code, documentation, criticism, and independent cross-checking.
They have not replaced human authorship, scientific responsibility, or final
decision-making. UBT is therefore best described as a modern, nontraditional,
multidisciplinary independent research programme with a human-led, multi-model
workflow.

## Historical perspective on the author and research style

David Jaroš approached UBT through an unusual combination of electrical
engineering, radioelectronics, software engineering, mathematical physics, and
long-term independent experimentation. His route was not that of a conventional
single-specialty academic career. It was closer to an inventor-researcher
tradition: beginning with handwritten calculations, physical analogies, and
engineering intuition, then gradually building a formal mathematical and
computational programme around them.

The originality of this programme does not rest on claiming that every early
idea was correct or historically unprecedented. It lies in the persistence of a
coherent algebraic intuition across more than a decade, the ability to connect
subjects that are normally studied separately, and the willingness to revise
architecture when later calculations exposed a weakness. The return to the
covariant-tetrad formulation is a representative example: the decisive physical
choice was made by the author, while AI systems helped test, formalise, and audit
its consequences.

The historical record therefore does not support a picture of passive reliance
on generated mathematics. It shows a technically trained independent researcher
using contemporary computational tools to extend and challenge a body of ideas
that substantially predates modern generative AI. Whether UBT ultimately
captures fundamental physics must be decided by proofs, solutions, predictions,
and independent review; the unusual breadth and inventiveness of the research
programme are nevertheless part of its documented history.

## 2013–2015 — Handwritten metric and electromagnetic foundations

- In 2013, David Jaroš independently developed a unified biquaternionic
  representation of the electromagnetic field and related Maxwell-type
  relations in handwritten work. This is an authorship statement about the
  origin of UBT, not a claim of historical priority over earlier quaternionic
  and biquaternionic formulations of electromagnetism.
- During 2013–2015 he calculated several candidate metric tensors and associated
  algebraic constructions on paper, without AI assistance. These were not merely
  later reconstructions prompted by language models: they formed part of the
  pre-AI mathematical foundation from which the UBT gravity programme grew.
- Commutators and anticommutators already appeared in the early calculations.
  A persistent intuition was that the symmetric algebraic product should encode
  metric information, while antisymmetric or noncommutative structures should
  encode orientation, spin, field strength, or curvature.
- The notebooks also explored Pauli–quaternion correspondences, toroidal
  resonator ideas, longitudinal modes, extended relativistic kinematics, null
  conditions, and a geometric ``invisibility machine'' based on
  biquaternionic-coordinate hypotheses.
- Two especially strong early conclusions are preserved as **historical research
  hypotheses**, not current canonical theorems: that superluminal propagation
  could occur only in a genuinely biquaternionic spacetime and only through
  longitudinal modes, and that a geometry-based invisibility device would
  require biquaternionic coordinates. Their precise scope cannot be judged
  without reconstructing the original derivations.
- Current physics places important constraints on any revival of those claims.
  Ordinary Lorentz transformations preserve the null cone and do not transform
  a causal light signal into a superluminal one; source-free plane
  electromagnetic waves in standard vacuum Maxwell theory are transverse; and
  transformation-optics/metamaterial cloaking can be formulated without
  biquaternionic spacetime coordinates. A viable modern version of the early
  hypotheses would therefore have to specify a nonstandard extension of the
  physical kinematics, a different mode or medium, or a narrower notion of
  geometric invisibility, and then derive experimentally distinguishable
  consequences.
- The modern covariant-tetrad equations, connection reconstruction, and rank
  theorems did not yet exist in their present form, but the algebraic and metric
  intuition from which they later developed was already present.

## 1 August 2026 — Revival of the biquaternionic invisibility program

- The early invisibility hypothesis was restored as an explicit speculative
  research track rather than left only as a historical remark.
- The current covariant-tetrad algebra distinguishes the full ordered tensor
  $\mathfrak G_{\mu\nu}=E_\mu^\sharp E_\nu$ from its symmetric central metric
  channel and antisymmetric biquaternionic channel $\Sigma_{\mu\nu}$.
- This clarified why the noncentral part appeared to disappear: for commuting
  coordinate differentials it cancels from the ordinary quadratic line element,
  although it remains present in the full ordered product and oriented-area
  channel.
- Three separate hypotheses are now tracked: curve-null configurations,
  volume-null central metrics ($\det\gamma=0$), and metric-null but
  biquaternionically active configurations ($\gamma=0$, $\Sigma\ne0$).
- An explicit pointwise algebraic witness for the last class was recorded.
- A subsequent Whitney-type spherical construction supplied one global
  integrable off-shell `Theta` with a null central angular metric, an everywhere
  nonzero invariant biquaternionic area two-form, and exact matching to a flat
  central exterior.
- The first action-regularity audit then proved that the simplest metric-free
  pure-`Theta` sharp-quartic four-form is regular at the null surface but exact
  and topological.  It therefore admits the shell non-selectively and cannot
  provide stability; a non-topological profile-weighted or auxiliary
  first-order action remains the next action-level target.
- No on-shell invisible object, stable degenerate region, or engineering device
  is claimed; action regularity, coupling decoupling, stability, and exterior
  scattering remain open.

## 18 March 2016 — Public biquaternion electroscalar formulation

- A Google Sites post with the embedded date 18 March 2016 publicly documented
  a biquaternion gradient, biquaternion vector potential, generalized
  eight-intensity equation, and a scalar component denoted by `G`.
- The claim is mechanism-specific. It establishes the documented public
  electroscalar formalism, not the later projection-free tetrad theorem or
  Einstein dynamics. Archive and page hashes are listed in
  `docs/priority_evidence/OCTONION_MULTIVERSE_EVIDENCE.json`.

## 1 December 2017 — Periodicity and GR-duality research note

- A dated public research note recorded the author's spacetime-periodicity
  direction and a contemporaneous claim of a relation to general relativity.
- The entry is historical provenance, not a retrospective proof of GR
  equivalence.

## 8 November 2020 — Archived Octonion Multiverse snapshot

- The dated site backup contains the biquaternion theory page and a gravity
  appendix that heuristically links the scalar `G` energy sector to gravity.
- This establishes continuity of the research programme while leaving the
  modern tetrad and dynamical GR claims to the 2025-2026 proof record.

## c. 2019 — Complex time and Jacobi-theta structure

- Complex time became a central element of the developing framework:
  \[
  \tau=t+i\psi.
  \]
- Jacobi theta functions, toroidal periodicity, diffusion, spectral structure,
  and complex-time evolution became increasingly important.
- These ideas prepared the later formulation of a fundamental field
  \(\Theta(q,\tau)\) and the use of periodic analytic structures to connect
  topology, dynamics, and observable spectra.

## Before June 2025 — Consolidation into a broader unification programme

- Earlier biquaternionic, complex-time, and theta-function work was consolidated
  into a programme extending beyond electromagnetism toward gravity, quantum
  equations, gauge structure, particle generations, mass hierarchies, and
  cosmology.
- David Jaroš laid the conceptual foundations of the later **Layer 1**
  programme and opened the first **Layer 2** questions: first build a
  reproducible algebraic and geometric core, then investigate deeper spectral,
  topological, and dynamical selection mechanisms.
- Author-led investigations included the **3-qubit model**, the **SU(3)**
  direction, and related generation structures. These were not outputs of later
  automated repository analysis; they were part of the human-directed research
  programme.
- Much of this period remained exploratory and predated the repository's later
  claim-level and reproducibility discipline.

## June 2025 — AICON Seattle and the start of systematic AI-assisted research

- During **AICON 2025 in Seattle**, David Jaroš decided to make AI assistance a
  systematic part of the UBT research process rather than an occasional writing
  aid.
- The idea of incorporating a **Fokker–Planck equation** into the UBT dynamical
  picture also arose during this Seattle period. It offered a natural language
  for drift, diffusion, probability transport, periodic domains, and the
  emergence of Jacobi-theta solutions.
- The Seattle milestone marks the origin of the idea and research direction;
  the explicit mathematical and repository formulations were developed and
  revised afterward.
- AI systems were used for proposed derivations, symbolic checks, numerical
  experiments, software implementation, documentation, literature-oriented
  comparison, and adversarial review.
- From the beginning, AI outputs were treated as suggestions requiring human
  judgment and reproducible verification. Scientific ownership and final
  responsibility remained with David Jaroš.

## June 2025 — First public formulation of UBT

- The first public UBT formulation was released in June 2025, including an OSF
  publication and a public source repository shortly afterward.
- The central object was formulated as a biquaternion-valued field
  \[
  \Theta(q,\tau)
  \]
  over biquaternionic coordinates and complex time.
- Initial public research tracks addressed the GR limit, Dirac and Schrödinger
  limits, gauge structure, the fine-structure constant, mass hierarchies, dark
  matter candidates, and consciousness-related speculative extensions.
- This stage transformed UBT from a collection of private ideas into a public,
  testable, and versioned research programme.

## 2025 — Expansion of the mathematical and computational programme

- The repository expanded into separate gravity, gauge, alpha, mass, quantum,
  cosmology, and speculative research tracks.
- The Fokker–Planck/Jacobi-theta direction was progressively translated from the
  Seattle insight into more explicit equations and research documents.
- The Layer 1/Layer 2 distinction, 3-qubit constructions, SU(3) structure,
  generation questions, and links between algebra and physical observables were
  developed further under the author's direction.
- Symbolic and numerical verifiers, tests, derivation indexes, and claim levels
  were introduced. Strong early conjectures were increasingly separated from
  conditional or reproducible results.

## May 2026 — First cohesive GR paper

- The paper *General Relativity as a Real-Projected Limit of Unified
  Biquaternion Theory* presented the first cohesive attempt to organise the GR
  programme in a single manuscript.
- It used a projected bilinear of derivatives of \(\Theta\) as the metric
  readout, gave a five-step route to standard GR geometry, and included a
  reproducible numerical check of the spatial Schwarzschild metric.
- The manuscript was an important milestone because it converted the broad GR
  ambition into a concrete proof programme and exposed the exact places where
  representation, variation, dynamics, and uniqueness had to be distinguished.
- Later audits narrowed some of its strongest claims, especially concerning
  variational closure, the temporal Schwarzschild component, uniqueness, and
  the origin of Einstein dynamics. Useful calculations and the overall demand
  for a genuine UBT-native GR sector were retained.

## 2026 — NDC London and the move toward agentic development

- **NDC London in 2026** provided a further impulse for developing a more
  structured, multi-agent research and engineering workflow around UBT.
- The focus moved from ordinary AI-assisted work toward **agentic development**:
  assigning distinct roles such as derivation, verification, hostile review,
  consistency checking, code generation, and status-ledger maintenance.
- This workflow is still human-directed and is not yet fully automated.
  David Jaroš continues to choose research goals, resolve architectural
  questions, approve claims, and decide which proposed changes enter the
  canonical theory. A more automated orchestration platform remains under
  development.

## June–July 2026 — Audits and the explicit GAP-10 programme

- Detailed audits distinguished the ability to represent a metric from the
  stronger task of deriving all ten Einstein equations through variations of
  the fundamental UBT variables.
- `GAP-10` became the central GR closure programme, separating metric rank,
  connection dynamics, integrability, action origin, and on-shell solution
  selection.
- Claim ledgers were revised so that standard GR input, conditional closure, and
  genuinely UBT-native results were no longer treated as interchangeable.

## Early July 2026 — Compact-fiber completion route

- A compact \(\psi\)-fiber route was developed to enlarge the available
  variation space in an induced-metric formulation and obtain rank-ten closure.
- The route was mathematically consistent and demonstrated considerable
  representational flexibility.
- That flexibility also revealed weak canonical selection: multiple redundant
  representations could encode the same geometry without a sufficiently strong
  UBT-native mechanism selecting one of them.
- The route was therefore retained as a historical and exploratory framework,
  not dismissed as a mathematical failure. Some reported constructions remain
  subject to repository-level reproduction before being promoted to verified
  historical results.

## 15–16 July 2026 — Return to the covariant-tetrad architecture

- David Jaroš made the decisive human choice to return the GR programme to the
  original anticommutator and tetrad intuition, now in an explicit covariant
  form:
  \[
  E_\mu=\frac{1}{\sqrt{\mathcal N_0}}D_\mu\Theta,
  \qquad
  \frac12\left(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu\right)
  =g_{\mu\nu}\mathbf 1.
  \]
- This was not an autonomous AI pivot. The initial pressure for a tetrad/
  Clifford formulation and the later decision to restore it were both driven by
  the author's physical and algebraic intuition, with AI support used to
  formalise and audit the consequences.
- The metric was no longer based on an arbitrarily chosen real projection or
  fiber average; it arose from the central symmetric product of a
  biquaternionic tetrad.
- The local metric rank became
  \[
  16\text{ tetrad components}-6\text{ Lorentz gauge directions}
  =10\text{ metric components}.
  \]
- The programme then developed the relation between Christoffel symbols,
  frame/spin connections, torsion, and contorsion; an explicit affine
  single-field Minkowski representative; a conditional one-sided connection
  no-go; and a two-sided bimodule connection as the current minimal escape
  route.

## 16 July 2026 — Release v10.2.0: Covariant Tetrad and Connection Milestone

- Release `v10.2.0` publicly archived the projection-free tetrad metric, full
  local metric rank, explicit Minkowski realisation, and reconstruction of a
  metric-compatible connection from tetrad plus torsion.
- The release explicitly retained curved on-shell generation and the derivation
  of Einstein dynamics from the canonical UBT action as open problems.
- GitHub release tagging and automatic Zenodo archiving created a stable,
  citable record of this architectural milestone.

## From 16 July 2026 — Chinese AI models join the workflow

- From **16 July 2026**, Chinese-developed AI models were added to the UBT
  multi-model research environment.
- They were used alongside Western and local models for independent derivation
  attempts, code and proof review, mathematical criticism, and cross-checking of
  model-specific assumptions.
- No model family was granted privileged authority. Agreement between models
  counted as useful evidence only when supported by explicit mathematics,
  reproducible code, or primary-source verification.

## July 2026 — Architecture freeze, agent safeguards, and reproducible builds

- The covariant-tetrad architecture was frozen for the `v10.x` development
  line.
- The rule **architecture before repair** was adopted: before adding fields,
  dimensions, fibers, projections, or auxiliary modes, researchers and agents
  must first test whether the apparent obstruction is an artifact of the chosen
  formulation.
- Standard Cartan/tetrad geometry was explicitly separated from UBT-specific
  contributions.
- Repository-wide LaTeX workflows were redesigned to attempt all active PDF
  roots, continue after individual failures, preserve logs, publish successful
  builds, and protect the exact source-commit provenance of generated PDFs.
- Agentic tooling continued to expand, but canonical decisions remained subject
  to explicit human approval.

## July 2026 — Conditional GR subclosures toward v10.3.0

- In a minimal Palatini/Einstein–Cartan branch, the Cartan torsion map was
  verified to have full pointwise rank, so zero spin current gives zero torsion
  and specified spin current determines contorsion.
- The Lorentz real slice was characterised as the fixed set of a natural
  involution, with conditional symmetry-propagation results for its dynamical
  preservation.
- Exact augmented-holonomy criteria were formulated for local integrability when
  the tetrad and paired connections are prescribed.
- Under minimal Palatini and four-dimensional Lovelock assumptions, the
  low-energy gravitational tensor structure was conditionally narrowed to
  \[
  G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T_{\mu\nu}.
  \]
- This fixes the possible low-energy tensor form under the stated assumptions;
  the values and signs of \(\kappa\) and \(\Lambda\), and the derivation of those
  infrared assumptions from the fundamental UBT action, remain open research
  problems.

## Research method and verification discipline

- The author compares major structural results with physical intuition and with
  calculations developed by hand before the use of generative AI.
- Most decisive claims are subjected to logical criticism and to adversarial
  comparison across multiple model families rather than accepted from a single
  model output.
- At the exploratory stage, this process does not imply that every intermediate
  proof has already received a complete line-by-line human verification.
- Before a result is treated as final, the intended standard is a definition-by-
  definition and line-by-line review, reproducible symbolic or numerical checks
  where applicable, and ultimately independent human scrutiny.
- Multi-model agreement is treated as a useful error-detection mechanism, not as
  proof by consensus. Canonical status is controlled by explicit assumptions,
  derivation ledgers, tests, and human approval.

## Author-led decisions in the AI-assisted era

The following list is deliberately explicit because the research increasingly
uses AI tools, while the scientific direction remains human-authored. Major
choices made, initiated, or persistently defended by David Jaroš include:

- maintaining biquaternionic algebra as the non-negotiable mathematical core;
- placing Jacobi's theta function and complex time at the centre of UBT;
- introducing the Fokker–Planck direction after the Seattle 2025 insight;
- defining the Layer 1 programme and initiating Layer 2 investigations;
- developing the 3-qubit model, SU(3) direction, and generation structures;
- insisting that GR be derived from UBT-native principles rather than accepted
  as an independent metric theory;
- pressing the initial tetrad/Clifford interpretation and later deciding to
  restore the covariant-tetrad architecture;
- deciding which AI suggestions were accepted, revised, rejected, or retained
  only as exploratory work;
- creating a claim and audit discipline in which attractive calculations do not
  become canonical without reproducible support.

This list is not exhaustive. It can be extended as older notebooks, emails,
conference notes, commits, and research discussions are reviewed.

## Selected external context for the early programme

The historical wording above is intentionally narrower than the original
private conclusions. It is consistent with the following established context:

- quaternionic and biquaternionic representations of electromagnetism predate
  UBT, including Ludwik Silberstein's early twentieth-century work and the
  later Riemann–Silberstein formalism;
- the Lorentz group preserves the Minkowski interval and the vacuum light cone;
- standard transformation optics provides theoretical and experimental
  electromagnetic cloaking mechanisms using anisotropic material parameters.

Useful reference points include J. B. Pendry, D. Schurig, and D. R. Smith,
“Controlling Electromagnetic Fields,” *Science* **312** (2006), 1780–1782,
doi:10.1126/science.1125907, and D. Schurig et al., “Metamaterial
Electromagnetic Cloak at Microwave Frequencies,” *Science* **314** (2006),
977–980, doi:10.1126/science.1133628. These references do not decide whether a
more specific UBT construction is possible; they delimit what cannot be claimed
solely from the existence of quaternionic notation or standard Lorentz
transformations.

### 2026-08-01 — Hermitian support Gram for the null-shell track

The invisibility audit distinguished zero visible metric volume from zero
field-space support.  For the global Whitney shell, the central sharp metric
has a null angular block, while the scalar Hermitian Gram built with `ddagger`
is smooth and positive definite on the same sphere.  This established an exact
nonzero internal support area and a regular candidate support-volume action
route.  The result remained noncanonical because a full Lorentz/gauge-covariant
clock or compensator and a finite-radius stabilising dynamics were not derived.

### 2026-08-01 — Conditional clock compensation of the shell support Gram

The dedicated clock Fourier component of the explicit Whitney-shell field was
used to construct a Hermitian matrix compensator from the same `Theta`.  A
weighted trace Gram was proved invariant under the standard local `SL(2,C)`
paravector congruence and reduced exactly to the previously computed positive
support Gram on the shell.  The construction also produced an invariant scalar
clock equal to `t` on the ansatz and a regular Lorentzian internal support
tensor.  The result remained conditional and noncanonical because the clock
mode was selected by the shell ansatz rather than uniquely derived from the
master action, and full paired left/right covariance was still open.

## Current direction

The current programme keeps the covariant-tetrad architecture fixed and focuses
on the remaining bridges:

- derive the paired connections, torsion sector, and low-energy action from
  fundamental UBT principles;
- solve the self-consistent curved system for \(\Theta\), tetrad, and connection;
- derive rather than assume the Palatini/Lovelock infrared conditions;
- determine the normalization, Newton coupling, and cosmological constant;
- select Schwarzschild, cosmological, and perturbative solutions on shell;
- continue developing a human-governed agentic research platform while keeping
  every canonical claim auditable and reproducible.

The history of UBT is not a sequence of discarded theories. It is a progressive
refinement from long-standing physical intuition, through increasingly explicit
mathematics and computational testing, toward a smaller and more clearly stated
set of proof obligations. Its historical interest lies not only in the eventual
fate of the theory, but also in the attempt to combine independent invention,
engineering discipline, mathematical synthesis, and human-governed artificial
intelligence within one sustained research programme.

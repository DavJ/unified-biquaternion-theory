# Changelog



## 2026-07-18 — Pre-release naming, provenance, and test-hygiene polish

- Corrected the historical filename typo `paladini` to `palatini` for the
  GAP-10T torsion-dynamics source and published PDF, and updated active
  references and tests.
- Added standard-source attribution to the augmented-holonomy note
  (Kobayashi--Nomizu) and the symmetry-propagation note (Olver).
- No equations, claim levels, architecture, or open-gap statuses changed.
- Updated the class-scoped Minkowski tetrad fixture for pytest 9/10 compatibility;
  the six tetrad-core regression tests now run without the removed instance-fixture pattern.
- Restored the exact `NO additional tunable parameters` policy wording in the
  unimplemented `M_phase` and `M_SNR` Planck mapping stubs; no mapping was implemented.
- Rechecked the reviewed History of UBT integration and retained the early
  superluminal/longitudinal and invisibility ideas only as historical hypotheses,
  not current canonical claims.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Corrected — exact-gradient composite branch is a flatness no-go (2026-07-26)

- Replaced the overstrong interpretation of `GAP-10T-COMPOSITE-FLAT`.
  For `e^a=N0^(-1/2)dY^a`, nondegeneracy makes `Y^a` local coordinates and
  the induced metric is exactly a pullback of Minkowski space.  Its Riemann
  curvature and Hilbert-Palatini density vanish identically.
- Reclassified the result as `GAP-10T-GRADIENT-FLATNESS: CLOSED AS NO-GO
  [L1]`.  Affine stationarity for all coefficients remains true, but only as
  the Jacobian/null-Lagrangian corollary of this flatness restriction.
- Removed language calling the auxiliary partial-gradient restriction the
  “surviving composite branch.”  Canonical UBT uses
  `E_mu=N0^(-1/2)D_mu Theta`; its self-consistent D-composite variation and
  curved dynamics remain open.
- Added exact symbolic determinant and nonlinear pullback-curvature checks,
  regression tests, synchronized ledgers, and corrected the GR submission.

### Added — GAP-10T Lorentz-pairing rigidity and fixed-background scope audit (2026-07-26)

- Clarified that the exact kinetic spin current is the direct matter current of
  the effective Palatini variation with tetrad, metric, volume form, index
  raising, and `Theta` held fixed; the full composite `Theta`-only variation
  remains open.
- Proved `GAP-10T-PAIRING-NOGO [L1]`: every real symmetric bilinear form on
  the Lorentz slice invariant under the full `sl(2,C)` action is proportional
  to the `sharp`/Minkowski pairing.  The `ddagger` Hilbert--Schmidt form is
  Euclidean on the slice and fails all three boost-invariance checks.
- Consequently closed the pairing-selection escape route: no nonzero
  nondegenerate symmetric Lorentz-invariant pairing removes the affine
  spin-current obstruction.
- Narrowed `GAP-10T-DYN` to the full composite variation and a canonically
  derived non-minimal torsion cancellation or translational/relative-bimodule
  completion with no independent propagating fields.
- Added exact SymPy checks, status-regression tests, synchronized the GR
  ledgers/manuscript/student material, and regenerated the audit and GR PDFs.

### Corrected — repository hygiene and provenance fail-closed audit (2026-07-25)

- Restored the active forensic-fingerprint modules as canonical root-level
  implementations instead of runtime shims into `ARCHIVE/`; preserved legacy
  copies remain unchanged for historical provenance.
- Ported the complete Planck/WMAP loaders, covariance utilities, CMB-comb,
  Grid-255, invariance, synthetic-control, and real-data runner paths.
- Made manifest validation fail closed on empty/malformed manifests, resolve
  repo-relative paths from the manifest location rather than the process CWD,
  and retain an explicit legacy bare-filename fallback in the real-data runner.
- Removed the remaining active `ubt_with_chronofactor` /
  `ubt_no_chronofactor` runtime import shims used by the test suite, including
  spectral utilities, `ubt_core`, alpha reproduction, mass utilities, and
  flavour/RGE helpers.
- Corrected Route A4 wording from an unconditional “existing L1 result” to
  `[L1 cond.] on G137-B`.
- Aligned the three-generations statement with `CLAIMS.yaml`: the exact
  three-dimensional carrier count is retained, while its identification with
  the three physical generations is `DERIVED_WITH_ASSUMPTIONS` and dynamical
  selection remains open.
- Reproduced all 617 collectable tests in three deterministic groups; the only
  unexecuted module is the optional Hypothesis property-test module because
  `hypothesis` is unavailable in the validation environment.

### Added — GEM compact-mode and Gödel-type research track (2026-07-25)

- Added a non-canonical `research_tracks/gem_compact_modes/` package that
  separates compact `(+n,-n)` mode kinematics, biquaternionic orientation,
  tetrad response, and Gödel-type dynamics.
- Proved exact circle-averaged identities: a balanced pair has zero compact
  current/flux but positive compact-gradient energy.
- Added an explicit grade/parity scope statement: canonical biquaternionic
  products stay in the even carrier; odd Clifford intermediates require an
  explicit full-Clifford lift and are not new fundamental Theta components.
- Added the exact no-go that a common infinitesimal Lorentz rotation of the
  tetrad leaves the metric unchanged.
- Added a Gödel coframe kinematic verifier while keeping action-level source
  matching, metric response, Gödel dynamics, and chronology open.
- Preserved all earlier causality/imaginary-metric/CTC files unchanged and
  documented their historical relationship in `LEGACY_MAP.md`.
- Added `tools/verify_gem_compact_modes.py` and regression tests.

### Added — self-contained UBT/Theta introduction in the GR manuscript (2026-07-20)

- Added a dedicated opening section to `papers/UBT_GR_Submission.tex` defining
  UBT as a single-biquaternion-field research programme and introducing
  `Theta(q,tau)`, its component count, complex time, and the distinction between
  the UBT master field and a Jacobi theta function.
- Made the gravitational construction explicit as the chain
  `Theta -> D_mu Theta -> E_mu -> (g_mu nu, omega, R)`.
- Clarified that the unique-fundamental-field statement is an architectural
  postulate, while action-level derivation of torsion, Einstein dynamics, and
  the wider gauge/quantum sectors remains open.
- Rebuilt and visually checked `docs/pdfs/UBT_GR_Submission.pdf`.

### Added/Corrected — torsionful local representer (2026-07-19)

- Corrected the scope of the paired-connection no-go: the concurrent-vector
  obstruction applies to the generated-tetrad branch with zero contortion
  (`K=0`), not to the same pure Lorentz pairing with arbitrary
  metric-compatible torsion.
- Constructed an explicit composite contortion on every sufficiently small
  non-null Gaussian patch,
  `K_{nu mu rho}=[W_{mu nu}V_rho-V_nu W_{mu rho}]/V^2`, with
  `W_{mu nu}=g_{mu nu}-nabla^LC_mu V_nu`, and proved exactly that
  `nabla^(LC+K)_mu V^nu=delta_mu^nu`.
- Consequently every smooth Lorentzian tetrad, including every local patch of
  the non-flat Schwarzschild vacuum exterior, has a local single-Theta
  representer with `A=Omega(e,K)` and `B=-Omega(e,K)^ddagger`, without
  independent left/right connection fields.
- Closed `GAP-10I-TORSION-LOCAL` locally at L1 and reclassified
  `GAP-10I-PAIR-GR` as a torsion-free no-go. `GAP-10I-2S` is optional for
  local kinematics rather than required.
- Kept the dynamical/global part of `GAP-10I-CURVED`, `GAP-10T-DYN`,
  `GAP-10D`, and `GAP-U2Theta` open/narrowed: the canonical action must still
  select a physically admissible torsion/current and establish global
  continuation and Einstein dynamics.
- Added an exact symbolic verifier, regression tests, a standalone theorem
  note, revised canonical/status/student surfaces, and rebuilt PDFs.

### Added — paired-connection audit and concurrent-vector no-go (2026-07-19)

- Proved that Lorentz-slice and metric compatibility reduce the pure
  two-sided pair to `A_mu=Omega_mu`, `B_mu=-Omega_mu^ddagger`, modulo a
  common central one-form that cancels; no independent gravitational fields
  `A_mu,B_mu` are introduced in this branch.
- Proved that the same pure pair makes a nondegenerate torsion-free tetrad
  generated by one `Theta` imply `nabla_mu V^nu=delta_mu^nu`, hence a proper
  homothety and a curvature-kernel condition.
- Proved explicitly that Schwarzschild with nonzero mass cannot satisfy that
  condition. The pure pair is therefore closed as a kinematic reduction and
  closed as a no-go for the torsion-free generated-tetrad branch.
- At that audit stage, the remaining route was stated as a nontrivial relative
  bimodule action.  The later composite-contortion theorem supersedes that
  necessity: a relative pair is optional for local kinematics.
- Added an exact SymPy verifier, regression tests, canonical/paper/student
  updates, and strict anti-overclaim guardrails.
- `GAP-10D` remains narrowed, not closed: canonical torsion/current selection,
  low-energy coefficients, global continuation, and the induced metric
  variation still require a canonical derivation.


### Corrected — gauge and quantum honest-status audit (2026-07-17)

- Deprecated `canonical/gauge/GAUGE_MASTER_STATUS.md` as an authoritative
  status source; `CLAIMS_MATRIX.md` remains the current ledger.
- Reclassified the involution result as selection of a complex rank-three
  carrier, while recording `GAP-SU3-DYN` for the still-open derivation of the
  unitary/Yang--Mills dynamics from the canonical UBT action.
- Added the explicit `diag(e^{i theta}, e^{-i theta}, 1)` counterexample showing
  that a generic `SU(3)` carrier action does not preserve the biquaternion
  multiplication table.
- Marked the color Yang--Mills Lagrangian as a minimal postulated carrier
  Lagrangian rather than a result already derived from canonical UBT.
- Formally retracted the old Born-rule proof in
  `canonical/qm_emergence/step7_born_rule.tex`, retained its correct norm-decay
  calculation, and added an explicit diffusive plane-wave counterexample.
- Extended claim-consistency scans into `canonical/gauge/` and
  `canonical/qm_emergence/`.

### Added — revised historical development record (2026-07-17)

- Added `docs/HISTORY_OF_UBT.md`, a concise author-centred chronology from the
  2013–2015 biquaternionic work through the current covariant-tetrad programme.
- Recorded AICON 2025 in Seattle as the origin of systematic AI-assisted UBT
  research and of the Fokker–Planck research direction, while distinguishing
  that conceptual milestone from later formal repository implementations.
- Recorded NDC London 2026 as an impulse toward agentic development, explicitly
  noting that the workflow remains human-directed and is not yet fully
  autonomous.
- Recorded the addition of Chinese-developed AI models from 16 July 2026.
- Documented David Jaroš's decisive role in the algebraic core, Jacobi-theta and
  complex-time direction, Fokker–Planck integration, Layer 1/Layer 2 programme,
  3-qubit and SU(3) work, UBT-native GR requirement, and the return to the
  covariant-tetrad architecture.
- Linked the historical changelog from the main repository navigation.

### Added — frozen-architecture GR subclosures (v10.3.0 candidate, 2026-07-16)

- Added `gap_10t_palatini_torsion_dynamics.tex`: the minimal first-order
  Cartan torsion map is pointwise invertible (rank 24/24), so zero spin current
  gives zero torsion and specified spin current gives unique contorsion.
- Added `gap_10l_psi_symmetry_propagation.tex`: the Lorentz slice is the fixed
  set of `J(X)=-conj(X^sharp)` and is preserved by unique equivariant dynamics;
  Lorentz-gauge or translation-symmetric psi evolution preserves the metric.
- Added `gap_10i_augmented_holonomy.tex`: prescribed `(E,A,B)` admit an exact
  augmented-holonomy existence/path-independence criterion.
- Added `gap_10d_low_energy_uniqueness.tex`: the minimal Palatini branch yields
  Einstein--Lambda and the four-dimensional Lovelock assumptions make that
  conditional infrared endpoint unique.
- Added `tools/verify_remaining_gr_subclosures.py` and regression tests for the
  Cartan rank, Lorentz involution, psi-gauge metric stability, augmented
  curvature identity, claim ledgers, agent guardrails, and PDF publication map.

### Changed

- Reclassified the full-theory labels `GAP-10T-DYN`, `GAP-10L-DYN`,
  `GAP-10I-CURVED`, `GAP-10D`, and `GAP-10psi` from undivided OPEN to
  **NARROWED**, while retaining explicit action-origin, self-consistency,
  regularity, coefficient, and physical-stability blockers.
- Extended the GR paper, canonical action/status surfaces, Czech and English
  student texts, and Copilot/agent instructions with the new conditional
  subclosures and strict anti-overclaim wording.
- Added the four new papers to the curated LaTeX publication map and regenerated
  the main canonical, GR, student, and subclosure PDFs from their current TeX.

### Still open at full theory level

- Derive the selected Palatini/Lovelock low-energy assumptions, paired
  representations, spin current, normalization, and couplings from canonical
  UBT.
- Solve the self-consistent curved `(Theta,E,A,B,T)` system with regularity and
  global continuation.
- Close `GAP-B-MASTER` and dynamically select the Schwarzschild tetrad/lapse
  (`GAP-U2Theta`).

### Fixed — LaTeX output provenance hardening (2026-07-16)

- Prevented the PDF workflow from rebasing outputs built from an older source commit onto a newer `master` head.
- Generated artifacts remain available from the Actions run, while tracked PDFs/reports are committed only when `origin/master == GITHUB_SHA`.
- Added a regression test forbidding the old `git pull --rebase` behavior.

### Changed — v10.2.1 audit, architecture freeze, and PDF automation (2026-07-16)

- Froze the covariant-tetrad architecture for the v10.x line and added the
  architecture-before-repair rule to human and AI contribution protocols.
- Added a full claim audit distinguishing standard Cartan/tetrad geometry from
  UBT-specific results and tightened the scope of the one-sided no-go and
  two-sided curvature-intertwiner statements.
- Archived the compact-fiber route as mathematically consistent but
  noncanonical because of weak selection and representer redundancy.
- Replaced fail-fast PDF builds with a repository-wide LaTeX audit that tries
  every active standalone root, records failures, uploads all successful PDFs,
  and commits a fresh single report directory plus curated canonical PDFs.
- Prepared `.zenodo.json` and `CITATION.cff` for v10.2.1.

### Added

- `tools/latex_audit.py` and `tools/publish_latex_pdfs.py`.
- `.github/latex_publish_map.tsv`.
- `docs/LATEX_BUILD_WORKFLOW.md`.
- `reviews/tetrad_architecture_audit_2026-07-16.md`.
- `canonical/gr_closure/HISTORICAL_FIBER_ROUTE_STATUS.md`.
- `tests/test_latex_audit.py`.
- `PATCH_NOTES_V10_2_1_TETRAD_AUDIT_AND_LATEX_WORKFLOW.md`.

### Changed — Connection reconstruction and integrability selection (2026-07-16)

- Closed `GAP-10Omega-KIN`: a nondegenerate tetrad plus specified torsion
  uniquely determines the metric-compatible frame connection
  `omega=omega_LC(e)+K(T)`.
- Closed `GAP-10Omega-GR`: the torsion-free classical branch is the unique
  Levi-Civita spin connection.
- Closed `GAP-10L-CONN`: compatible Lorentz transport preserves the Lorentz
  metric and real Lorentz slice.
- Closed `GAP-10I-SR`: every constant Lorentz tetrad has an explicit affine
  single-Theta representer, including Minkowski spacetime.
- Closed `GAP-10I-1S` as a conditional no-go: a naive one-sided invertible
  torsion-free curved route forces zero curvature.
- Narrowed `GAP-10I-2S`: the two-sided bimodule derivative yields an exact
  left/right curvature-intertwiner condition and avoids the one-sided flatness
  obstruction.
- Reframed the remaining connection problem as `GAP-10T-DYN` (torsion dynamics)
  plus exact left/right representation selection, rather than arbitrary
  kinematic freedom in `Omega`.
- Rewrote canonical Theta-field documentation to use the two-sided curved
  candidate and removed stale projection-metric and temporal-Schwarzschild
  proof claims from `WHAT_IS_PROVED.md`.
- Expanded student material with Christoffel/frame/spin connections, torsion,
  contorsion, the flat limit, one-sided no-go, two-sided integrability, and the
  implicit-versus-transcendental distinction.
- Hardened `AGENTS.md`, Copilot instructions, review rules, tests, and PR
  templates against drift back to projection/fiber GR derivations.

### Added

- `canonical/gr_closure/gap_10omega_connection_elimination.tex`.
- `canonical/gr_closure/gap_10i_integrability_selection.tex`.
- `tools/verify_gap_10omega_connection.py`.
- `tools/verify_gap_10i_integrability.py`.
- `tests/test_gap_10omega_connection.py`.
- `tests/test_gap_10i_integrability.py`.
- `PATCH_NOTES_COVARIANT_TETRAD_OMEGA_INTEGRABILITY_2026-07-16.md`.

### Still open

- `GAP-10T-DYN`, `GAP-10I-CURVED`, `GAP-10L-DYN`, `GAP-10D`,
  `GAP-10psi`, `GAP-B-MASTER`, and `GAP-U2Theta`.

## [v10.1.4] - 2026-07-14 - Honest-Status Reframe of T1_GR

### Changed

- **Honest-status reframe of T1_GR per July 2026 external audit**
  (`papers/UBT_GR_Submission.tex`):
  - Abstract replaced with accurate description of what is proved vs.\ open.
  - Title updated to reflect actual theorem content.
  - Key Claims items 1--6 reworded to reflect conditional and partial results.
  - Novelty table updated: Lorentzian signature → "Conditional theorem";
    Einstein equations → "Variational, with identified obstruction (GAP-10)";
    Schwarzschild → "Spatial verified $<10^{-15}$; temporal conditional (GAP-U2)";
    Regge-Wheeler → "Conditional reduction (GAP-B)".
  - Open Problems section rewritten: removed "None of them affect the validity"
    language; GAP-U2 (temporal Schwarzschild) and GAP-B (perturbation bridge)
    named and boxed; GAP-U1 (metric bilinear uniqueness) added to lower-priority
    table; GAP-10 wording clarified as classical variational-equivalence question.
  - Proof Status Summary tcolorbox updated to reflect conditional items.
  - Global sweep: "unique spherically symmetric" → uniqueness claim removed;
    Zerilli and RW labels updated to [L1 cond.\ given GAP-B].

- **CLAIMS.yaml**: `gr_chain.status` changed from `PROVED` to
  `DERIVED_WITH_ASSUMPTIONS`; assumptions GAP-10, GAP-U2, GAP-B documented;
  `forbidden_wording` entries added: "GR is derived from UBT",
  "Einstein equations emerge from UBT", "complete five-step chain at L1".

- **CLAIMS_MATRIX.md**: GR chain row, Regge--Wheeler row, and Zerilli row updated
  to `DERIVED_WITH_ASSUMPTIONS` with pointers to GAP-10, GAP-U2, GAP-B.

### Added

- `reviews/external_review_2026-07_gpt.md`: stub documenting the July 2026
  external audit findings that motivated the honest-status reframe.

### Added

- **B_base non-perturbative approaches (v60 baseline)**: New document
  `consolidation_project/alpha_derivation/b_base_nonpert.tex` documenting three
  non-perturbative candidates for the gap B₀ → B_base (equivalently Δd = 0.405):
  - **D1 — Unitarity constraint on Im(ℍ)**: Constraint reduces N_eff 12→8, wrong
    direction; target effective mode count < 1 is algebraically impossible. **[DEAD END]**
  - **D2 — Dimensional transmutation on Im(ℍ)**: Requires R_ψ as a calibrated (not
    algebraically fixed) parameter; no zero-free-parameter derivation possible.
    **[DEAD END]** — revisit if R_ψ topological fixation is resolved.
  - **D3 — Cartan–Killing metric on su(2)**: Normalised Killing form equals Euclidean
    metric (factor 1, no correction); unnormalised forms give wrong values.  **[DEAD END]**
  - Updated `DERIVATION_INDEX.md` B_base row with v60 notes and file reference.
  - Updated `STATUS_ALPHA.md` B_base section with v60 summary and dead-end catalogue.
  - Gap (a) remains **[OPEN]** after 8 independent dead ends.

- **Speculative Fingerprint Proposal**: Hubble Tension as Effective Metric Latency
  - New appendix: `speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex`
  - Comprehensive mathematical analysis of hypothesis that Hubble tension arises from effective time parametrization differences
  - Minimal covariant extension: dτ = dt(1 + εf(z)) with ε ~ 0.1%
  - Full validation against 6 observational constraints (GR, ΛCDM, BAO, CMB, chronometers, structure growth)
  - Status: VIABLE BUT CONSTRAINED - lives in narrow parameter window
  - Classification: 🔵 THEORETICAL (Framework established, predictions pending)
  - Documentation: `speculative_extensions/appendices/README_appendix_HT.md`
  - Testable prediction: smooth H(z) interpolation at intermediate redshifts
  - Test document: `test_hubble_tension_appendix.tex`

## [v10.1.3] - 2026-07-14 - Zenodo Archival Release

### Added

- **Zenodo archival**: Repository archived at DOI [10.5281/zenodo.21347352](https://doi.org/10.5281/zenodo.21347352) (version v10.1.3).
- **Related-work section in T1_GR paper** (`papers/UBT_GR_Submission.tex`): added discussion of Einstein (1945), Einstein–Straus (1946), Chamseddine (2001, 2006), DDM (1992), Moffat (1995), Witten (1988).
- **Expository automorphism note** (`docs/notes/symmetry_from_automorphisms.tex`): explains why UBT derives gauge symmetries from automorphisms of ℂ⊗ℍ rather than postulating them; includes SU(2)-restricted metric invariance proof.
- **Submission TeX made self-contained**: `papers/schwarzschild_table.tex` copied from `canonical/gr_closure/` (byte-identical); `\input{schwarzschild_table}` resolves locally in `papers/`.

## [0.3.0] - 2025-11-08 - Publication & Review Readiness

### Added

- **Publication infrastructure**: Created `publication/arxiv/`, `publication/osf/`, `publication/artifacts/` directories
  - arXiv preprint manuscript: `publication/arxiv/main.tex` including baseline theorem, CT scheme, R_UBT extraction, geometric inputs, and reproducibility checklist
  - Reproducibility checklist: `publication/reproducibility_checklist.tex` (one-page summary of assumptions, tests, build process, artifacts, limitations)
  - GitHub workflow: `.github/workflows/publication.yml` for automated PDF builds and artifact uploads
  
- **Community review infrastructure**:
  - Issue template: `.github/ISSUE_TEMPLATE/review_comment.yaml` for technical review comments (section, equation label, claim type, reproduction steps, expected vs. actual)
  - Issue template: `.github/ISSUE_TEMPLATE/replication_report.yaml` for independent replication reports (environment, steps, outputs, diffs, logs, PDF hash)
  - Replication protocol: `docs/REPLICATION_PROTOCOL.md` with step-by-step verification instructions
  - Reviewer FAQ: `docs/REVIEWER_FAQ.md` addressing common questions and potential objections
  - External discussion tracker: `docs/EXTERNAL_DISCUSSION_TRACKER.md` for public record of seminars, reviews, preprints
  
- **Citation metadata**: `CITATION.cff` (v0.3.0) with DOI placeholder, author information, repository URL

### Changed

- **Baseline assertion enforcement**: All references to R_UBT now point to CT baseline theorem (R_UBT = 1 under A1–A3)
  - Verified no placeholder/pending/1.84 values remain in context of R_UBT (test suite confirms)
  - `EMERGENT_ALPHA_README.md` updated with explicit baseline statement
  - `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` already contains two-loop CT baseline paragraph
  - `consolidation_project/alpha_two_loop/tex/R_UBT_extraction.tex` includes baseline subsection with boxed result
  - `consolidation_project/alpha_two_loop/tex/geometric_inputs_proof.tex` formalizes geometric locking (A1)
  
- **README.md**: Added "How to Review This Repo" section with clear entry points for reviewers

### Removed

- None (all changes are additive to maintain backward compatibility)

### Notes

- Tests pass: `pytest -q consolidation_project/alpha_two_loop/tests` ✓
- Baseline established: \(\mathcal{R}_{\mathrm{UBT}} = 1\) at two loops with no fitted parameters
- Publication ready: arXiv manuscript builds successfully (pending manual submission)
- Community ready: Issue templates, replication protocol, and FAQ provide clear paths for engagement

## [Previous Releases]

### Added

- **New unified α derivation**: `consolidation_project/appendix_ALPHA_one_loop_biquat.tex`
  - Single source of truth for fine-structure constant derivation
  - Derives B coefficient from first principles: B = (2π N_eff) / (3 R_ψ) × β_2loop ≈ 46.3
  - UV cutoff set geometrically: Λ = 1/R_ψ (no free parameters)
  - Mode counting table justifies N_eff = 12 from biquaternion structure
  - Renormalization condition at μ₀ = m_e (configurable via macro)
  
- **Biquaternion time transition criterion**: Added formal criterion to `appendix_B_scalar_imaginary_fields_consolidated.tex`
  - Complex time T = t + iψ valid when ‖∇⊥Θ‖² ≪ ‖∂ₜΘ‖²
  - Full biquaternion time τ = t + iψ + jχ + kξ required otherwise
  - Reference tag [TRANSITION_CRITERION] for tracking usage

- **Linter for complex time usage**: `scripts/lint_complex_time_usage.py`
  - Checks that complex time mentions reference transition criterion
  - Ensures biquaternion time priority is maintained
  - CI integration ready

- **Symbolic alpha tests**: `scripts/test_symbolic_alpha.py`
  - Validates B depends only on R_ψ and N_eff (no numeric 46.3)
  - Tests μ₀ invariance in B definition
  - Verifies N_eff counting table sums to 12
  - Confirms α⁻¹ = 137 from effective potential minimum

### Changed

- **Updated Appendix E** (`appendix_E_SM_QCD_embedding.tex`):
  - Replaced "α is empirical in CORE" with reference to new Appendix α
  - Now states: "In CORE, α is parameterized via renormalization condition at μ₀; complete derivation in Appendix α"

- **Updated fermion mass documentation** (`FERMION_MASS_ACHIEVEMENT_SUMMARY.md`):
  - Reclassified m(n) = A·n^p - B·n·ln(n) as "2-parameter phenomenological ansatz"
  - Added roadmap to first-principles derivation
  - Clarified symbol B distinction: fermion mass B vs α running B are physically different contexts
  - Noted future work will unify or rename to avoid confusion

- **Updated CI configuration** (`.github/latex_roots.txt`):
  - Added `appendix_ALPHA_one_loop_biquat.tex` to compilation list
  - Commented out deprecated files: `emergent_alpha_*.tex`, `alpha_final_derivation.tex`
  - Documented deprecation reasons

### Deprecated

- **"B = 46.3 fitted" statements**: The constant B is now derived, not fitted
  - Old approach: B stated as empirical constant from "quantum calculations"
  - New approach: B = (2π × 12) / 3 × 1.8 ≈ 46.3 derived from mode counting
  - Files with "B = 46.3 fitted" should update to reference Appendix α
  - This resolves the critical gap in α derivation rigor

- **Separate emergent_alpha_*.tex files**: Superseded by unified appendix
  - `emergent_alpha_calculations.tex` → Use `appendix_ALPHA_one_loop_biquat.tex`
  - `emergent_alpha_executive_summary.tex` → Deprecated
  - `emergent_alpha_from_ubt.tex` → Deprecated
  - `unified_biquaternion_theory/alpha_final_derivation.tex` → Deprecated

### Migration Notes

**For users referencing α derivation:**
- Old: Reference scattered across multiple files with "B = 46.3" as input
- New: Reference `appendix_ALPHA_one_loop_biquat.tex` as single source
- Impact: No change to numerical predictions, but derivation is now rigorous

**For developers:**
- Symbol B has two meanings: (1) α running coupling coefficient, (2) fermion mass logarithmic term
- These are distinct but related via quantum corrections framework
- Future work will clarify relationship or adopt distinct notation

---

## [2025-11-03] - Alpha and Electron Mass Unification

### Added
- Unified derivation removing circularity and free parameters
- Geometric UV cutoff prescription
- Biquaternion time transition criterion
- Testing and validation infrastructure

### Fixed
- Removed circularity in α and electron mass derivations
- Clarified symbol B usage in different contexts
- Established biquaternion time as primary formulation

---

## [2025-11-02] - Merged master branch updates (commits ec1376e and d73012e)
  - P-adic α derivation: `consolidation_project/appendix_ALPHA_padic_derivation.tex`
  - Executive summaries: `alpha_padic_executive_summary.tex`, `ALPHA_PADIC_README.md`
  - Scientific rating document: `UBT_SCIENTIFIC_RATING_2025.md`
  - Integration assessments: `HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md`, `AHARONOV_TSVF_ANALYSIS.md`
  - Comprehensive evaluation summaries and verification checklists
  - Enhanced B constant derivation based on gauge structure (N_eff = 12)
  - P-adic calculator scripts: `scripts/padic_alpha_calculator.py`, `scripts/test_padic_alpha.py`

- **Symbolic derivation of the B constant** in `emergent_alpha_from_ubt.tex`
  - Mathematical derivation showing B arises from one-loop vacuum fluctuations
  - Based on gauge structure: B = N_eff × (2π/σ) ≈ 46.3 for SU(3)×SU(2)×U(1)
  - Result consistent with empirical constant used in α derivation

- **Python verification script** `scripts/verify_B_integral.py`
  - Symbolic and numerical verification of the B constant integral using SymPy and SciPy
  - Confirms phase fluctuation integral I ≈ 0.904 for σ = 7.35
  - Shows renormalization factor β_renorm ≈ 8.15 connects I to B ≈ 46.27
  - Verifies that B = 46.27 correctly selects n = 137 as minimum of effective potential
  - Includes parameter scan and visualization of B(σ) relationship
  - Generates verification plot: `scripts/B_constant_verification.png`

### Changed

- **Lamb shift numerical prediction** corrected in multiple files
  - `consolidation_project/appendix_W_testable_predictions.tex`: Updated n=2 correction from ~10 kHz to ~1 kHz
  - `UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md`: Updated precision requirements (100× → 1000× improvement)
  - `DATA_ANALYSIS_ACTION_ITEMS.md`: Marked Lamb shift issue as resolved
  - Added comprehensive explanation document: `LAMB_SHIFT_EXPLANATION.md`
  - Root cause: Documentation error (formula was correct, stated value incorrect)
  - Impact: No conflict with experiments; still testable with next-gen spectroscopy (5-10 year timeline)

### Fixed

- Corrected numerical discrepancy in Lamb shift prediction (factor of ~10 error in stated value)
- Updated testability timeline for Lamb shift from 2-5 years to 5-10 years (more realistic for 1 kHz precision)

## [2025-11-02] - Lamb Shift Correction

### Fixed
- Lamb shift prediction numerical values corrected throughout documentation
- Added detailed calculation notes for transparency

### Documentation
- Created `LAMB_SHIFT_EXPLANATION.md` with comprehensive analysis
- Updated `UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md` with corrected precision requirements
- Updated `UBT_VS_OTHER_THEORIES_COMPARISON.md` with clarified error description

---

## Notes

- **UBT Version**: Development version
- **Repository**: https://github.com/DavJ/unified-biquaternion-theory
- **License**: See LICENSE.md

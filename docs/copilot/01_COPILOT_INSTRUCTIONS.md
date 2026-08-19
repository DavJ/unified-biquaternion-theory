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

# Copilot Instructions 01 — Canonical UBT Work

1. Read `AGENTS.md`, `.github/copilot-instructions.md`,
   `canonical/AXIOMS.md`, and `STATUS_OF_UBT.md` first.
2. Use `E_mu=N0^(-1/2)D_mu Theta` and the central anticommutator metric.
3. Do not restore trace/real projection, phase projection, compact-fiber
   averaging, or embedding-map GR routes to canonical status.
4. Keep `Gamma`, `omega`, and `Omega=rho_*(omega)` distinct.
5. Reconstruct `omega=omega_LC(e)+K(T)` from tetrad and specified torsion;
   do not treat it as arbitrary kinematic freedom.
6. Use the exact split status labels from `AGENTS.md`, including
   `GAP-10Omega-KIN`, `GAP-10T-DYN`, and the `GAP-10I-*` subgaps.
7. Reject the naive one-sided invertible torsion-free curved route.  For the
   pure Lorentz pair, state the concurrent-vector result only as a $K=0$ no-go;
   use the explicit composite-contortion theorem for local curved existence,
   without claiming canonical action selection or global continuation.
8. State assumptions, proof level, gauge freedom, and remaining gaps.
9. Update all status surfaces, students' explanations, tests, and patch notes
   in the same change.

10. **Architecture before repair:** before adding structure to solve an
    obstruction, test whether the obstruction is an artefact of the chosen
    formulation.
11. **Framework freeze:** no v10.x architecture pivot is allowed without an
    explicit human decision and comparative audit. Work on the current gaps.

12. Treat the minimal Palatini torsion equation, symmetry propagation, augmented holonomy for prescribed coefficients, and Lovelock infrared uniqueness as conditional subclosures. `GAP-10I-TORSION-LOCAL` closes only local kinematic representability. These results narrow but do not replace `GAP-10T-DYN`, the dynamical/global part of `GAP-10I-CURVED`, or `GAP-10D`.

13. **Derivation verification:** every active paper follows
    `docs/DERIVATION_VERIFICATION_POLICY.md`; existing papers are migrated
    progressively and every new/materially modified paper must comply in the same patch.  Prefer compiled Lean proofs for
    theorem-critical exact claims and add independent CAS/numerical checks
    (SymPy, Maxima, NumPy, Octave, MATLAB, Mathcad, etc.).
14. If Lean is unavailable or incomplete, record `LEAN-PENDING` explicitly;
    never describe uncompiled generated Lean code as a formal proof.
15. Main paper conclusions should normally have two independent verification
    channels, with tool/version/artifact/scope/limitations recorded.

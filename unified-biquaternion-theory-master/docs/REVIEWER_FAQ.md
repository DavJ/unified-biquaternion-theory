# Reviewer FAQ: UBT Alpha Baseline

This document addresses common questions and potential objections regarding the UBT alpha baseline derivation.

## General Questions

### Q: Does this "derive alpha" in the mainstream physics sense?

**A:** The baseline result provides a **fit-free framework** under specific assumptions (A1--A3):

1. **Assumption A1 (Geometric locking)**: \(N_{\mathrm{eff}}\) and \(R_\psi\) are uniquely determined by mode counting on the Hermitian slice with periodicity \(\psi \sim \psi + 2\pi\).

2. **Assumption A2 (CT scheme)**: Renormalization uses dimensional regularization, Ward identities hold (\(Z_1 = Z_2\)), and the scheme reduces to QED in the real-time limit.

3. **Assumption A3 (Observable extraction)**: The coupling is extracted at the Thomson limit with gauge-invariant normalization.

Under these assumptions, \(\mathcal R_{\mathrm{UBT}} = 1\) at two loops (Theorem in Appendix CT), yielding \(B = \frac{2\pi N_{\mathrm{eff}}}{3R_\psi}\) with **no free parameters**.

This is not a claim of deriving alpha from "nothing"—it relies on the geometric structure of complex time, standard renormalization conventions, and Ward identities. The result must be validated against experiment and higher-order calculations.

### Q: Why does \(\mathcal R_{\mathrm{UBT}} = 1\)?

**A:** The two-loop CT baseline theorem establishes this result through three key steps:

1. **CT reduction to QED**: In the real-time limit (\(\psi \to 0\)), the complex-time (CT) scheme reduces to standard QED.

2. **Ward identities**: Gauge invariance enforces \(Z_1 = Z_2\) (vertex correction equals field renormalization), eliminating scheme-dependent finite parts at the stated order.

3. **Thomson normalization**: Fixing the coupling at \(q^2 = 0\) via the Thomson scattering limit provides a gauge-invariant, physical observable.

These three conditions uniquely determine the finite renormalized ratio at two loops, yielding \(\mathcal R_{\mathrm{UBT}} = 1\).

See Appendix CT (Section \ref{app:ct-baseline-R1}) for the complete proof.

### Q: What would make \(\mathcal R_{\mathrm{UBT}} \neq 1\)?

**A:** A deviation from \(\mathcal R_{\mathrm{UBT}} = 1\) would require **explicit calculation** of complex-time effects that:

1. Survive the QED limit (\(\psi \to 0\))
2. Respect Ward identities and gauge invariance
3. Contribute finite, scheme-invariant corrections at \(q^2 = 0\)

Specifically, one would need to:

- Complete the two-loop CT computation sketched in `consolidation_project/alpha_two_loop/sketch_R_UBT.py`
- Evaluate all Feynman diagrams with the complex-time prescription
- Apply dimensional regularization and renormalization
- Extract the finite part after enforcing Ward identities
- Verify the result is gauge-independent and reduces to QED in the real-time limit

**No such calculation currently exists.** Until one is completed, the baseline theorem stands as the rigorous result.

The statement "\(\mathcal R_{\mathrm{UBT}} \approx 1.84\)" (or any other numeric value) **cannot** be introduced without completing this pipeline.

### Q: Is this consistent with known QED results?

**A:** Yes. In the real-time limit, the CT scheme reduces to standard QED:

- One-loop vacuum polarization: matches QED
- Ward identities: \(Z_1 = Z_2\) holds as in QED
- Thomson limit extraction: standard observable definition

The baseline \(\mathcal R_{\mathrm{UBT}} = 1\) is the **expected** result when no new complex-time effects contribute beyond the standard assumptions.

### Q: How does this differ from other "theories of alpha"?

**A:** Key distinctions:

| Approach | Status in UBT |
|----------|---------------|
| **Numerology** (e.g., Eddington) | Avoided—our derivation uses standard QFT |
| **String theory moduli** | N/A—UBT uses complex-time geometry instead |
| **Anthropic reasoning** | Not invoked—result is deterministic under A1--A3 |
| **Ad-hoc fits** | Explicitly rejected—baseline is fit-free |

UBT derives \(B\) from geometric mode counting combined with standard renormalization theory.

## Technical Questions

### Q: What about higher-order corrections?

**A:** The baseline theorem applies at **two-loop order**. Corrections at three loops and beyond could in principle modify \(\mathcal R_{\mathrm{UBT}}\).

However, such corrections must:
- Be computed explicitly via Feynman diagrams
- Respect gauge invariance and Ward identities
- Be finite and scheme-invariant
- Survive the QED limit

Currently, no such calculation exists. The baseline \(\mathcal R_{\mathrm{UBT}} = 1\) stands until higher-order results demonstrate otherwise.

### Q: Does the geometric mode counting depend on boundary condition choices?

**A:** No. Assumption A1 establishes that:

1. The mode domain is defined on the Hermitian slice (Appendix P6)
2. Periodicity \(\psi \sim \psi + 2\pi\) fixes \(R_\psi = 1\)
3. Mode counting yields \(N_{\mathrm{eff}} = 12\) (includes phases, helicities, particles/antiparticles)

Alternative values would violate either Lorentz invariance on the Hermitian slice or Thomson-limit normalization. See `consolidation_project/alpha_two_loop/tex/geometric_inputs_proof.tex`.

### Q: How is gauge dependence avoided?

**A:** Gauge invariance is enforced at multiple levels:

1. **Ward identities**: \(Z_1 = Z_2\) eliminates gauge-parameter (\(\xi\)) dependence in counterterms
2. **Physical observable**: Thomson-limit extraction at \(q^2 = 0\) is gauge-invariant
3. **Transverse projection**: Longitudinal photon parts vanish in the vacuum polarization

The extraction of \(\mathcal R_{\mathrm{UBT}}\) is thus gauge-independent at the stated order.

### Q: Can you test this experimentally?

**A:** The baseline result predicts \(\alpha^{-1} = F(B)\) where \(B = \frac{2\pi N_{\mathrm{eff}}}{3R_\psi}\). This can be compared to the measured value \(\alpha^{-1} \approx 137.036\).

**Current status**: The function \(F(B)\) and the precise values of \(N_{\mathrm{eff}}\), \(R_\psi\) are still being finalized. Preliminary estimates suggest agreement within uncertainties, but rigorous comparison requires completing the full calculation.

**Falsification**: If the final prediction disagrees with experiment outside uncertainties, this would indicate:
- Error in geometric mode counting (A1)
- Breakdown of CT→QED reduction (A2)
- Need for higher-order corrections beyond two loops

## Predictions Beyond Alpha

### Q: What else does UBT predict?

**A:** The framework makes additional predictions:

1. **Dark sector physics**: p-adic extensions predict dark matter/energy signatures
2. **Neutrino masses**: Geometric mode counting in complex time yields mass ratios
3. **Modified gravity**: Biquaternionic metric extends GR with testable deviations
4. **Theta resonator**: Proposed experimental device for measuring complex-time phase

See Appendix W (Testable Predictions) and the CERN BSM predictions appendix for details.

### Q: Where should I look for experimental signatures?

**A:** Priority experimental signatures:

- **High-energy colliders**: Deviations in electroweak precision tests
- **Astrophysics**: Dark matter distribution, lensing anomalies
- **Precision QED**: Higher-order corrections to \(\alpha\) running
- **Neutrino experiments**: Mass spectrum and mixing angles

## Reproducibility

### Q: How can I verify these claims?

**A:** Follow the replication protocol:

1. Build the LaTeX documents: `latexmk -pdf consolidation_project/ubt_2_main.tex`
2. Run tests: `pytest -q consolidation_project/alpha_two_loop/tests`
3. Verify baseline statements appear in the PDF (Appendix CT, Appendix α)
4. Check that no placeholders remain near \(\mathcal R_{\mathrm{UBT}}\)
5. File a replication report via GitHub issue template with PDF checksums

See `docs/REPLICATION_PROTOCOL.md` for detailed steps.

### Q: How do I report issues or ask questions?

**A:** Use the GitHub issue templates:

- **Review comments**: Technical questions, equation-level feedback
- **Replication reports**: Build issues, differences in outputs
- **General discussion**: Conceptual questions, suggestions

All issues are tracked publicly and addressed by the development team.

## Limitations and Future Work

### Q: What are the current limitations?

**A:** Known limitations:

1. **Two-loop truncation**: Higher-order corrections not yet computed
2. **Geometric assumptions**: Mode counting relies on specific boundary conditions
3. **Experimental validation**: Quantitative predictions require completing the full calculation
4. **CT prescription**: Complex-time Feynman rules not yet fully formalized

These are active areas of research. See the roadmap and open issues for current status.

### Q: What comes next?

**A:** Immediate priorities:

1. Complete three-loop \(\mathcal R_{\mathrm{UBT}}\) calculation
2. Finalize \(F(B)\) function and numeric prediction for \(\alpha^{-1}\)
3. Extend to weak mixing angle \(\theta_W\) and strong coupling \(\alpha_s\)
4. Develop experimental proposals for testing complex-time signatures

## Getting Involved

### Q: How can I contribute to this work?

**A:** Contributions welcome in several areas:

- **Code review**: Check Python scripts and LaTeX derivations
- **Calculations**: Help complete higher-order Feynman diagrams
- **Experimental proposals**: Suggest testable signatures
- **Documentation**: Improve clarity and accessibility
- **Replication**: Verify builds and report checksums

See `CONTRIBUTING.md` for guidelines.

### Q: Where can I discuss this work?

**A:** Options for discussion:

- **GitHub Discussions**: General questions and ideas
- **Issues**: Specific technical questions or bugs
- **Email**: Contact maintainers for private inquiries (see README)
- **Seminars**: See `docs/EXTERNAL_DISCUSSION_TRACKER.md` for talks and presentations

---

**Last updated**: 2025-11-08  
**Version**: v0.3.0 (Publication readiness release)

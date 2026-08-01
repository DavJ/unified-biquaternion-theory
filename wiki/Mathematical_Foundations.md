<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Mathematical Foundations

This section covers the mathematical background underlying UBT.

---

## Pages in This Section

| Page | Topic |
|------|-------|
| [Biquaternion Algebra](Biquaternion_Algebra) | The algebra ℂ⊗ℍ, quaternion basics, Mat(2,ℂ) isomorphism |
| [Modular Forms](Modular_Forms) | Hecke operators, modular forms, their role in UBT |
| [Operator Formalism](Operator_Formalism) | Covariant derivative ∇, quaternionic conjugate ∇†, spectral theory |

---

## Key Mathematical Structures

| Structure | Role in UBT |
|-----------|-------------|
| Quaternion algebra ℍ | Coordinate space for q; imaginary part → color space |
| Complex numbers ℂ | Time extension τ = t + iψ; field values |
| Biquaternions ℂ⊗ℍ | Full algebra; ≅ Mat(2,ℂ) |
| Involutions P_I, P_J, P_K | Generate Z₂×Z₂×Z₂ → SU(3)_c |
| Hecke operators T_p | Act on modular forms; select physical sector at p = 137 |
| Modular forms (weight 6) | Encode lepton mass ratios via Fourier coefficients |
| Biquaternionic derivative ∇ | Covariant derivative with gauge connection |

---

## Canonical References

| File | Content |
|------|---------|
| [`canonical/algebra/biquaternion_algebra.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/algebra/biquaternion_algebra.tex) | Algebra foundations |
| [`canonical/algebra/algebra_summary_table.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/algebra/algebra_summary_table.tex) | Summary table |
| [`canonical/explanation_of_nabla.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/explanation_of_nabla.tex) | ∇ operator |
| [`canonical/appendices/symbol_dictionary.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/appendices/symbol_dictionary.tex) | Symbol standardization |

<!-- BEGIN GENERATED: provenance_footer -->
---
> **AI provenance — Tier C (working):** AI assistance may have been used in
> drafting or maintenance. Exhaustive human review is not claimed. See the
> [repository provenance policy](https://github.com/UBT-Institute/unified-biquaternion-theory/blob/master/AI_PROVENANCE.md).
<!-- END GENERATED: provenance_footer -->

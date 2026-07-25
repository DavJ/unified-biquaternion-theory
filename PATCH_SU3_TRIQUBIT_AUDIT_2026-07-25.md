# UBT differential patch — SU(3) triqubit audit correction

**Patch date:** 2026-07-25  
**Base ZIP:** `unified-biquaternion-theory-master (1)(3).zip`  
**Base archive commit marker:** `2a3144d664c347ae04f53b733646f440317cdb20`

This is a root-relative overlay patch. Extract it directly from the repository
root so that paths such as `canonical/`, `research_tracks/`, and `tools/` merge
with the existing tree.

## Main corrections

1. Fixes the factor-of-two normalization inconsistency in
   `canonical/interactions/su3_qubit_encoding.tex` while retaining
   `G_a=P lambda_a P†`.
2. Replaces the incorrect claim that the three-dimensional one-hot sector is a
   Pauli stabilizer code. The precise result is single-`X_i` leakage detection;
   phase errors are not detected.
3. Clarifies that three qubits are minimal only under the one-hot/channel axiom;
   a general isometric qutrit embedding needs only two qubits.
4. Adds the natural fermionic Fock action and verifies
   `1⊕3⊕3bar⊕1` on all eight states.
5. Separates the one-hot `3⊕1^5` extension from the Fock
   `1⊕3⊕3bar⊕1` extension.
6. States explicitly that the six non-singlet states are not the six quark
   flavors and that state counting does not derive dark-sector energy ratios.
7. Downgrades numerical SU(3) scripts/status language from full physical QCD
   derivation to the representation/algebra result actually tested.

## Validation

```text
pytest research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/tests -q
python tools/verify_three_qubit_su3.py
python -m py_compile tools/verify_three_qubit_su3.py \
  research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/su3_qubit_core/fock.py \
  research_tracks/alpha/layer2_coding_alpha_scan.py

pdflatex canonical/interactions/su3_qubit_encoding.tex
pdflatex research_tracks/gray_transport_layer/gray_path_fingerprint.tex
```

Validated result: 60 relevant pytest tests passed; both edited standalone TeX
files compiled successfully with `pdflatex`; the Fock `su(3)` commutator residual
was `1.755e-16`.

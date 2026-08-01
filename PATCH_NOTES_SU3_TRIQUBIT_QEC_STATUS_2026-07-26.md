<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT differential patch — triqubit SU(3) error-status closure

**Patch date:** 2026-07-26  
**Base ZIP:** `unified-biquaternion-theory-master(25).zip`  
**Overlay form:** root-relative; extract directly into the repository root.

## Exact result

The one-hot color carrier

```text
C = span{|100>, |010>, |001>}
```

is an exact three-qubit embedding of a color qutrit and an exact
single-qubit `X_i`/`Y_i` leakage detector:

```text
P_C X_i P_C = P_C Y_i P_C = 0.
```

It is not a quantum error-correcting code. The Knill--Laflamme conditions fail
for the candidate error set `{I, X_1, X_2, X_3}`. An explicit witness is

```text
P_C X_1 X_2 P_C = |100><010| + |010><100|,
```

which is a color swap rather than a scalar multiple of the code projector.
Compressed `Z_i` errors are non-scalar logical phase operations and are not
detected by occupation measurement.

## Closed statuses

- `GAP-SU3-TRIQUBIT-LEAKAGE: CLOSED [L1]`
- `GAP-SU3-TRIQUBIT-QEC: CLOSED AS NO-GO [L1]`

The result supports a constrained quantum-simulation register. It does not
supply a decoder/recovery channel, a physical noise model, a UBT-derived penalty
Hamiltonian, or evidence for Matrix/simulation ontology.

## Validation

```text
python tools/verify_triqubit_qec_status.py
python tools/verify_three_qubit_su3.py
pytest -q tests/test_triqubit_qec_status.py \
  research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/tests
pytest -q tests/test_claims_consistency.py tests/test_gr_status_consistency.py
python -m py_compile tools/verify_triqubit_qec_status.py \
  tools/verify_three_qubit_su3.py tests/test_triqubit_qec_status.py
```

Results:

- triqubit QEC-status verifier: 5/5 checks PASS;
- SU(3) algebra verifier: 8/8 residual groups PASS;
- focused SU(3) + QEC tests: 65 collected, all PASS;
- claim/status consistency tests: PASS (one pre-existing optional skip);
- `CLAIMS.yaml` parsed successfully;
- both affected standalone LaTeX documents compiled twice;
- generated PDFs rendered and visually inspected.

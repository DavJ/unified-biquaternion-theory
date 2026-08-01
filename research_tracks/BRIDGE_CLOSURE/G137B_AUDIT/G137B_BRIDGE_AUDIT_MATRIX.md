<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# G137-B Bridge Audit Matrix

Status vocabulary:

- **AUDITED-L1-COND** — internally audited, conditional on named UBT bridges.
- **EXTERNAL-AUDIT** — internally coherent but requires independent reviewer audit.

| ID | Bridge | Role in alpha | Current status | Main file | Remaining attack surface |
|---|---|---|---|---|---|
| A1 | Complete spin-structure trace | Gives `eta^-2 theta2 theta3 theta4 = 2 eta` | **AUDITED-L1-COND** | `A1_complete_spin_structure_trace_theorem.tex` | Triad-to-spin-structure map |
| A2 | Four-channel geometric mean | Gives fourth root `Z^(1/4)` | **AUDITED-L1-COND** | `A2_four_channel_geometric_mean_theorem.tex` | Exact equivalence of the four readout channels |
| A3 | Odd-winding parity / fermionic measure | Gives `theta4` and parity trace | **AUDITED-L1-COND** | `A3_odd_winding_measure_attack_response.tex` | Full exchange-phase -> Berezin measure proof remains externally auditable |
| A4 | SU(2) twist uniqueness | Gives periodic/shifted split `theta3/theta2` | **AUDITED-L1-COND** | `A4_su2_twist_uniqueness_theorem.tex` | Why nontrivial twist is selected over trivial twist |
| A5 | EM modular normalisation | Identifies `n=alpha^-1` | **AUDITED-L1-COND** | `A5_em_modular_normalisation_attack_response.tex` | Primitive compact U(1)_EM projection |

## Overall status

```text
G137-B bridge package: internally audited.
Alpha route: bridge-derived inside current UBT canonical bridges.
External audit remains required.
```

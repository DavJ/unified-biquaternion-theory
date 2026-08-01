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


# Alpha Layer2 kernel refinement reproduction

This folder reproduces the numerical values from:

`research_tracks/T3_ALPHA/information_loss_alpha_self_consistency.tex`

Run from the repository root:

```bash
python experiments/alpha_information_loss/reproduce_info_loss_alpha.py
```

The script evaluates four models:

1. self-dual eta-winding, `rho = 1`;
2. minimal four-channel information loss, `C_Q = 4`;
3. sharp Layer2 eta-spectral projection, `r_eff = 3`;
4. first Layer2 eta-kernel refinement,

```text
r_eff = 3 * (1 + Omega_eta(1))
Omega_eta(1) = sum_{m>=1} m/(exp(2*pi*m)-1)
             = 1/24 - 1/(8*pi)
```

Expected headline result:

```text
n = alpha^-1 = 137.035999177549...
```

Compared with CODATA/NIST 2022,

```text
alpha^-1 = 137.035999177(21)
```

this is about `+0.026 sigma`.

Status: research-track only. The remaining proof gap is the derivation of the
Layer2 readout kernel from canonical UBT.

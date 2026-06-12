<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Alpha Layer2 projection reproduction

This folder reproduces the numerical values from:

`research_tracks/T3_ALPHA/information_loss_alpha_self_consistency.tex`

Run from the repository root:

```bash
python experiments/alpha_information_loss/reproduce_info_loss_alpha.py
```

The script evaluates three models:

1. self-dual eta-winding, `rho = 1`;
2. minimal four-channel information loss, `C_Q = 4`;
3. Layer2 eta-spectral projection correction,

```text
C_Q(n) = 4 - ((pi - 3)/2) * ((n - 3)/n)
```

Expected headline result:

```text
n = alpha^-1 = 137.035999142931...
```

Compared with CODATA/NIST 2022,

```text
alpha^-1 = 137.035999177(21)
```

this is about `-1.62 sigma`.

Status: research-track only. The remaining proof gap is the derivation of the
Layer2 projection-rank factor `(n - 3)/n` from the canonical UBT projection
kernel.

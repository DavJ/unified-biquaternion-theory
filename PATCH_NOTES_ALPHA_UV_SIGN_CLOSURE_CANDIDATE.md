# Patch notes — alpha UV sign closure candidate

Adds:

- `research_tracks/T3_ALPHA/theta0_uv_sign_from_psi_casimir_candidate.tex`
- `docs/reports/alpha_uv_sign_closure_candidate.md`

Updates:

- `research_tracks/T3_ALPHA/alpha_derivation_complete.tex`

The new candidate theorem states that if

```math
m_eff^2 = m_{0,EW}^2 - Gamma_psi M_psi^2,
m_{0,EW}^2 = 0,
Gamma_psi > 0,
```

then

```math
m_eff^2 < 0,
mu_EW^2 = Gamma_psi M_psi^2 > 0.
```

This supplies a compact-psi/Casimir-like UV sign mechanism for the EW
symmetry-breaking term needed by the alpha chain.

Important: this is intentionally marked as L2 candidate.  To make the alpha
proof unconditional within UBT, the repository still needs canonical derivations
of the two UV hypotheses:

```math
m_{0,EW}^2 = 0,
Gamma_psi > 0.
```

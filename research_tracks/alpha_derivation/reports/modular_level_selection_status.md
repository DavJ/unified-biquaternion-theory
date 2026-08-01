<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# Modular level-selection status (non-fitted scan)

## Scope

Scanned levels: N in [2, 500] using parameter-free proxy families for V_mod(N).
No alpha_exp, fitted B target, or hand-set preferred level was used as input.

## Results

| model | expression | minimizing levels | interior minimizers | selected N_* | mu(Gamma0(N_*))/3 | status |
|---|---|---|---|---:|---:|---|
| log_mu | `V_mod(N)=log(mu(Gamma0(N)))` | [2] | [] | 2 | 1.000000 | boundary_only_no_interior_attractor |
| minus_log_mu | `V_mod(N)=-log(mu(Gamma0(N)))` | [420, 462, 480] | [420, 462, 480] | 420 | 384.000000 | interior_stationary_found |
| log_mu_minus_log_n | `V_mod(N)=log(mu(Gamma0(N)))-log(N)` | [499] | [499] | 499 | 166.666667 | interior_stationary_found |
| log_n_minus_log_mu | `V_mod(N)=log(N)-log(mu(Gamma0(N)))` | [210, 420] | [210, 420] | 210 | 192.000000 | interior_stationary_found |
| mu_over_n | `V_mod(N)=mu(Gamma0(N))/N` | [499] | [499] | 499 | 166.666667 | interior_stationary_found |
| n_over_mu | `V_mod(N)=N/mu(Gamma0(N))` | [210, 420] | [210, 420] | 210 | 192.000000 | interior_stationary_found |

## Interpretation

- At least one proxy family produced an interior minimizer, but cross-family uniqueness is not established.
- Therefore no model-independent canonical level selection is closed.

## Missing theorem

Required theorem not currently available: from canonical S[Theta] and compact toroidal boundary data alone, derive a unique renormalization-scheme-independent V_mod(N) with a unique interior stationary level N_* and fixed finite modular residue delta_mod.

## Verdict

Route remains open/falsified at current stage: level must not be inserted by hand, and no unique canonical level selection is obtained from the tested non-fitted modular proxies.

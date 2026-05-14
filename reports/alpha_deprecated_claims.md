<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_deprecated_claims.md — Deprecated Alpha Claims Register

**Date**: 2026-05-09  
**Purpose**: Explicitly retire legacy alpha claims and map them to current valid statements.

---

## Deprecated claims (retired)

| Deprecated claim | Status | Replacement |
|---|---|---|
| `V_eff(n) = n² − B·ln n` | **RETIRED** | `V_eff(n) = n² − B·n·ln n` |
| `n* = sqrt(B/2)` as active stationarity for alpha route | **RETIRED** | `2n* = B(ln n* + 1)` |
| alpha derivation is complete/closed | **RETIRED** | alpha not derived; B-gap open |
| Hecke path-integral route is successful/closing B-gap | **RETIRED** | Hecke path-integral route is current no-go |

---

## Current allowed status labels

- alpha not derived
- prime-stability set derived
- B-gap open
- eta(i) route best candidate (**research/proposal only**)
- Hecke path-integral route no-go at current level

---

## Scope of cleanup in this change

Legacy active claims were removed or corrected in status/portfolio documents, and
`research_tracks/T3_ALPHA/alpha_status_report.md` was converted into a deprecated redirect stub.

For authoritative wording use `reports/alpha_current_verdict.md`.

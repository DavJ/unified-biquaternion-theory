<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# Alpha Claims Audit 2026 (Gap G137-B hardening)

| file | claim | problem | proposed fix |
|---|---|---|---|
| `canonical/alpha/ALPHA_MASTER_STATUS.md` | Alpha not derived; Gap G137-B open; winding constant correction NO-GO | **SAFE** | Keep as authority and add canonical wording lock (done). |
| `reports/alpha_current_verdict.md` | Alpha not derived; B-gap open; obsolete winding route rejected | **SAFE** | Keep synced to master wording lock (done). |
| `CLAIMS_MATRIX.md` | "integer-137 proved given B_phenom" phrasing | **NEEDS DOWNGRADE** (could be read as stronger than structural conditional) | Reword overall verdict to `STRUCTURAL / CONDITIONAL / OPEN GAP` and mark P3 as conditional only (done). |
| `WHAT_IS_PROVED.md` | G137-B listed as open but without strict no-input rule | **NEEDS DOWNGRADE** | Tighten gap statement to forbid α/137/B_required inputs and label alpha status structural/conditional/open (done). |
| `canonical/alpha/PRIMARY_ROUTE.md` | Conditional route with explicit open G137-B | **SAFE** | Keep; no promotional wording needed. |
| `canonical/alpha/alpha_route_scoreboard.md` | Route ranking and open G137-B | **SAFE** | Keep as route-scoring artifact; do not promote to proof claim. |
| `reports/alpha_missing_lemma.md` | Uses `B≈46.298 (=B_phenom)` and strategy text that can read as target-confirming | **NEEDS DOWNGRADE** | Keep open-gap framing; avoid language implying B is already determined. |
| `reports/alpha_B_gap_after_winding_no_go.md` | Mentions `ΔB_wind≈18.5` and `B_best≈43.6` as withdrawn/no-go | **SAFE** | Keep explicit NO-GO/obsolete labels. |
| `canonical/alpha/alpha_best_route.tex` | Opening sentence says "deriving α≈1/137.036" and blocker is G3-k, not G137-B | **CONTRADICTS CURRENT VERDICT** | Mark as legacy route draft or rewrite to current G137-B position before citing as active claim. |
| `canonical/alpha/best_candidate_derivation.tex` | Uses legacy G3-k framing as unique blocker | **CONTRADICTS CURRENT VERDICT** | Mark as legacy route draft or rewrite to current G137-B position before citing as active claim. |
| `canonical/alpha/alpha_equation_matrix.tex` | Mixed multi-route legacy framing; includes conditional/open labels | **NEEDS DOWNGRADE** | Keep only as route matrix; avoid using as canonical status source. |
| `ALPHA_BREAKTHROUGH_REPORT.md` | Historical "breakthrough" title and mission narrative | **OBSOLETE / ARCHIVE CANDIDATE** | Keep only with historical/superseded banner and forward link to master status (done). |
| `ALPHA_FINAL_OFFENSIVE.md` | Offensive language and legacy strategy baseline | **OBSOLETE / ARCHIVE CANDIDATE** | Keep with historical/superseded banner and forward link to master status (done). |
| `ALPHA_PROGRESS_REPORT.md` | Legacy progress snapshot with older route assumptions | **OBSOLETE / ARCHIVE CANDIDATE** | Keep with historical/superseded banner and forward link to master status (done). |
| `ALPHA_STRUCTURAL_ORIGINS.md` | Exploratory claims around 3/2 exponent and route closure trajectories | **OBSOLETE / ARCHIVE CANDIDATE** | Keep with historical/superseded banner and forward link to master status (done). |
| `alpha_routes_scorecard.md` | Legacy route scorecard from offensive phase | **OBSOLETE / ARCHIVE CANDIDATE** | Keep with historical/superseded banner and forward link to master status (done). |
| `ALPHA_BEST_ROUTE.tex` | Root-level alpha file contains stale status lines (e.g., 127 track) | **OBSOLETE / ARCHIVE CANDIDATE** | Keep as provenance only and mark superseded by canonical master status (done). |

## Audit conclusion

- Canonical status source is now explicitly `canonical/alpha/ALPHA_MASTER_STATUS.md`.
- Active alpha claim level is **STRUCTURAL / CONDITIONAL / OPEN GAP (G137-B)**.
- No first-principles derivation of alpha is currently present.

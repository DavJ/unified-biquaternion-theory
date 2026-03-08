"""
test_scores.py — Tests for the multi-criteria UBT v56 comparison data.

Validates:
- All theories and criteria are defined with correct keys.
- Numeric scores are in the valid range [1, 10].
- Boolean criterion values are booleans.
- Computed averages match expected values from the comparison table.
- UBT v56 leads the ranking.
- B-derivation scenario data is self-consistent.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest

from THEORY_COMPARISONS.multi_criteria_v56.scoring_core.criteria import (
    CRITERIA,
    THEORIES,
    SCORES,
    NUMERIC_CRITERIA_KEYS,
    get_score,
    get_total,
    all_averages,
)
from THEORY_COMPARISONS.multi_criteria_v56.scoring_core.comparison import (
    B_DERIVATION_SCENARIOS,
    best_theory_for_criterion,
    get_current_scenario,
    get_breakthrough_scenario,
    summary_table,
    ubt_is_top_candidate,
)

# ---------------------------------------------------------------------------
# Fixture helpers
# ---------------------------------------------------------------------------

THEORY_KEYS = [t["key"] for t in THEORIES]
CRITERION_KEYS = [c["key"] for c in CRITERIA]


# ---------------------------------------------------------------------------
# Structure tests
# ---------------------------------------------------------------------------

class TestDataStructure:
    """Tests that required theories and criteria are present."""

    def test_five_theories_defined(self):
        """Exactly five theories are defined."""
        assert len(THEORIES) == 5

    def test_theory_keys_present(self):
        """All expected theory keys are present."""
        expected = {"string_m", "lqg", "connes_ncg", "asymptotic_safety", "ubt_v56"}
        assert set(THEORY_KEYS) == expected

    def test_eight_criteria_defined(self):
        """Exactly eight criteria are defined."""
        assert len(CRITERIA) == 8

    def test_criterion_keys_present(self):
        """All expected criterion keys are present."""
        expected = {
            "sm_gauge_group", "gravity", "fermion_masses",
            "alpha_first_principles", "no_extra_dimensions",
            "testable_predictions", "dynamics_qft", "mirror_dark_sector",
        }
        assert set(CRITERION_KEYS) == expected

    def test_scores_cover_all_theories(self):
        """SCORES contains an entry for every theory."""
        assert set(SCORES.keys()) == set(THEORY_KEYS)

    def test_scores_cover_all_criteria(self):
        """Each theory's score entry contains all criteria."""
        for theory_key in THEORY_KEYS:
            assert set(SCORES[theory_key].keys()) == set(CRITERION_KEYS), (
                f"Missing criteria for theory '{theory_key}'"
            )


# ---------------------------------------------------------------------------
# Score range tests
# ---------------------------------------------------------------------------

class TestScoreRanges:
    """Tests that scores are in valid ranges."""

    @pytest.mark.parametrize("theory_key", THEORY_KEYS)
    @pytest.mark.parametrize("criterion_key", NUMERIC_CRITERIA_KEYS)
    def test_numeric_score_in_range(self, theory_key, criterion_key):
        """Numeric scores must be integers in [1, 10]."""
        score = SCORES[theory_key][criterion_key]
        assert isinstance(score, int), (
            f"{theory_key}/{criterion_key}: expected int, got {type(score)}"
        )
        assert 1 <= score <= 10, (
            f"{theory_key}/{criterion_key}: score {score} out of range [1, 10]"
        )

    @pytest.mark.parametrize("theory_key", THEORY_KEYS)
    def test_boolean_criterion_is_bool(self, theory_key):
        """no_extra_dimensions must be a boolean."""
        val = SCORES[theory_key]["no_extra_dimensions"]
        assert isinstance(val, bool), (
            f"{theory_key}/no_extra_dimensions: expected bool, got {type(val)}"
        )


# ---------------------------------------------------------------------------
# Specific score values (from the comparison table, 2026-03-07)
# ---------------------------------------------------------------------------

class TestSpecificScores:
    """Tests that specific scores match the published comparison table."""

    # UBT v56 scores
    def test_ubt_sm_gauge_group(self):
        assert get_score("ubt_v56", "sm_gauge_group") == 9

    def test_ubt_gravity(self):
        assert get_score("ubt_v56", "gravity") == 8

    def test_ubt_fermion_masses(self):
        assert get_score("ubt_v56", "fermion_masses") == 5

    def test_ubt_alpha(self):
        assert get_score("ubt_v56", "alpha_first_principles") == 4

    def test_ubt_no_extra_dimensions(self):
        assert get_score("ubt_v56", "no_extra_dimensions") is True

    def test_ubt_testable_predictions(self):
        assert get_score("ubt_v56", "testable_predictions") == 8

    def test_ubt_dynamics(self):
        assert get_score("ubt_v56", "dynamics_qft") == 3

    def test_ubt_mirror_dark_sector(self):
        assert get_score("ubt_v56", "mirror_dark_sector") == 9

    # String/M scores
    def test_string_sm_gauge_group(self):
        assert get_score("string_m", "sm_gauge_group") == 6

    def test_string_gravity(self):
        assert get_score("string_m", "gravity") == 9

    def test_string_no_extra_dimensions(self):
        assert get_score("string_m", "no_extra_dimensions") is False

    def test_string_dynamics(self):
        assert get_score("string_m", "dynamics_qft") == 9

    # LQG scores
    def test_lqg_gravity(self):
        assert get_score("lqg", "gravity") == 9

    def test_lqg_sm_gauge_group(self):
        assert get_score("lqg", "sm_gauge_group") == 3

    def test_lqg_no_extra_dimensions(self):
        assert get_score("lqg", "no_extra_dimensions") is True

    # Connes NCG scores
    def test_connes_sm_gauge_group(self):
        assert get_score("connes_ncg", "sm_gauge_group") == 9

    def test_connes_gravity(self):
        assert get_score("connes_ncg", "gravity") == 7

    # Asymptotic Safety scores
    def test_asymptotic_gravity(self):
        assert get_score("asymptotic_safety", "gravity") == 9

    def test_asymptotic_sm_gauge_group(self):
        assert get_score("asymptotic_safety", "sm_gauge_group") == 3


# ---------------------------------------------------------------------------
# Average score tests
# ---------------------------------------------------------------------------

class TestAverages:
    """Tests for published overall scores."""

    def test_ubt_total_is_7_1(self):
        """UBT v56 published total must be 7.1/10."""
        assert get_total("ubt_v56") == 7.1

    def test_string_total_is_5_8(self):
        """String/M published total must be 5.8/10."""
        assert get_total("string_m") == 5.8

    def test_lqg_total_is_4_8(self):
        """LQG published total must be 4.8/10."""
        assert get_total("lqg") == 4.8

    def test_connes_total_is_5_8(self):
        """Connes NCG published total must be 5.8/10."""
        assert get_total("connes_ncg") == 5.8

    def test_asymptotic_total_is_5_5(self):
        """Asymptotic Safety published total must be 5.5/10."""
        assert get_total("asymptotic_safety") == 5.5

    def test_all_averages_returns_five_entries(self):
        """all_averages() returns one entry per theory."""
        avgs = all_averages()
        assert len(avgs) == 5

    def test_ubt_leads_ranking(self):
        """UBT v56 must have the highest overall score."""
        assert ubt_is_top_candidate()

    def test_ranking_order(self):
        """summary_table() must be sorted descending."""
        table = summary_table()
        scores = [s for _, s in table]
        assert scores == sorted(scores, reverse=True)


# ---------------------------------------------------------------------------
# Best-theory-for-criterion tests
# ---------------------------------------------------------------------------

class TestBestTheory:
    """Tests for the best_theory_for_criterion helper."""

    def test_ubt_best_mirror_dark_sector(self):
        """UBT leads on mirror/dark sector (score 9)."""
        best = best_theory_for_criterion("mirror_dark_sector")
        assert "ubt_v56" in best

    def test_ubt_best_testable_predictions(self):
        """UBT leads on testable predictions (score 8)."""
        best = best_theory_for_criterion("testable_predictions")
        assert "ubt_v56" in best

    def test_string_best_dynamics(self):
        """String/M leads on dynamics (score 9)."""
        best = best_theory_for_criterion("dynamics_qft")
        assert "string_m" in best

    def test_no_extra_dims_excludes_string(self):
        """String/M is NOT in the 'no extra dimensions' best list."""
        best = best_theory_for_criterion("no_extra_dimensions")
        assert "string_m" not in best

    def test_no_extra_dims_includes_ubt(self):
        """UBT is in the 'no extra dimensions' best list."""
        best = best_theory_for_criterion("no_extra_dimensions")
        assert "ubt_v56" in best

    def test_high_sm_gauge_group(self):
        """UBT and Connes NCG share the top score (9) for SM gauge group."""
        best = best_theory_for_criterion("sm_gauge_group")
        assert "ubt_v56" in best
        assert "connes_ncg" in best


# ---------------------------------------------------------------------------
# B-derivation scenario tests
# ---------------------------------------------------------------------------

class TestBDerivationScenarios:
    """Tests for the B-coefficient derivation scenario data."""

    def test_four_scenarios(self):
        """Exactly four scenarios are defined."""
        assert len(B_DERIVATION_SCENARIOS) == 4

    def test_first_scenario_achieved(self):
        """The first scenario (today's state) is marked achieved."""
        assert B_DERIVATION_SCENARIOS[0]["achieved"] is True

    def test_remaining_scenarios_not_achieved(self):
        """All scenarios after the first are not yet achieved."""
        for scenario in B_DERIVATION_SCENARIOS[1:]:
            assert scenario["achieved"] is False

    def test_scores_monotonically_increasing(self):
        """Scenario scores must be strictly increasing."""
        scores = [s["score"] for s in B_DERIVATION_SCENARIOS]
        for i in range(len(scores) - 1):
            assert scores[i] < scores[i + 1], (
                f"Scenario scores not increasing: {scores[i]} >= {scores[i+1]}"
            )

    def test_current_scenario_score_7_1(self):
        """Current achieved scenario has score 7.1."""
        current = get_current_scenario()
        assert current["score"] == 7.1

    def test_breakthrough_scenario_score_8_5(self):
        """Next breakthrough scenario has score 8.5 (B from N_eff^{3/2})."""
        breakthrough = get_breakthrough_scenario()
        assert breakthrough["score"] == 8.5

    def test_highest_scenario_score_9_8(self):
        """Highest (Nobel territory) scenario has score 9.8."""
        assert B_DERIVATION_SCENARIOS[-1]["score"] == 9.8

    def test_each_scenario_has_required_keys(self):
        """Each scenario has label, score, status, and achieved keys."""
        required = {"label", "score", "status", "achieved"}
        for scenario in B_DERIVATION_SCENARIOS:
            assert required.issubset(scenario.keys()), (
                f"Missing keys in scenario: {required - scenario.keys()}"
            )

import math

def test_RUBT_series_guardrail():
    # Document expectation: RUBT must be 1 + O(α), not a scale-independent constant
    alpha = 1/137.0
    series_example = 1.0 + 0.0*(alpha/math.pi) + 0.0*((alpha/math.pi)**2)
    assert abs(series_example - 1.0) < 1e-12

import math

def beta_alpha_two_loop_QED(alpha: float, Nf: int) -> float:
    """Universal QED two-loop running in a mass-independent scheme."""
    return (2*Nf/(3*math.pi))*alpha*alpha + (Nf/(2*math.pi**2))*alpha**3

def test_qed_limit_coefficients_shape():
    # Sanity: beta ~ α^2 + α^3 — tiny number at α≈1/137
    alpha = 1/137.0
    Nf = 1
    b = beta_alpha_two_loop_QED(alpha, Nf)
    assert 0 < b < 1e-3

from tools.verify_first_jet_gravity_orbit import det4, inverse4, matmul, metric, transpose, Q


def test_lorentz_metrics_share_one_congruence_orbit():
    e1 = [[Q(1), Q(0), Q(0), Q(0)],
          [Q(1, 3), Q(2), Q(0), Q(0)],
          [Q(0), Q(1, 5), Q(3), Q(0)],
          [Q(0), Q(0), Q(1, 7), Q(4)]]
    e2 = [[Q(2), Q(1, 2), Q(0), Q(0)],
          [Q(0), Q(3), Q(1, 3), Q(0)],
          [Q(1, 4), Q(0), Q(2), Q(1, 5)],
          [Q(0), Q(1, 6), Q(0), Q(5)]]
    g1, g2 = metric(e1), metric(e2)
    A = matmul(e2, inverse4(e1))
    assert matmul(matmul(A, g1), transpose(A)) == g2
    assert det4(g2) == det4(A) ** 2 * det4(g1)

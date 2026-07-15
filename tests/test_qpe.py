import numpy as np

from ft_ham_sim.qpe import most_likely_phase, qpe_distribution


def test_qpe_distribution_normalized():
    probabilities = qpe_distribution(0.37, 5)
    assert np.isclose(probabilities.sum(), 1.0)
    assert np.all(probabilities >= 0)


def test_qpe_peak_near_phase():
    phase = 0.37
    probabilities = qpe_distribution(phase, 6)
    estimate = most_likely_phase(probabilities)
    assert abs(phase - estimate) <= 1 / 64

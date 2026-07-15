import numpy as np

from ft_ham_sim.hamiltonians import tfim_components
from ft_ham_sim.metrics import operator_error, state_fidelity
from ft_ham_sim.operators import basis_state
from ft_ham_sim.trotter import exact_unitary, trotter_unitary


def test_exact_unitary_at_zero_time():
    h_zz, h_x = tfim_components(2)
    unitary = exact_unitary(h_zz + h_x, 0.0)
    assert np.allclose(unitary, np.eye(4))


def test_second_order_improves_small_step_error():
    h_zz, h_x = tfim_components(2, coupling=1.0, field=0.7)
    exact = exact_unitary(h_zz + h_x, 0.3)
    first = trotter_unitary((h_zz, h_x), 0.3, 2, order=1)
    second = trotter_unitary((h_zz, h_x), 0.3, 2, order=2)
    assert operator_error(exact, second) < operator_error(exact, first)


def test_fidelity_is_one_for_global_phase():
    state = basis_state("00")
    assert np.isclose(state_fidelity(state, 1j * state), 1.0)

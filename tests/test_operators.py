import numpy as np

from ft_ham_sim.operators import X, Z, basis_state, pauli_string_matrix


def test_pauli_string_is_hermitian():
    matrix = pauli_string_matrix("XIZ")
    assert np.allclose(matrix, matrix.conj().T)


def test_basis_state():
    state = basis_state("101")
    assert state.shape == (8,)
    assert np.argmax(abs(state)) == 5
    assert np.isclose(np.linalg.norm(state), 1.0)


def test_pauli_square_is_identity():
    assert np.allclose(X @ X, np.eye(2))
    assert np.allclose(Z @ Z, np.eye(2))

"""Hamiltonian constructors used throughout the course."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .operators import X, Z, operator_on_qubit, two_qubit_product

ComplexArray = NDArray[np.complex128]


def tfim_components(
    n_qubits: int,
    coupling: float = 1.0,
    field: float = 1.0,
    periodic: bool = False,
) -> tuple[ComplexArray, ComplexArray]:
    """Return ``(H_ZZ, H_X)`` for a one-dimensional TFIM.

    The sign convention is

        H = coupling * sum_i Z_i Z_{i+1} + field * sum_i X_i.
    """
    if n_qubits < 2:
        raise ValueError("TFIM examples require at least two qubits.")

    dimension = 2**n_qubits
    h_zz = np.zeros((dimension, dimension), dtype=complex)
    h_x = np.zeros_like(h_zz)

    for qubit in range(n_qubits - 1):
        h_zz += coupling * two_qubit_product(Z, qubit, Z, qubit + 1, n_qubits)

    if periodic and n_qubits > 2:
        h_zz += coupling * two_qubit_product(Z, n_qubits - 1, Z, 0, n_qubits)

    for qubit in range(n_qubits):
        h_x += field * operator_on_qubit(X, qubit, n_qubits)

    return h_zz, h_x


def tfim_hamiltonian(
    n_qubits: int,
    coupling: float = 1.0,
    field: float = 1.0,
    periodic: bool = False,
) -> ComplexArray:
    """Return the full dense TFIM Hamiltonian."""
    h_zz, h_x = tfim_components(n_qubits, coupling, field, periodic)
    return h_zz + h_x

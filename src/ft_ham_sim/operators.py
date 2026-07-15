"""Small dense-matrix operator utilities.

Convention: labels are written left-to-right as qubits q0, q1, ..., q(n-1).
This differs from some circuit SDK display conventions, so conversions should be
made explicitly.
"""

from __future__ import annotations

from functools import reduce
from typing import Iterable

import numpy as np
from numpy.typing import NDArray

ComplexArray = NDArray[np.complex128]

I2: ComplexArray = np.eye(2, dtype=complex)
X: ComplexArray = np.array([[0, 1], [1, 0]], dtype=complex)
Y: ComplexArray = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z: ComplexArray = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}


def kron_all(operators: Iterable[ComplexArray]) -> ComplexArray:
    """Kronecker product of all operators in iteration order."""
    operators = list(operators)
    if not operators:
        raise ValueError("At least one operator is required.")
    return reduce(np.kron, operators).astype(complex)


def pauli_string_matrix(label: str) -> ComplexArray:
    """Return the dense matrix for a Pauli string such as ``'ZIX'``."""
    if not label:
        raise ValueError("Pauli label cannot be empty.")
    try:
        return kron_all(PAULI[symbol] for symbol in label.upper())
    except KeyError as exc:
        raise ValueError(f"Unknown Pauli symbol: {exc.args[0]}") from exc


def operator_on_qubit(operator: ComplexArray, qubit: int, n_qubits: int) -> ComplexArray:
    """Embed a one-qubit operator on ``qubit`` using q0-first ordering."""
    if operator.shape != (2, 2):
        raise ValueError("operator must be a 2x2 matrix")
    if not 0 <= qubit < n_qubits:
        raise ValueError("qubit index is outside the register")
    factors = [I2] * n_qubits
    factors[qubit] = operator
    return kron_all(factors)


def two_qubit_product(
    first: ComplexArray,
    q_first: int,
    second: ComplexArray,
    q_second: int,
    n_qubits: int,
) -> ComplexArray:
    """Embed a product of two one-qubit operators on distinct qubits."""
    if q_first == q_second:
        raise ValueError("The two qubit indices must be distinct.")
    factors = [I2] * n_qubits
    factors[q_first] = first
    factors[q_second] = second
    return kron_all(factors)


def basis_state(bits: str) -> ComplexArray:
    """Return a computational-basis ket using q0-first bit-string ordering."""
    if not bits or any(bit not in "01" for bit in bits):
        raise ValueError("bits must be a non-empty string containing only 0 and 1")
    dimension = 2 ** len(bits)
    state = np.zeros(dimension, dtype=complex)
    state[int(bits, 2)] = 1.0
    return state


def normalize(state: ComplexArray) -> ComplexArray:
    """Return a normalized copy of a state vector."""
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return np.asarray(state, dtype=complex) / norm

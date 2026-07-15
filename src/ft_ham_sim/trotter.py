"""Exact and product-formula time evolution."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

ComplexArray = NDArray[np.complex128]


def exact_unitary(hamiltonian: ComplexArray, time: float) -> ComplexArray:
    """Compute ``exp(-i time H)`` with dense matrix exponentiation."""
    _validate_square(hamiltonian)
    return expm(-1j * time * hamiltonian)


def trotter_unitary(
    terms: tuple[ComplexArray, ...] | list[ComplexArray],
    time: float,
    steps: int,
    order: int = 1,
) -> ComplexArray:
    """Construct a first- or symmetric second-order product formula.

    Parameters
    ----------
    terms:
        Hamiltonian groups whose exponentials can be evaluated separately.
    time:
        Total simulation time.
    steps:
        Number of product-formula repetitions.
    order:
        ``1`` for Lie-Trotter or ``2`` for symmetric second order.
    """
    terms = tuple(np.asarray(term, dtype=complex) for term in terms)
    if not terms:
        raise ValueError("At least one Hamiltonian term/group is required.")
    for term in terms:
        _validate_square(term)
    if any(term.shape != terms[0].shape for term in terms):
        raise ValueError("All terms must have the same dimensions.")
    if steps < 1:
        raise ValueError("steps must be a positive integer")
    if order not in (1, 2):
        raise ValueError("Only first- and second-order formulas are implemented.")

    dt = time / steps
    dimension = terms[0].shape[0]

    if order == 1:
        one_step = np.eye(dimension, dtype=complex)
        for term in terms:
            one_step = one_step @ expm(-1j * dt * term)
    else:
        one_step = np.eye(dimension, dtype=complex)
        for term in terms[:-1]:
            one_step = one_step @ expm(-1j * dt * term / 2)
        one_step = one_step @ expm(-1j * dt * terms[-1])
        for term in reversed(terms[:-1]):
            one_step = one_step @ expm(-1j * dt * term / 2)

    result = np.eye(dimension, dtype=complex)
    for _ in range(steps):
        result = result @ one_step
    return result


def _validate_square(matrix: ComplexArray) -> None:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Expected a square matrix.")

"""Error and fidelity metrics."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import norm

ComplexArray = NDArray[np.complex128]


def operator_error(exact: ComplexArray, approximate: ComplexArray) -> float:
    """Spectral norm ``||exact - approximate||_2``."""
    if exact.shape != approximate.shape:
        raise ValueError("Matrices must have the same shape.")
    return float(norm(exact - approximate, ord=2))


def state_fidelity(first: ComplexArray, second: ComplexArray) -> float:
    """Pure-state fidelity ``|<first|second>|^2`` after normalization."""
    if first.shape != second.shape:
        raise ValueError("States must have the same shape.")
    first_norm = np.linalg.norm(first)
    second_norm = np.linalg.norm(second)
    if first_norm == 0 or second_norm == 0:
        raise ValueError("State vectors cannot be zero.")
    overlap = np.vdot(first / first_norm, second / second_norm)
    return float(abs(overlap) ** 2)

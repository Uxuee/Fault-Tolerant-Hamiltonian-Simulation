"""Ideal finite-register phase-estimation distributions."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def qpe_distribution(phase: float, counting_qubits: int) -> NDArray[np.float64]:
    """Return the ideal QPE outcome probabilities for an exact eigenphase.

    ``phase`` is interpreted modulo one.
    """
    if counting_qubits < 1:
        raise ValueError("counting_qubits must be positive")
    phase = phase % 1.0
    size = 2**counting_qubits
    k = np.arange(size)
    probabilities = np.empty(size, dtype=float)
    for outcome in range(size):
        offset = phase - outcome / size
        amplitude = np.exp(2j * np.pi * k * offset).mean()
        probabilities[outcome] = abs(amplitude) ** 2
    probabilities /= probabilities.sum()
    return probabilities


def most_likely_phase(probabilities: NDArray[np.float64]) -> float:
    """Convert the most likely QPE outcome into a phase in [0, 1)."""
    size = len(probabilities)
    if size == 0 or size & (size - 1):
        raise ValueError("Probability-vector length must be a nonzero power of two.")
    return int(np.argmax(probabilities)) / size

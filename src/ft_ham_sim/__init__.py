"""Teaching utilities for Hamiltonian simulation and FT resource estimation."""

from .hamiltonians import tfim_components, tfim_hamiltonian
from .trotter import exact_unitary, trotter_unitary
from .metrics import operator_error, state_fidelity

__all__ = [
    "tfim_components",
    "tfim_hamiltonian",
    "exact_unitary",
    "trotter_unitary",
    "operator_error",
    "state_fidelity",
]

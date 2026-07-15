"""Exact evolution of one qubit under H = 0.5 X + 0.7 Z."""

import numpy as np

from ft_ham_sim.operators import X, Z, basis_state
from ft_ham_sim.trotter import exact_unitary

hamiltonian = 0.5 * X + 0.7 * Z
initial = basis_state("0")
time = 1.2

final = exact_unitary(hamiltonian, time) @ initial
expectation_z = float(np.real(np.vdot(final, Z @ final)))

print("Final state:")
print(final)
print(f"Norm:          {np.linalg.norm(final):.12f}")
print(f"<Z>(t={time}): {expectation_z:.8f}")

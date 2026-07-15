"""Compare exact, first-order, and second-order TFIM evolution."""

from ft_ham_sim.hamiltonians import tfim_components
from ft_ham_sim.metrics import operator_error, state_fidelity
from ft_ham_sim.operators import basis_state
from ft_ham_sim.trotter import exact_unitary, trotter_unitary

n_qubits = 4
simulation_time = 1.0
steps = 4
h_zz, h_x = tfim_components(n_qubits, coupling=1.0, field=0.8)
exact = exact_unitary(h_zz + h_x, simulation_time)
first = trotter_unitary((h_zz, h_x), simulation_time, steps, order=1)
second = trotter_unitary((h_zz, h_x), simulation_time, steps, order=2)

initial = basis_state("0" * n_qubits)
exact_state = exact @ initial
first_state = first @ initial
second_state = second @ initial

print(f"n={n_qubits}, t={simulation_time}, steps={steps}")
print(f"First-order operator error:  {operator_error(exact, first):.6e}")
print(f"Second-order operator error: {operator_error(exact, second):.6e}")
print(f"First-order infidelity:      {1-state_fidelity(exact_state, first_state):.6e}")
print(f"Second-order infidelity:     {1-state_fidelity(exact_state, second_state):.6e}")

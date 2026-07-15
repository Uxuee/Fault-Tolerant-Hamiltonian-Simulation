"""Optional Qiskit circuit synthesis for TFIM time evolution.

Install with: pip install -e ".[qiskit]"
"""

from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import SparsePauliOp
from qiskit.synthesis import LieTrotter, SuzukiTrotter


def qiskit_tfim(n_qubits: int, coupling: float, field: float) -> SparsePauliOp:
    terms: list[tuple[str, float]] = []
    for qubit in range(n_qubits - 1):
        label = ["I"] * n_qubits
        # Qiskit labels display q_(n-1) ... q_0.
        label[n_qubits - 1 - qubit] = "Z"
        label[n_qubits - 1 - (qubit + 1)] = "Z"
        terms.append(("".join(label), coupling))
    for qubit in range(n_qubits):
        label = ["I"] * n_qubits
        label[n_qubits - 1 - qubit] = "X"
        terms.append(("".join(label), field))
    return SparsePauliOp.from_list(terms)


n_qubits = 6
simulation_time = 2.0
steps = 8
hamiltonian = qiskit_tfim(n_qubits, coupling=1.0, field=0.8)

for name, synthesis in (
    ("Lie-Trotter", LieTrotter(reps=steps)),
    ("Suzuki order 2", SuzukiTrotter(order=2, reps=steps)),
):
    circuit = QuantumCircuit(n_qubits)
    circuit.append(PauliEvolutionGate(hamiltonian, time=simulation_time, synthesis=synthesis), range(n_qubits))
    decomposed = transpile(circuit, basis_gates=["rz", "sx", "x", "cx"], optimization_level=1)
    print(f"\n{name}")
    print(f"Depth: {decomposed.depth()}")
    print(f"Gate counts: {dict(decomposed.count_ops())}")

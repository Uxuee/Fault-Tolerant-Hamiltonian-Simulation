"""Plot the ideal finite-register QPE distribution."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from ft_ham_sim.qpe import most_likely_phase, qpe_distribution

output = Path("results/figures")
output.mkdir(parents=True, exist_ok=True)

phase = 0.37
counting_qubits = 5
probabilities = qpe_distribution(phase, counting_qubits)
outcomes = np.arange(len(probabilities))
approximation = most_likely_phase(probabilities)

plt.bar(outcomes, probabilities)
plt.xlabel("Integer outcome y")
plt.ylabel("Probability")
plt.title(f"Ideal QPE distribution: phase={phase}, m={counting_qubits}")
plt.tight_layout()
plt.savefig(output / "qpe_distribution.png", dpi=180)

print(f"True phase:        {phase:.8f}")
print(f"Most likely phase: {approximation:.8f}")
print(f"Absolute error:    {abs(phase-approximation):.8f}")
print("Wrote results/figures/qpe_distribution.png")

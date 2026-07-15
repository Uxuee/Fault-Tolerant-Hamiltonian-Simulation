"""Generate TFIM Trotter convergence data and a log-log figure."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from ft_ham_sim.hamiltonians import tfim_components
from ft_ham_sim.metrics import operator_error
from ft_ham_sim.trotter import exact_unitary, trotter_unitary

output_tables = Path("results/tables")
output_figures = Path("results/figures")
output_tables.mkdir(parents=True, exist_ok=True)
output_figures.mkdir(parents=True, exist_ok=True)

n_qubits = 4
simulation_time = 1.0
steps_values = [1, 2, 4, 8, 16, 32]
h_zz, h_x = tfim_components(n_qubits, coupling=1.0, field=0.8)
exact = exact_unitary(h_zz + h_x, simulation_time)

rows = []
for steps in steps_values:
    for order in (1, 2):
        approximate = trotter_unitary((h_zz, h_x), simulation_time, steps, order)
        rows.append(
            {
                "n_qubits": n_qubits,
                "time": simulation_time,
                "steps": steps,
                "order": order,
                "operator_error": operator_error(exact, approximate),
            }
        )

data = pd.DataFrame(rows)
data.to_csv(output_tables / "trotter_convergence.csv", index=False)

for order, group in data.groupby("order"):
    plt.loglog(group["steps"], group["operator_error"], marker="o", label=f"order {order}")
plt.xlabel("Trotter steps")
plt.ylabel("Spectral-norm error")
plt.title("TFIM product-formula convergence")
plt.legend()
plt.tight_layout()
plt.savefig(output_figures / "trotter_convergence.png", dpi=180)

print(data.to_string(index=False))
print("\nWrote results/tables/trotter_convergence.csv")
print("Wrote results/figures/trotter_convergence.png")

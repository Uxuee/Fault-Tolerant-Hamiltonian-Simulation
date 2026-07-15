"""Compare naive logical resources for first- and second-order TFIM formulas."""

import pandas as pd

from ft_ham_sim.resources import tfim_trotter_resources

rows = []
for order in (1, 2):
    estimate = tfim_trotter_resources(
        n_qubits=16,
        steps=100,
        order=order,
        synthesis_error_budget=2.5e-4,
    )
    rows.append(estimate.as_dict())

frame = pd.DataFrame(rows)
print(frame.to_string(index=False))
print("\nThese are naive logical counts. Second-order half layers are not merged.")
print("The T values are synthesis proxies, not production compiler results.")

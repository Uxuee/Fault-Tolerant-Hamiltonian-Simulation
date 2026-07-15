"""Sweep physical error rate in the transparent surface-code planning model."""

import pandas as pd

from ft_ham_sim.surface_code import estimate_surface_code

rows = []
for physical_error_rate in (1e-3, 5e-4, 2e-4, 1e-4):
    estimate = estimate_surface_code(
        logical_qubits=32,
        logical_locations=2_000_000,
        qec_error_budget=2.5e-4,
        physical_error_rate=physical_error_rate,
        cycle_time_seconds=1e-6,
    )
    row = {"physical_error_rate": physical_error_rate, **estimate.as_dict()}
    rows.append(row)

print(pd.DataFrame(rows).to_string(index=False))
print("\nExcluded: routing, lattice-surgery layout, decoder latency, and factories.")

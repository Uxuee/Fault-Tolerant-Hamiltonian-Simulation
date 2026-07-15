$ErrorActionPreference = "Stop"
pytest
python examples/01_exact_single_qubit.py
python examples/02_ising_exact_vs_trotter.py
python examples/03_trotter_convergence.py
python examples/04_phase_estimation_distribution.py
python examples/05_logical_resource_estimate.py
python examples/06_surface_code_toy_model.py

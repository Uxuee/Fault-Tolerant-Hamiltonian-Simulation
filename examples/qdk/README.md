# Microsoft Quantum Resource Estimator lab

This optional example follows the current layered `qdk.qre` workflow:

1. Load a Q# Hamiltonian-simulation-like circuit.
2. Wrap it as a `QSharpApplication`.
3. Declare a gate-based hardware architecture.
4. Query surface-code and round-based-factory choices.
5. Inspect the Pareto frontier.

Install and run:

```bash
pip install -e ".[qre]"
python examples/qdk/run_qre.py
```

The Q# program uses fixed constants so that its resource trace is deterministic. Change the number of qubits, Trotter steps, and rotation angles, then compare the resulting frontier. Save both the source file and architecture parameters with any estimate you quote.

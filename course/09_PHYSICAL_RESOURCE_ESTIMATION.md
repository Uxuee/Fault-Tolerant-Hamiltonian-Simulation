# Module 9 — From Logical Counts to Physical Resources

A physical estimate requires assumptions about:

- physical gate and measurement error rates;
- gate and measurement times;
- the QEC code and decoder;
- logical layout and routing;
- non-Clifford synthesis;
- magic-state distillation and throughput;
- allowed total failure probability.

There is no assumption-free number of “physical qubits required.”

## Two labs

### Transparent teaching model

`examples/06_surface_code_toy_model.py` converts logical qubits and fault locations into a code distance, data-block footprint, and runtime proxy. Every formula is visible in `src/ft_ham_sim/surface_code.py`.

### Microsoft Quantum Resource Estimator

The optional lab in `examples/qdk/` uses the maintained `qdk.qre` Python interface. It builds:

1. a Q# application model;
2. a gate-based architecture model;
3. a surface-code and round-based-factory query;
4. a Pareto frontier of physical-qubit/runtime estimates.

Install it with:

```bash
pip install -e ".[qre]"
python examples/qdk/run_qre.py
```

Treat tool output as conditional on its model inputs. Save the inputs beside every reported estimate.

## Deliverable

Create a comparison table with at least two physical error rates and two gate times. Report the Pareto-optimal result you would choose under:

- a qubit-constrained scenario;
- a runtime-constrained scenario.

Continue to [Module 10](10_CAPSTONE.md).

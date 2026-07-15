# Contributing

Use small, testable changes. Every numerical claim should identify parameters, conventions, and an error metric.

Suggested branch names:

- `lesson/module-04-qpe`
- `experiment/trotter-field-sweep`
- `feature/qre-scenarios`
- `fix/qubit-ordering`

Before opening a pull request:

```bash
pytest
python examples/02_ising_exact_vs_trotter.py
```

Do not silently replace a teaching approximation with a more sophisticated model. Document the old and new assumptions so results remain reproducible.

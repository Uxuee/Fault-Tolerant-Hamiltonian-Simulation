# Module 1 — Pauli Hamiltonians

## Learning goals

By the end of this module you should be able to:

- express a spin Hamiltonian as a weighted sum of Pauli strings;
- distinguish matrix size from description size;
- construct the TFIM Hamiltonian numerically;
- check Hermiticity and simple commutation relations.

## Pauli-string representation

Any \(n\)-qubit Hermitian operator can be expanded as

\[
H=\sum_{P\in\{I,X,Y,Z\}^{\otimes n}} \alpha_P P,
\qquad
\alpha_P=2^{-n}\operatorname{Tr}(PH).
\]

There are \(4^n\) possible strings, but physically useful Hamiltonians are often sparse: only polynomially many coefficients are nonzero.

For the open-chain TFIM,

\[
H_Z=J\sum_{i=0}^{n-2}Z_iZ_{i+1},
\qquad
H_X=h\sum_{i=0}^{n-1}X_i.
\]

All terms inside \(H_Z\) commute with one another, and all terms inside \(H_X\) commute with one another. In general, \([H_Z,H_X]\ne0\). That single noncommutation is the source of product-formula error.

## Lab

Inspect `src/ft_ham_sim/operators.py` and `hamiltonians.py`, then run:

```bash
python -c "from ft_ham_sim.hamiltonians import tfim_hamiltonian; print(tfim_hamiltonian(3))"
```

For \(n=3\), verify numerically that:

```python
import numpy as np
from ft_ham_sim.hamiltonians import tfim_components
hz, hx = tfim_components(3)
print(np.linalg.norm(hz @ hx - hx @ hz))
```

The result should be nonzero.

## Research habit

Always document:

- qubit ordering;
- boundary conditions;
- signs and units in the Hamiltonian;
- whether coefficients have been rescaled;
- the norm used in an error claim.

Continue to [Module 2](02_EXACT_EVOLUTION.md).

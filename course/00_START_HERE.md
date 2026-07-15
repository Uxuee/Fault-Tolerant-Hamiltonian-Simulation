# Module 0 — Start Here: From Hamiltonian to Hardware

## The central pipeline

A useful way to organize the field is

\[
H \rightarrow U(t)=e^{-iHt}
\rightarrow \widetilde U(t)
\rightarrow \text{logical circuit}
\rightarrow \text{fault-tolerant layout}
\rightarrow \text{physical qubits and runtime}.
\]

Each arrow introduces a different approximation or engineering assumption. A trustworthy resource estimate must state all of them.

## Four error sources

We will use an additive planning budget,

\[
\epsilon_{\mathrm{total}}
\approx \epsilon_{\mathrm{model}}
+\epsilon_{\mathrm{algorithm}}
+\epsilon_{\mathrm{synthesis}}
+\epsilon_{\mathrm{QEC}}.
\]

This is not automatically a rigorous theorem. It is a disciplined bookkeeping convention. Later modules explain when stronger norm inequalities are available.

- **Model error:** Does the encoded Hamiltonian represent the physical problem?
- **Algorithmic error:** Trotter error, truncation error, phase-estimation error, and so on.
- **Synthesis error:** Approximation of arbitrary rotations by a discrete fault-tolerant gate set.
- **QEC failure:** Probability that logical faults corrupt the computation.

## What this course does and does not do

The course begins with dense matrices because they make approximations visible. Dense simulation scales exponentially and is used only for small validation examples. We then move to Pauli descriptions, circuit counts, and fault-tolerant abstractions that can be analyzed without constructing a \(2^n\times2^n\) matrix.

## Your first task

Run:

```bash
python examples/02_ising_exact_vs_trotter.py
```

Then answer:

1. Why is the second-order error smaller for the chosen parameters?
2. Which cost grows when the number of Trotter steps increases?
3. Which reported quantity is algorithmic, and which is a circuit-resource proxy?

Continue to [Module 1](01_PAULI_HAMILTONIANS.md).

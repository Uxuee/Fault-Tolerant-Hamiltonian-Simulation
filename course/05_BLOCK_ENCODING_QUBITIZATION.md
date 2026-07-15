# Module 5 — Block Encoding and Qubitization

Product formulas decompose time into many short steps. Modern algorithms often take a different route: encode the Hamiltonian inside a larger unitary and transform its spectrum.

## Block encoding

A unitary \(U_H\) is an \((\alpha,a,\epsilon)\) block encoding of \(H\) when

\[
\left\|H-\alpha
(\langle0|^{\otimes a}\otimes I)
U_H
(|0\rangle^{\otimes a}\otimes I)
\right\|\le\epsilon.
\]

The normalization \(\alpha\), ancilla count \(a\), and implementation cost of \(U_H\) are resource parameters—not decorative notation.

## PREPARE and SELECT

For a decomposition

\[
H=\sum_{j=0}^{L-1}\alpha_j P_j,
\]

one common construction uses:

- `PREPARE`: create amplitudes related to \(\sqrt{|\alpha_j|/\alpha}\);
- `SELECT`: apply the indexed Pauli operation \(P_j\).

The asymptotic query complexity may be excellent while the concrete cost of these oracles remains substantial. Resource estimation must open the oracle box.

## Qubitization and QSP

Qubitization constructs a walk operator whose invariant subspaces encode eigenvalues of the block-encoded Hamiltonian. Quantum signal processing then applies a polynomial transformation to those eigenvalues. Hamiltonian simulation emerges by approximating \(e^{-itx}\) with a suitable polynomial.

## Module deliverable

For the TFIM, design a register layout for an indexed list of the \(2n-1\) Pauli terms. Write down:

1. the index-register size;
2. the coefficient-state preparation problem;
3. a high-level `SELECT` implementation;
4. which operations would likely dominate a fault-tolerant cost.

This module is intentionally conceptual. Do not claim a qubitization advantage until the oracle costs and error conventions have been compared on equal footing.

Continue to [Module 6](06_QEC_STABILIZERS.md).

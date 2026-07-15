# Module 2 — Exact Evolution as a Validation Oracle

For a time-independent Hamiltonian,

\[
|\psi(t)\rangle=e^{-iHt}|\psi(0)\rangle.
\]

For small systems we evaluate the exponential directly with `scipy.linalg.expm`. This is not a scalable quantum algorithm. It is a reference calculation against which approximate methods can be tested.

## Useful checks

For Hermitian \(H\), the propagator is unitary:

\[
U(t)^\dagger U(t)=I.
\]

For a normalized state, the norm should remain one. Expectation values of Hermitian observables should be real up to floating-point noise.

## State fidelity

For pure states, we use

\[
F(\psi,\phi)=|\langle\psi|\phi\rangle|^2.
\]

Fidelity is state dependent. Two unitaries may agree on one state but differ strongly on another. Therefore the repository also reports operator-norm error,

\[
\|U-\widetilde U\|_2.
\]

## Lab

Run:

```bash
python examples/01_exact_single_qubit.py
python examples/02_ising_exact_vs_trotter.py
```

Modify the initial state in the second script from \(|0000\rangle\) to a random normalized state. Compare how the state infidelity changes while the operator error stays fixed.

Continue to [Module 3](03_PRODUCT_FORMULAS.md).

# Module 10 — Capstone: End-to-End TFIM Estimate

## Specification

Choose and freeze:

- \(n\), \(J\), \(h\), \(t\);
- initial state and target observable or energy precision;
- total allowed error;
- simulation algorithm;
- physical scenarios.

A suggested starting specification is

\[
n=16,\quad J=h=1,\quad t=10,\quad
\epsilon_{\mathrm{total}}=10^{-3}.
\]

## Required analysis

### 1. Small-system validation

Use \(n\le6\) dense simulations to validate implementation and error scaling. Do not extrapolate dense runtime as quantum runtime.

### 2. Algorithmic choice

Select a product formula or formulate a block-encoding/qubitization alternative. State the theorem, heuristic, or numerical procedure used to choose parameters.

### 3. Logical estimate

Report logical qubits, rotations, Clifford operations, CNOTs, \(T\)-proxy/count, and depth assumptions.

### 4. Physical estimate

Compare at least two hardware models. Include code distance, data qubits, factory qubits when available, runtime, and failure probability.

### 5. Sensitivity analysis

Plot resources against at least three of:

- target precision;
- physical error rate;
- simulation time;
- system size;
- rotation-synthesis allocation;
- factory throughput.

## Final report structure

1. Executive summary
2. Problem definition
3. Hamiltonian encoding
4. Simulation algorithm
5. Error budget
6. Logical resources
7. Physical resources
8. Sensitivity analysis
9. Limitations
10. Reproducibility instructions

A good capstone does not hide unfavorable numbers. Its value is the transparent chain from scientific question to hardware assumptions.

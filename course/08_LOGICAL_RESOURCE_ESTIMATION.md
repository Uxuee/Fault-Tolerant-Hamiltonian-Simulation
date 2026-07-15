# Module 8 — Logical Resource Estimation

Logical resource estimation should be performed before hardware assumptions are introduced.

For the open-chain TFIM, a naive first-order Trotter step contains:

- \(n-1\) two-qubit \(ZZ\) rotations;
- \(n\) single-qubit \(X\) rotations.

If a \(ZZ\) rotation is decomposed as CNOT–\(R_Z\)–CNOT, a step contains \(2(n-1)\) CNOTs and \(2n-1\) arbitrary rotations.

For the symmetric second-order formula, the naive count doubles the \(ZZ\) layer. Adjacent half-layers can sometimes be merged, so distinguish **naive counts** from **optimized counts**.

## Rotation synthesis

An arbitrary-angle rotation is not generally an exact Clifford+\(T\) operation. A compiler approximates it to an error tolerance \(\epsilon_R\). The course uses a configurable proxy for \(T\)-cost to make this dependency visible. It is intentionally labelled as a proxy, because concrete synthesis algorithms and ancilla assumptions change the constants.

## Error-budget trap

If there are \(N_R\) rotations, assigning the full synthesis budget to each rotation is wrong. A conservative allocation may use

\[
\epsilon_R\approx\epsilon_{\mathrm{synthesis}}/N_R.
\]

That tighter per-rotation precision increases \(T\)-cost.

## Lab

Run:

```bash
python examples/05_logical_resource_estimate.py
```

Then compare first- and second-order formulas at a fixed number of steps. This is not yet a fair algorithm comparison: you must first choose the step counts required to meet the same simulation-error target.

Continue to [Module 9](09_PHYSICAL_RESOURCE_ESTIMATION.md).

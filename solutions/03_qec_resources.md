# Solution 3 — Syndromes and resources

## Part A

An X error anticommutes with a Z stabilizer when it acts on a qubit contained in that stabilizer.

| Error | S1 | S2 | Correction |
|---|---:|---:|---|
| I | +1 | +1 | I |
| X0 | -1 | +1 | X0 |
| X1 | -1 | -1 | X1 |
| X2 | +1 | -1 | X2 |

## Part B

For first order:

- ZZ rotations: \(r(n-1)=500\times19=9500\)
- X rotations: \(rn=500\times20=10000\)
- arbitrary rotations: 19500
- CNOTs: \(2\times9500=19000\)
- per-rotation error: \(10^{-4}/19500\)

Use `tfim_trotter_resources(20, 500, 1, 1e-4)` for the proxy result.

## Part C

Evaluate odd distances until \(N p_L(d)\le2.5\times10^{-4}\). The package performs this search directly. The rough data-block cost is \(40\times2d^2\). Omitted costs include magic-state factories, routing/layout, lattice surgery, syndrome ancillas beyond the patch proxy, decoding latency, idle errors, classical control, and state preparation.

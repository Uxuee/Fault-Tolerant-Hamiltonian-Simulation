# Module 6 — Quantum Error Correction and Stabilizers

A quantum code embeds a logical state into a larger Hilbert space so that a set of likely errors can be detected and corrected without measuring the logical information directly.

## Stabilizer codes

A stabilizer code is the simultaneous \(+1\) eigenspace of a commuting subgroup of the Pauli group. If generators are \(S_1,\ldots,S_r\), measuring them yields a syndrome. Errors that anticommute with a generator flip its measured sign.

For the three-qubit bit-flip code,

\[
|0_L\rangle=|000\rangle,\qquad |1_L\rangle=|111\rangle,
\]

with stabilizers

\[
S_1=Z_0Z_1,\qquad S_2=Z_1Z_2.
\]

The syndrome identifies a single \(X\) error, but the code does not correct arbitrary single-qubit errors.

## Code distance

The distance \(d\) is the minimum weight of a Pauli operator that acts nontrivially on the logical subspace while commuting with all stabilizers. A distance-\(d\) code corrects up to \(\lfloor(d-1)/2\rfloor\) errors under the idealized code model.

## Fault tolerance is stronger than error correction

A circuit is fault tolerant when a small number of physical faults does not spread into an uncorrectable logical error. Syndrome extraction itself must therefore be designed carefully.

## Exercise

Complete the syndrome table in `exercises/03_qec_resources.md`. Then study how the table follows from commutation rather than from inspecting basis states.

Continue to [Module 7](07_SURFACE_CODE_FAULT_TOLERANCE.md).

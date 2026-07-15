# Module 4 — Quantum Phase Estimation

Suppose

\[
U|u\rangle=e^{2\pi i\phi}|u\rangle,
\qquad \phi\in[0,1).
\]

Quantum phase estimation (QPE) uses controlled powers of \(U\), phase kickback, and an inverse quantum Fourier transform to estimate \(\phi\). For Hamiltonian eigenstates,

\[
U(t)=e^{-iHt},\qquad H|E\rangle=E|E\rangle,
\]

so the measured phase encodes the energy modulo the chosen time scale.

## Why Hamiltonian simulation cost is amplified

QPE requires controlled evolutions for different effective times. A small time-evolution subroutine can therefore be invoked many times. Precision in the output energy is tied to the number of counting qubits and the maximum coherent evolution time.

## Ideal distribution

The example `examples/04_phase_estimation_distribution.py` calculates the ideal measurement distribution without constructing a circuit. It isolates the finite-register effect:

\[
p(y)=\left|\frac{1}{2^m}
\sum_{k=0}^{2^m-1}
 e^{2\pi i k(\phi-y/2^m)}\right|^2.
\]

Run it and compare \(m=4,5,6\). Record the most probable binary estimate and its absolute error.

## Key warning

Energy aliasing occurs if the mapping between \(E\) and \(\phi\) is not chosen so that the relevant spectrum maps injectively into the phase interval. Resource estimates must include the cost of any spectral shifting, rescaling, or state preparation.

Continue to [Module 5](05_BLOCK_ENCODING_QUBITIZATION.md).

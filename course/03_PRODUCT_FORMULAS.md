# Module 3 — Lie–Trotter and Suzuki Product Formulas

Let \(H=A+B\). If \([A,B]=0\), then

\[
e^{-it(A+B)}=e^{-itA}e^{-itB}.
\]

When they do not commute, the first-order formula is

\[
S_1(t/r)^r=
\left(e^{-iAt/r}e^{-iBt/r}\right)^r,
\]

and the symmetric second-order formula is

\[
S_2(t/r)^r=
\left(e^{-iAt/(2r)}e^{-iBt/r}e^{-iAt/(2r)}\right)^r.
\]

For fixed \(t\) and sufficiently regular operators, first-order global error scales roughly as \(O(t^2/r)\), whereas second-order error scales roughly as \(O(t^3/r^2)\). The constants depend on commutators and can matter enormously.

## What to measure

A complete experiment should vary:

- system size \(n\);
- simulation time \(t\);
- number of steps \(r\);
- formula order;
- coupling ratio \(h/J\);
- initial state.

Report both approximation error and implementation cost. A method is not useful merely because its error is low; the question is how much cost was required to achieve it.

## Lab

Run:

```bash
python examples/03_trotter_convergence.py
```

The script produces a log-log plot. Estimate the slopes of the first- and second-order curves. Explain why finite precision and the selected parameter range may prevent the fitted slopes from exactly matching asymptotic theory.

## Exercise

Complete `exercises/02_trotter.md`, then compare with `solutions/02_trotter.md`.

Continue to [Module 4](04_PHASE_ESTIMATION.md).

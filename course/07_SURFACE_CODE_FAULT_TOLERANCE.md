# Module 7 — Surface Codes, Logical Gates, and Magic States

Surface codes store logical information nonlocally in a two-dimensional stabilizer lattice. Their appeal comes from local checks and comparatively high thresholds under suitable noise models. The cost is substantial space-time overhead.

## Planning formula

The repository's teaching model uses

\[
p_L(d)=A\left(\frac{p}{p_{\mathrm{th}}}\right)^{(d+1)/2},
\]

where \(p\) is a physical error rate and \(d\) is an odd code distance. This is a phenomenological scaling law, not a universal law of nature. The constants depend on architecture, decoder, circuit, and noise model.

Given \(N\) logical fault locations and budget \(\epsilon_{\mathrm{QEC}}\), the model selects the smallest odd \(d\) satisfying

\[
N p_L(d)\le\epsilon_{\mathrm{QEC}}.
\]

It then uses a rough patch cost of \(2d^2\) physical qubits per logical qubit. Production tools use richer layout, routing, scheduling, and factory models.

## Non-Clifford operations

Clifford gates alone are not computationally universal. Fault-tolerant architectures often implement non-Clifford gates by consuming distilled magic states. Consequently, \(T\)-count, \(T\)-depth, factory throughput, and factory footprint become central resource metrics.

## Lab

Run:

```bash
python examples/06_surface_code_toy_model.py
```

Explain why a modest change in physical error rate can cause a discrete jump in selected code distance and therefore a large jump in qubit cost.

Continue to [Module 8](08_LOGICAL_RESOURCE_ESTIMATION.md).

# Fault-Tolerant Hamiltonian Simulation

A project-based course that connects three questions:

1. How do we approximate \(U(t)=e^{-iHt}\)?
2. What logical circuit resources does the approximation require?
3. What fault-tolerant machine could execute that circuit?

The running example is the one-dimensional transverse-field Ising model (TFIM),

\[
H = J\sum_{i=0}^{n-2} Z_i Z_{i+1} + h\sum_{i=0}^{n-1} X_i.
\]

This repository is designed for a physicist who already knows linear algebra and quantum mechanics and wants to build research-grade intuition through derivations, numerical experiments, circuits, tests, and progressively less idealized resource models.

## Start here

### 1. Create the environment

Using Conda:

```bash
conda env create -f environment.yml
conda activate ft-ham-sim
pip install -e ".[dev]"
```

Or using `venv`:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 2. Check that everything works

```bash
pytest
python examples/01_exact_single_qubit.py
python examples/02_ising_exact_vs_trotter.py
python examples/03_trotter_convergence.py
```

The convergence script writes a table and figure to `results/`.

### 3. Follow the course in order

Open [`course/00_START_HERE.md`](course/00_START_HERE.md), then work through the modules and labs. The first notebook is [`notebooks/00_start_here.ipynb`](notebooks/00_start_here.ipynb).

## Course map

| Module | Main question | Runnable work | Deliverable |
|---|---|---|---|
| 0 | How does the whole stack connect? | Start-here notebook | One-page concept map |
| 1 | How are Hamiltonians represented computationally? | Pauli utilities | Build a TFIM matrix |
| 2 | What does exact evolution look like? | Exact matrix exponentiation | Observable-vs-time plot |
| 3 | How do product formulas approximate evolution? | First/second-order Trotter | Error scaling study |
| 4 | How does simulation enter phase estimation? | Ideal QPE distribution | Precision analysis |
| 5 | Why do block encodings and qubitization matter? | Paper-and-pencil oracle design | PREPARE/SELECT sketch |
| 6 | How are logical qubits protected? | Repetition/stabilizer exercises | Syndrome table |
| 7 | What makes a circuit fault tolerant? | Surface-code planning model | Code-distance sweep |
| 8 | Which logical resources dominate? | Logical gate counter | Error-budget table |
| 9 | How do logical counts become physical resources? | Toy model + Microsoft QRE lab | Qubit/runtime comparison |
| 10 | Can we produce an end-to-end estimate? | Capstone | Technical report + figures |

## Repository structure

```text
Fault-Tolerant-Hamiltonian-Simulation/
├── course/                 # Guided lessons and derivations
├── examples/               # Small runnable programs
│   └── qdk/                # Optional Microsoft QRE example
├── exercises/              # Problems without answers
├── solutions/              # Worked solutions
├── notebooks/              # Interactive labs
├── src/ft_ham_sim/         # Reusable Python package
├── tests/                  # Unit tests
├── results/                # Generated figures and tables
├── environment.yml
└── pyproject.toml
```

## The two levels of resource estimation

This course deliberately keeps these separate:

- **Logical estimation:** logical qubits, arbitrary rotations, Clifford gates, CNOTs, \(T\)-count proxies, depth, and algorithmic error.
- **Physical estimation:** code distance, physical qubits, code cycles, magic-state factories, runtime, and total failure probability.

The included surface-code calculator is a **transparent teaching model**, not a production estimator. It exposes every assumption. The optional Microsoft Quantum Resource Estimator lab then shows how a modern tool explores architecture, QEC, and factory choices.

## Optional tooling

Install only what you need:

```bash
pip install -e ".[qiskit]"   # circuit synthesis and gate counts
pip install -e ".[qualtran]" # hierarchical logical resource analysis
pip install -e ".[qre]"      # Microsoft qdk.qre physical estimation
```

The Qiskit example uses `SparsePauliOp`, `PauliEvolutionGate`, and product-formula synthesis. The QRE example uses the current `qdk.qre` Python interface rather than the older VS Code-only estimator workflow.

## Capstone

Estimate the resources for a TFIM simulation with a declared specification, for example

\[
n=16,\quad J=h=1,\quad t=10,\quad \epsilon_{\mathrm{total}}=10^{-3}.
\]

Your final report should contain:

1. The Hamiltonian and initial state.
2. The selected simulation algorithm.
3. A justified error budget.
4. Logical resource scaling and concrete counts.
5. At least two physical-hardware scenarios.
6. Sensitivity plots showing which assumptions dominate.
7. A limitations section separating rigorous results from planning approximations.

## GitHub setup

After downloading this folder:

```bash
cd Fault-Tolerant-Hamiltonian-Simulation
git init -b main
git add .
git commit -m "Initial fault-tolerant Hamiltonian simulation course"
git remote add origin https://github.com/Uxuee/Fault-Tolerant-Hamiltonian-Simulation.git
git push -u origin main
```

Create the empty GitHub repository before the final two commands. Do not initialize it with another README, because this project already contains one.

## References and live documentation

The lessons point to primary papers and maintained documentation. Useful starting points include IBM Quantum Learning's Hamiltonian-simulation material, IBM's Qiskit API documentation, Microsoft's `qdk.qre` documentation, and Qualtran's bloq/resource-estimation documentation.

## License

MIT. See [`LICENSE`](LICENSE).

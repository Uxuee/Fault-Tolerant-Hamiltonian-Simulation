# Course syllabus

This is a twelve-week suggested schedule. Compress or expand it according to your available time; keep the order because later estimates depend on earlier conventions.

| Week | Reading | Practical work | Evidence of completion |
|---:|---|---|---|
| 1 | Modules 0–1 | Pauli utilities and TFIM construction | Hermiticity/commutator checks |
| 2 | Module 2 | Exact small-system evolution | Observable and fidelity calculations |
| 3 | Module 3 | First-order Trotter study | Error-versus-step plot |
| 4 | Module 3 | Second-order and parameter sweeps | Fitted convergence slopes |
| 5 | Module 4 | Ideal QPE | Phase-resolution table |
| 6 | Module 5 | Block encoding | PREPARE/SELECT design note |
| 7 | Module 6 | Stabilizers and syndromes | Completed syndrome exercises |
| 8 | Module 7 | Surface code and magic states | Code-distance sensitivity table |
| 9 | Module 8 | Logical resource estimation | Logical-count notebook |
| 10 | Module 9 | Physical resource estimation | Toy-model and QRE comparison |
| 11 | Module 10 | Capstone experiments | Draft figures and tables |
| 12 | Module 10 | Report and reproducibility | Tagged repository release |

## Weekly workflow

1. Read the module and rewrite its central derivation by hand.
2. Run the supplied example without modifications.
3. Change one physical parameter and one numerical/resource parameter.
4. Record what changed and why in a short lab note.
5. Complete the exercise before opening the solution.
6. Commit with a message that describes the scientific change, not merely “update.”

## Suggested lab-note template

```text
Question:
Model and conventions:
Parameters:
Method:
Error metric:
Resource metric:
Result:
Interpretation:
Limitations:
Next experiment:
```

The goal is not to collect notebooks. It is to develop an auditable chain of reasoning from a Hamiltonian to a resource claim.

"""Transparent logical-resource planning models.

These functions are deliberately simple. They are useful for learning and
sensitivity analysis, but they are not substitutes for a compiler-level
resource estimator.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import ceil, log2


@dataclass(frozen=True)
class LogicalResources:
    logical_qubits: int
    trotter_steps: int
    formula_order: int
    zz_rotations: int
    x_rotations: int
    arbitrary_rotations: int
    cnot_count: int
    rotation_error: float
    t_per_rotation_proxy: int
    t_count_proxy: int

    def as_dict(self) -> dict[str, int | float]:
        return asdict(self)


def rotation_t_proxy(error: float, slope: float = 3.0, intercept: float = 0.0) -> int:
    """Pedagogical proxy ``ceil(slope*log2(1/error)+intercept)``.

    It exposes precision dependence but should not be quoted as a definitive
    synthesis cost. Replace it with a selected compiler/synthesis model in a
    serious estimate.
    """
    if not 0 < error < 1:
        raise ValueError("Rotation error must lie strictly between zero and one.")
    return max(0, ceil(slope * log2(1.0 / error) + intercept))


def tfim_trotter_resources(
    n_qubits: int,
    steps: int,
    order: int = 1,
    synthesis_error_budget: float = 1e-3,
) -> LogicalResources:
    """Naive open-chain TFIM logical counts.

    Each ZZ rotation is counted as CNOT-RZ-CNOT. Adjacent second-order half
    layers are not merged, so the second-order values are intentionally naive.
    """
    if n_qubits < 2:
        raise ValueError("n_qubits must be at least two")
    if steps < 1:
        raise ValueError("steps must be positive")
    if order not in (1, 2):
        raise ValueError("order must be 1 or 2")
    if not 0 < synthesis_error_budget < 1:
        raise ValueError("synthesis_error_budget must lie between zero and one")

    zz_per_step = (n_qubits - 1) if order == 1 else 2 * (n_qubits - 1)
    x_per_step = n_qubits
    zz_rotations = steps * zz_per_step
    x_rotations = steps * x_per_step
    rotations = zz_rotations + x_rotations
    per_rotation_error = synthesis_error_budget / rotations
    t_per_rotation = rotation_t_proxy(per_rotation_error)

    return LogicalResources(
        logical_qubits=n_qubits,
        trotter_steps=steps,
        formula_order=order,
        zz_rotations=zz_rotations,
        x_rotations=x_rotations,
        arbitrary_rotations=rotations,
        cnot_count=2 * zz_rotations,
        rotation_error=per_rotation_error,
        t_per_rotation_proxy=t_per_rotation,
        t_count_proxy=rotations * t_per_rotation,
    )

"""A transparent, phenomenological surface-code planning model."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class SurfaceCodeEstimate:
    distance: int
    logical_error_per_location: float
    estimated_failure_probability: float
    physical_qubits_per_logical: int
    data_block_physical_qubits: int
    code_cycles: int
    runtime_seconds: float

    def as_dict(self) -> dict[str, int | float]:
        return asdict(self)


def logical_error_rate(
    physical_error_rate: float,
    distance: int,
    threshold: float = 1e-2,
    prefactor: float = 0.1,
) -> float:
    """Phenomenological logical-error scaling law."""
    if not 0 < physical_error_rate < threshold:
        raise ValueError("physical_error_rate must be positive and below threshold")
    if distance < 1 or distance % 2 == 0:
        raise ValueError("distance must be a positive odd integer")
    return prefactor * (physical_error_rate / threshold) ** ((distance + 1) / 2)


def estimate_surface_code(
    logical_qubits: int,
    logical_locations: int,
    qec_error_budget: float,
    physical_error_rate: float,
    cycle_time_seconds: float = 1e-6,
    cycles_per_location_factor: float = 1.0,
    threshold: float = 1e-2,
    prefactor: float = 0.1,
    maximum_distance: int = 99,
) -> SurfaceCodeEstimate:
    """Select the smallest odd distance satisfying a union-bound budget.

    Runtime and qubit counts include only a data-block proxy. Routing, lattice
    surgery, idle errors, decoding latency, and magic-state factories are not
    included.
    """
    if logical_qubits < 1 or logical_locations < 1:
        raise ValueError("logical_qubits and logical_locations must be positive")
    if not 0 < qec_error_budget < 1:
        raise ValueError("qec_error_budget must lie between zero and one")
    if cycle_time_seconds <= 0 or cycles_per_location_factor <= 0:
        raise ValueError("time and cycle factors must be positive")

    selected_distance = None
    selected_rate = None
    for distance in range(1, maximum_distance + 1, 2):
        rate = logical_error_rate(
            physical_error_rate, distance, threshold=threshold, prefactor=prefactor
        )
        if logical_locations * rate <= qec_error_budget:
            selected_distance = distance
            selected_rate = rate
            break

    if selected_distance is None or selected_rate is None:
        raise ValueError("No code distance within maximum_distance meets the budget.")

    physical_per_logical = 2 * selected_distance**2
    cycles = int(round(logical_locations * selected_distance * cycles_per_location_factor))

    return SurfaceCodeEstimate(
        distance=selected_distance,
        logical_error_per_location=selected_rate,
        estimated_failure_probability=logical_locations * selected_rate,
        physical_qubits_per_logical=physical_per_logical,
        data_block_physical_qubits=logical_qubits * physical_per_logical,
        code_cycles=cycles,
        runtime_seconds=cycles * cycle_time_seconds,
    )

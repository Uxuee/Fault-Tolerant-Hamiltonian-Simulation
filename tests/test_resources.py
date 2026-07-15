from ft_ham_sim.resources import tfim_trotter_resources
from ft_ham_sim.surface_code import estimate_surface_code


def test_first_order_resource_counts():
    resources = tfim_trotter_resources(4, 10, order=1, synthesis_error_budget=1e-3)
    assert resources.zz_rotations == 30
    assert resources.x_rotations == 40
    assert resources.cnot_count == 60
    assert resources.arbitrary_rotations == 70


def test_surface_code_distance_is_odd_and_budget_met():
    estimate = estimate_surface_code(
        logical_qubits=10,
        logical_locations=100_000,
        qec_error_budget=1e-3,
        physical_error_rate=1e-3,
    )
    assert estimate.distance % 2 == 1
    assert estimate.estimated_failure_probability <= 1e-3

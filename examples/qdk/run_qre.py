"""Optional Microsoft Quantum Resource Estimator example.

Install with: pip install -e ".[qre]"
Run from the repository root: python examples/qdk/run_qre.py
"""

from pathlib import Path

import qdk
from qdk import qsharp
from qdk.qre import estimate
from qdk.qre.application import QSharpApplication
from qdk.qre.models import GateBased, RoundBasedFactory, SurfaceCode

qsharp_source = Path("examples/qdk/ising_trotter.qs")
qsharp.eval(qsharp_source.read_text(encoding="utf-8"))

application = QSharpApplication(qdk.code.Main)
architecture = GateBased(error_rate=1e-4, gate_time=100, measurement_time=500)
isa_query = SurfaceCode.q() * RoundBasedFactory.q()

results = estimate(
    application,
    architecture,
    isa_query=isa_query,
    max_error=0.01,
)

print(results.as_frame())

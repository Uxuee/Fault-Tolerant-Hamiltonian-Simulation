import Std.Math.*;

operation Main() : Unit {
    use qubits = Qubit[8];
    let steps = 20;
    let zzAngle = 0.10;
    let xAngle = 0.08;

    for _ in 1..steps {
        // exp(-i theta Z_i Z_(i+1)) via CNOT-Rz-CNOT.
        for i in 0..6 {
            CNOT(qubits[i], qubits[i + 1]);
            Rz(2.0 * zzAngle, qubits[i + 1]);
            CNOT(qubits[i], qubits[i + 1]);
        }

        // exp(-i phi X_i).
        for q in qubits {
            Rx(2.0 * xAngle, q);
        }
    }

    ResetAll(qubits);
}

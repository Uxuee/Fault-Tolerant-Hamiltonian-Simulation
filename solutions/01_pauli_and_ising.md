# Solution 1 — Pauli strings and the TFIM

Using \(Z\otimes Z=\operatorname{diag}(1,-1,-1,1)\),

\[
H=J(Z\otimes Z)+h(X\otimes I+I\otimes X).
\]

Each term is Hermitian because every Pauli matrix is Hermitian and tensor products preserve Hermiticity. The commutators are nonzero because \(ZX=-XZ\):

\[
[Z_0Z_1,X_0]=2iY_0Z_1,
\qquad
[Z_0Z_1,X_1]=2iZ_0Y_1.
\]

An open chain has \((n-1)+n=2n-1\) Pauli terms. A periodic chain with \(n>2\) has \(n+n=2n\) terms. A longitudinal field adds \(n\) further \(Z_i\) terms.

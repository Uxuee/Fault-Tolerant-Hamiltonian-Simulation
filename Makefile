.PHONY: setup test examples clean

setup:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

examples:
	python examples/01_exact_single_qubit.py
	python examples/02_ising_exact_vs_trotter.py
	python examples/03_trotter_convergence.py

clean:
	rm -f results/figures/*.png results/tables/*.csv

#!/usr/bin/env bash
set -euo pipefail

if ! git config user.name >/dev/null || ! git config user.email >/dev/null; then
  echo "Set your Git identity first:"
  echo '  git config --global user.name "Ariadna Palomino"'
  echo '  git config --global user.email "YOUR_GITHUB_EMAIL"'
  exit 1
fi

git init -b main
git add .
git commit -m "Initial fault-tolerant Hamiltonian simulation course"

echo
echo "Next: create an empty GitHub repository, then run:"
echo "git remote add origin https://github.com/Uxuee/Fault-Tolerant-Hamiltonian-Simulation.git"
echo "git push -u origin main"

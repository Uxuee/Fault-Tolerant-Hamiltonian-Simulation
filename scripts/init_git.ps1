$ErrorActionPreference = "Stop"

$name = git config user.name
$email = git config user.email
if (-not $name -or -not $email) {
    Write-Host "Set your Git identity first:"
    Write-Host '  git config --global user.name "Ariadna Palomino"'
    Write-Host '  git config --global user.email "YOUR_GITHUB_EMAIL"'
    exit 1
}

git init -b main
git add .
git commit -m "Initial fault-tolerant Hamiltonian simulation course"

Write-Host ""
Write-Host "Next: create an empty GitHub repository, then run:"
Write-Host "git remote add origin https://github.com/Uxuee/Fault-Tolerant-Hamiltonian-Simulation.git"
Write-Host "git push -u origin main"

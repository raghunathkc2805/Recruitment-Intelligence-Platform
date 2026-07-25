$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 Enterprise Audit Verification" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

Set-Location (Split-Path $PSScriptRoot -Parent)

Write-Host "[1/5] Running Ruff..."
ruff check .

if ($LASTEXITCODE -ne 0) {
    throw "Ruff validation failed."
}

Write-Host ""
Write-Host "[2/5] Running Black..."
black --check .

if ($LASTEXITCODE -ne 0) {
    throw "Black validation failed."
}

Write-Host ""
Write-Host "[3/5] Running MyPy..."
mypy api database

if ($LASTEXITCODE -ne 0) {
    throw "MyPy validation failed."
}

Write-Host ""
Write-Host "[4/5] Running Pytest..."
python -m pytest -q

if ($LASTEXITCODE -ne 0) {
    throw "Pytest failed."
}

Write-Host ""
Write-Host "[5/5] Verifying API imports..."

python - <<'PYCODE'
import importlib

modules = [
    "api.routes.audit",
    "api.middleware.audit_middleware",
    "api.services.audit_service",
    "api.services.audit_export_service",
    "api.services.audit_retention_service",
    "api.repositories.audit_repository",
    "api.dependencies.audit_permission",
    "database.models.audit_log",
]

for module in modules:
    importlib.import_module(module)
    print(f"[OK] {module}")

print()
print("Sprint 6 Audit Verification Successful.")
PYCODE

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host " Sprint 6 Verification PASSED" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

Write-Host ""
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 Enterprise Audit Runner" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/8] Installing dependencies..."
python -m pip install -U pip
python -m pip install -r requirements.txt

Write-Host ""
Write-Host "[2/8] Applying Alembic migrations..."
alembic upgrade head

Write-Host ""
Write-Host "[3/8] Formatting source..."
black .

Write-Host ""
Write-Host "[4/8] Linting..."
ruff check .

Write-Host ""
Write-Host "[5/8] Type checking..."
mypy api database

Write-Host ""
Write-Host "[6/8] Running all tests..."
python -m pytest -q

if ($LASTEXITCODE -ne 0) {
    throw "Pytest execution failed."
}

Write-Host ""
Write-Host "[7/8] Import verification..."

python -c @"
import importlib

modules = [
    'database.models.audit_log',
    'api.schemas.audit',
    'api.repositories.audit_repository',
    'api.services.audit_service',
    'api.services.audit_export_service',
    'api.services.audit_retention_service',
    'api.middleware.audit_middleware',
    'api.dependencies.audit_permission',
    'api.routes.audit',
]

for module in modules:
    importlib.import_module(module)
    print(f'[OK] {module}')

print()
print('All Sprint 6 Audit modules loaded successfully.')
"@

if ($LASTEXITCODE -ne 0) {
    throw "Module verification failed."
}

Write-Host ""
Write-Host "[8/8] Starting FastAPI..."
uvicorn api.main:app --reload

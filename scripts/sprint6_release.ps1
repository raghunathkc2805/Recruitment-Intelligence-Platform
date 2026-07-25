$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 Release" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/7] Cleaning Python cache..."
Get-ChildItem -Recurse -Directory -Filter "__pycache__" |
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Get-ChildItem -Recurse -Include "*.pyc" |
    Remove-Item -Force -ErrorAction SilentlyContinue

Write-Host "[2/7] Running formatters..."
black .
ruff check .

if ($LASTEXITCODE -ne 0) {
    throw "Formatting/Lint failed."
}

Write-Host "[3/7] Running unit tests..."
python -m pytest -q

if ($LASTEXITCODE -ne 0) {
    throw "Tests failed."
}

Write-Host "[4/7] Applying migrations..."
alembic upgrade head

if ($LASTEXITCODE -ne 0) {
    throw "Migration failed."
}

Write-Host "[5/7] Creating Git tag..."

$Tag = "v6.1.0-sprint6-audit"

git add .
git commit -m "Sprint 6 Enterprise Audit Logging"

git tag -a $Tag -m "Sprint 6 Release"

Write-Host "[6/7] Git Status"
git status

Write-Host "[7/7] Sprint 6 completed successfully."

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host " Sprint 6 RELEASE READY" -ForegroundColor Green
Write-Host " Tag : v6.1.0-sprint6-audit" -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green

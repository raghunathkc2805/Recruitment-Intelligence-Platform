$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

Write-Host ""
Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 Final Production Finalization" -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host ""

$Folders = @(
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".coverage",
    "htmlcov",
    "dist",
    "build"
)

Write-Host "[1/8] Cleaning temporary folders..."

foreach ($Folder in $Folders) {
    if (Test-Path $Folder) {
        Remove-Item $Folder -Recurse -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "[2/8] Removing __pycache__..."

Get-ChildItem -Recurse -Directory -Filter "__pycache__" |
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Get-ChildItem -Recurse -Filter "*.pyc" |
    Remove-Item -Force -ErrorAction SilentlyContinue

Write-Host "[3/8] Running formatting checks..."
black --check .
ruff check .

Write-Host "[4/8] Running type checks..."
mypy api database

Write-Host "[5/8] Running complete test suite..."
python -m pytest -q

if ($LASTEXITCODE -ne 0) {
    throw "Final validation failed."
}

Write-Host "[6/8] Displaying repository status..."
git status

Write-Host "[7/8] Displaying latest commit..."
git log -1 --stat

Write-Host "[8/8] Sprint 6 production baseline verified."

Write-Host ""
Write-Host "=========================================================" -ForegroundColor Green
Write-Host " SPRINT 6 PRODUCTION BASELINE COMPLETE" -ForegroundColor Green
Write-Host " Repository Ready for Sprint 7" -ForegroundColor Green
Write-Host "=========================================================" -ForegroundColor Green

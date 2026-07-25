$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform"
Write-Host " Sprint 6 Production Health Check"
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

$Checks = @()

function Add-Result {
    param(
        [string]$Name,
        [bool]$Passed
    )

    $script:Checks += [PSCustomObject]@{
        Check  = $Name
        Status = if ($Passed) { "PASS" } else { "FAIL" }
    }
}

Write-Host "[1/9] Python"

python --version
Add-Result "Python Installed" ($LASTEXITCODE -eq 0)

Write-Host "[2/9] Pip"

pip --version
Add-Result "Pip Installed" ($LASTEXITCODE -eq 0)

Write-Host "[3/9] Alembic"

alembic current *> $null
Add-Result "Alembic" ($LASTEXITCODE -eq 0)

Write-Host "[4/9] Ruff"

ruff --version
Add-Result "Ruff" ($LASTEXITCODE -eq 0)

Write-Host "[5/9] Black"

black --version
Add-Result "Black" ($LASTEXITCODE -eq 0)

Write-Host "[6/9] MyPy"

mypy --version
Add-Result "MyPy" ($LASTEXITCODE -eq 0)

Write-Host "[7/9] Pytest"

pytest --version
Add-Result "Pytest" ($LASTEXITCODE -eq 0)

Write-Host "[8/9] Git"

git --version
Add-Result "Git" ($LASTEXITCODE -eq 0)

Write-Host "[9/9] Uvicorn"

uvicorn --version
Add-Result "Uvicorn" ($LASTEXITCODE -eq 0)

Write-Host ""
Write-Host "================ HEALTH REPORT ================"

$Checks | Format-Table -AutoSize

if (($Checks.Status -contains "FAIL")) {
    Write-Host ""
    Write-Host "Sprint 6 Health Check FAILED." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "All production dependencies verified." -ForegroundColor Green
Write-Host "Sprint 6 Environment Healthy." -ForegroundColor Green

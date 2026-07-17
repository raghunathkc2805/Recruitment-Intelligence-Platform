$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot

Push-Location $ProjectRoot

Write-Host ""
Write-Host "============================================================"
Write-Host "Recruitment Intelligence Builder Validation"
Write-Host "============================================================"
Write-Host ""

# -----------------------------------------------------------------
# Compile
# -----------------------------------------------------------------

Write-Host "[1/3] Compile"

python -m compileall api database

if ($LASTEXITCODE -ne 0)
{
    throw "Compilation Failed."
}

# -----------------------------------------------------------------
# Tests
# -----------------------------------------------------------------

Write-Host ""
Write-Host "[2/3] Tests"

$Tests = Get-ChildItem `
    "api\tests" `
    -Filter "test_*.py" `
    -Recurse `
    -ErrorAction SilentlyContinue

if ($Tests.Count -gt 0)
{
    python -m pytest

    if ($LASTEXITCODE -ne 0)
    {
        throw "Pytest Failed."
    }
}
else
{
    Write-Host "No tests found."
}

# -----------------------------------------------------------------
# Startup
# -----------------------------------------------------------------

Write-Host ""
Write-Host "[3/3] Startup"

$Job = Start-Job -ScriptBlock {

    param($Root)

    Set-Location $Root

    python -m uvicorn api.app:app --host 127.0.0.1 --port 8000

} -ArgumentList $ProjectRoot

Start-Sleep -Seconds 8

if ($Job.State -eq "Running")
{
    Stop-Job -Job $Job
}

Receive-Job -Job $Job -ErrorAction SilentlyContinue | Out-Null

Remove-Job -Job $Job -Force -ErrorAction SilentlyContinue

Write-Host "Startup Successful."

Pop-Location

Write-Host ""
Write-Host "============================================================"
Write-Host "VALIDATION SUCCESSFUL"
Write-Host "============================================================"

$ErrorActionPreference = "Stop"


Write-Host "=== Container Runtime Check ==="


$docker = Get-Command docker -ErrorAction SilentlyContinue


if ($docker) {

    Write-Host "Docker detected"

    docker --version

    Write-Host ""
    Write-Host "Run Docker validation using:"
    Write-Host "powershell -ExecutionPolicy Bypass -File deployment\docker_health_check.ps1"

    exit 0

}


Write-Host ""
Write-Host "Docker runtime not installed."
Write-Host ""
Write-Host "Executing native production validation instead."


Write-Host ""

Write-Host "=== API Validation ==="


python deployment\final_release_check.py


if ($LASTEXITCODE -ne 0) {

    throw "Production validation failed"

}



Write-Host ""

Write-Host "=== Database Validation ==="


python deployment\database_migration_check.py


if ($LASTEXITCODE -ne 0) {

    throw "Database validation failed"

}



Write-Host ""

Write-Host "PRODUCTION VALIDATION PASSED"
Write-Host ""
Write-Host "Docker container validation pending Docker installation."

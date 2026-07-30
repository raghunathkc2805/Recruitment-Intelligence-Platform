cd "D:\Recruitment Automation 2nd Version"



Write-Host "Running Production Validation"


python deploymentelease_validation.py


if ($LASTEXITCODE -ne 0) {

    throw "Validation Failed"

}



Write-Host "Running Database Validation"


python deployment\database_migration_check.py


if ($LASTEXITCODE -ne 0) {

    throw "Database Validation Failed"

}



Write-Host ""

Write-Host "Production Deployment Package Ready"

Write-Host ""

Write-Host "Start Application Using:"

Write-Host "docker compose up -d"
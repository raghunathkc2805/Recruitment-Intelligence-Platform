cd "D:\Recruitment Automation 2nd Version"


python deployment\production_check.py


if ($LASTEXITCODE -ne 0) {

    throw "Production validation failed"

}


Write-Host "System Ready For Deployment"
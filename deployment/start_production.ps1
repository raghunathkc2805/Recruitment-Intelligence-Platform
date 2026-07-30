cd "D:\Recruitment Automation 2nd Version"


python deploymentelease_validation.py


if ($LASTEXITCODE -ne 0) {

    throw "Release validation failed"

}


Write-Host ""
Write-Host "Starting Recruitment Intelligence Platform"


python -m uvicorn api.app:app `
    --host 0.0.0.0 `
    --port 8000
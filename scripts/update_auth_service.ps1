$ErrorActionPreference = "Stop"

Set-Location "D:\Recruitment Automation Version 2"

git checkout -- api\auth\auth_service.py

python -m pytest -q

$ErrorActionPreference = "Stop"

Set-Location "D:\Recruitment Automation Version 2"

git checkout -- api\auth\jwt_handler.py

python -m pytest -q

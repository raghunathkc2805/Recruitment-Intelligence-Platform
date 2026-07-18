$ErrorActionPreference = "Stop"

Set-Location "D:\Recruitment Automation Version 2"

git checkout -- api\routers\auth.py

python -m pytest -q

$ErrorActionPreference = "Stop"

Set-Location "D:\Recruitment Automation Version 2"

git checkout -- api\auth\dependencies.py

python -m pytest -q

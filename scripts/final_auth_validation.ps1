$ErrorActionPreference = "Stop"

Set-Location "D:\Recruitment Automation Version 2"

git checkout -- api\main.py
git checkout -- api\app.py

python -m pytest -q

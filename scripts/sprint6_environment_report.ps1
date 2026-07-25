$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$ReportFolder = ".\release"

if (!(Test-Path $ReportFolder)) {
    New-Item -ItemType Directory -Force -Path $ReportFolder | Out-Null
}

$Report = Join-Path $ReportFolder "SPRINT6_ENVIRONMENT_REPORT.txt"

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host " Sprint 6 Environment Report"
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

$PythonVersion = python --version 2>&1
$PipVersion = pip --version 2>&1
$GitVersion = git --version 2>&1
$UvicornVersion = uvicorn --version 2>&1
$AlembicVersion = alembic --version 2>&1
$PytestVersion = pytest --version 2>&1
$BlackVersion = black --version 2>&1
$RuffVersion = ruff --version 2>&1
$MypyVersion = mypy --version 2>&1

@"
===================================================
Recruitment Intelligence Platform
Sprint 6 Environment Report
===================================================

Generated:
$(Get-Date)

Python
------
$PythonVersion

Pip
---
$PipVersion

Git
---
$GitVersion

Uvicorn
-------
$UvicornVersion

Alembic
--------
$AlembicVersion

Pytest
------
$PytestVersion

Black
-----
$BlackVersion

Ruff
----
$RuffVersion

MyPy
-----
$MypyVersion

Repository
----------
$(Get-Location)

Branch
------
$(git branch --show-current)

Latest Commit
-------------
$(git log -1 --oneline)

===================================================
Environment Verification Complete
===================================================
"@ | Set-Content -Encoding UTF8 $Report

Write-Host ""
Write-Host "Environment report created:"
Write-Host $Report

Write-Host ""
Write-Host "===================================================" -ForegroundColor Green
Write-Host " Sprint 6 Environment Report Generated"
Write-Host "===================================================" -ForegroundColor Green

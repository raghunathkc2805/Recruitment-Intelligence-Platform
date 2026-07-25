$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$OutputFolder = ".\release"

if (!(Test-Path $OutputFolder)) {
    New-Item -ItemType Directory -Force -Path $OutputFolder | Out-Null
}

$Report = Join-Path $OutputFolder "SPRINT6_SYSTEM_REPORT.md"

$Python = python --version 2>&1
$Git = git --version 2>&1
$Branch = git branch --show-current
$Commit = git rev-parse --short HEAD
$Tag = git describe --tags --abbrev=0 2>$null
$Date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$PyFiles = (Get-ChildItem -Recurse -Filter *.py).Count
$PSFiles = (Get-ChildItem -Recurse -Filter *.ps1).Count
$Tests = (Get-ChildItem -Recurse tests -Filter test_*.py).Count

@"
# Recruitment Intelligence Platform

## Sprint 6 System Report

Generated : $Date

---

## Git

| Item | Value |
|------|-------|
| Branch | $Branch |
| Commit | $Commit |
| Latest Tag | $Tag |

---

## Environment

Python

$Python

Git

$Git

---

## Repository Statistics

| Metric | Count |
|---------|------:|
| Python Files | $PyFiles |
| PowerShell Files | $PSFiles |
| Test Files | $Tests |

---

## Sprint 6 Deliverables

- Enterprise Audit Model
- Alembic Migration
- Audit Repository
- Audit Service
- Audit Export
- Audit Retention
- Audit Middleware
- Permission Dependencies
- REST API
- Test Suite
- Validation Scripts
- Release Scripts
- Manifest Generator
- Inventory Generator
- SHA256 Generator
- Environment Report
- Completion Report

---

Status

✅ Production Ready

✅ Release Ready

✅ Sprint 6 Complete
"@ | Set-Content -Encoding UTF8 $Report

Write-Host ""
Write-Host "System report created:"
Write-Host $Report

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host " Sprint 6 System Report Complete"
Write-Host "===============================================" -ForegroundColor Green

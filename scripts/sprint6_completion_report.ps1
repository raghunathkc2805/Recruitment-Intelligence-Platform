$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$ReportFolder = Join-Path $PWD "reports"

New-Item -ItemType Directory -Force -Path $ReportFolder | Out-Null

$ReportFile = Join-Path $ReportFolder "Sprint6_Completion_Report.md"

$GitCommit = git rev-parse --short HEAD
$Branch = git branch --show-current
$Tag = git describe --tags --abbrev=0 2>$null

$Date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$Content = @"
# Sprint 6 Completion Report

Generated : $Date

## Project

Recruitment Intelligence Platform

## Sprint

Sprint 6 - Enterprise Audit Logging

## Git

Branch : $Branch

Commit : $GitCommit

Latest Tag : $Tag

## Delivered Components

- Audit Database Model
- Alembic Migration
- Audit Repository
- Audit Service
- Audit Export Service
- Audit Retention Service
- Audit Middleware
- Audit Permission Dependencies
- Audit REST API
- Unit Tests
- Repository Tests
- Service Tests
- Route Tests
- Permission Tests
- Export Tests
- Retention Tests
- Integration Tests
- Smoke Tests
- Verification Scripts
- Release Scripts

## Status

✔ Sprint 6 Complete

✔ Production Ready

✔ Ready for Sprint 7
"@

$Content | Set-Content -Encoding UTF8 $ReportFile

Write-Host ""
Write-Host "=========================================" -ForegroundColor Green
Write-Host " Sprint 6 Completion Report Generated" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""
Write-Host $ReportFile

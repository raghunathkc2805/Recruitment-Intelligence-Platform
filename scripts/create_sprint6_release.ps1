$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$Tag = "v6.1.0-sprint6-audit"
$Title = "Sprint 6 - Enterprise Audit Logging"

$Notes = @"
# Sprint 6 - Enterprise Audit Logging

## Features
- Enterprise Audit Log model
- Audit Repository
- Audit Service
- Audit Export Service
- Audit Retention Service
- Audit Middleware
- Audit Permission Dependencies
- Audit REST API
- Alembic Migration
- Unit Tests
- Repository Tests
- Service Tests
- Route Tests
- Integration Tests
- Export Tests
- Retention Tests
- Verification Scripts

## Status
Production Ready

All automated tests passing.
"@

$temp = Join-Path $env:TEMP "Sprint6_ReleaseNotes.md"
$Notes | Set-Content -Encoding UTF8 $temp

Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host " Creating GitHub Release" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

gh release create `
    $Tag `
    --title $Title `
    --notes-file $temp

if ($LASTEXITCODE -ne 0) {
    throw "GitHub release creation failed."
}

Remove-Item $temp -Force

Write-Host ""
Write-Host "=============================================" -ForegroundColor Green
Write-Host " Sprint 6 GitHub Release Created" -ForegroundColor Green
Write-Host " Tag : $Tag" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green

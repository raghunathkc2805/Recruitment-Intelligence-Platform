$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$Tag = "v6.1.0-sprint6-audit"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " Sprint 6 Release Tagging" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/6] Checking Git repository..."
git rev-parse --is-inside-work-tree

if ($LASTEXITCODE -ne 0) {
    throw "Current directory is not a Git repository."
}

Write-Host "[2/6] Checking working tree..."
git diff --quiet
if ($LASTEXITCODE -ne 0) {
    throw "Working tree contains uncommitted changes."
}

Write-Host "[3/6] Checking existing tag..."
$Existing = git tag --list $Tag

if ($Existing) {
    Write-Host "Tag already exists: $Tag"
}
else {
    git tag -a $Tag -m "Sprint 6 Enterprise Audit Logging"
}

Write-Host "[4/6] Listing latest tags..."
git tag --sort=-creatordate | Select-Object -First 10

Write-Host "[5/6] Current commit..."
git log -1 --oneline

Write-Host "[6/6] Release verification complete."

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host " Sprint 6 Tag Ready" -ForegroundColor Green
Write-Host " $Tag" -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green

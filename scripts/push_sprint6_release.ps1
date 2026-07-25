$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$Branch = git branch --show-current
$Tag = "v6.1.0-sprint6-audit"

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 GitHub Publish" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/8] Fetching latest remote..."
git fetch origin

if ($LASTEXITCODE -ne 0) {
    throw "Git fetch failed."
}

Write-Host "[2/8] Checking repository status..."
git status --short

Write-Host "[3/8] Verifying current branch..."
Write-Host "Current Branch : $Branch"

Write-Host "[4/8] Pushing commits..."
git push origin $Branch

if ($LASTEXITCODE -ne 0) {
    throw "Commit push failed."
}

Write-Host "[5/8] Pushing release tag..."
git push origin $Tag

if ($LASTEXITCODE -ne 0) {
    throw "Tag push failed."
}

Write-Host "[6/8] Remote branches..."
git branch -r

Write-Host "[7/8] Latest commit..."
git log --oneline -1

Write-Host "[8/8] Sprint 6 successfully published."

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host " Sprint 6 Successfully Published" -ForegroundColor Green
Write-Host " Branch : $Branch" -ForegroundColor Green
Write-Host " Tag    : $Tag" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green

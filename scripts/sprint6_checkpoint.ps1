$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$Checkpoint = "v6.1.0-sprint6-final"

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 Final Checkpoint" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/9] Repository Status"
git status

Write-Host ""
Write-Host "[2/9] Current Branch"
git branch --show-current

Write-Host ""
Write-Host "[3/9] Latest Commit"
git log -1 --oneline

Write-Host ""
Write-Host "[4/9] Executing Full Test Suite"
python -m pytest -q

if ($LASTEXITCODE -ne 0) {
    throw "Pytest execution failed."
}

Write-Host ""
Write-Host "[5/9] Creating Checkpoint Tag"

$Exists = git tag --list $Checkpoint

if (-not $Exists) {
    git tag -a $Checkpoint -m "Sprint 6 Final Baseline"
}
else {
    Write-Host "Checkpoint tag already exists."
}

Write-Host ""
Write-Host "[6/9] Verifying Tag"
git tag --list $Checkpoint

Write-Host ""
Write-Host "[7/9] Exporting Commit Information"

git show --stat --summary HEAD |
    Set-Content ".\reports\Sprint6_LastCommit.txt"

Write-Host ""
Write-Host "[8/9] Exporting Tag List"

git tag --sort=-creatordate |
    Set-Content ".\reports\GitTags.txt"

Write-Host ""
Write-Host "[9/9] Sprint 6 Baseline Complete"

Write-Host ""
Write-Host "==================================================" -ForegroundColor Green
Write-Host " Sprint 6 FINAL BASELINE CREATED" -ForegroundColor Green
Write-Host " Tag : $Checkpoint" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green

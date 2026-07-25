$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$ReleaseFolder = Join-Path $PWD "release"
$ArchiveName = "Recruitment_Intelligence_Platform_Sprint6_v6.1.0.zip"
$ArchivePath = Join-Path $ReleaseFolder $ArchiveName

New-Item -ItemType Directory -Force -Path $ReleaseFolder | Out-Null

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Recruitment Intelligence Platform" -ForegroundColor Cyan
Write-Host " Sprint 6 Archive Builder" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/6] Removing previous archive..."
if (Test-Path $ArchivePath) {
    Remove-Item $ArchivePath -Force
}

Write-Host "[2/6] Cleaning Python cache..."
Get-ChildItem -Recurse -Directory -Filter "__pycache__" |
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Get-ChildItem -Recurse -Include "*.pyc" |
    Remove-Item -Force -ErrorAction SilentlyContinue

Write-Host "[3/6] Running tests..."
python -m pytest -q

if ($LASTEXITCODE -ne 0) {
    throw "Tests failed. Archive cancelled."
}

Write-Host "[4/6] Building release archive..."

$Items = @(
    "api",
    "database",
    "tests",
    "scripts",
    "alembic",
    "requirements.txt",
    "README.md"
)

Compress-Archive `
    -Path $Items `
    -DestinationPath $ArchivePath `
    -CompressionLevel Optimal `
    -Force

Write-Host "[5/6] Archive information..."

$Zip = Get-Item $ArchivePath

Write-Host ""
Write-Host "Name : $($Zip.Name)"
Write-Host "Size : $([Math]::Round($Zip.Length/1MB,2)) MB"

Write-Host "[6/6] Archive completed."

Write-Host ""
Write-Host "==================================================" -ForegroundColor Green
Write-Host " Sprint 6 Release Package Ready" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host $ArchivePath

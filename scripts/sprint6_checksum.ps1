$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$OutputFolder = ".\release"

if (!(Test-Path $OutputFolder)) {
    New-Item -ItemType Directory -Force -Path $OutputFolder | Out-Null
}

$ChecksumFile = Join-Path $OutputFolder "SPRINT6_SHA256SUMS.txt"

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host " Sprint 6 SHA256 Integrity Generator"
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

$Extensions = @(
    "*.py",
    "*.ps1",
    "*.sql",
    "*.json",
    "*.yaml",
    "*.yml",
    "*.toml",
    "*.ini",
    "*.md",
    "*.txt"
)

$Results = foreach ($Pattern in $Extensions) {

    Get-ChildItem -Recurse -File -Filter $Pattern |
    Sort-Object FullName |
    ForEach-Object {

        $Hash = Get-FileHash $_.FullName -Algorithm SHA256

        "{0}  {1}" -f `
            $Hash.Hash, `
            $_.FullName.Replace((Get-Location).Path + "\", "")
    }
}

$Results | Set-Content -Encoding UTF8 $ChecksumFile

Write-Host ""
Write-Host "Checksum File:"
Write-Host $ChecksumFile

Write-Host ""
Write-Host "Files Processed : $($Results.Count)"

Write-Host ""
Write-Host "===================================================" -ForegroundColor Green
Write-Host " Sprint 6 SHA256 Verification Complete"
Write-Host "===================================================" -ForegroundColor Green

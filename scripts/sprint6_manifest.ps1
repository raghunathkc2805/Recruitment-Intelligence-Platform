$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$ManifestFolder = ".\release"

if (!(Test-Path $ManifestFolder)) {
    New-Item -ItemType Directory -Force -Path $ManifestFolder | Out-Null
}

$Manifest = Join-Path $ManifestFolder "SPRINT6_MANIFEST.json"

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host " Sprint 6 Production Manifest Generator"
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

$Files = Get-ChildItem `
    -Recurse `
    -File `
    -Exclude *.pyc

$Inventory = foreach ($File in $Files) {

    $Hash = Get-FileHash $File.FullName -Algorithm SHA256

    [PSCustomObject]@{
        File      = $File.FullName.Replace((Get-Location).Path + "\", "")
        Size      = $File.Length
        SHA256    = $Hash.Hash
        Modified  = $File.LastWriteTimeUtc.ToString("o")
    }
}

$ManifestObject = [PSCustomObject]@{
    Project             = "Recruitment Intelligence Platform"
    Sprint              = "Sprint 6"
    Version             = "6.1.0"
    GeneratedUTC        = (Get-Date).ToUniversalTime().ToString("o")
    TotalFiles          = $Inventory.Count
    Files               = $Inventory
}

$ManifestObject |
    ConvertTo-Json -Depth 5 |
    Set-Content -Encoding UTF8 $Manifest

Write-Host ""
Write-Host "Manifest Created:"
Write-Host $Manifest

Write-Host ""
Write-Host "Total Files : $($Inventory.Count)"

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host " Sprint 6 Manifest Generated Successfully"
Write-Host "===============================================" -ForegroundColor Green

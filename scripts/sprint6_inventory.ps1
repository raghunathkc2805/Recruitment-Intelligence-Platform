$ErrorActionPreference = "Stop"

Set-Location (Split-Path $PSScriptRoot -Parent)

$OutputFolder = ".\release"

if (!(Test-Path $OutputFolder)) {
    New-Item -ItemType Directory -Force -Path $OutputFolder | Out-Null
}

$InventoryFile = Join-Path $OutputFolder "SPRINT6_REPOSITORY_INVENTORY.csv"

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host " Sprint 6 Repository Inventory Generator"
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

$Inventory = Get-ChildItem -Recurse -File |
Sort-Object FullName |
ForEach-Object {

    $Hash = Get-FileHash $_.FullName -Algorithm SHA256

    [PSCustomObject]@{
        RelativePath = $_.FullName.Replace((Get-Location).Path + "\", "")
        Extension    = $_.Extension
        SizeKB       = [Math]::Round($_.Length / 1KB, 2)
        SHA256       = $Hash.Hash
        ModifiedUTC  = $_.LastWriteTimeUtc.ToString("yyyy-MM-dd HH:mm:ss")
    }
}

$Inventory |
Export-Csv `
    -Path $InventoryFile `
    -NoTypeInformation `
    -Encoding UTF8

Write-Host ""
Write-Host "Inventory File:"
Write-Host $InventoryFile

Write-Host ""
Write-Host "Total Files : $($Inventory.Count)"

Write-Host ""
Write-Host "===================================================" -ForegroundColor Green
Write-Host " Sprint 6 Repository Inventory Complete"
Write-Host "===================================================" -ForegroundColor Green

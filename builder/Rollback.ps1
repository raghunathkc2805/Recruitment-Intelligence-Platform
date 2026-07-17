$ErrorActionPreference = "Stop"

Import-Module "$PSScriptRoot\Utils.ps1" -Force

Write-Host ""
Write-Host "============================================================"
Write-Host "Recruitment Intelligence Builder Rollback"
Write-Host "============================================================"
Write-Host ""

if(!(Test-Path $BackupRoot))
{
    throw "Backup folder not found."
}

$Backups = Get-ChildItem `
    $BackupRoot `
    -Directory |
    Sort-Object LastWriteTime -Descending

if($Backups.Count -eq 0)
{
    throw "No backups available."
}

$Latest = $Backups[0]

Write-Host "Using Backup:"
Write-Host $Latest.FullName
Write-Host ""

Get-ChildItem `
    $Latest.FullName `
    -Recurse `
    -File | ForEach-Object {

    $Relative = $_.FullName.Substring($Latest.FullName.Length).TrimStart("\")

    $Target = Join-Path $ProjectRoot $Relative

    $Parent = Split-Path $Target

    Ensure-Folder $Parent

    Copy-Item `
        $_.FullName `
        $Target `
        -Force

    Write-Host "[RESTORED] $Relative" -ForegroundColor Green

}

Write-Host ""
Write-Host "============================================================"
Write-Host "Rollback Completed Successfully"
Write-Host "============================================================"

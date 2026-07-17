$ProjectRoot=Split-Path -Parent $PSScriptRoot

$BackupFolder=Join-Path `
$PSScriptRoot `
"backups"

$Stamp=Get-Date `
-Format "yyyyMMdd_HHmmss"

$Destination=Join-Path `
$BackupFolder `
$Stamp

New-Item `
-ItemType Directory `
-Force `
-Path $Destination | Out-Null

robocopy `
$ProjectRoot `
$Destination `
/E `
/XD `
builder\backups `
builder\output `
builder\logs `
.git `
__pycache__ `
.pytest_cache `
> $null

Write-Host ""
Write-Host "Backup Created"

Write-Host $Destination

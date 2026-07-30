$root = "D:\Recruitment Automation 2nd Version"

$backupFolder = Join-Path $root "backups"

if (!(Test-Path $backupFolder)) {

    New-Item `
        -ItemType Directory `
        -Path $backupFolder

}


$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

$backupFile = Join-Path `
    $backupFolder `
    "recruitment_db_$timestamp.sqlite"


Copy-Item `
    "$root\*.db" `
    $backupFile `
    -Force


Write-Host "Database Backup Created:"
Write-Host $backupFile
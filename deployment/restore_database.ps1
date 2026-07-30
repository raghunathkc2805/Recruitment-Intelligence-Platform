param(
    [string]$BackupFile
)


$root = "D:\Recruitment Automation 2nd Version"


if (!(Test-Path $BackupFile)) {

    throw "Backup file not found"

}


Copy-Item `
    $BackupFile `
    "$root\recruitment.db" `
    -Force


Write-Host "Database Restore Completed"
$ProjectRoot=Split-Path `
    -Parent `
    $PSScriptRoot

$Output=Join-Path `
    $PSScriptRoot `
    "output"

$Stamp=Get-Date `
    -Format "yyyyMMdd_HHmmss"

$Zip=Join-Path `
    $Output `
    "Recruitment_Intelligence_$Stamp.zip"

Compress-Archive `
    -Path "$ProjectRoot\*" `
    -DestinationPath $Zip `
    -CompressionLevel Optimal `
    -Force

Write-Host ""
Write-Host "Snapshot Created"
Write-Host $Zip

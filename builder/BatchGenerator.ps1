param(
    [Parameter(Mandatory)]
    [string]$Batch,

    [Parameter(Mandatory)]
    [string]$Name
)

$ManifestFolder = Join-Path $PSScriptRoot "manifests"
$PayloadFolder  = Join-Path $PSScriptRoot "payloads"

New-Item -ItemType Directory -Force -Path $ManifestFolder,$PayloadFolder | Out-Null

@"
@{
    Batch="$Batch"
    Name="$Name"
    Version="1.0.0"
}
"@ | Set-Content `
(Join-Path $ManifestFolder "$Batch.psd1") `
-Encoding UTF8

@"
# $Batch

# Add-DeploymentFile `
# -RelativePath `"relative\path.py`" `
# -Content @'
# Complete File
# '@
"@ | Set-Content `
(Join-Path $PayloadFolder "$Batch.ps1") `
-Encoding UTF8

Write-Host ""
Write-Host "Created:"
Write-Host "$Batch.psd1"
Write-Host "$Batch.ps1"

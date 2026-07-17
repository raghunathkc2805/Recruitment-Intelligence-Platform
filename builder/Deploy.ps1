param(
    [Parameter(Mandatory)]
    [string]$Batch
)

$ErrorActionPreference = "Stop"

. "$PSScriptRoot\Utils.ps1"

$Manifest = Join-Path $PSScriptRoot "manifests\$Batch.psd1"
$Payload  = Join-Path $PSScriptRoot "payloads\$Batch.ps1"

if(!(Test-Path $Manifest))
{
    throw "Manifest not found : $Manifest"
}

if(!(Test-Path $Payload))
{
    throw "Payload not found : $Payload"
}

$BatchInfo = Import-PowerShellDataFile $Manifest

Write-Host ""
Write-Host "=============================================================="
Write-Host "Recruitment Intelligence Builder"
Write-Host "=============================================================="
Write-Host ""
Write-Host "Batch      : $($BatchInfo.Batch)"
Write-Host "Name       : $($BatchInfo.Name)"
Write-Host "Version    : $($BatchInfo.Version)"
Write-Host ""

$script:DeploymentFiles = New-Object System.Collections.Generic.List[object]

function Add-DeploymentFile
{
    param(
        [string]$RelativePath,
        [string]$Content
    )

    $script:DeploymentFiles.Add(
        [PSCustomObject]@{
            RelativePath=$RelativePath
            Content=$Content
        }
    )
}

. $Payload

Write-Host "Files : $($DeploymentFiles.Count)"
Write-Host ""

foreach($File in $DeploymentFiles)
{
    Deploy-File `
        -RelativePath $File.RelativePath `
        -Content $File.Content
}

Write-Host ""
Write-Host "=============================================================="
Write-Host "Deployment Successful"
Write-Host "=============================================================="

param(
    [Parameter(Mandatory)]
    [string]$Batch,

    [Parameter(Mandatory)]
    [string]$Name,

    [string]$Version="1.0.0",

    [string[]]$Validation=@()
)

$ManifestFolder = Join-Path $PSScriptRoot "manifests"

if(!(Test-Path $ManifestFolder))
{
    New-Item `
        -ItemType Directory `
        -Path $ManifestFolder `
        -Force | Out-Null
}

$Manifest = Join-Path `
    $ManifestFolder `
    "$Batch.psd1"

@"
@{
    Batch="$Batch"
    Name="$Name"
    Version="$Version"

    Validation=@(
$(($Validation | ForEach-Object { '        "'+$_+'"' }) -join ",`n")
    )
}
"@ | Set-Content `
    $Manifest `
    -Encoding UTF8

Write-Host ""
Write-Host "Manifest Created"
Write-Host $Manifest

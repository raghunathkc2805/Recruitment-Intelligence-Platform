param(
    [Parameter(Mandatory)]
    [string]$Batch
)

$ErrorActionPreference = "Stop"

$Deploy = Join-Path $PSScriptRoot "Deploy.ps1"

if (!(Test-Path $Deploy))
{
    throw "Deploy.ps1 not found."
}

& powershell `
    -ExecutionPolicy Bypass `
    -NoProfile `
    -File $Deploy `
    -Batch $Batch

if ($LASTEXITCODE -ne 0)
{
    exit $LASTEXITCODE
}

$Validate = Join-Path $PSScriptRoot "Validate.ps1"

if (Test-Path $Validate)
{
    & powershell `
        -ExecutionPolicy Bypass `
        -NoProfile `
        -File $Validate
}
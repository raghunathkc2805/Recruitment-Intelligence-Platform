param(
    [Parameter(Mandatory)]
    [string]$Message
)

$ReportFolder=Join-Path $PSScriptRoot "reports"

if(!(Test-Path $ReportFolder))
{
    New-Item `
        -ItemType Directory `
        -Force `
        -Path $ReportFolder | Out-Null
}

$Report=Join-Path `
    $ReportFolder `
    "BuilderHistory.log"

Add-Content `
    $Report `
    ("[{0}] {1}" -f (Get-Date),$Message)

Write-Host "Registered."

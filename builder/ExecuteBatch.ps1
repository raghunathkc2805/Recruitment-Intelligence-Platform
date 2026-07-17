param(
    [Parameter(Mandatory)]
    [string]$Batch
)

& "$PSScriptRoot\Build.ps1" $Batch

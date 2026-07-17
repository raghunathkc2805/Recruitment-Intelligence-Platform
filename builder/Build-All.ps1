param(
    [Parameter(Mandatory)]
    [string[]]$Batches
)

foreach($Batch in $Batches)
{
    Write-Host ""
    Write-Host "====================================================="
    Write-Host "Executing $Batch"
    Write-Host "====================================================="

    & "$PSScriptRoot\Build.ps1" `
        $Batch

    if($LASTEXITCODE -ne 0)
    {
        exit $LASTEXITCODE
    }
}

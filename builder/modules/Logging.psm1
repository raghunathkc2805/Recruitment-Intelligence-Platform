function Write-BuilderLog
{
    param(
        [string]$Message
    )

    $Folder=Join-Path `
        $PSScriptRoot `
        "..\logs"

    if(!(Test-Path $Folder))
    {
        New-Item `
            -ItemType Directory `
            -Force `
            -Path $Folder | Out-Null
    }

    $Log=Join-Path `
        $Folder `
        ("Builder_"+(Get-Date -Format "yyyyMMdd")+".log")

    Add-Content `
        $Log `
        ("[{0}] {1}" -f (Get-Date),$Message)
}

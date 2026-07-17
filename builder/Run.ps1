param(
    [Parameter(Mandatory)]
    [ValidateSet(
        "build",
        "validate",
        "snapshot",
        "rollback",
        "backup",
        "statistics",
        "health",
        "history",
        "dashboard",
        "clean"
    )]
    [string]$Action,

    [string]$Batch
)

switch($Action)
{
    "build"
    {
        if([string]::IsNullOrWhiteSpace($Batch))
        {
            throw "Batch is required."
        }

        & "$PSScriptRoot\Build.ps1" $Batch
    }

    "validate"
    {
        & "$PSScriptRoot\Validate.ps1"
    }

    "snapshot"
    {
        & "$PSScriptRoot\Snapshot.ps1"
    }

    "rollback"
    {
        & "$PSScriptRoot\Rollback.ps1"
    }

    "backup"
    {
        & "$PSScriptRoot\Backup.ps1"
    }

    "statistics"
    {
        & "$PSScriptRoot\Statistics.ps1"
    }

    "health"
    {
        & "$PSScriptRoot\Health.ps1"
    }

    "history"
    {
        & "$PSScriptRoot\History.ps1"
    }

    "dashboard"
    {
        & "$PSScriptRoot\Dashboard.ps1"
    }

    "clean"
    {
        & "$PSScriptRoot\Cleanup.ps1"
    }
}

$BuilderRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $BuilderRoot

$BackupRoot = Join-Path $BuilderRoot "backups"

$Utf8 = [System.Text.UTF8Encoding]::new($false)

function Ensure-Folder
{
    param([string]$Folder)

    if(!(Test-Path $Folder))
    {
        New-Item `
            -ItemType Directory `
            -Force `
            -Path $Folder | Out-Null
    }
}

function Backup-File
{
    param([string]$File)

    if(!(Test-Path $File))
    {
        return
    }

    $Stamp = Get-Date -Format "yyyyMMdd_HHmmss"

    $Relative = $File.Substring($ProjectRoot.Length).TrimStart("\")

    $Target = Join-Path `
        $BackupRoot `
        "$Stamp\$Relative"

    Ensure-Folder `
        (Split-Path $Target)

    Copy-Item `
        $File `
        $Target `
        -Force
}

function Deploy-File
{
    param(
        [string]$RelativePath,
        [string]$Content
    )

    $Target = Join-Path `
        $ProjectRoot `
        $RelativePath

    Backup-File $Target

    Ensure-Folder `
        (Split-Path $Target)

    [System.IO.File]::WriteAllText(
        $Target,
        $Content,
        $Utf8
    )

    Write-Host "[OK] $RelativePath"
}
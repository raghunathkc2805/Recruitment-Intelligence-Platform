function Get-BuilderConfiguration
{
    $Config=Join-Path `
        $PSScriptRoot `
        "..\config\BuilderConfig.json"

    Get-Content `
        $Config `
        -Raw | ConvertFrom-Json
}

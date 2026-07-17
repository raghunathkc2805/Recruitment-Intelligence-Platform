$ProjectRoot = Split-Path -Parent $PSScriptRoot

$Output = Join-Path $PSScriptRoot "output\ProjectInventory"

if(Test-Path $Output)
{
    Remove-Item $Output -Recurse -Force
}

New-Item `
    -ItemType Directory `
    -Path $Output `
    -Force | Out-Null

Get-ChildItem `
    $ProjectRoot `
    -Recurse `
    -File `
    -Include *.py,*.ps1,*.psm1,*.json,*.yaml,*.yml |
ForEach-Object {

    $Relative = $_.FullName.Substring($ProjectRoot.Length).TrimStart("\")

    $Target = Join-Path `
        $Output `
        ($Relative.Replace("\","__"))

    @{
        Path=$Relative
        Size=$_.Length
        Modified=$_.LastWriteTime
    } | ConvertTo-Json |
    Set-Content `
        ($Target + ".json") `
        -Encoding UTF8

    Copy-Item `
        $_.FullName `
        ($Target + ".txt")
}

Write-Host ""
Write-Host "Inventory Created Successfully"
Write-Host $Output

param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [Parameter(Mandatory = $true)]
    [string]$Content
)

$FullPath = Join-Path (Get-Location) $Path

$Directory = Split-Path $FullPath -Parent

if (-not (Test-Path $Directory)) {
    New-Item -ItemType Directory -Path $Directory -Force | Out-Null
}

$Utf8NoBom = [System.Text.UTF8Encoding]::new($false)

[System.IO.File]::WriteAllText(
    $FullPath,
    $Content,
    $Utf8NoBom
)

Write-Host ""
Write-Host "========================================"
Write-Host "File written successfully" -ForegroundColor Green
Write-Host $FullPath
Write-Host "========================================"
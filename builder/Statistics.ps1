$ProjectRoot=Split-Path -Parent $PSScriptRoot

Write-Host ""
Write-Host "==============================="
Write-Host "Builder Statistics"
Write-Host "==============================="
Write-Host ""

Write-Host ("Python Files      : {0}" -f ((Get-ChildItem $ProjectRoot -Recurse -Filter *.py -ErrorAction SilentlyContinue).Count))
Write-Host ("PowerShell Files  : {0}" -f ((Get-ChildItem $ProjectRoot -Recurse -Filter *.ps1 -ErrorAction SilentlyContinue).Count))
Write-Host ("PowerShell Modules: {0}" -f ((Get-ChildItem $ProjectRoot -Recurse -Filter *.psm1 -ErrorAction SilentlyContinue).Count))
Write-Host ("JSON Files        : {0}" -f ((Get-ChildItem $ProjectRoot -Recurse -Filter *.json -ErrorAction SilentlyContinue).Count))
Write-Host ("Folders           : {0}" -f ((Get-ChildItem $ProjectRoot -Recurse -Directory -ErrorAction SilentlyContinue).Count))
Write-Host ("Files             : {0}" -f ((Get-ChildItem $ProjectRoot -Recurse -File -ErrorAction SilentlyContinue).Count))

Write-Host ""
Write-Host "Builder Ready."

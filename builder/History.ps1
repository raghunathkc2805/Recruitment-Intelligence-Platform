$History=Join-Path `
$PSScriptRoot `
"reports\BatchHistory.md"

if(!(Test-Path $History))
{
"# Batch History" |
Set-Content `
$History `
-Encoding UTF8
}

Get-Content `
$History

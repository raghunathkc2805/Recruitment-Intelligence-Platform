$Folders=@(
"output",
"cache",
"logs"
)

foreach($Folder in $Folders)
{
Get-ChildItem `
(Join-Path $PSScriptRoot $Folder) `
-ErrorAction SilentlyContinue |
Remove-Item `
-Recurse `
-Force `
-ErrorAction SilentlyContinue
}

Write-Host "Cleanup Completed."

Remove-Item `
"$PSScriptRoot\output\*" `
-Recurse `
-Force `
-ErrorAction SilentlyContinue

Remove-Item `
"$PSScriptRoot\cache\*" `
-Recurse `
-Force `
-ErrorAction SilentlyContinue

Write-Host "Builder Cleaned."

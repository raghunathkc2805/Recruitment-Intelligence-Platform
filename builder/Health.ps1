$ProjectRoot=Split-Path -Parent $PSScriptRoot

Write-Host ""
Write-Host "============================================================"
Write-Host "Recruitment Intelligence Platform Health Check"
Write-Host "============================================================"
Write-Host ""

$Checks=@(
    "api",
    "database",
    "builder",
    "resume_parser",
    "jd_parser"
)

foreach($Item in $Checks)
{
    $Path=Join-Path $ProjectRoot $Item

    if(Test-Path $Path)
    {
        Write-Host "[ OK ] $Item"
    }
    else
    {
        Write-Host "[FAIL] $Item"
    }
}

Write-Host ""

Write-Host "Python Version"

python --version

Write-Host ""

Write-Host "Git"

git --version

Write-Host ""

Write-Host "Builder Ready."

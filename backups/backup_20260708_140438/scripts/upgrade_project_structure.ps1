$root = "D:\Recruitment Automation Version 2"

Write-Host ""
Write-Host "==========================================="
Write-Host "Recruitment Intelligence Platform Upgrade"
Write-Host "==========================================="
Write-Host ""

# --------------------------------------------
# Remove duplicate folders (only if empty)
# --------------------------------------------

$removeFolders = @(
    "jd_parser\knowledge_base",
    "resume_parser\knowledge_base",
    "jd_parser\models",
    "resume_parser\models"
)

foreach ($folder in $removeFolders) {

    $path = Join-Path $root $folder

    if (Test-Path $path) {

        if ((Get-ChildItem $path -Force | Measure-Object).Count -eq 0) {

            Remove-Item $path -Force

            Write-Host "Removed Empty Folder: $folder"

        }
        else {

            Write-Host "Skipped (Not Empty): $folder"

        }

    }

}

# --------------------------------------------
# Enterprise folders
# --------------------------------------------

$folders = @(

".github\workflows",

"api",
"api\routes",
"api\services",
"api\middleware",
"api\schemas",
"api\auth",

"common",
"common\extractors",
"common\matchers",
"common\utils",

"config",

"database",
"database\sqlite",
"database\migrations",
"database\seed",

"docs",

"frontend",
"frontend\web",
"frontend\desktop",

"integrations",
"integrations\gmail",
"integrations\outlook",
"integrations\linkedin",
"integrations\naukri",
"integrations\foundit",
"integrations\shine",

"intelligence_engine",

"jd_parser",

"logs",

"matching_engine",

"ml",
"ml\models",
"ml\training",
"ml\inference",

"ocr",
"ocr\tesseract",
"ocr\image_preprocessing",

"output",

"ranking_engine",

"resume_parser",

"scripts",

"search_engine",

"shared",
"shared\models",
"shared\knowledge_base",
"shared\utils",

"tests",

"tools"

)

foreach ($folder in $folders) {

    New-Item -ItemType Directory -Force `
        -Path (Join-Path $root $folder) | Out-Null

}

Write-Host ""
Write-Host "Folders Verified."
Write-Host ""

# --------------------------------------------
# Create common __init__.py
# --------------------------------------------

$initFiles = @(

"common\__init__.py",
"common\extractors\__init__.py",
"common\matchers\__init__.py",
"common\utils\__init__.py",

"shared\__init__.py",
"shared\models\__init__.py",
"shared\utils\__init__.py",

"api\__init__.py",
"api\routes\__init__.py",
"api\services\__init__.py",

"resume_parser\__init__.py",
"jd_parser\__init__.py"

)

foreach($file in $initFiles){

    $path = Join-Path $root $file

    if(!(Test-Path $path)){

        New-Item `
            -ItemType File `
            -Path $path | Out-Null

    }

}

Write-Host ""
Write-Host "Package files created."
Write-Host ""

Write-Host "==========================================="
Write-Host "Architecture Upgrade Completed"
Write-Host "==========================================="
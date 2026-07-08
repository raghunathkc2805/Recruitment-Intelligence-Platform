$root = "D:\Recruitment Automation Version 2\resume_parser"

$folders = @(
"extractors",
"pipeline",
"models",
"printers",
"utils",
"knowledge_base",
"tests",
"sample_resumes",
"parsers",
"matchers",
"ranking",
"exporters",
"validators",
"schemas",
"config",
"logs",
"output",
"output\json",
"output\excel",
"output\csv",
"output\reports"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path (Join-Path $root $folder) | Out-Null
}

$files = @(
"__init__.py",
"main.py",
"resume_service.py",

"extractors\__init__.py",
"extractors\text_extractor.py",
"extractors\name_extractor.py",
"extractors\contact_extractor.py",
"extractors\email_extractor.py",
"extractors\phone_extractor.py",
"extractors\location_extractor.py",
"extractors\summary_extractor.py",
"extractors\experience_extractor.py",
"extractors\education_extractor.py",
"extractors\skills_extractor.py",
"extractors\certification_extractor.py",
"extractors\project_extractor.py",
"extractors\employer_extractor.py",
"extractors\designation_extractor.py",
"extractors\domain_extractor.py",
"extractors\achievements_extractor.py",
"extractors\languages_extractor.py",
"extractors\resume_score_extractor.py",
"extractors\candidate_match_extractor.py",
"extractors\candidate_ranking_extractor.py",
"extractors\ai_recommendation_extractor.py",
"extractors\boolean_search_extractor.py",
"extractors\recruiter_query_extractor.py",
"extractors\resume_search_extractor.py",

"pipeline\__init__.py",
"pipeline\resume_pipeline.py",

"models\__init__.py",
"models\resume.py",
"models\candidate.py",
"models\education.py",
"models\employment.py",
"models\project.py",
"models\certification.py",
"models\skill.py",

"printers\__init__.py",
"printers\console_printer.py",
"printers\json_printer.py",
"printers\csv_printer.py",

"utils\__init__.py",
"utils\file_reader.py",
"utils\pdf_reader.py",
"utils\docx_reader.py",
"utils\text_cleaner.py",
"utils\regex_patterns.py",
"utils\constants.py",
"utils\knowledge_base.py",

"knowledge_base\designation_master.json",
"knowledge_base\skills_master.json",
"knowledge_base\certification_master.json",
"knowledge_base\company_master.json",
"knowledge_base\domain_master.json",
"knowledge_base\location_master.json",
"knowledge_base\education_master.json",
"knowledge_base\language_master.json",
"knowledge_base\keyword_synonyms.json",

"tests\__init__.py",
"tests\test_name_extractor.py",
"tests\test_contact_extractor.py",
"tests\test_email_extractor.py",
"tests\test_phone_extractor.py",
"tests\test_location_extractor.py",
"tests\test_summary_extractor.py",
"tests\test_experience_extractor.py",
"tests\test_education_extractor.py",
"tests\test_skills_extractor.py",
"tests\test_certification_extractor.py",
"tests\test_project_extractor.py",
"tests\test_employer_extractor.py",
"tests\test_designation_extractor.py",
"tests\test_domain_extractor.py",
"tests\test_achievements_extractor.py",
"tests\test_languages_extractor.py",
"tests\test_resume_score_extractor.py",
"tests\test_candidate_match_extractor.py",
"tests\test_candidate_ranking_extractor.py",
"tests\test_ai_recommendation_extractor.py",
"tests\test_boolean_search_extractor.py",
"tests\test_recruiter_query_extractor.py",
"tests\test_resume_search_extractor.py",
"tests\test_resume_pipeline.py",
"tests\test_pdf_parser.py",
"tests\test_docx_parser.py",
"tests\test_txt_parser.py",
"tests\test_overall_matcher.py",
"tests\test_scoring_engine.py",
"tests\test_resume_validator.py",

"parsers\__init__.py",
"parsers\pdf_parser.py",
"parsers\docx_parser.py",
"parsers\txt_parser.py",
"parsers\parser_factory.py",

"matchers\__init__.py",
"matchers\skill_matcher.py",
"matchers\designation_matcher.py",
"matchers\education_matcher.py",
"matchers\experience_matcher.py",
"matchers\certification_matcher.py",
"matchers\location_matcher.py",
"matchers\overall_matcher.py",

"ranking\__init__.py",
"ranking\scoring_engine.py",
"ranking\ranking_engine.py",
"ranking\recommendation_engine.py",

"exporters\__init__.py",
"exporters\excel_exporter.py",
"exporters\csv_exporter.py",
"exporters\json_exporter.py",
"exporters\pdf_exporter.py",

"validators\__init__.py",
"validators\email_validator.py",
"validators\phone_validator.py",
"validators\experience_validator.py",
"validators\education_validator.py",
"validators\resume_validator.py",

"schemas\resume_schema.py",
"schemas\response_schema.py",

"config\__init__.py",
"config\settings.py",
"config\weights.py",

"logs\.gitkeep",

"sample_resumes\sample_resume_01.pdf",
"sample_resumes\sample_resume_02.docx",
"sample_resumes\sample_resume_03.txt"
)

foreach ($file in $files) {
    $path = Join-Path $root $file

    if (!(Test-Path $path)) {

        $directory = Split-Path $path -Parent

        if (!(Test-Path $directory)) {
            New-Item -ItemType Directory -Force -Path $directory | Out-Null
        }

        New-Item -ItemType File -Force -Path $path | Out-Null
    }
}

Write-Host ""
Write-Host "======================================="
Write-Host " Resume Parser Structure Created"
Write-Host "======================================="
Write-Host ""
Write-Host "Root: $root"
Write-Host ""
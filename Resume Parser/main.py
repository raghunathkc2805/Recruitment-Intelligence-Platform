from config.settings import *
from core.pdf_reader import extract_pdf_text
from core.docx_reader import extract_docx_text

from extractors.contact_extractor import (
    extract_name,
    extract_email,
    extract_mobile
)

from extractors.experience_extractor import (
    extract_employment_history,
    extract_current_company,
    extract_current_designation,
    get_experience_type
)

from models.candidate import Candidate
from utils.json_writer import save_candidate


print("=" * 60)
print(APP_NAME)
print("Version:", VERSION)
print("=" * 60)

files = list(INPUT_FOLDER.iterdir())

if not files:
    print("No resumes found in Input folder.")
    raise SystemExit

for file in files:

    print(f"\nProcessing: {file.name}")

    # ---------------------------------
    # Read Resume
    # ---------------------------------

    if file.suffix.lower() == ".pdf":
        text = extract_pdf_text(file)

    elif file.suffix.lower() == ".docx":
        text = extract_docx_text(file)

    else:
        print("Unsupported file.")
        continue

    # ---------------------------------
    # Contact Extraction
    # ---------------------------------

    name = extract_name(text)
    email = extract_email(text)
    mobile = extract_mobile(text)

    # ---------------------------------
    # Experience Extraction
    # ---------------------------------

    history = extract_employment_history(text)

    experience_type = get_experience_type(history)

    current_company = extract_current_company(history)

    current_designation = extract_current_designation(history)

    companies = [item["company"] for item in history]

    # ---------------------------------
    # Candidate Object
    # ---------------------------------

    candidate = Candidate(
        name=name,
        email=email,
        mobile=mobile,

        experience_type=experience_type,
        current_company=current_company,
        current_designation=current_designation,

        companies=companies,
        employment_history=history,

        resume_file=file.name,
        parser_version=VERSION
    )

    # ---------------------------------
    # Console Output
    # ---------------------------------

    print(f"Name                : {candidate.name}")
    print(f"Email               : {candidate.email}")
    print(f"Mobile              : {candidate.mobile}")
    print(f"Experience Type     : {candidate.experience_type}")
    print(f"Current Company     : {candidate.current_company}")
    print(f"Current Designation : {candidate.current_designation}")
    print(f"Companies Found     : {len(candidate.companies)}")

    # ---------------------------------
    # Save Text
    # ---------------------------------

    text_file = OUTPUT_FOLDER / f"{file.stem}.txt"

    text_file.write_text(text, encoding="utf-8")

    # ---------------------------------
    # Save JSON
    # ---------------------------------

    json_file = JSON_FOLDER / f"{file.stem}.json"

    save_candidate(candidate, json_file)

    print("Text extracted successfully.")
    print("JSON created successfully.")
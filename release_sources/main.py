from pathlib import Path

from config.settings import *

from core.pdf_reader import extract_pdf_text
from core.docx_reader import extract_docx_text

from services.jd_service import JDService
from printers.console_printer import print_job_description
from utils.json_writer import save_job_description


print("=" * 60)
print("JD Intelligence Engine")
print("Version:", VERSION)
print("=" * 60)

service = JDService()

files = list(INPUT_FOLDER.iterdir())

if not files:
    print("No Job Descriptions found in input folder.")
    raise SystemExit

for file in files:

    print(f"\nProcessing: {file.name}")

    if file.suffix.lower() == ".pdf":
        text = extract_pdf_text(file)

    elif file.suffix.lower() == ".docx":
        text = extract_docx_text(file)

    else:
        print("Unsupported file.")
        continue

    job = service.parse(
        text=text,
        jd_file=file.name,
        parser_version=VERSION
    )

    print_job_description(job)

    json_file = OUTPUT_FOLDER / f"{file.stem}.json"

    save_job_description(job, json_file)

    print("JSON created successfully.")
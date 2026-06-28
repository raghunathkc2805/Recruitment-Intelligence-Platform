from config.settings import *

from core.pdf_reader import extract_pdf_text
from core.docx_reader import extract_docx_text

from services.candidate_service import CandidateService
from printers.console_printer import print_candidate

from utils.json_writer import save_candidate


def read_resume(file):

    if file.suffix.lower() == ".pdf":
        return extract_pdf_text(file)

    if file.suffix.lower() == ".docx":
        return extract_docx_text(file)

    return None


def process_file(file):

    print(f"\nProcessing: {file.name}")

    text = read_resume(file)

    if text is None:
        print("Unsupported file.")
        return

    candidate = CandidateService.process_resume(
        text=text,
        resume_file=file.name,
        parser_version=VERSION
    )

    print_candidate(candidate)

    text_file = OUTPUT_FOLDER / f"{file.stem}.txt"
    text_file.write_text(text, encoding="utf-8")

    json_file = JSON_FOLDER / f"{file.stem}.json"
    save_candidate(candidate, json_file)

    print("Text extracted successfully.")
    print("JSON created successfully.")


def main():

    print("=" * 60)
    print(APP_NAME)
    print("Version:", VERSION)
    print("=" * 60)

    files = list(INPUT_FOLDER.iterdir())

    if not files:
        print("No resumes found in Input folder.")
        return

    for file in files:
        process_file(file)


if __name__ == "__main__":
    main()
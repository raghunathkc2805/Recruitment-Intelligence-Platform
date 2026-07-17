from pathlib import Path

from jd_parser.config.settings import INPUT_FOLDER, OUTPUT_FOLDER, VERSION
from jd_parser.core.docx_reader import extract_docx_text
from jd_parser.core.pdf_reader import extract_pdf_text
from jd_parser.printers.console_printer import print_job_description
from jd_parser.services.jd_service import JDService
from jd_parser.utils.json_writer import save_job_description


def main() -> None:
    """Run the JD processing pipeline over supported input files."""
    print("=" * 60)
    print("JD Intelligence Engine")
    print("Version:", VERSION)
    print("=" * 60)

    if not INPUT_FOLDER.exists():
        print("No Job Descriptions found in input folder.")
        print("Total Files: 0")
        print("Success: 0")
        print("Failed: 0")
        raise SystemExit

    files = sorted(
        (
            file_path
            for file_path in INPUT_FOLDER.iterdir()
            if file_path.is_file()
            and not file_path.name.startswith(".")
            and file_path.suffix.lower() in {".pdf", ".docx"}
        ),
        key=lambda path: path.name.lower(),
    )

    if not files:
        print("No Job Descriptions found in input folder.")
        print("Total Files: 0")
        print("Success: 0")
        print("Failed: 0")
        raise SystemExit

    service = JDService()
    success = 0
    failed = 0

    for file_path in files:
        print(f"\nProcessing: {file_path.name}")

        try:
            if file_path.suffix.lower() == ".pdf":
                text = extract_pdf_text(file_path)
            elif file_path.suffix.lower() == ".docx":
                text = extract_docx_text(file_path)
            else:
                continue

            job = service.parse(
                text=text,
                jd_file=file_path.name,
                parser_version=VERSION,
            )

            print_job_description(job)

            json_file = OUTPUT_FOLDER / f"{file_path.stem}.json"
            save_job_description(job, json_file)

            print("JSON created successfully.")
            success += 1
        except Exception as exc:
            failed += 1
            print(f"Failed to process {file_path.name}: {exc}")

    print("\nSummary")
    print(f"Total Files: {len(files)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()

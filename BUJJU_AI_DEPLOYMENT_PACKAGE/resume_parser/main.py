"""
Recruitment Intelligence Platform
resume_parser/main.py
"""

from __future__ import annotations

from pathlib import Path

from resume_parser.resume_service import ResumeService
from resume_parser.utils.constants import SAMPLE_RESUMES


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}


def main() -> None:

    if not SAMPLE_RESUMES.exists():
        print("Sample resume folder not found.")
        return

    files = sorted(
        [
            file
            for file in SAMPLE_RESUMES.iterdir()
            if file.is_file()
            and file.suffix.lower() in SUPPORTED_EXTENSIONS
        ]
    )

    if not files:
        print("No resumes found.")
        return

    success = 0
    failed = 0

    for resume in files:

        print("=" * 80)
        print(f"Processing : {resume.name}")

        try:

            result = ResumeService.parse(resume)

            candidate = result.get("candidate", {})

            print(f"Name         : {candidate.get('name')}")
            print(f"Email        : {candidate.get('email')}")
            print(f"Phone        : {candidate.get('phone')}")
            print(f"Experience   : {candidate.get('experience')}")
            print(
                f"Skills       : "
                f"{candidate.get('skills', {}).get('matched_skills', 0)}"
            )

            success += 1

        except Exception as exc:

            failed += 1

            print(f"Failed : {exc}")

    print("=" * 80)
    print("SUMMARY")
    print(f"Total   : {len(files)}")
    print(f"Success : {success}")
    print(f"Failed  : {failed}")


if __name__ == "__main__":
    main()
"""
Recruitment Intelligence Platform
Resume Service
"""

from __future__ import annotations

from tempfile import NamedTemporaryFile
from pathlib import Path

from resume_parser.resume_service import ResumeService as Parser


class ResumeService:

    @classmethod
    def parse(
        cls,
        upload_file,
    ) -> dict:

        suffix = Path(upload_file.filename).suffix

        with NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as tmp:

            tmp.write(upload_file.file.read())

            file_path = tmp.name

        return Parser.parse(
            file_path
        )
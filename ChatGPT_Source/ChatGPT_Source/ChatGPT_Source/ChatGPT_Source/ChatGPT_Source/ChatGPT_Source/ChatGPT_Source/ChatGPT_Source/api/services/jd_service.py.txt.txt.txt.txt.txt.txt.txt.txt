"""
Recruitment Intelligence Platform
JD Service
"""

from __future__ import annotations

from tempfile import NamedTemporaryFile
from pathlib import Path

from jd_parser.services.jd_service import JDService as Parser


class JDService:

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
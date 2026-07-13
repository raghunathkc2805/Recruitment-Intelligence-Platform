"""
Recruitment Intelligence Platform
DOCX Resume Parser
"""

from __future__ import annotations

from pathlib import Path
import zipfile

import docx
import docx2txt

from resume_parser.utils import text_cleaner
from resume_parser.utils.constants import (
    DEFAULT_ENCODING,
    KEY_ERRORS,
    KEY_FILE_NAME,
    KEY_FILE_SIZE,
    KEY_FILE_TYPE,
    KEY_METADATA,
    KEY_PAGE_COUNT,
    KEY_STATUS,
    KEY_SUCCESS,
    KEY_TEXT,
    STATUS_SUCCESS,
)


class DOCXParser:
    """
    Production DOCX parser.

    Primary:
        python-docx

    Secondary:
        docx2txt

    Final fallback:
        Read as plain text
    """

    @staticmethod
    def _read_python_docx(path: Path) -> str:

        document = docx.Document(path)

        paragraphs = []

        for paragraph in document.paragraphs:

            value = paragraph.text.strip()

            if value:
                paragraphs.append(value)

        return "\n".join(paragraphs)

    @staticmethod
    def _read_docx2txt(path: Path) -> str:

        return docx2txt.process(str(path))

    @staticmethod
    def _read_text(path: Path) -> str:

        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    @classmethod
    def parse(cls, file_path: str | Path):

        path = Path(file_path)

        engine = None

        try:

            raw_text = cls._read_python_docx(path)

            engine = "python-docx"

        except (zipfile.BadZipFile, ValueError, OSError):

            try:

                raw_text = cls._read_docx2txt(path)

                engine = "docx2txt"

            except Exception:

                raw_text = cls._read_text(path)

                engine = "text-fallback"

        cleaned = text_cleaner.clean(raw_text)

        return {

            KEY_SUCCESS: True,

            KEY_STATUS: STATUS_SUCCESS,

            KEY_FILE_NAME: path.name,

            KEY_FILE_TYPE: ".docx",

            KEY_FILE_SIZE: path.stat().st_size,

            KEY_PAGE_COUNT: None,

            KEY_TEXT: cleaned,

            KEY_METADATA: {

                "encoding": DEFAULT_ENCODING,

                "engine": engine,

            },

            KEY_ERRORS: [],

        }
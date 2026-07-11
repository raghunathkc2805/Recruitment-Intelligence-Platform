"""
Recruitment Intelligence Platform
DOCX Resume Parser
"""

from pathlib import Path

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

    Primary Engine:
        python-docx

    Fallback:
        docx2txt
    """

    @staticmethod
    def _read_using_python_docx(path: Path) -> str:

        document = docx.Document(path)

        paragraphs = []

        for paragraph in document.paragraphs:
            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return "\n".join(paragraphs)

    @staticmethod
    def _read_using_docx2txt(path: Path) -> str:

        return docx2txt.process(str(path))

    @classmethod
    def parse(cls, file_path: str | Path) -> dict:

        path = Path(file_path)

        try:

            raw_text = cls._read_using_python_docx(path)

        except Exception:

            raw_text = cls._read_using_docx2txt(path)

        cleaned_text = text_cleaner.clean(raw_text)

        return {

            KEY_SUCCESS: True,

            KEY_STATUS: STATUS_SUCCESS,

            KEY_FILE_NAME: path.name,

            KEY_FILE_TYPE: ".docx",

            KEY_FILE_SIZE: path.stat().st_size,

            KEY_PAGE_COUNT: None,

            KEY_TEXT: cleaned_text,

            KEY_METADATA: {

                "encoding": DEFAULT_ENCODING,

                "engine": "python-docx/docx2txt"

            },

            KEY_ERRORS: []

        }
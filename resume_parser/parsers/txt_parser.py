"""
Recruitment Intelligence Platform
TXT Resume Parser
"""

from pathlib import Path

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


class TXTParser:
    """
    Parses plain text resumes.
    """

    @staticmethod
    def parse(file_path: str | Path) -> dict:

        path = Path(file_path)

        with open(
            path,
            "r",
            encoding=DEFAULT_ENCODING,
            errors="ignore",
        ) as f:
            raw_text = f.read()

        cleaned_text = text_cleaner.clean(raw_text)

        return {
            KEY_SUCCESS: True,
            KEY_STATUS: STATUS_SUCCESS,
            KEY_FILE_NAME: path.name,
            KEY_FILE_TYPE: ".txt",
            KEY_FILE_SIZE: path.stat().st_size,
            KEY_PAGE_COUNT: 1,
            KEY_TEXT: cleaned_text,
            KEY_METADATA: {
                "encoding": DEFAULT_ENCODING
            },
            KEY_ERRORS: [],
        }
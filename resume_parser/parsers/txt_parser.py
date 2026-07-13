"""
Recruitment Intelligence Platform
TXT Resume Parser
"""

from __future__ import annotations

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
    STATUS_FAILED,
    STATUS_SUCCESS,
)


class TXTParser:
    """
    Production TXT parser.
    """

    @classmethod
    def parse(cls, file_path: str | Path):

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(path)

        try:

            raw_text = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            cleaned = text_cleaner.clean(raw_text)

            return {

                KEY_SUCCESS: True,

                KEY_STATUS: STATUS_SUCCESS,

                KEY_FILE_NAME: path.name,

                KEY_FILE_TYPE: ".txt",

                KEY_FILE_SIZE: path.stat().st_size,

                KEY_PAGE_COUNT: 1,

                KEY_TEXT: cleaned,

                KEY_METADATA: {

                    "encoding": DEFAULT_ENCODING,

                },

                KEY_ERRORS: [],

            }

        except Exception as exc:

            return {

                KEY_SUCCESS: False,

                KEY_STATUS: STATUS_FAILED,

                KEY_FILE_NAME: path.name,

                KEY_FILE_TYPE: ".txt",

                KEY_FILE_SIZE: 0,

                KEY_PAGE_COUNT: 0,

                KEY_TEXT: "",

                KEY_METADATA: {

                    "encoding": DEFAULT_ENCODING,

                },

                KEY_ERRORS: [str(exc)],

            }
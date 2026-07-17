"""
Recruitment Intelligence Platform
PDF Resume Parser
"""

from __future__ import annotations

from pathlib import Path

import pdfplumber
from PyPDF2 import PdfReader
from PyPDF2.errors import EmptyFileError

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


class PDFParser:
    """
    Production PDF parser.
    """

    @staticmethod
    def _read_pdfplumber(path: Path):

        text = []

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                value = page.extract_text()

                if value:
                    text.append(value)

            return "\n".join(text), len(pdf.pages)

    @staticmethod
    def _read_pypdf2(path: Path):

        reader = PdfReader(str(path))

        text = []

        for page in reader.pages:

            value = page.extract_text()

            if value:
                text.append(value)

        return "\n".join(text), len(reader.pages)

    @classmethod
    def parse(cls, file_path: str |Path):

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(path)

        if path.stat().st_size == 0:

            return {

                KEY_SUCCESS: False,

                KEY_STATUS: STATUS_FAILED,

                KEY_FILE_NAME: path.name,

                KEY_FILE_TYPE: ".pdf",

                KEY_FILE_SIZE: 0,

                KEY_PAGE_COUNT: 0,

                KEY_TEXT: "",

                KEY_METADATA: {
                    "encoding": DEFAULT_ENCODING,
                    "engine": None,
                },

                KEY_ERRORS: [
                    "PDF file is empty."
                ],
            }

        try:

            raw_text, pages = cls._read_pdfplumber(path)

            engine = "pdfplumber"

        except Exception:

            try:

                raw_text, pages = cls._read_pypdf2(path)

                engine = "PyPDF2"

            except EmptyFileError:

                return {

                    KEY_SUCCESS: False,

                    KEY_STATUS: STATUS_FAILED,

                    KEY_FILE_NAME: path.name,

                    KEY_FILE_TYPE: ".pdf",

                    KEY_FILE_SIZE: path.stat().st_size,

                    KEY_PAGE_COUNT: 0,

                    KEY_TEXT: "",

                    KEY_METADATA: {
                        "encoding": DEFAULT_ENCODING,
                        "engine": None,
                    },

                    KEY_ERRORS: [
                        "PDF file is empty."
                    ],
                }

        cleaned = text_cleaner.clean(raw_text)

        return {

            KEY_SUCCESS: True,

            KEY_STATUS: STATUS_SUCCESS,

            KEY_FILE_NAME: path.name,

            KEY_FILE_TYPE: ".pdf",

            KEY_FILE_SIZE: path.stat().st_size,

            KEY_PAGE_COUNT: pages,

            KEY_TEXT: cleaned,

            KEY_METADATA: {

                "encoding": DEFAULT_ENCODING,

                "engine": engine,

            },

            KEY_ERRORS: [],

        }
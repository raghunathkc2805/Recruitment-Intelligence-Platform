"""
Recruitment Intelligence Platform
Parser Factory
"""

from pathlib import Path

from resume_parser.parsers.docx_parser import DOCXParser
from resume_parser.parsers.pdf_parser import PDFParser
from resume_parser.parsers.txt_parser import TXTParser


class ParserFactory:
    """
    Factory responsible for returning the
    correct parser implementation.

    Usage:
        parser = ParserFactory.get_parser(file)
        result = parser.parse(file)
    """

    _PARSERS = {
        ".pdf": PDFParser,
        ".docx": DOCXParser,
        ".txt": TXTParser,
    }

    @classmethod
    def get_parser(cls, file_path: str | Path):

        extension = Path(file_path).suffix.lower()

        parser = cls._PARSERS.get(extension)

        if parser is None:
            raise ValueError(
                f"Unsupported resume format: {extension}"
            )

        return parser
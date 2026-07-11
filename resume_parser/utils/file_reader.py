"""
Recruitment Intelligence Platform
Resume Parser - File Reader

Central entry point for reading supported resume files.
"""

from pathlib import Path

from resume_parser.utils.constants import (
    MAX_FILE_SIZE_BYTES,
    SUPPORTED_EXTENSIONS,
)


class FileReader:
    """
    Reads any supported resume file.
    """

    @staticmethod
    def exists(file_path: str |Path) -> bool:
        return Path(file_path).exists()

    @staticmethod
    def extension(file_path: str | Path) -> str:
        return Path(file_path).suffix.lower()

    @staticmethod
    def size(file_path: str | Path) -> int:
        return Path(file_path).stat().st_size

    @staticmethod
    def validate(file_path: str | Path) -> None:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        if path.stat().st_size == 0:
            raise ValueError(
                "File is empty."
            )

        if path.stat().st_size > MAX_FILE_SIZE_BYTES:
            raise ValueError(
                "File exceeds maximum allowed size."
            )

    @classmethod
    def read(cls, file_path: str | Path) -> dict:
        """
        Read any supported resume file.
        """

        # Local import prevents circular imports
        from resume_parser.parsers.parser_factory import ParserFactory

        cls.validate(file_path)

        parser = ParserFactory.get_parser(file_path)

        return parser.parse(file_path)
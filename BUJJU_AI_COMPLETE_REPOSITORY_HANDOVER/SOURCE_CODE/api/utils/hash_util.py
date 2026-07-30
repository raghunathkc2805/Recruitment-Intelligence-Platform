"""
SHA256 Hash Utility
"""

from __future__ import annotations

import hashlib
from pathlib import Path


class HashUtil:

    CHUNK_SIZE = 1024 * 1024

    @classmethod
    def calculate(
        cls,
        file_path: str | Path,
    ) -> str:

        path = Path(file_path)

        sha256 = hashlib.sha256()

        with path.open(
            "rb",
        ) as file:

            while True:

                chunk = file.read(
                    cls.CHUNK_SIZE
                )

                if not chunk:
                    break

                sha256.update(
                    chunk
                )

        return sha256.hexdigest()

    @classmethod
    def verify(
        cls,
        file_path: str | Path,
        expected_hash: str,
    ) -> bool:

        return (
            cls.calculate(
                file_path
            )
            == expected_hash
        )

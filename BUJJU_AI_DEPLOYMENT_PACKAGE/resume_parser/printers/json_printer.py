"""
Recruitment Intelligence Platform
JSON Printer
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JSONPrinter:
    """
    Writes parsed resume output as formatted JSON.
    """

    @staticmethod
    def save(
        data: dict[str, Any],
        output_file: str | Path,
        indent: int = 4,
    ) -> Path:

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=indent,
                ensure_ascii=False,
            )

        return output_path

    @staticmethod
    def dumps(
        data: dict[str, Any],
        indent: int = 4,
    ) -> str:

        return json.dumps(
            data,
            indent=indent,
            ensure_ascii=False,
        )
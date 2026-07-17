"""Loading utilities for canonical knowledge-base data."""

import json
from pathlib import Path
from typing import Any


KNOWLEDGE_BASE_DIRECTORY = Path(__file__).resolve().parent


def load_json(filename: str) -> Any:
    """Load a named knowledge-base JSON document."""
    with (KNOWLEDGE_BASE_DIRECTORY / filename).open(encoding="utf-8") as file:
        return json.load(file)

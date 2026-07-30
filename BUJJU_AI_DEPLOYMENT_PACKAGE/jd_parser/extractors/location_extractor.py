import re

from jd_parser.utils.knowledge_base import INDIA_CITIES


FIELD_PATTERNS = [
    r"Location\s*\(Base\)\s*:\s*(.+)",
    r"Location\s*:\s*(.+)",
    r"Base\s*Location\s*:\s*(.+)"
]


def extract_location(text):
    """
    Extract job location.
    """

    # --------------------------------------
    # Structured fields
    # --------------------------------------

    for pattern in FIELD_PATTERNS:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

    # --------------------------------------
    # Knowledge Base fallback
    # --------------------------------------

    text_lower = text.lower()

    for city in INDIA_CITIES:

        if city.lower() in text_lower:
            return city

    return ""
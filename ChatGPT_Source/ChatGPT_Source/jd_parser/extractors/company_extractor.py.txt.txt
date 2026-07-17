import re


DEFAULT_COMPANY = "Deltapro Technologies"


FIELD_PATTERNS = [
    r"^\s*Company\s*Name\s*:\s*(.+)$",
    r"^\s*Company\s*:\s*(.+)$",
    r"^\s*Client\s*:\s*(.+)$",
    r"^\s*Customer\s*:\s*(.+)$"
]


def extract_company(text):
    """
    Extract company from Job Description.
    """

    # --------------------------------------
    # Structured fields only
    # --------------------------------------

    for pattern in FIELD_PATTERNS:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE | re.MULTILINE
        )

        if match:
            return match.group(1).strip()

    # --------------------------------------
    # Teleindia GRC detection
    # --------------------------------------

    if "Talent Requisition Form" in text:
        return DEFAULT_COMPANY

    if "GRC" in text.upper():
        return DEFAULT_COMPANY

    return ""
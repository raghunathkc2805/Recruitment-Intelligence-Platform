import re


def extract_openings(text):
    """
    Extract number of openings from the JD.
    """

    patterns = [

        r"Resources\s+Needed\s*\(Nos\.\)\s*:?\s*(\d+)",

        r"No\.?\s+of\s+Positions\s*:?\s*(\d+)",

        r"Openings\s*:?\s*(\d+)",

        r"Vacancies\s*:?\s*(\d+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:
            return int(match.group(1))

    return 0
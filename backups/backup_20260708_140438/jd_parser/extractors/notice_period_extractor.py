import re


# Notice Period Patterns
NOTICE_PERIOD_PATTERNS = [
    # Immediate variants
    (r"\b(immediate\s+joiner|join\s+immediately|early\s+joiner|immediate)\b", "Immediate"),

    # Negotiable variants
    (r"\b(serving\s+notice|negotiable)\b", "Negotiable"),

    # Sequence variants
    (r"\b15\s*[-/]\s*30\s*[-/]\s*45\s*[-/]\s*60\s*[-/]\s*90\s*days\b", "15 Days"),

    # Days variants
    (r"\b15\s*[-/]?\s*days\b", "15 Days"),
    (r"\b30\s*[-/]?\s*days\b", "30 Days"),
    (r"\b45\s*[-/]?\s*days\b", "45 Days"),
    (r"\b60\s*[-/]?\s*days\b", "60 Days"),
    (r"\b90\s*[-/]?\s*days\b", "90 Days"),

    # Month variants
    (r"\b1\s*months?\b", "30 Days"),
    (r"\b2\s*months?\b", "60 Days"),
    (r"\b3\s*months?\b", "90 Days"),
]


def extract_notice_period(text):
    """
    Extract notice period from Job Description.

    Returns:
        dict: {
            "notice_period": str
        }
    """

    if not text:
        return {
            "notice_period": ""
        }

    text_lower = text.lower()

    for pattern, period in NOTICE_PERIOD_PATTERNS:
        if re.search(pattern, text_lower):
            return {
                "notice_period": period
            }

    return {
        "notice_period": ""
    }

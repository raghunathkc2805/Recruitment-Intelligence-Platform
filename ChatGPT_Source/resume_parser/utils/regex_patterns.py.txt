"""
Recruitment Intelligence Platform
Common Regular Expression Patterns
"""

from __future__ import annotations

import re

EMAIL = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    re.IGNORECASE,
)

PHONE = re.compile(
    r"""
    (?:
        (?:\+?\d{1,3})?
        [\s\-./]*
    )
    (?:
        \(?\d{2,5}\)?
        [\s\-./]*
    )?
    (?:
        \d[\d\s\-./]{8,15}\d
    )
    """,
    re.VERBOSE,
)

URL = re.compile(
    r"(?:https?://|www\.)[^\s]+",
    re.IGNORECASE,
)

LINKEDIN = re.compile(
    r"(?:https?://)?(?:www\.)?linkedin\.com/[^\s]+",
    re.IGNORECASE,
)

GITHUB = re.compile(
    r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_.-]+",
    re.IGNORECASE,
)

PINCODE = re.compile(
    r"\b\d{6}\b"
)

YEAR = re.compile(
    r"\b(?:19|20)\d{2}\b"
)

PERCENTAGE = re.compile(
    r"\b\d{2,3}(?:\.\d+)?\s*%"
)

CGPA = re.compile(
    r"\b\d(?:\.\d+)?\s*/\s*10\b",
    re.IGNORECASE,
)

NAME = re.compile(
    r"^[A-Z][a-zA-Z]+(?:[\s\-'][A-Z][a-zA-Z]+){1,4}$"
)

WHITESPACE = re.compile(
    r"\s+"
)

MULTIPLE_NEWLINES = re.compile(
    r"\n{2,}"
)

DATE = re.compile(
    r"""
    (?:
        \b(?:0?[1-9]|[12][0-9]|3[01])
        [/\-.]
        (?:0?[1-9]|1[0-2])
        [/\-.]
        (?:19|20)\d{2}\b
    )
    |
    (?:
        \b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|
        January|February|March|April|May|June|July|August|
        September|October|November|December)
        \s+
        (?:19|20)\d{2}\b
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)

EXPERIENCE = re.compile(
    r"""
    (\d+(?:\.\d+)?)
    \s*
    (?:\+)?\s*
    (?:years?|yrs?|year|yr)
    (?:\s*(?:and|&)?\s*)?
    (?:
        (\d+)
        \s*
        (?:months?|mos?|month|mo)
    )?
    """,
    re.IGNORECASE | re.VERBOSE,
)
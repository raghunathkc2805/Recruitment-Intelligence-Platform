"""
Recruitment Intelligence Platform
Resume Parser - Regular Expression Library

Centralized compiled regex patterns used across
all extractors and validators.
"""

import re

# --------------------------------------------------
# Email
# --------------------------------------------------

EMAIL = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    re.IGNORECASE
)

# --------------------------------------------------
# Phone Numbers
# --------------------------------------------------

PHONE = re.compile(
    r"(\+?\d{1,3}[\s\-]?)?(\(?\d{3,5}\)?[\s\-]?)?\d{5}[\s\-]?\d{5}",
    re.IGNORECASE
)

# --------------------------------------------------
# URLs
# --------------------------------------------------

URL = re.compile(
    r"https?://[^\s]+",
    re.IGNORECASE
)

LINKEDIN = re.compile(
    r"(https?://)?(www\.)?linkedin\.com/[^\s]+",
    re.IGNORECASE
)

GITHUB = re.compile(
    r"(https?://)?(www\.)?github\.com/[^\s]+",
    re.IGNORECASE
)

# --------------------------------------------------
# Experience
# --------------------------------------------------

EXPERIENCE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:\+)?\s*"
    r"(?:years?|yrs?|y)\s*"
    r"(?:and)?\s*"
    r"(\d+)?\s*"
    r"(?:months?|mos?|m)?",
    re.IGNORECASE
)

# --------------------------------------------------
# Date Formats
# --------------------------------------------------

DATE = re.compile(
    r"\b("
    r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}"
    r"|"
    r"\d{4}[/-]\d{1,2}[/-]\d{1,2}"
    r"|"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    r"[a-z]*\s+\d{4}"
    r")\b",
    re.IGNORECASE
)

# --------------------------------------------------
# Education
# --------------------------------------------------

CGPA = re.compile(
    r"\b\d(?:\.\d{1,2})?\s*/\s*10\b"
)

PERCENTAGE = re.compile(
    r"\b\d{2,3}(?:\.\d+)?\s*%\b"
)

# --------------------------------------------------
# Name
# --------------------------------------------------

NAME = re.compile(
    r"^[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,4}$",
    re.MULTILINE
)

# --------------------------------------------------
# Postal Codes
# --------------------------------------------------

PINCODE = re.compile(
    r"\b\d{6}\b"
)

# --------------------------------------------------
# Whitespace
# --------------------------------------------------

MULTIPLE_SPACES = re.compile(
    r"[ \t]{2,}"
)

MULTIPLE_NEWLINES = re.compile(
    r"\n{3,}"
)

LEADING_TRAILING_SPACE = re.compile(
    r"^\s+|\s+$",
    re.MULTILINE
)

CONTROL_CHARACTERS = re.compile(
    r"[\x00-\x1F\x7F]"
)

# --------------------------------------------------
# Resume Sections
# --------------------------------------------------

SECTION_HEADERS = re.compile(
    r"\b("
    r"summary|profile|objective|"
    r"experience|employment|work history|"
    r"education|qualification|"
    r"skills|technical skills|"
    r"projects|"
    r"certifications?|"
    r"languages?|"
    r"achievements?|"
    r"awards?"
    r")\b",
    re.IGNORECASE
)

# --------------------------------------------------
# Common Cleanup
# --------------------------------------------------

BULLETS = re.compile(
    r"[•●■▪►◆◇○]"
)

HYPHENS = re.compile(
    r"[–—]"
)
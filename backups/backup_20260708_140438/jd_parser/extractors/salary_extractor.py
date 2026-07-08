import re


SALARY_PATTERNS = [

    r"₹\s?[\d,]+(?:\.\d+)?",

    r"\bINR\s?[\d,]+(?:\.\d+)?",

    r"\bCTC\s*:?\s*[\d.,]+\s?LPA",

    r"\b[\d.]+\s?Lakhs Per Annum\b",

    r"\b[\d.]+\s?Lakhs/Annum\b",

    r"\b[\d.]+\s?Lakhs?\b",

    r"\b[\d.]+\s?Lacs?\b",

    r"\b[\d.]+\s?LPA\b",

    r"\bRs\.?\s?[\d,]+"

]


def extract_salary(text):
    """
    Extract salary information from Job Description.

    Returns:
        str
    """

    if not text:
        return ""

    for pattern in SALARY_PATTERNS:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            salary = match.group().strip()

            # Strip informal suffixes (case-sensitive to preserve formal patterns)
            salary = re.sub(r'\s+per\s+annum\b', '', salary)
            salary = re.sub(r'\s+per\s+year\b', '', salary)
            salary = re.sub(r'\s+annually\b', '', salary)

            return salary.strip()

    return ""
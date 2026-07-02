import re


SALARY_PATTERNS = [

    r"₹\s?[\d,]+(?:\.\d+)?",

    r"INR\s?[\d,]+(?:\.\d+)?",

    r"CTC\s*:?\s*[\d.,]+\s?LPA",

    r"[\d.]+\s?LPA",

    r"[\d.]+\s?Lakhs",

    r"[\d.]+\s?Lakhs Per Annum",

    r"[\d.]+\s?Lakhs/Annum",

    r"[\d.]+\s?Lacs",

    r"Rs\.?\s?[\d,]+"

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
            return match.group().strip()

    return ""
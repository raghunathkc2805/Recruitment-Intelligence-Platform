import re


QUALIFICATIONS = [
    "BE",
    "B.E",
    "BTech",
    "B.Tech",
    "ME",
    "M.E",
    "MTech",
    "M.Tech",
    "Diploma",
    "ITI",
    "BCA",
    "MCA",
    "BSc",
    "MSc",
    "MBA"
]


BRANCHES = [
    "Electrical",
    "Electronics",
    "Electronics and Communication",
    "ECE",
    "EEE",
    "Mechanical",
    "Civil",
    "Computer Science",
    "Information Science",
    "IT"
]


def _search_terms(text):
    """
    Search qualifications using whole-word matching.
    """

    results = []

    for qualification in QUALIFICATIONS:

        pattern = r"\b" + re.escape(qualification) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            results.append(qualification)

    for branch in BRANCHES:

        pattern = r"\b" + re.escape(branch) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            results.append(branch)

    return sorted(set(results))


def extract_education(text):
    """
    Extract education requirements.
    """

    # --------------------------------------------------
    # Step 1
    # Education Preference section
    # --------------------------------------------------

    section = re.search(

        r"Education\s+Preference\s*:?(.*?)(?:\n\s*\n|$)",

        text,

        flags=re.IGNORECASE | re.DOTALL

    )

    if section:

        education = _search_terms(section.group(1))

        if education:
            return education

    # --------------------------------------------------
    # Step 2
    # Explicit education statements
    # --------------------------------------------------

    explicit_patterns = [

        r"(Bachelor.?s Degree.*)",

        r"(Master.?s Degree.*)",

        r"(Diploma.*)",

        r"(BE.*)",

        r"(B\.E.*)",

        r"(BTech.*)",

        r"(B\.Tech.*)"

    ]

    for pattern in explicit_patterns:

        match = re.search(

            pattern,

            text,

            flags=re.IGNORECASE

        )

        if match:

            education = _search_terms(match.group(1))

            if education:
                return education

    return []
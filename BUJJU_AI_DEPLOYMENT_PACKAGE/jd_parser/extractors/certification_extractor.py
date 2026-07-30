import re

from jd_parser.utils.knowledge_base import CERTIFICATIONS


def extract_certifications(text):
    """
    Extract certifications from Job Description.
    """

    if not text:
        return []

    matches = []

    for certification in CERTIFICATIONS:

        if certification.endswith("+"):
            pattern = r"(?<!\w)" + re.escape(certification) + r"(?!\w)"
        else:
            pattern = r"\b" + re.escape(certification) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            matches.append(certification)

    return sorted(set(matches))
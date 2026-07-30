import re

from jd_parser.utils.knowledge_base import (
    DESIGNATIONS,
    TECHNICAL_SKILLS,
    CERTIFICATIONS,
)


def _flatten_designations():
    if isinstance(DESIGNATIONS, dict):
        values = []
        for group in DESIGNATIONS.values():
            if isinstance(group, list):
                values.extend(group)
        return values
    return DESIGNATIONS


def _extract(text, lookup):
    results = []

    for item in sorted(set(lookup), key=len, reverse=True):
        if re.search(r"\b" + re.escape(item) + r"\b", text, re.IGNORECASE):
            results.append(item)

    return results


def extract_resume_search(text):
    """
    Generate recruiter resume search keywords.

    Returns
    -------
    {
        "resume_keywords": [...],
        "resume_search": "..."
    }
    """

    if not text:
        return {
            "resume_keywords": [],
            "resume_search": ""
        }

    keywords = []

    keywords.extend(_extract(text, _flatten_designations()))
    keywords.extend(_extract(text, TECHNICAL_SKILLS))
    keywords.extend(_extract(text, CERTIFICATIONS))

    seen = set()
    ordered = []

    for keyword in keywords:
        if keyword.lower() not in seen:
            ordered.append(keyword)
            seen.add(keyword.lower())

    return {
        "resume_keywords": ordered,
        "resume_search": " ".join(ordered)
    }
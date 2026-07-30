import re

from jd_parser.utils.knowledge_base import (
    DESIGNATIONS,
    TECHNICAL_SKILLS,
    CERTIFICATIONS,
    FUNCTIONAL_SKILLS,
)


def _flatten_designations():
    if isinstance(DESIGNATIONS, dict):
        result = []
        for values in DESIGNATIONS.values():
            if isinstance(values, list):
                result.extend(values)
        return result
    return DESIGNATIONS


def _find_matches(text, items):
    matches = []

    for item in sorted(set(items), key=len, reverse=True):
        if re.search(r"\b" + re.escape(item) + r"\b", text, re.IGNORECASE):
            matches.append(item)

    return matches


def extract_boolean_search(text):
    """
    Generate recruiter Boolean search string.

    Returns:
    {
        "boolean_search": str
    }
    """

    if not text:
        return {"boolean_search": ""}

    designations = _find_matches(text, _flatten_designations())
    skills = _find_matches(text, TECHNICAL_SKILLS)
    certifications = _find_matches(text, CERTIFICATIONS)
    functional = _find_matches(text, FUNCTIONAL_SKILLS)

    keywords = []

    keywords.extend(designations)
    keywords.extend(skills)
    keywords.extend(certifications)
    keywords.extend(functional)

    seen = set()
    ordered = []

    for keyword in keywords:
        if keyword.lower() not in seen:
            ordered.append(keyword)
            seen.add(keyword.lower())

    boolean = " AND ".join(f'"{keyword}"' for keyword in ordered)

    return {
        "boolean_search": boolean
    }
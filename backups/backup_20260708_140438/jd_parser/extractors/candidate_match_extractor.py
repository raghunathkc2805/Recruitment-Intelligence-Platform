import re

from jd_parser.utils.knowledge_base import (
    DESIGNATIONS,
    TECHNICAL_SKILLS,
    CERTIFICATIONS,
    FUNCTIONAL_SKILLS,
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


def extract_candidate_match(text):
    """
    Generate candidate matching intelligence.

    Returns
    -------
    {
        "match_score": int,
        "designation_keywords": [...],
        "technical_keywords": [...],
        "certification_keywords": [...],
        "functional_keywords": [...]
    }
    """

    if not text:
        return {
            "match_score": 0,
            "designation_keywords": [],
            "technical_keywords": [],
            "certification_keywords": [],
            "functional_keywords": [],
        }

    designations = _extract(text, _flatten_designations())
    technical = _extract(text, TECHNICAL_SKILLS)
    certifications = _extract(text, CERTIFICATIONS)
    functional = _extract(text, FUNCTIONAL_SKILLS)

    score = (
        len(designations) * 30 +
        len(technical) * 5 +
        len(certifications) * 10 +
        len(functional) * 3
    )

    score = min(score, 100)

    return {
        "match_score": score,
        "designation_keywords": designations,
        "technical_keywords": technical,
        "certification_keywords": certifications,
        "functional_keywords": functional,
    }
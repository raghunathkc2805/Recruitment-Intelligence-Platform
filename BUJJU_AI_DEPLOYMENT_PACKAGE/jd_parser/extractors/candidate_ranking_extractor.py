import re

from jd_parser.utils.knowledge_base import (
    DESIGNATIONS,
    TECHNICAL_SKILLS,
    CERTIFICATIONS,
    FUNCTIONAL_SKILLS,
)


def _flatten_designations():
    """
    Flatten designation knowledge base into a single list.
    """
    if isinstance(DESIGNATIONS, dict):
        values = []
        for group in DESIGNATIONS.values():
            if isinstance(group, list):
                values.extend(group)
        return values

    return DESIGNATIONS


def _extract(text, lookup):
    """
    Extract matching keywords from the supplied lookup list.
    """
    results = []

    if not lookup:
        return results

    for item in sorted(set(lookup), key=len, reverse=True):

        if not item:
            continue

        if re.search(
            r"\b" + re.escape(str(item)) + r"\b",
            text,
            re.IGNORECASE,
        ):
            results.append(item)

    return results


def extract_candidate_ranking(text):
    """
    Generate candidate ranking intelligence.

    Returns
    -------
    {
        "ranking_score": int,
        "ranking": str,
        "designation_keywords": [...],
        "technical_keywords": [...],
        "certification_keywords": [...],
        "functional_keywords": [...]
    }
    """

    if not text:
        return {
            "ranking_score": 0,
            "ranking": "Not Suitable",
            "designation_keywords": [],
            "technical_keywords": [],
            "certification_keywords": [],
            "functional_keywords": [],
        }

    designations = _extract(
        text,
        _flatten_designations(),
    )

    technical = _extract(
        text,
        TECHNICAL_SKILLS,
    )

    certifications = _extract(
        text,
        CERTIFICATIONS,
    )

    functional = _extract(
        text,
        FUNCTIONAL_SKILLS,
    )

    score = (
        len(designations) * 30
        + len(technical) * 5
        + len(certifications) * 10
        + len(functional) * 3
    )

    score = min(score, 100)

    if score >= 95:
        ranking = "Outstanding"
    elif score >= 90:
        ranking = "Excellent"
    elif score >= 80:
        ranking = "Very Good"
    elif score >= 70:
        ranking = "Good"
    elif score >= 50:
        ranking = "Average"
    else:
        ranking = "Not Suitable"

    return {
        "ranking_score": score,
        "ranking": ranking,
        "designation_keywords": designations,
        "technical_keywords": technical,
        "certification_keywords": certifications,
        "functional_keywords": functional,
    }
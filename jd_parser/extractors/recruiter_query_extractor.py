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


def extract_recruiter_query(text):
    """
    Generate recruiter search query.

    Returns
    -------
    {
        "recruiter_keywords": [...],
        "recruiter_query": "..."
    }
    """

    if not text:
        return {
            "recruiter_keywords": [],
            "recruiter_query": ""
        }

    keywords = []

    keywords.extend(_extract(text, _flatten_designations()))
    keywords.extend(_extract(text, TECHNICAL_SKILLS))
    keywords.extend(_extract(text, CERTIFICATIONS))
    keywords.extend(_extract(text, FUNCTIONAL_SKILLS))

    seen = set()
    ordered = []

    for keyword in keywords:
        key = keyword.lower()
        if key not in seen:
            ordered.append(keyword)
            seen.add(key)

    designation_terms = []
    skill_terms = []

    designation_set = {d.lower() for d in _flatten_designations()}

    for keyword in ordered:
        if keyword.lower() in designation_set:
            designation_terms.append(f'"{keyword}"')
        else:
            skill_terms.append(f'"{keyword}"')

    query_parts = []

    if designation_terms:
        query_parts.append("(" + " OR ".join(designation_terms) + ")")

    if skill_terms:
        query_parts.append(" AND ".join(skill_terms))

    return {
        "recruiter_keywords": ordered,
        "recruiter_query": " AND ".join(query_parts)
    }
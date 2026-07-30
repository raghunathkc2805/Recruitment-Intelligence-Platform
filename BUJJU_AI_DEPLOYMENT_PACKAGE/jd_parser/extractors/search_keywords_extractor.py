import re

from jd_parser.utils.knowledge_base import (
    DESIGNATIONS,
    TECHNICAL_SKILLS,
    CERTIFICATIONS,
    FUNCTIONAL_SKILLS,
)


def _flatten_designations():
    """
    Flatten designation hierarchy into a single list.
    """
    flattened = []

    if isinstance(DESIGNATIONS, dict):
        for values in DESIGNATIONS.values():
            if isinstance(values, list):
                flattened.extend(values)
    elif isinstance(DESIGNATIONS, list):
        flattened.extend(DESIGNATIONS)

    return flattened


def _prepare_lookup(items):
    """
    Sort by longest keyword first to avoid partial matches.
    Example:
        Project Manager -> before -> Manager
        Network Engineer -> before -> Engineer
    """
    return sorted(set(items), key=len, reverse=True)


def extract_search_keywords(text):
    """
    Extract recruiter search keywords from a Job Description.

    - Matches longest phrases first.
    - Returns keywords in JD order.
    - Removes duplicates.
    """

    if not text:
        return []

    designations = _prepare_lookup(_flatten_designations())
    technical_skills = _prepare_lookup(TECHNICAL_SKILLS)
    certifications = _prepare_lookup(CERTIFICATIONS)
    functional_skills = _prepare_lookup(FUNCTIONAL_SKILLS)

    lookup_lists = [
    designations,
    certifications,
    technical_skills,
    functional_skills,
]

    matches = []

    for lookup in lookup_lists:
        for keyword in lookup:
            pattern = r"\b" + re.escape(keyword) + r"\b"

            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                matches.append((match.start(), len(keyword), keyword))

    # Sort by:
    # 1. Position in JD
    # 2. Longest keyword first (same position)
    matches.sort(key=lambda x: (x[0], -x[1]))

    keywords = []
    seen = set()

    for position, length, keyword in matches:
        lower = keyword.lower()

        # Skip if already added
        if lower in seen:
            continue

        # Skip shorter keyword if longer keyword already starts here
        duplicate = False
        for _, _, existing in [(0, 0, k) for k in keywords]:
            if (
                keyword.lower() in existing.lower()
                and keyword.lower() != existing.lower()
            ):
                duplicate = True
                break

        if duplicate:
            continue

        keywords.append(keyword)
        seen.add(lower)

    return keywords
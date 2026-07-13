from jd_parser.utils.knowledge_base import (
    SKILLS,
    DESIGNATIONS,
    DOMAINS,
    KEYWORD_SYNONYMS
)


def extract_search_keywords(candidate):
    """
    Build searchable keywords from candidate data.
    """

    keywords = set()

    # Technical Skills
    for skill in candidate.technical_skills:
        keywords.add(skill)

    # Functional Skills
    for skill in candidate.functional_skills:
        keywords.add(skill)

    # Soft Skills
    for skill in candidate.soft_skills:
        keywords.add(skill)

    # Current Company
    if candidate.current_company:
        keywords.add(candidate.current_company)

    # Current Designation
    if candidate.current_designation:
        keywords.add(candidate.current_designation)

    # Previous Companies
    for company in candidate.companies:
        keywords.add(company)

    # Domains
    if candidate.primary_domain:
        keywords.add(candidate.primary_domain)

    if candidate.secondary_domain:
        keywords.add(candidate.secondary_domain)

    # Synonyms
    final_keywords = set()

    for keyword in keywords:

        final_keywords.add(keyword)

        lower = keyword.lower()

        if lower in KEYWORD_SYNONYMS:
            for synonym in KEYWORD_SYNONYMS[lower]:
                final_keywords.add(synonym)

    return sorted(final_keywords)
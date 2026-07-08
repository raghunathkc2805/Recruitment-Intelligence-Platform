def calculate_resume_score(candidate):
    """
    Calculate overall resume score.
    """

    score = 0

    # Contact (10)
    if candidate.name:
        score += 3
    if candidate.email:
        score += 3
    if candidate.mobile:
        score += 4

    # Experience (20)
    if candidate.current_company:
        score += 10
    if candidate.current_designation:
        score += 10

    # Skills (20)
    score += min(len(candidate.technical_skills), 10)
    score += min(len(candidate.functional_skills), 5)
    score += min(len(candidate.soft_skills), 5)

    # Education (15)
    if candidate.highest_qualification:
        score += 10
    if candidate.education:
        score += 5

    # Certifications (10)
    score += min(len(candidate.certifications) * 2, 10)

    # Domain (10)
    if candidate.primary_domain:
        score += 10

    # Company (10)
    score += min(len(candidate.companies), 10)

    # Location (5)
    if candidate.primary_city:
        score += 3
    if candidate.primary_state:
        score += 2

    return min(score, 100)
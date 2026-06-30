def calculate_overall_score(result):
    """
    Calculate weighted overall score.
    Scores are expected to be between 0.0 and 1.0.
    """

    weights = {
        "skills": 40,
        "experience": 20,
        "education": 10,
        "certification": 10,
        "domain": 10,
        "location": 10
    }

    weighted_score = (
        result.skills_score * weights["skills"] +
        result.experience_score * weights["experience"] +
        result.education_score * weights["education"] +
        result.certification_score * weights["certification"] +
        result.domain_score * weights["domain"] +
        result.location_score * weights["location"]
    )

    # Convert to percentage (0–100)
    result.overall_score = round(weighted_score, 2)

    score = result.overall_score

    if score >= 90:
        result.grade = "A+"
    elif score >= 80:
        result.grade = "A"
    elif score >= 70:
        result.grade = "B"
    elif score >= 60:
        result.grade = "C"
    else:
        result.grade = "D"

    return result
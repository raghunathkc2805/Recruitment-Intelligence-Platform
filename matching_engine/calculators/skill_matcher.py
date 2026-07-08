from typing import List, Dict


def _normalize(skills: List[str]) -> List[str]:
    """
    Normalize skills for comparison.
    """
    if not skills:
        return []

    normalized = []

    for skill in skills:
        if skill:
            normalized.append(skill.strip().lower())

    return sorted(set(normalized))


def calculate_skill_match(candidate_skills: List[str],
                          jd_skills: List[str]) -> Dict:
    """
    Calculate skill matching.

    Returns:
        {
            skills_score,
            matched_skills,
            missing_skills,
            additional_skills
        }
    """

    candidate = set(_normalize(candidate_skills))
    required = set(_normalize(jd_skills))

    matched = sorted(candidate & required)
    missing = sorted(required - candidate)
    additional = sorted(candidate - required)

    if len(required) == 0:
        score = 100.0
    else:
        score = round(
            len(matched) / len(required) * 100,
            2
        )

    return {

        "skills_score": score,

        "matched_skills": matched,

        "missing_skills": missing,

        "additional_skills": additional

    }
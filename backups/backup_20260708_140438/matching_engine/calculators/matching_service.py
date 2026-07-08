from typing import Dict


def calculate_experience_match(
    candidate_experience: float,
    minimum_required: float,
    maximum_required: float
) -> Dict:
    """
    Calculate experience matching.

    Scores are returned as percentages (0–100).
    """

    if minimum_required <= 0:
        return {
            "experience_score": 100.0,
            "experience_gap": 0.0,
            "qualified": True
        }

    if candidate_experience < minimum_required:

        gap = round(
            minimum_required - candidate_experience,
            2
        )

        score = round(
            (candidate_experience / minimum_required) * 100,
            2
        )

        return {
            "experience_score": score,
            "experience_gap": gap,
            "qualified": False
        }

    if maximum_required > 0 and candidate_experience > maximum_required:

        return {
            "experience_score": 100.0,
            "experience_gap": 0.0,
            "qualified": True
        }

    return {
        "experience_score": 100.0,
        "experience_gap": 0.0,
        "qualified": True
    }
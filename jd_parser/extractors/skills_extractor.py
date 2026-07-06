import re

from jd_parser.utils.knowledge_base import (
    TECHNICAL_SKILLS,
    FUNCTIONAL_SKILLS,
    SOFT_SKILLS,
)

def _find_matches(text, skill_list):
    """
    Find whole-word skill matches.
    """

    matches = []

    for skill in skill_list:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):

            if skill not in matches:
                matches.append(skill)

    return sorted(matches)


def extract_skills(text):
    """
    Extract skills from Job Description.
    """

    return {

        "technical_skills": _find_matches(
            text,
            TECHNICAL_SKILLS
        ),

        "functional_skills": _find_matches(
            text,
            FUNCTIONAL_SKILLS
        ),

        "soft_skills": _find_matches(
            text,
            SOFT_SKILLS
        )

    }
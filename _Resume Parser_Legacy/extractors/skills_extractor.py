from jd_parser.utils.knowledge_base import SKILLS


def extract_skills(text):
    """
    Extract technical, functional and soft skills
    from resume text using the Knowledge Base.
    """

    text_lower = text.lower()

    technical = []
    functional = []
    soft = []

    # Technical Skills
    for skill in SKILLS["technical_skills"]:
        if skill.lower() in text_lower:
            technical.append(skill)

    # Functional Skills
    for skill in SKILLS["functional_skills"]:
        if skill.lower() in text_lower:
            functional.append(skill)

    # Soft Skills
    for skill in SKILLS["soft_skills"]:
        if skill.lower() in text_lower:
            soft.append(skill)

    return {
        "technical_skills": sorted(set(technical)),
        "functional_skills": sorted(set(functional)),
        "soft_skills": sorted(set(soft))
    }
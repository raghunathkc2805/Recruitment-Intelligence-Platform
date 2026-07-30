from resume_parser.extractors.skills_extractor import (
    SkillsExtractor,
)


def test_extract_technical_skill():

    result = SkillsExtractor.extract(
        "Experienced in Python, Docker and Kubernetes."
    )

    assert "Python" in result["technical_skills"]


def test_extract_functional_skill():

    result = SkillsExtractor.extract(
        "Strong Project Management and Stakeholder Management skills."
    )

    assert "Project Management" in result["functional_skills"]


def test_extract_soft_skill():

    result = SkillsExtractor.extract(
        "Excellent Communication and Leadership."
    )

    assert "Communication" in result["soft_skills"]


def test_extract_empty():

    result = SkillsExtractor.extract("")

    assert result["technical_skills"] == []

    assert result["functional_skills"] == []

    assert result["soft_skills"] == []

    assert result["matched_skills"] == 0
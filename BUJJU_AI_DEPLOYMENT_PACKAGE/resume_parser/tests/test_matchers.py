from resume_parser.matchers.certification_matcher import (
    CertificationMatcher,
)
from resume_parser.matchers.designation_matcher import (
    DesignationMatcher,
)
from resume_parser.matchers.education_matcher import (
    EducationMatcher,
)
from resume_parser.matchers.experience_matcher import (
    ExperienceMatcher,
)
from resume_parser.matchers.location_matcher import (
    LocationMatcher,
)
from resume_parser.matchers.overall_matcher import (
    OverallMatcher,
)
from resume_parser.matchers.skill_matcher import (
    SkillMatcher,
)


def test_skill_matcher():

    result = SkillMatcher.match(
        ["Python", "Docker", "AWS"],
        ["Python", "AWS", "Kubernetes"],
    )

    assert result["matched_count"] == 2

    assert result["required_count"] == 3


def test_experience_matcher():

    result = ExperienceMatcher.match(
        {"years": 5},
        4,
    )

    assert result["qualified"] is True


def test_education_matcher():

    result = EducationMatcher.match(
        [
            {"degree": "B.E"}
        ],
        ["B.E", "M.Tech"],
    )

    assert result["matched_count"] == 1


def test_designation_matcher():

    result = DesignationMatcher.match(
        ["Software Engineer"],
        ["Software Engineer"],
    )

    assert result["matched_count"] == 1


def test_location_matcher():

    result = LocationMatcher.match(
        [
            {"location": "Bangalore"}
        ],
        ["Bangalore"],
    )

    assert result["matched_count"] == 1


def test_certification_matcher():

    result = CertificationMatcher.match(
        [
            {
                "certification": "AWS Certified Solutions Architect"
            }
        ],
        [
            "AWS Certified Solutions Architect"
        ],
    )

    assert result["matched_count"] == 1


def test_overall_matcher():

    candidate = {
        "skills": ["Python", "Docker"],
        "experience": {"years": 5},
        "education": [{"degree": "B.E"}],
        "designations": ["Software Engineer"],
        "locations": [{"location": "Bangalore"}],
        "certifications": [
            {
                "certification": "AWS Certified Solutions Architect"
            }
        ],
    }

    requirements = {
        "skills": ["Python"],
        "experience": 3,
        "education": ["B.E"],
        "designations": ["Software Engineer"],
        "locations": ["Bangalore"],
        "certifications": [
            "AWS Certified Solutions Architect"
        ],
    }

    result = OverallMatcher.match(
        candidate,
        requirements,
    )

    assert "overall_score" in result

    assert result["overall_score"] >= 0

    assert result["overall_score"] <= 100
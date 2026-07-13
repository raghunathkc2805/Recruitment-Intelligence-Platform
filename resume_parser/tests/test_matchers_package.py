from resume_parser.matchers import (
    CertificationMatcher,
    DesignationMatcher,
    EducationMatcher,
    ExperienceMatcher,
    LocationMatcher,
    OverallMatcher,
    SkillMatcher,
)


def test_matchers_package_exports():

    assert CertificationMatcher is not None

    assert DesignationMatcher is not None

    assert EducationMatcher is not None

    assert ExperienceMatcher is not None

    assert LocationMatcher is not None

    assert OverallMatcher is not None

    assert SkillMatcher is not None
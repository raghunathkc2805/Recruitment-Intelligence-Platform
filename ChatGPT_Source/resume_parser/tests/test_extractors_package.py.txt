from resume_parser.extractors import (
    CertificationExtractor,
    EducationExtractor,
    EmailExtractor,
    EmployerExtractor,
    ExperienceExtractor,
    LanguageExtractor,
    LocationExtractor,
    NameExtractor,
    PhoneExtractor,
    ProjectExtractor,
    SkillsExtractor,
    SummaryExtractor,
)


def test_extractors_package_exports():

    assert CertificationExtractor is not None

    assert EducationExtractor is not None

    assert EmailExtractor is not None

    assert EmployerExtractor is not None

    assert ExperienceExtractor is not None

    assert LanguageExtractor is not None

    assert LocationExtractor is not None

    assert NameExtractor is not None

    assert PhoneExtractor is not None

    assert ProjectExtractor is not None

    assert SkillsExtractor is not None

    assert SummaryExtractor is not None
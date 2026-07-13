from resume_parser.utils.knowledge_base import (
    CERTIFICATIONS,
    COMPANY_ALIASES,
    DESIGNATION_ALIASES,
    DOMAINS,
    EDUCATION,
    KEYWORDS,
    LANGUAGES,
    LOCATIONS,
    SKILLS,
)


def test_skills_loaded():

    assert isinstance(SKILLS, dict)

    assert "technical_skills" in SKILLS

    assert "functional_skills" in SKILLS

    assert "soft_skills" in SKILLS


def test_education_loaded():

    assert isinstance(EDUCATION, list)

    assert len(EDUCATION) > 0


def test_certifications_loaded():

    assert isinstance(CERTIFICATIONS, list)


def test_locations_loaded():

    assert isinstance(LOCATIONS, list)


def test_languages_loaded():

    assert isinstance(LANGUAGES, list)


def test_domains_loaded():

    assert isinstance(DOMAINS, list)


def test_company_aliases_loaded():

    assert isinstance(COMPANY_ALIASES, dict)


def test_designation_aliases_loaded():

    assert isinstance(DESIGNATION_ALIASES, dict)


def test_keyword_synonyms_loaded():

    assert KEYWORDS is not None
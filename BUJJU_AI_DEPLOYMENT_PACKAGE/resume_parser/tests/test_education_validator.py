from resume_parser.validators.education_validator import (
    EducationValidator,
)


def test_education_validator_valid():

    education = [
        {
            "degree": "B.E",
            "text": "B.E in Computer Science",
            "year": "2022",
        }
    ]

    assert EducationValidator.validate(education)


def test_education_validator_empty():

    assert not EducationValidator.validate([])


def test_education_validator_none():

    assert not EducationValidator.validate(None)


def test_education_validator_missing_degree():

    education = [
        {
            "text": "Computer Science"
        }
    ]

    assert not EducationValidator.validate(education)


def test_education_validator_invalid_record():

    education = [
        "B.E Computer Science"
    ]

    assert not EducationValidator.validate(education)
from resume_parser.validators.experience_validator import (
    ExperienceValidator,
)


def test_experience_validator_valid():

    experience = {
        "years": 5,
        "months": 6,
        "total_months": 66,
    }

    assert ExperienceValidator.validate(experience)


def test_experience_validator_none():

    assert not ExperienceValidator.validate(None)


def test_experience_validator_negative():

    experience = {
        "years": -1,
        "months": 0,
        "total_months": -12,
    }

    assert not ExperienceValidator.validate(experience)


def test_experience_validator_excessive():

    experience = {
        "years": 100,
        "months": 0,
        "total_months": 1200,
    }

    assert not ExperienceValidator.validate(experience)
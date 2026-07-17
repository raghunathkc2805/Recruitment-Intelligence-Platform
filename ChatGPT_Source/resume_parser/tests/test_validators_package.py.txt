from resume_parser.validators import (
    EducationValidator,
    EmailValidator,
    ExperienceValidator,
    PhoneValidator,
    ResumeValidator,
)


def test_validators_package_exports():

    assert ResumeValidator is not None

    assert EmailValidator is not None

    assert PhoneValidator is not None

    assert ExperienceValidator is not None

    assert EducationValidator is not None
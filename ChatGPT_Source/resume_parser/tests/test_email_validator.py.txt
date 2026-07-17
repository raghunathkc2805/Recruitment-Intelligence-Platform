from resume_parser.validators.email_validator import EmailValidator


def test_email_validator_valid():

    assert EmailValidator.validate(
        "candidate@example.com"
    )


def test_email_validator_invalid():

    assert not EmailValidator.validate(
        "candidateexample.com"
    )


def test_email_validator_empty():

    assert not EmailValidator.validate("")
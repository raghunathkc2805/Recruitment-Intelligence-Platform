from resume_parser.validators.phone_validator import PhoneValidator


def test_phone_validator_valid():

    assert PhoneValidator.validate(
        "+919876543210"
    )


def test_phone_validator_valid_without_country_code():

    assert PhoneValidator.validate(
        "9876543210"
    )


def test_phone_validator_invalid():

    assert not PhoneValidator.validate(
        "12345"
    )


def test_phone_validator_empty():

    assert not PhoneValidator.validate("")
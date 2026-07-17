from resume_parser.utils import regex_patterns


def test_email_pattern():

    assert regex_patterns.EMAIL.search(
        "john.doe@example.com"
    )


def test_phone_pattern():

    assert regex_patterns.PHONE.search(
        "+91 9876543210"
    )


def test_name_pattern():

    assert regex_patterns.NAME.fullmatch(
        "John Michael Doe"
    )


def test_year_pattern():

    assert regex_patterns.YEAR.search(
        "Graduated in 2022"
    )


def test_percentage_pattern():

    assert regex_patterns.PERCENTAGE.search(
        "Scored 85%"
    )


def test_cgpa_pattern():

    assert regex_patterns.CGPA.search(
        "CGPA: 8.75/10"
    )


def test_experience_pattern():

    assert regex_patterns.EXPERIENCE.search(
        "5 years 6 months"
    )


def test_url_pattern():

    assert regex_patterns.URL.search(
        "https://example.com"
    )


def test_linkedin_pattern():

    assert regex_patterns.LINKEDIN.search(
        "https://www.linkedin.com/in/johndoe"
    )


def test_github_pattern():

    assert regex_patterns.GITHUB.search(
        "https://github.com/johndoe"
    )
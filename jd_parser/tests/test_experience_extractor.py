import pytest

from jd_parser.extractors.experience_extractor import extract_experience


@pytest.mark.parametrize(
    "text,expected_min,expected_max",
    [
        ("Freshers", 0, 0),
        ("Freshers can apply", 0, 0),
        ("0 Years", 0, 0),
        ("0 year", 0, 0),
        ("0 yrs", 0, 0),
        ("0 yoe", 0, 0),
        ("0–1 Years", 0, 1),
        ("0-1 Years", 0, 1),
        ("0 to 1 years", 0, 1),
        ("1 Year", 1, 1),
        ("1 yr", 1, 1),
        ("1 yoe", 1, 1),
        ("1–3 Years", 1, 3),
        ("1-3 years", 1, 3),
        ("1 to 3 years", 1, 3),
        ("2–4 years", 2, 4),
        ("2-4 years", 2, 4),
        ("2 to 4 years", 2, 4),
        ("3–5 Years", 3, 5),
        ("3-5 years", 3, 5),
        ("5+ Years", 5, 99),
        ("5+ years", 5, 99),
        ("7–10 Years", 7, 10),
        ("7-10 years", 7, 10),
        ("10+ Years", 10, 99),
        ("12–15 Years", 12, 15),
        ("12-15 years", 12, 15),
        ("15+ Years", 15, 99),
        ("0 to 2 years", 0, 2),
        ("Minimum 5 years", 5, 99),
        ("At least 7 years", 7, 99),
        ("5 yrs", 5, 5),
        ("5 yr", 5, 5),
        ("5 yoe", 5, 5),
        ("Experience: 8 years", 8, 8),
        ("Relevant Experience: 6 years", 6, 6),
        ("Overall Experience: 9 years", 9, 9),
        ("3+ years", 3, 99),
        ("More than 10 years", 11, 99),
        ("Minimum 5 yrs", 5, 99),
        ("At least 7 yrs", 7, 99),
        ("More than 10 yrs", 11, 99),
        ("More than 10 yoe", 11, 99),
        ("Experience 4 years", 4, 4),
        ("Relevant experience 4 years", 4, 4),
        ("Overall experience 4 years", 4, 4),
        ("1   -   3   years", 1, 3),
        ("2   –   4   years", 2, 4),
        ("5   yrs", 5, 5),
        ("Minimum   5   years", 5, 99),
        ("At   least   7   years", 7, 99),
        ("Experience:   8   years", 8, 8),
        ("Freshers   can   apply", 0, 0),
        ("3 + years", 3, 99),
        ("10 + Years", 10, 99),
        ("15 + Years", 15, 99),
        ("5years", 5, 5),
        ("10years", 10, 10),
        ("More than   10   years", 11, 99),
        ("0years", 0, 0),
        ("0-year", 0, 0),
        ("0 to 2yrs", 0, 2),
    ],
)
def test_extract_experience_normalizes_values(text, expected_min, expected_max):
    result = extract_experience(text)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == expected_min
    assert result[1] == expected_max


def test_extract_experience_returns_zero_for_none_text():
    result = extract_experience(None)
    assert result == (0, 0)


def test_extract_experience_returns_zero_for_empty_text():
    result = extract_experience("")
    assert result == (0, 0)


def test_extract_experience_returns_zero_when_no_experience_is_found():
    result = extract_experience("This JD does not mention any experience")
    assert result == (0, 0)

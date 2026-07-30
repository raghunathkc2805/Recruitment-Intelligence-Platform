import pytest

from jd_parser.extractors.notice_period_extractor import extract_notice_period


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Immediate", "Immediate"),
        ("Immediate Joiner", "Immediate"),
        ("Join Immediately", "Immediate"),
        ("Early Joiner", "Immediate"),
        ("Serving Notice", "Negotiable"),
        ("Notice period is negotiable", "Negotiable"),
        ("15 Days", "15 Days"),
        ("30 Days", "30 Days"),
        ("45 Days", "45 Days"),
        ("60 Days", "60 Days"),
        ("90 Days", "90 Days"),
        ("15/30/45/60/90 Days", "15 Days"),
        ("15-30-45-60-90 Days", "15 Days"),
        ("15 days notice", "15 Days"),
        ("30 days notice", "30 Days"),
        ("45 days notice", "45 Days"),
        ("60 days notice", "60 Days"),
        ("90 days notice", "90 Days"),
        ("1 Month", "30 Days"),
        ("2 Months", "60 Days"),
        ("3 Months", "90 Days"),
        ("1 month notice", "30 Days"),
        ("2 months notice", "60 Days"),
        ("3 months notice", "90 Days"),
        ("Candidate can join immediately after discussion", "Immediate"),
        ("Candidate is an early joiner", "Immediate"),
        ("Candidate is serving notice currently", "Negotiable"),
        ("Notice period: negotiable", "Negotiable"),
        ("Available in 15 Days", "15 Days"),
        ("Available in 30 Days", "30 Days"),
        ("Available in 45 Days", "45 Days"),
        ("Available in 60 Days", "60 Days"),
        ("Available in 90 Days", "90 Days"),
        ("Available in 1 Month", "30 Days"),
        ("Available in 2 Months", "60 Days"),
        ("Available in 3 Months", "90 Days"),
        ("Immediate joining is possible", "Immediate"),
        ("Serving notice period", "Negotiable"),
        ("Notice: 15 Days", "15 Days"),
        ("Notice: 30 Days", "30 Days"),
        ("Negotiable notice period", "Negotiable"),
        ("The candidate is on a 1 month notice period", "30 Days"),
        ("The candidate is on a 2 month notice period", "60 Days"),
        ("The candidate is on a 3 month notice period", "90 Days"),
        ("Candidate will join immediately after notice", "Immediate"),
    ],
)
def test_extract_notice_period_normalizes_values(text, expected):
    result = extract_notice_period(text)
    assert isinstance(result, dict)
    assert result["notice_period"] == expected


def test_extract_notice_period_returns_empty_for_none_text():
    result = extract_notice_period(None)
    assert result == {"notice_period": ""}


def test_extract_notice_period_returns_empty_for_empty_text():
    result = extract_notice_period("")
    assert result == {"notice_period": ""}


def test_extract_notice_period_returns_empty_when_no_notice_period_is_found():
    result = extract_notice_period("This job description has no notice period information.")
    assert result == {"notice_period": ""}

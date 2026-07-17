from resume_parser.extractors.location_extractor import (
    LocationExtractor,
)


def test_extract_location():

    result = LocationExtractor.extract(
        "Currently based in Bangalore."
    )

    assert len(result) >= 1

    assert result[0]["location"] == "Bangalore"


def test_extract_multiple_locations():

    result = LocationExtractor.extract(
        "Worked in Bangalore, Hyderabad and Chennai."
    )

    assert len(result) >= 2


def test_extract_empty():

    assert LocationExtractor.extract("") == []


def test_extract_unknown_location():

    result = LocationExtractor.extract(
        "Working on a confidential offshore project."
    )

    assert result == []
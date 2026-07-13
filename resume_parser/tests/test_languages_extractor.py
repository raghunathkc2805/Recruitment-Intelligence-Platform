from resume_parser.extractors.languages_extractor import (
    LanguageExtractor,
)


def test_extract_language():

    result = LanguageExtractor.extract(
        "Languages: English (Fluent), Hindi (Native)"
    )

    assert len(result) >= 2

    assert result[0]["language"] in {
        "English",
        "Hindi",
    }


def test_extract_language_with_proficiency():

    result = LanguageExtractor.extract(
        "Kannada - Professional"
    )

    assert len(result) == 1

    assert result[0]["proficiency"] == "Professional"


def test_extract_empty():

    assert LanguageExtractor.extract("") == []


def test_extract_unknown_language():

    result = LanguageExtractor.extract(
        "Alien Language"
    )

    assert result == []
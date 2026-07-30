from resume_parser.extractors.achievements_extractor import (
    AchievementsExtractor,
)


def test_extract_achievements():

    text = """
    ACHIEVEMENTS

    Employee of the Year - 2023

    Received Star Performer Award

    SKILLS

    Python
    """

    result = AchievementsExtractor.extract(text)

    assert len(result) == 2

    assert "Employee of the Year - 2023" in result

    assert "Received Star Performer Award" in result


def test_extract_empty():

    assert AchievementsExtractor.extract("") == []


def test_extract_without_section():

    text = """
    Experience

    Software Engineer
    """

    assert AchievementsExtractor.extract(text) == []


def test_extract_multiple_lines():

    text = """
    Awards

    Best Innovator Award

    Best Team Player

    Education

    B.E
    """

    result = AchievementsExtractor.extract(text)

    assert len(result) == 2
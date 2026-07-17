from matching_engine.matchers.skill_matcher import (
    SkillMatcher,
)


def test_skill_match():

    result = SkillMatcher.match(
        ["Python", "Docker", "AWS"],
        ["Python", "Docker"],
    )

    assert result["score"] == 100.0

    assert len(result["matched"]) == 2

    assert result["missing"] == []


def test_skill_partial_match():

    result = SkillMatcher.match(
        ["Python"],
        ["Python", "Docker"],
    )

    assert result["score"] == 50.0

    assert "docker" in result["missing"]


def test_skill_no_requirement():

    result = SkillMatcher.match(
        ["Python"],
        [],
    )

    assert result["score"] == 100.0
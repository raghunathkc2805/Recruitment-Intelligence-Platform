from matching_engine.utils.score_utils import (
    normalize_score,
)
from matching_engine.utils.weight_utils import (
    calculate_weighted_score,
)


def test_normalize_score():

    assert normalize_score(120) == 100

    assert normalize_score(-10) == 0

    assert normalize_score(87.55) == 87.55


def test_weighted_score():

    result = calculate_weighted_score(
        {
            "skill_match": {"score": 100},
            "experience_match": {"score": 100},
            "education_match": {"score": 100},
            "designation_match": {"score": 100},
            "location_match": {"score": 100},
            "certification_match": {"score": 100},
        }
    )

    assert result == 100.0
from ranking_engine.utils.score_utils import (
    normalize_score,
)
from ranking_engine.utils.sorting_utils import (
    sort_candidates,
)


def test_normalize():

    assert normalize_score(120) == 100

    assert normalize_score(-5) == 0

    assert normalize_score(77.77) == 77.77


def test_sort():

    data = [
        {"overall_score": 20},
        {"overall_score": 90},
        {"overall_score": 50},
    ]

    ranked = sort_candidates(data)

    assert ranked[0]["overall_score"] == 90
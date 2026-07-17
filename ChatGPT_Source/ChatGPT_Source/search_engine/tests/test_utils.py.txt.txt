from search_engine.utils.query_utils import (
    QueryUtils,
)
from search_engine.utils.score_utils import (
    ScoreUtils,
)


def test_query_utils():

    assert (
        QueryUtils.normalize(
            "  Python   Docker "
        )
        == "python docker"
    )


def test_score_utils():

    score = ScoreUtils.calculate_keyword_score(
        "Python Docker",
        "Python Docker AWS",
    )

    assert score == 100.0
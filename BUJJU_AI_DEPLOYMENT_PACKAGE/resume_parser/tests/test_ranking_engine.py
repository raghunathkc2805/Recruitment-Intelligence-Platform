from resume_parser.ranking.ranking_engine import (
    RankingEngine,
)


def test_ranking_engine():

    candidates = [
        {
            "name": "Candidate A",
            "match_result": {
                "skill_match": {"score": 90},
                "experience_match": {"score":80},
                "education_match":{"score":85},
                "designation_match":{"score":80},
                "location_match":{"score":100},
                "certification_match":{"score":70},
            },
        },
        {
            "name": "Candidate B",
            "match_result": {
                "skill_match": {"score":70},
                "experience_match":{"score":70},
                "education_match":{"score":70},
                "designation_match":{"score":70},
                "location_match":{"score":70},
                "certification_match":{"score":70},
            },
        },
    ]

    ranked = RankingEngine.rank(candidates)

    assert len(ranked) == 2

    assert ranked[0]["ranking_score"] >= ranked[1]["ranking_score"]

    assert ranked[0]["rank"] == 1

    assert ranked[1]["rank"] == 2
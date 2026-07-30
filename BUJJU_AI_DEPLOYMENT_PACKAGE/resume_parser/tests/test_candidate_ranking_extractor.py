from resume_parser.extractors.candidate_ranking_extractor import (
    CandidateRankingExtractor,
)


def test_candidate_ranking():

    candidates = [
        {
            "name": "Candidate A",
            "match_result": {
                "skill_match": {"score": 95},
                "experience_match": {"score": 90},
                "education_match": {"score": 85},
                "designation_match": {"score": 80},
                "location_match": {"score": 100},
                "certification_match": {"score": 70},
            },
        },
        {
            "name": "Candidate B",
            "match_result": {
                "skill_match": {"score": 75},
                "experience_match": {"score": 70},
                "education_match": {"score": 70},
                "designation_match": {"score": 70},
                "location_match": {"score": 70},
                "certification_match": {"score": 70},
            },
        },
    ]

    result = CandidateRankingExtractor.extract(
        candidates
    )

    assert "total_candidates" in result

    assert "ranked_candidates" in result

    assert result["total_candidates"] == 2

    assert result["ranked_candidates"][0]["rank"] == 1


def test_candidate_ranking_empty():

    result = CandidateRankingExtractor.extract([])

    assert result["total_candidates"] == 0

    assert result["ranked_candidates"] == []
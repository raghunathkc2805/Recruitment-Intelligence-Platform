from matching_engine.models.candidate_match import (
    CandidateMatch,
)
from matching_engine.models.job_requirement import (
    JobRequirement,
)
from matching_engine.models.matching_result import (
    MatchingResult,
)


def test_candidate_match():

    model = CandidateMatch()

    assert model.to_dict()["overall_score"] == 0.0


def test_job_requirement():

    model = JobRequirement()

    assert model.to_dict()["experience"] == 0.0


def test_matching_result():

    model = MatchingResult()

    assert model.to_dict()["overall_score"] == 0.0
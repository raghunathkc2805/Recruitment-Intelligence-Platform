import pytest


@pytest.fixture
def candidates():

    return [
        {
            "candidate_id": "C001",
            "candidate_name": "John",
            "overall_score": 92.5,
            "experience": {
                "years": 8,
            },
        },
        {
            "candidate_id": "C002",
            "candidate_name": "Alice",
            "overall_score": 85.0,
            "experience": {
                "years": 6,
            },
        },
        {
            "candidate_id": "C003",
            "candidate_name": "David",
            "overall_score": 92.5,
            "experience": {
                "years": 10,
            },
        },
    ]
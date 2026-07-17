"""
Candidate Security Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_candidates_require_authentication():

    response = client.get("/candidates")

    assert response.status_code == 401


def test_candidate_post_requires_authentication():

    response = client.post(
        "/candidates",
        json={
            "candidate_code": "C001",
            "full_name": "John Doe",
            "email": "john@example.com",
        },
    )

    assert response.status_code == 401
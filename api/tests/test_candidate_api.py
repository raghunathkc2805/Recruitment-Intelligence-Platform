"""
Candidate API CRUD Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_candidates_endpoint_exists():

    response = client.get("/candidates")

    assert response.status_code == 401


def test_get_candidate_requires_auth():

    response = client.get(
        "/candidates/test-id",
    )

    assert response.status_code == 401


def test_create_candidate_requires_auth():

    response = client.post(
        "/candidates",
        json={
            "candidate_code": "C001",
            "full_name": "John Doe",
            "email": "john@example.com",
        },
    )

    assert response.status_code == 401


def test_update_candidate_requires_auth():

    response = client.put(
        "/candidates/test-id",
        json={
            "full_name": "Updated Name",
        },
    )

    assert response.status_code == 401


def test_delete_candidate_requires_auth():

    response = client.delete(
        "/candidates/test-id",
    )

    assert response.status_code == 401
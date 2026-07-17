"""
Candidate CRUD Route Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_candidate_routes_registered():

    response = client.get(
        "/openapi.json",
    )

    paths = response.json()["paths"]

    assert "/candidates" in paths
    assert "/candidates/{candidate_id}" in paths

    assert "get" in paths["/candidates"]
    assert "post" in paths["/candidates"]

    assert "get" in paths["/candidates/{candidate_id}"]
    assert "put" in paths["/candidates/{candidate_id}"]
    assert "delete" in paths["/candidates/{candidate_id}"]
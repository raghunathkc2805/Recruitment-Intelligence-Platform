"""
OpenAPI Validation Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_openapi_document_available():

    response = client.get("/openapi.json")

    assert response.status_code == 200


def test_auth_routes_documented():

    paths = client.get("/openapi.json").json()["paths"]

    assert "/auth/login" in paths
    assert "/auth/register" in paths


def test_candidate_routes_documented():

    paths = client.get("/openapi.json").json()["paths"]

    assert "/candidates" in paths
    assert "/candidates/{candidate_id}" in paths


def test_swagger_available():

    response = client.get("/docs")

    assert response.status_code == 200


def test_redoc_available():

    response = client.get("/redoc")

    assert response.status_code == 200
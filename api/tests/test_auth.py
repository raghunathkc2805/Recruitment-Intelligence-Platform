"""
Authentication Integration Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_openapi_contains_auth():

    response = client.get("/openapi.json")

    assert response.status_code == 200

    paths = response.json()["paths"]

    assert "/auth/login" in paths
    assert "/auth/register" in paths


def test_login_endpoint_exists():

    response = client.post(
        "/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "password",
        },
    )

    assert response.status_code == 401


def test_register_endpoint_exists():

    response = client.post(
        "/auth/register",
        json={
            "username": "integration_test_user",
            "email": "integration_test_user@example.com",
            "password": "Password@123",
            "role": "Recruiter",
        },
    )

    assert response.status_code in (
        200,
        400,
    )
"""
Application Integration Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_application_health():

    response = client.get("/health")

    assert response.status_code == 200


def test_openapi_available():

    response = client.get("/openapi.json")

    assert response.status_code == 200


def test_docs_available():

    assert client.get("/docs").status_code == 200


def test_redoc_available():

    assert client.get("/redoc").status_code == 200


def test_every_registered_router_exists():

    paths = client.get("/openapi.json").json()["paths"]

    expected_prefixes = [
        "/health",
        "/resume",
        "/jd",
        "/matching",
        "/ranking",
        "/search",
        "/candidates",
        "/auth",
    ]

    for prefix in expected_prefixes:

        assert any(
            path.startswith(prefix)
            for path in paths
        ), f"{prefix} router is not registered."
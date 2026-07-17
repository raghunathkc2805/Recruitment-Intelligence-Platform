"""
Enterprise System Validation Tests
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_health():

    assert client.get("/health").status_code == 200


def test_openapi():

    response = client.get("/openapi.json")

    assert response.status_code == 200


def test_swagger():

    assert client.get("/docs").status_code == 200


def test_redoc():

    assert client.get("/redoc").status_code == 200


def test_all_required_modules_registered():

    paths = client.get("/openapi.json").json()["paths"]

    required = {
        "Health": "/health",
        "Resume": "/resume",
        "JD": "/jd",
        "Matching": "/matching",
        "Ranking": "/ranking",
        "Search": "/search",
        "Authentication": "/auth",
        "Candidates": "/candidates",
    }

    missing = []

    for _, prefix in required.items():

        if not any(
            path.startswith(prefix)
            for path in paths
        ):
            missing.append(prefix)

    assert not missing, (
        "Missing routers: "
        + ", ".join(missing)
    )


def test_application_metadata():

    openapi = client.get("/openapi.json").json()

    assert openapi["info"]["title"] == "Recruitment Intelligence Platform"

    assert "version" in openapi["info"]
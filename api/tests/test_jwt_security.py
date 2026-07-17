"""
JWT Security Tests
"""

from __future__ import annotations

import pytest

from api.auth.jwt_handler import (
    create_access_token,
    decode_access_token,
)


def test_create_and_decode_token():

    token = create_access_token(
        {
            "sub": "1",
            "email": "admin@example.com",
            "role": "Admin",
        }
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "1"
    assert payload["email"] == "admin@example.com"
    assert payload["role"] == "Admin"


def test_invalid_token():

    with pytest.raises(Exception):

        decode_access_token(
            "invalid.jwt.token",
        )
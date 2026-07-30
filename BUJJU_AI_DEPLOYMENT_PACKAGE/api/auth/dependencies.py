"""
Authentication Dependencies
"""

from __future__ import annotations

from api.auth.security import BearerToken
from api.auth.security import CurrentUser
from api.auth.security import get_current_user
from api.auth.jwt_handler import decode_access_token


def get_current_token(
    credentials: BearerToken,
):
    return decode_access_token(credentials.credentials)


__all__ = [
    "BearerToken",
    "CurrentUser",
    "get_current_token",
    "get_current_user",
]

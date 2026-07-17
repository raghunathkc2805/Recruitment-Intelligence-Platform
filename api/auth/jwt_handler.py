"""
JWT Handler
"""

from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta

from jose import JWTError
from jose import jwt

SECRET_KEY = (
    "CHANGE_THIS_TO_A_64_CHARACTER_SECRET_KEY_BEFORE_PRODUCTION"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 30


def _create_token(
    data: dict,
    expires: timedelta,
    token_type: str,
) -> str:

    payload = data.copy()

    payload["type"] = token_type

    payload["exp"] = (
        datetime.now(UTC)
        + expires
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def create_access_token(
    data: dict,
) -> str:

    return _create_token(
        data,
        timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
        "access",
    )


def create_refresh_token(
    data: dict,
) -> str:

    return _create_token(
        data,
        timedelta(
            days=REFRESH_TOKEN_EXPIRE_DAYS,
        ),
        "refresh",
    )


def decode_access_token(
    token: str,
) -> dict:

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        if payload.get("type") != "access":
            raise ValueError(
                "Invalid token type."
            )

        return payload

    except JWTError as exc:

        raise ValueError(
            "Invalid JWT token."
        ) from exc


def decode_refresh_token(
    token: str,
) -> dict:

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        if payload.get("type") != "refresh":
            raise ValueError(
                "Invalid token type."
            )

        return payload

    except JWTError as exc:

        raise ValueError(
            "Invalid refresh token."
        ) from exc
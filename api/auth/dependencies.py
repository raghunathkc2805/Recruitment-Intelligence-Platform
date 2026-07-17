"""
Authentication Dependencies
"""

from __future__ import annotations

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from api.auth.jwt_handler import decode_access_token
from api.auth.security import BearerToken
from api.auth.security import security


def get_current_token(
    credentials: BearerToken = Depends(
        security,
    ),
):

    try:
        return decode_access_token(
            credentials.credentials,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token.",
        ) from exc
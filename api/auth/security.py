"""
Enterprise Security Layer
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from api.auth.jwt_handler import decode_access_token

oauth2_scheme = HTTPBearer(auto_error=True)

BearerToken = Annotated[
    HTTPAuthorizationCredentials,
    Depends(oauth2_scheme),
]


class CurrentUser(dict):
    """Authenticated user payload."""


def get_current_user(
    token: BearerToken,
) -> CurrentUser:

    try:

        payload = decode_access_token(
            token.credentials,
        )

        if "sub" not in payload:
            raise ValueError

        return CurrentUser(payload)

    except Exception as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required.",
        ) from exc


def require_roles(
    *roles: str,
):

    def dependency(
        current_user: CurrentUser = Depends(
            get_current_user,
        ),
    ) -> CurrentUser:

        if current_user["role"] not in roles:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions.",
            )

        return current_user

    return dependency
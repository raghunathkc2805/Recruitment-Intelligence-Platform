"""
Authentication Security
"""

from __future__ import annotations

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from jose import JWTError

from api.auth.jwt_handler import decode_access_token

security = HTTPBearer(auto_error=True)

BearerToken = HTTPAuthorizationCredentials


def get_current_user(
    credentials: BearerToken = Depends(security),
) -> dict:

    try:
        payload = decode_access_token(credentials.credentials)

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token.",
            )

        if not payload.get("sub"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token.",
            )

        return payload

    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token.",
        ) from exc


CurrentUser = dict


def require_roles(*roles: str):

    allowed = set(roles)

    def dependency(
        current_user=Depends(get_current_user),
    ) -> dict:

        if current_user.get("role") not in allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions.",
            )

        return current_user

    return dependency

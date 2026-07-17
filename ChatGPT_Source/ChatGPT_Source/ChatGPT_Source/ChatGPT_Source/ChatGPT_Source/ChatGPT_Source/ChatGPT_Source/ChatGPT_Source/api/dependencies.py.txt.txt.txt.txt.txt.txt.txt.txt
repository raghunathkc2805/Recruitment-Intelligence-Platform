"""
Database dependency injection.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.session import get_db


def get_database() -> Session:
    """
    FastAPI dependency wrapper.
    """
    return next(get_db())
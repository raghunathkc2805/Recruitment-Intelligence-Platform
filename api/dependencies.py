"""
Database dependency injection.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from database.session import get_db


DatabaseSession = Annotated[
    Session,
    Depends(get_db),
]
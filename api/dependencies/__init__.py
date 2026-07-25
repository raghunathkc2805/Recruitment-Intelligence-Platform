"""
Dependency package.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from database.session import get_db

from .audit_permission import *

DatabaseSession = Annotated[
    Session,
    Depends(get_db),
]

"""
Recruitment Intelligence Platform
Database Engine
"""

from __future__ import annotations

from sqlalchemy import create_engine

from database.settings import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    future=True,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=3600,
)
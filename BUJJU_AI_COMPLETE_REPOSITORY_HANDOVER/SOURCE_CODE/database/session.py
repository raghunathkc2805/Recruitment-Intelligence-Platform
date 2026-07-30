"""
Recruitment Intelligence Platform
Database Session
"""

from __future__ import annotations

from sqlalchemy.orm import sessionmaker

from database.engine import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
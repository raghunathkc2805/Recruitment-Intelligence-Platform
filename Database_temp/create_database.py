"""
Database Schema Creator
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.base import Base
from database.engine import engine

# Import all ORM models
import database.models  # noqa: F401

if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)

    print("Database schema created successfully.")
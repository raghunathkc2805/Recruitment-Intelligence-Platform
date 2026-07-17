from __future__ import annotations

from database.base import Base
from database.engine import engine

# Register all ORM models
import database.models  # noqa: F401


def create_database() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database schema created successfully.")


if __name__ == "__main__":
    create_database()
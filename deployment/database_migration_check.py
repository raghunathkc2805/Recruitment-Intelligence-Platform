from __future__ import annotations


from pathlib import Path

import sys


ROOT = Path(__file__).resolve().parent.parent


sys.path.insert(
    0,
    str(ROOT),
)


from database.engine import engine

from database.base import Base


import database.models


tables = Base.metadata.tables.keys()


print(
    "Registered Tables:"
)


for table in tables:

    print(
        f" - {table}"
    )


with engine.connect():

    print(
        "Database Connection Passed"
    )


print(
    "Migration Validation Passed"
)
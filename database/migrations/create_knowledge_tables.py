
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT)
    )

from database.engine import engine
from database.models.knowledge_entry import KnowledgeEntry
from database.models.knowledge_audit import KnowledgeAudit
from database.base import Base


def upgrade():

    Base.metadata.create_all(
        bind=engine,
        tables=[
            KnowledgeEntry.__table__,
            KnowledgeAudit.__table__,
        ],
    )

    print("Knowledge tables created successfully")


if __name__ == "__main__":
    upgrade()

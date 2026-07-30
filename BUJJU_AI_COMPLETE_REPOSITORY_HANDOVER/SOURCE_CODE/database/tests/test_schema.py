from database.base import Base

# Import models so metadata is populated
from database.models import *  # noqa: F401,F403


def test_metadata():

    assert Base.metadata is not None

    assert len(Base.metadata.tables) > 0
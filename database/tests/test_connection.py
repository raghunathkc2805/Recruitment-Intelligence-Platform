from database.engine import engine


def test_database_engine():

    assert engine is not None
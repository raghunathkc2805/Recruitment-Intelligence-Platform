from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

from api.config import DATABASE_URL
from api.config import DB_POOL_SIZE
from api.config import DB_MAX_OVERFLOW
from api.config import DB_POOL_TIMEOUT
from api.config import DB_POOL_RECYCLE


engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=DB_POOL_SIZE,
    max_overflow=DB_MAX_OVERFLOW,
    pool_timeout=DB_POOL_TIMEOUT,
    pool_recycle=DB_POOL_RECYCLE,
    pool_pre_ping=True,
    future=True,
)

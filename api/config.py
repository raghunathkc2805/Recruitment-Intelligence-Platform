from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Recruitment Intelligence Platform"
    APP_ENV: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    REDIS_URL: str = "redis://redis:6379/0"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

REDIS_HOST="localhost"
REDIS_PORT=6379
REDIS_DB=0
CACHE_DEFAULT_TTL=3600


MEMORY_CACHE_SIZE=5000
MEMORY_CACHE_TTL=300


DEFAULT_PAGE_SIZE = 50
MAX_PAGE_SIZE = 500
QUERY_TIMEOUT_SECONDS = 30


DB_POOL_SIZE = 20
DB_MAX_OVERFLOW = 40
DB_POOL_TIMEOUT = 30
DB_POOL_RECYCLE = 1800


GZIP_ENABLED = True
GZIP_MINIMUM_SIZE = 1024
GZIP_LEVEL = 6


TRACE_ENABLED=True
TRACE_EXPORT=True


OTEL_ENABLED=True
OTEL_EXPORTER="otlp"
OTEL_SERVICE_NAME="bujju-ai"


PROMETHEUS_ENABLED=True
PROMETHEUS_ENDPOINT="/metrics"


HEALTH_ENDPOINT="/health"
READINESS_ENDPOINT="/ready"
LIVENESS_ENDPOINT="/live"


DATABASE_URL = settings.DATABASE_URL
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM


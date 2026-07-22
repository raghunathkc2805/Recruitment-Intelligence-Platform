from contextvars import ContextVar

request_id = ContextVar(
    "request_id",
    default="-",
)

user_id = ContextVar(
    "user_id",
    default="-",
)

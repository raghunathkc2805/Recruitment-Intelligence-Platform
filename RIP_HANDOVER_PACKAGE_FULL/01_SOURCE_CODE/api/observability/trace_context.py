from contextvars import ContextVar

trace_id = ContextVar("trace_id", default=None)
span_id = ContextVar("span_id", default=None)
parent_span_id = ContextVar("parent_span_id", default=None)

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

def instrument(app):

    FastAPIInstrumentor.instrument_app(app)

    RequestsInstrumentor().instrument()

    HTTPXClientInstrumentor().instrument()

from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

def create_exporter():

    exporter = OTLPSpanExporter()

    return BatchSpanProcessor(exporter)

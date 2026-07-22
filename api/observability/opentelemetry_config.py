from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider

from api.observability.resource import build_resource
from api.observability.exporters import create_exporter

def configure_tracing():

    provider = TracerProvider(
        resource=build_resource()
    )

    provider.add_span_processor(
        create_exporter()
    )

    trace.set_tracer_provider(provider)

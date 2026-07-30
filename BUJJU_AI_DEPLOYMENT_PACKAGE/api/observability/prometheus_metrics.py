from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

def metrics_response():

    return (
        generate_latest(),
        CONTENT_TYPE_LATEST
    )

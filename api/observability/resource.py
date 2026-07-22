from opentelemetry.sdk.resources import Resource

def build_resource():

    return Resource.create({

        "service.name":"bujju-ai",

        "service.namespace":"recruitment-intelligence",

        "service.version":"1.0.0",

        "deployment.environment":"production"

    })

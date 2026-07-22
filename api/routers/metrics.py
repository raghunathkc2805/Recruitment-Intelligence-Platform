from fastapi import APIRouter
from fastapi.responses import Response

from api.observability.prometheus_metrics import metrics_response

router = APIRouter(tags=["Metrics"])

@router.get("/metrics")

def metrics():

    data,ctype = metrics_response()

    return Response(
        content=data,
        media_type=ctype
    )

from fastapi import APIRouter

from .executive_models import (
    ExecutiveMetricsRequest,
    ExecutiveMetricsResponse
)

from .executive_service import (
    BujjuExecutiveService
)


router = APIRouter(
    prefix="/bujju-ai/executive",
    tags=["Bujju AI Executive"]
)


service = BujjuExecutiveService()


@router.post(
    "/dashboard",
    response_model=ExecutiveMetricsResponse
)
def executive_dashboard(
    request: ExecutiveMetricsRequest
):

    return service.generate(request)

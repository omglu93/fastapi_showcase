from fastapi import APIRouter

from app.schemas.calculation import CPUResponse, CPURequest
import app.services.services as services


calc_router = APIRouter()


@calc_router.post("/", response_model=CPUResponse)
def post_cpu_operation(data_in: CPURequest):

    number = services.cpu_intensive_operations(data_in.data.number)

    return CPUResponse(results=number)


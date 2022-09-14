from fastapi import APIRouter

import app.schemas.calculation as calculation
import app.services.services as services


calc_router = APIRouter()


@calc_router.post("/", response_model=calculation.CPUResponse)
def post_check_if_prime(data_in: calculation.CPURequest):

    number = services.cpu_intensive_operations(data_in.data.number)

    return calculation.CPUResponse(results=number)


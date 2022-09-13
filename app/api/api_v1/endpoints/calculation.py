from fastapi import APIRouter

import app.schemas.calculation as calculation
import app.services.services as services


calc_router = APIRouter()


@calc_router.post("/", response_model=calculation.PrimeResponse)
def post_check_if_prime(data_in: calculation.PrimeRequest):

    number = services.is_prime(data_in.data.number)

    return calculation.PrimeResponse(bool=number)


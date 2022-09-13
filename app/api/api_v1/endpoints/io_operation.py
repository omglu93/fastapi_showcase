from fastapi import APIRouter

import app.schemas.io_operation as io_operation
import app.services.services as services


io_router = APIRouter()


@io_router.get("/", response_model=io_operation.IoOperationResult)
def get_io_operation_result():

    result = services.io_operation()

    return io_operation.IoOperationResult(data=result)

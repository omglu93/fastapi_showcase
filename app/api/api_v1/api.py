from fastapi import APIRouter
from app.api.api_v1.endpoints.calculation import calc_router
from app.api.api_v1.endpoints.io_operation import io_router
from app.api.api_v1.endpoints.order import order_router

router = APIRouter()

router.include_router(calc_router, prefix="/prime")
router.include_router(io_router, prefix="/io-operation")
router.include_router(order_router, prefix="/database-operation")

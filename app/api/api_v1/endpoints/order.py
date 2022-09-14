from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from app.crud.order import orders
from app.api.deps import get_db
from app.schemas.order import CustomerOrderCreate,\
    CustomerOrderResult


order_router = APIRouter()


@order_router.post("/", response_model=CustomerOrderResult)
def create_new_user(*,
                    db: Session = Depends(get_db),
                    order_in: CustomerOrderCreate) -> Any:

    return orders.create(db, obj_in=order_in).__dict__

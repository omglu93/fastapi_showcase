from .base import CRUDBase
from app.models.order import CustomerOrders
from app.schemas.order import CustomerOrderCreate

from sqlalchemy.orm import Session


class CRUDOrders(CRUDBase[CustomerOrders, CustomerOrderCreate]):

    @staticmethod
    def create(db: Session, *,
               obj_in: CustomerOrderCreate) -> CustomerOrders:

        obj_schema = CustomerOrders(
            customer_name=obj_in.customer_name,
            item=obj_in.item,
            cost=obj_in.cost,
            order_status=0)

        db.add(obj_schema)
        db.commit()
        db.refresh(obj_schema)

        return obj_schema


orders = CRUDOrders(CustomerOrders)

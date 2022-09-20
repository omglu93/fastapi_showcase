from pydantic import BaseModel


class CustomerOrderCreate(BaseModel):
    customer_name: str
    item: str
    cost: float

    class Config:
        orm_mode = True


class CustomerOrderResult(BaseModel):
    cost: float
    customer_name: str
    id: int
    item: str
    order_status: int


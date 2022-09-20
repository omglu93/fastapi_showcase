from sqlalchemy import String, Integer, Column, Float, ForeignKey
from app.models.base import BaseClass


class CustomerOrders(BaseClass):

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(50), nullable=False, unique=False)
    item = Column(String(50), nullable=False, unique=False)
    cost = Column(Float(), nullable=False, unique=False)
    order_status = Column(Integer(), nullable=False, unique=False)

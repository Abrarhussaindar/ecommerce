from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

class Order(BaseModel):
    orderid: str
    quantity: int
    productid: str
    price: float
    status: str

    class Config:
        orm_mode = True

class Cart(BaseModel):
    cartid: uuid.UUID
    orders: Optional[List[Order]] = None
    total_quantity: int
    total_price: float
    created_at: datetime
    update_at: datetime


    class Config:
        orm_mode = True


class CartCreateModel(BaseModel):
    orders: Optional[List[Order]] = None
    total_quantity: int
    total_price: float

    class Config:
        orm_mode = True


class CartUpdateModel(BaseModel):
    cartid: uuid.UUID
    orders: Optional[List[Order]] = None
    total_quantity: int
    total_price: float

    class Config:
        orm_mode = True
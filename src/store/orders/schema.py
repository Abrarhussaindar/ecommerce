from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class Product(BaseModel):
    orderid: uuid.UUID
    productid: str
    userid: str
    paymentid: str
    category: str
    status: str
    quantity: int
    price: float
    seller_uid: str
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True  # To enable compatibility with ORM models like SQLModel

class ProductCreateModel(BaseModel):
    productid: str
    userid: str
    paymentid: str
    category: str
    status: str
    quantity: int
    price: float
    seller_uid: str

class ProductUpdateModel(BaseModel):
    productid: Optional[str]  # Optional since you might not update every field
    userid: Optional[str]
    paymentid: Optional[str]
    category: Optional[str]
    status: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    seller_uid: Optional[str]

    class Config:
        orm_mode = True  # To enable compatibility with ORM models like SQLModel

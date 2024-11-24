from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class Product(BaseModel):
    productid: uuid.UUID
    name: str
    description: str
    category: str
    sub_category: str
    quantity: int
    price: float
    rating: str
    seller_uid: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # To enable compatibility with ORM models like SQLModel

class ProductCreateModel(BaseModel):
    name: str
    description: str
    category: str
    sub_category: str
    quantity: int
    price: float
    rating: str
    seller_uid: str

class ProductUpdateModel(BaseModel):
    name: Optional[str]  # Optional because not all fields need to be updated
    description: Optional[str]
    category: Optional[str]
    sub_category: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    rating: Optional[str]
    seller_uid: Optional[str]

    class Config:
        orm_mode = True  # To enable compatibility with ORM models like SQLModel

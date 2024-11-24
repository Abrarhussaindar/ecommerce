from pydantic import BaseModel
import uuid
from datetime import datetime

class Product(BaseModel):
    uid: uuid.UUID
    name: str
    description: str
    category: str
    sub_category: str
    quantity: int
    price: float
    rating: str
    seller_uid: str
    created_at: datetime
    update_at: datetime

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
    name: str
    description: str
    category: str
    sub_category: str
    quantity: int
    price: float
    rating: str
    seller_uid: str
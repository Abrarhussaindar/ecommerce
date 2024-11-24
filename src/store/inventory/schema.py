from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

class Product(BaseModel):
    productid: str
    quantity: int

    class Config:
        orm_mode = True

class Inventory(BaseModel):
    inventoryid: uuid.UUID
    category: str
    quantity: int
    seller_uid: str
    created_at: datetime
    update_at: datetime
    products: Optional[List[Product]] = None

    class Config:
        orm_mode = True

class InventoryCreateModel(BaseModel):
    category: str
    quantity: int
    seller_uid: str
    products: Optional[List[Product]] = None

    class Config:
        orm_mode = True


class InventoryUpdateModel(BaseModel):
    inventoryid: uuid.UUID
    category: Optional[str]
    quantity: Optional[int]
    seller_uid: Optional[str]
    products: Optional[List[Product]] = None

    class Config:
        orm_mode = True
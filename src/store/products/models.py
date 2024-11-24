from sqlmodel import SQLModel, Field, Column
from datetime import  datetime
import uuid
import sqlalchemy.dialects.postgresql as pg

class Product(SQLModel, table=True):
    __tablename__ = "products"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4()
        )
    )
    name: str
    description: str
    category: str
    sub_category: str
    quantity: int
    price: float
    rating: str
    seller_uid: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<Product {self.name}>"
from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import uuid
import sqlalchemy.dialects.postgresql as pg

class Order(SQLModel, table=True):
    __tablename__ = "orders"

    orderid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default_factory=uuid.uuid4  # Corrected to default_factory
        )
    )
    productid: str = Field(nullable=False)
    userid: str = Field(nullable=False)
    paymentid: str = Field(nullable=False)
    category: str = Field(nullable=False)
    status: str = Field(nullable=False)
    quantity: int = Field(nullable=False)
    price: float = Field(nullable=False)
    seller_uid: str = Field(nullable=False)
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.utcnow)
    )
    update_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    )

    def __repr__(self):
        return f"<Order {self.orderid}>"

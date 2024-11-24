from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import uuid
import sqlalchemy.dialects.postgresql as pg

class Cart(SQLModel, table=True):
    __tablename__ = "cart"  # Changed table name from 'orders' to 'inventory' to reflect the model purpose

    cartid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default_factory=uuid.uuid4
        )
    )
    orders: list[dict] = Field(
        sa_column=Column(pg.ARRAY(pg.JSONB), nullable=True)  # Keeping it flexible with JSONB array
    )
    total_price: float = Field(nullable=False)
    total_quantity: int = Field(nullable=False)
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.utcnow)
    )
    update_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    )


    def __repr__(self):
        return f"<Cart {self.cartid}>"

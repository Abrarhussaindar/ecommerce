from sqlmodel.ext.asyncio.session import AsyncSession
from .models import Order

class OrderService:
    async def create_new_order(self, session: AsyncSession) -> Order:
        pass

    async def get_order_by_id(self, session: AsyncSession):
        pass

    async def get_product_by_userid(self, session: AsyncSession):
        pass

    async def update_order(self, session: AsyncSession):
        pass

    async def delete_order(self, session: AsyncSession):
        pass
from sqlmodel.ext.asyncio.session import AsyncSession
from .models import Inventory

class InventoryService:
    async def create_new_inventory(self, session: AsyncSession) -> Inventory:
        pass

    async def add_products(self, session: AsyncSession):
        pass

    async def get_product(self, session: AsyncSession):
        pass

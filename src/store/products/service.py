from sqlmodel.ext.asyncio.session import AsyncSession
from .models import Product

class ProductService:
    async def create_new_product(self, session: AsyncSession) -> Product:
        pass

    async def get_product_by_id(self, session: AsyncSession):
        pass

    async def get_product_by_category(self, session: AsyncSession):
        pass

    async def update_product(self, session: AsyncSession):
        pass

    async def delete_product(self, session: AsyncSession):
        pass


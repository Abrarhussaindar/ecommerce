from sqlmodel.ext.asyncio.session import AsyncSession
from .models import Cart

class CartServices:
    async def create_new_cart(self, session: AsyncSession) -> Cart:
        pass

    async def get_cart(self, session: AsyncSession):
        pass
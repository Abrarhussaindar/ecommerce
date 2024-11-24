from typing import Optional, List

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel.ext.asyncio.session import AsyncSession
from .models import Product
from .schema import ProductCreateModel
from datetime import datetime
import uuid
from sqlmodel import select


class ProductService:
    async def create_new_product(self, product_data: ProductCreateModel, session: AsyncSession) -> Product:
        product_data_dict = product_data.dict()
        product_data_dict['productid'] = uuid.uuid4()
        product_data_dict['created_at'] = datetime.utcnow()
        product_data_dict['updated_at'] = datetime.utcnow()
        new_product = Product(**product_data_dict)

        try:
            session.add(new_product)
            await session.commit()
            await session.refresh(new_product)
            return Product.from_orm(new_product)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def get_product_by_id(self, productid: str, session: AsyncSession) -> Optional[Product]:
        statement = select(Product).where(Product.productid == productid)
        try:
            res = await session.execute(statement)
            return res.scalar_one_or_none()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def get_all_products(self, session: AsyncSession) -> List[Product]:
        statement = select(Product)
        try:
            res = await session.execute(statement)
            products = res.scalars().all()
            return products
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def get_product_by_category(self, cate: str, session: AsyncSession) -> List[Product]:
        statement = select(Product).where(Product.category == cate)
        try:
            res = await session.execute(statement)
            products = res.scalars().all()
            return products
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def update_product(self, session: AsyncSession):
        pass

    async def delete_product(self, productid: str, session: AsyncSession) -> Optional[dict] :
        product_to_delete = await self.get_product_by_id(productid, session)
        if product_to_delete is not None:
            try:
                await session.delete(product_to_delete)
                await session.commit()
                return {"message": "Product deleted successfully"}
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
        return None


from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.store.products.schema import ProductCreateModel
from src.store.products.service import ProductService
from src.database.db import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.store.products.models import Product

product_router = APIRouter(
    prefix="/product"
)

product_service = ProductService()

@product_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Product)
async def create_product(product_data: ProductCreateModel, session: AsyncSession = Depends(get_session)):
    try:
        new_product = await product_service.create_new_product(product_data, session)
        return new_product
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server error: {str(e)}"
        )
@product_router.get("/all")
async def get_all_products(session: AsyncSession = Depends(get_session)):
    try:
        products = await product_service.get_all_products(session)
        return products
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error {str(e)}"
        )

@product_router.get("/{productid}", status_code=status.HTTP_200_OK)
async def get_product(productid: str, session: AsyncSession = Depends(get_session)):
    try:
        product = await product_service.get_product_by_id(productid, session)
        if product:
            return product
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not found")
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}"
        )



@product_router.get("/category/{cate}", status_code=status.HTTP_200_OK)
async def get_product_by_category(cate: str, session: AsyncSession = Depends(get_session)):
    try:
        products = await product_service.get_product_by_category(cate, session)
        return products
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error {str(e)}"
        )

@product_router.put("/update/{uid}", status_code=status.HTTP_200_OK)
async def update_product(uid: str):
    return {"message": "coming soon..."}

@product_router.delete("/{productid}", status_code=status.HTTP_200_OK)
async def delete_product(productid: str, session: AsyncSession = Depends(get_session)):
    try:
        product_to_delete = await product_service.delete_product(productid, session)
        if product_to_delete:
            return {"message": "Product deleted successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error {str(e)}"
        )


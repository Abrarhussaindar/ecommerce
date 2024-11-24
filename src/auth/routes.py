from fastapi import APIRouter, status, Depends, HTTPException
from src.database.db import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
auth_router = APIRouter(
    prefix="/auth"
)

@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(session: AsyncSession = Depends(get_session)):
    return {"message": "registered"}

@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(session: AsyncSession = Depends(get_session)):
    pass





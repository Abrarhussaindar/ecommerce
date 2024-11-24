from src.database.db import get_session
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import List
from src.users.models import User
from src.users.service import UserService
from src.users.schemas import UserUpdateModel
from sqlalchemy.exc import SQLAlchemyError  # Import for handling DB exceptions

user_router = APIRouter(
    prefix="/user"
)
user_service = UserService()

@user_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_new_user(user_data: User, session: AsyncSession = Depends(get_session)):
    try:
        new_user = await user_service.create_new_user(user_data, session)
        return new_user
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error occurred: {str(e)}"
        )




@user_router.get("/all", response_model=List[User])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    try:
        users = await user_service.get_all_users(session)
        return users
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error occurred: {str(e)}"
        )
@user_router.get("/{uid}")
async def get_user_by_uid(uid: str, session: AsyncSession = Depends(get_session)):
    try:
        user = await user_service.get_user(uid, session)
        if user:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error occurred: {str(e)}"
        )
        
        
@user_router.put("/update/{uid}", status_code=status.HTTP_200_OK, response_model=User)
async def update_user(uid: str, user_update_data: UserUpdateModel, session: AsyncSession = Depends(get_session)):
    try:
        updated_user = await user_service.update_user(uid, user_update_data, session)
        if updated_user:
            return updated_user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error occurred: {str(e)}"
        )

@user_router.delete("/{uid}", status_code=status.HTTP_200_OK, response_model=User)
async def delete_user(uid: str, session: AsyncSession = Depends(get_session)):
    try:
        user_to_delete = await user_service.delete_user(uid, session)
        if user_to_delete:
            return {"message": "user deleted."}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error occurred: {str(e)}"
        )

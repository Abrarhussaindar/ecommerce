from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import UserCreateModel, UserUpdateModel
from sqlmodel import select
from .models import User
from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError

class UserService:
    async def create_new_user(self, user_data: UserCreateModel, session: AsyncSession) -> User:
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        try:
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            # Handle the exception, log it, and rollback if needed
            await session.rollback()
            raise e  # Or handle it appropriately

    async def get_user(self, user_uid: str, session: AsyncSession) -> Optional[User]:
        statement = select(User).where(User.uid == user_uid)
        try:
            result = await session.execute(statement)
            return result.scalar_one_or_none()  # Use scalar_one_or_none() to get a single result
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def get_all_users(self, session: AsyncSession) -> List[User]:
        statement = select(User)  # Using SQLAlchemy ORM query instead of raw SQL
        try:
            result = await session.execute(statement)
            users = result.scalars().all()  # Use scalars() to extract the results
            return users
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def update_user(self, user_uid: str, update_data: UserUpdateModel, session: AsyncSession) -> Optional[User]:
        user_to_update = await self.get_user(user_uid, session)
        if user_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v in update_data_dict.items():
                setattr(user_to_update, k, v)
            try:
                await session.commit()
                await session.refresh(user_to_update)
                return user_to_update
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
        return None

    async def delete_user(self, user_uid: str, session: AsyncSession) -> Optional[dict]:
        user_to_delete = await self.get_user(user_uid, session)
        if user_to_delete is not None:
            try:
                await session.delete(user_to_delete)
                await session.commit()
                return {"message": "User deleted successfully"}
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
        return None

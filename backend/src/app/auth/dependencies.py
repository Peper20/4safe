import uuid


from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers
from sqlalchemy.ext.asyncio import AsyncSession


from app.services.db_service.sql_alchemy import get_async_session
from app.services.db_service.sql_alchemy.models.auth import User

from .service import auth_backend, UserManager




async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
	yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)

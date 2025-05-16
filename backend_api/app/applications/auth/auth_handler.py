import datetime

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.status import HTTP_400_BAD_REQUEST

from applications.auth.password_handler import PasswordEncrypt
from applications.database.session_dependencies import get_async_session
from applications.settings import settings
from applications.users.crud import get_user_by_email


class AuthHandler:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM
    async def get_login_token_pairs(self, data: OAuth2PasswordRequestForm, session: AsyncSession = get_async_session):
        user_email = data.username
        user_password = data.password
        user = await get_user_by_email(user_email, session)

        if not user:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail='User not found'
            )
        is_valid_password = await PasswordEncrypt.verify_password(user_password, user.hashed_password)
        if not is_valid_password:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Incorrect password'
            )

auth_handler = AuthHandler()
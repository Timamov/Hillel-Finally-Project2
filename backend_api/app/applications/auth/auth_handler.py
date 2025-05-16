from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from applications.database.session_dependencies import get_async_session
from applications.settings import settings


class AuthHandler:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM
    async def get_login_token_pairs(self, data: OAuth2PasswordRequestForm, session: AsyncSession = get_async_session):
        pass

auth_handler = AuthHandler()
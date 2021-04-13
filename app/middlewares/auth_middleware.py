import base64

from database import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp.web import Response, Request, middleware
from utils.custom_exception import ExecutionException


@middleware
async def auth_middleware(request: Request, handler) -> Response:
    """Layer checks user credentials"""
    if await _check_auth(request):
        return await handler(request)
    message = 'Для выполнения запроса необходимо авторизваться через Basic Auth'
    raise ExecutionException('auth-error', message, 401)


async def _check_auth(request: Request) -> bool:
    """Method checks Basic Auth"""
    authorization = request.headers.get('Authorization')
    if authorization and authorization.lower().startswith('basic '):
        credentials = base64.b64decode(authorization[6:]).decode('utf-8')
        nickname, password = credentials.split(':')
        user: User = await _get_user(nickname, password, request)
        if user:
            request['user_id'] = user.id
            return True
    return False


async def _get_user(nickname: str, password: str, request: Request) -> User:
    """Get user from database by nickname and password"""
    session: AsyncSession = request['postgres_session']
    result = await session.execute(
        select(User).where(
            User.nickname == nickname,
            User.password == password
        )
    )
    return result.scalar()


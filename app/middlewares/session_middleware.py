from database import PGContextSession
from aiohttp.web import Response, Request, middleware


@middleware
async def session_middleware(request: Request, handler) -> Response:
    """Layer opens database connection during handling request"""
    async with PGContextSession() as session:
        request['postgres_session'] = session
        response = await handler(request)
    return response

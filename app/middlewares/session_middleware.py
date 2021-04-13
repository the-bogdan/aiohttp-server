from database.connection import context_session
from aiohttp.web import Response, Request, middleware


@middleware
async def session_middleware(request: Request, handler) -> Response:
    """Layer opens database connection during handling request"""
    async with context_session() as session:
        request['postgres_session'] = session
        response = await handler(request)
    return response

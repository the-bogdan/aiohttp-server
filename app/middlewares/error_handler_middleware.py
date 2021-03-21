from logger import logger
from utils.custom_exception import ExecutionException
from aiohttp.web import Response, Request, middleware, json_response


@middleware
async def error_handler_middleware(request: Request, handler) -> Response:
    """Layer handles errors and sends readable response"""
    try:
        return await handler(request)
    except ExecutionException as e:
        return json_response(
            status=e.http_code,
            data={'error': e.error, 'message': e.message}
        )
    except BaseException as e:
        logger.error(e, exc_info=True)
        return json_response(
            status=500,
            data={'error': f'{e.__class__.__name__}', 'message': str(e)}
        )

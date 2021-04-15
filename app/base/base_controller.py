from .request_data import RequestData
from .base_validator import BaseValidator
from utils.serializer import ResponseSerializer
from .base_business_model import BaseBusinessModel
from utils.custom_exception import ExecutionException

from aiohttp.web import Request, Response


class BaseController:
    """
    Base controller implements base CRUD actions for
    all database models in this module
    """

    @classmethod
    async def get_by_id(cls, request: Request) -> Response:
        """Get entity by id"""
        request_data = await RequestData.create(request)
        await BaseValidator.get_by_id(request_data)

        bm = BaseBusinessModel(request_data)
        entity = await bm.get_by_id()
        return ResponseSerializer() \
            .serialize_object(entity) \
            .response

    @classmethod
    async def get(cls, request: Request) -> Response:
        """Get filtered and ordered list of entities"""
        request_data = await RequestData.create(request)
        await BaseValidator.get(request_data)

        bm = BaseBusinessModel(request_data)
        entities = await bm.search()
        return ResponseSerializer() \
            .serialize_collection(entities) \
            .response

    @classmethod
    async def post(cls, request: Request) -> Response:
        """Create new entity"""
        request_data = await RequestData.create(request)
        await BaseValidator.post(request_data)

        bm = BaseBusinessModel(request_data)
        entity = await bm.create()
        return ResponseSerializer() \
            .serialize_object(entity) \
            .response

    @classmethod
    async def put(cls, request: Request) -> Response:
        """Update entity"""
        request_data = await RequestData.create(request)
        await BaseValidator.put(request_data)

        bm = BaseBusinessModel(request_data)
        entity = await bm.update()
        return ResponseSerializer() \
            .serialize_object(entity) \
            .response

    @classmethod
    async def delete(cls, request: Request) -> Response:
        """Delete entity"""
        request_data = await RequestData.create(request)
        await BaseValidator.delete(request_data)

        bm = BaseBusinessModel(request_data)
        entity = await bm.delete()
        return ResponseSerializer() \
            .serialize_object(entity) \
            .response

    @classmethod
    async def patch(cls, request: Request) -> None:
        """Not implemented"""
        cls._raise_not_implemented()

    @staticmethod
    def _raise_not_implemented() -> None:
        """
        This exception will be handled in error_middleware and will return
        response 405 with error and massage in json body
        """
        raise ExecutionException(
            error='not-implemented',
            message='HTTP method not implemented for entity',
            http_code=205
        )

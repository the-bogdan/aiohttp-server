from aiohttp.web import Request, Response
from utils.serializer import ResponseSerializer
from business_models import OrdersBusinessModel
from utils.abstract_controller import AbstractController


class OrdersController(AbstractController):
    """Class defines handlers for order instance"""
    entity_route = '/orders'

    @classmethod
    async def get(cls, request: Request) -> Response:
        """Get user entity by id"""
        bm = OrdersBusinessModel(request)
        user = await bm.get()
        return ResponseSerializer().serialize_object(user).response

    @classmethod
    async def post(cls, request: Request) -> Response:
        """Get user entities filtered by fields and optional with orders and products entities in included"""
        bm = OrdersBusinessModel(request)
        users, included = await bm.post()
        return ResponseSerializer() \
            .serialize_collection(users) \
            .append_collection_in_included(included) \
            .response

    @classmethod
    async def put(cls, request: Request) -> Response:
        """Create user"""
        bm = OrdersBusinessModel(request)
        user = await bm.put()
        return ResponseSerializer() \
            .serialize_object(user) \
            .response

    @classmethod
    async def patch(cls, request: Request) -> Response:
        """Update user"""
        bm = OrdersBusinessModel(request)
        user = await bm.patch()
        return ResponseSerializer() \
            .serialize_object(user) \
            .response

    @classmethod
    async def delete(cls, request: Request) -> Response:
        """Delete user"""
        bm = OrdersBusinessModel(request)
        user = await bm.delete()
        return ResponseSerializer() \
            .serialize_object(user) \
            .response

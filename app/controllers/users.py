from aiohttp.web import Request, Response
from business_models import UsersBusinessModel
from utils.serializer import ResponseSerializer
from utils.abstract_controller import AbstractController


class UsersController(AbstractController):
    """Class defines handlers for user instance"""
    entity_route = '/users'

    @classmethod
    async def get(cls, request: Request) -> Response:
        """Get user entity by id"""
        bm = UsersBusinessModel(request)
        user = await bm.get()
        return ResponseSerializer().serialize_object(user).response

    @classmethod
    async def post(cls, request: Request) -> Response:
        """Get user entities filtered by fields and optional with orders and products entities in included"""
        bm = UsersBusinessModel(request)
        users, included = await bm.post()
        return ResponseSerializer() \
            .serialize_collection(users) \
            .append_collection_in_included(included) \
            .response

    @classmethod
    async def put(cls, request: Request) -> Response:
        """Create user"""
        bm = UsersBusinessModel(request)
        user = await bm.put()
        return ResponseSerializer() \
            .serialize_object(user) \
            .response

    @classmethod
    async def patch(cls, request: Request) -> Response:
        """Update user"""
        bm = UsersBusinessModel(request)
        user = await bm.patch()
        return ResponseSerializer() \
            .serialize_object(user) \
            .response

    @classmethod
    async def delete(cls, request: Request) -> Response:
        """Delete user"""
        bm = UsersBusinessModel(request)
        user = await bm.delete()
        return ResponseSerializer() \
            .serialize_object(user) \
            .response

    @classmethod
    async def follow(cls, request: Request) -> Response:
        """Follow user"""
        bm = UsersBusinessModel(request)
        user_relation = await bm.follow()
        return ResponseSerializer() \
            .serialize_object(user_relation) \
            .response

    @classmethod
    async def followers(cls, request: Request) -> Response:
        """Follow user"""
        bm = UsersBusinessModel(request)
        users = await bm.followers()
        return ResponseSerializer() \
            .serialize_collection(users) \
            .response

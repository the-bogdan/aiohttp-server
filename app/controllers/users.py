# from business_models import UsersBusinessModel
# from utils.serializer import ResponseSerializer
# from aiohttp.web import Request, Response, View
#
#
# class UsersController(View):
#     """Class defines handlers for user instance"""
#
#     async def get(self) -> Response:
#         """Get user entity by id"""
#         bm = UsersBusinessModel(self.request)
#         user = await bm.get()
#         return ResponseSerializer().serialize_object(user).response
#
#     async def post(self) -> Response:
#         """Get user entities filtered by fields and optional with orders and products entities in included"""
#         bm = UsersBusinessModel(self.request)
#         users, included = await bm.search()
#         return ResponseSerializer() \
#             .serialize_collection(users) \
#             .append_collection_in_included(included) \
#             .response
#
#     async def put(self) -> Response:
#         """Create user"""
#         bm = UsersBusinessModel(self.request)
#         user = await bm.create()
#         return ResponseSerializer() \
#             .serialize_object(user) \
#             .response
#
#     async def patch(self) -> Response:
#         """Update user"""
#         bm = UsersBusinessModel(self.request)
#         user = await bm.update()
#         return ResponseSerializer() \
#             .serialize_object(user) \
#             .response
#
#     async def delete(self) -> Response:
#         """Delete user"""
#         bm = UsersBusinessModel(self.request)
#         user = await bm.delete()
#         return ResponseSerializer() \
#             .serialize_object(user) \
#             .response
#
#     @classmethod
#     async def follow(cls, request: Request) -> Response:
#         """Follow user"""
#         bm = UsersBusinessModel(request)
#         user_relation = await bm.follow()
#         return ResponseSerializer() \
#             .serialize_object(user_relation) \
#             .response
#
#     @classmethod
#     async def followers(cls, request: Request) -> Response:
#         """Follow user"""
#         bm = UsersBusinessModel(request)
#         users = await bm.followers()
#         return ResponseSerializer() \
#             .serialize_collection(users) \
#             .response

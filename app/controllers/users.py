from validators import UserValidator
from aiohttp.web import Response, Request
from base import BaseController, RequestData
from business_models import UsersBusinessModel
from utils.serializer import ResponseSerializer


class UsersController(BaseController):
    """Class defines handlers for user instance"""

    @classmethod
    async def get_by_id(cls, request: Request) -> Response:
        """
        @api {get} /users/{id} Get user by id
        @apiName UsersGetByID
        @apiGroup Users
        @apiDescription Get user by id if exists else 400

        @apiSuccessExample response body example
        {
          "data": {
            "id": 2,
            "model_type": "users",
            "attributes": {
              "id": "2",
              "first_name": "admin",
              "last_name": "admin",
              "family_name": null,
              "created_at": "2021-04-15 06:42:08",
              "created_by": "1",
              "updated_at": "2021-04-15 06:42:08",
              "updated_by": "1",
              "deleted_at": null,
              "deleted_by": null
            }
          },
          "included": {}
        }
        """
        return await super(UsersController, cls).get_by_id(request)

    @classmethod
    async def get(cls, request: Request) -> Response:
        """
        @api {get} /users Get users array
        @apiName UsersGet
        @apiGroup Users
        @apiDescription Get all users in array

        @apiSuccessExample response body example
        {
          "data": [
            {
              "id": 1,
              "model_type": "users",
              "attributes": {
                "id": "1",
                "first_name": "Система",
                "last_name": "System",
                "family_name": null,
                "created_at": "2021-04-15 06:42:08",
                "created_by": "1",
                "updated_at": "2021-04-15 06:42:08",
                "updated_by": "1",
                "deleted_at": null,
                "deleted_by": null
              }
            },
            {
              "id": 2,
              "model_type": "users",
              "attributes": {
                "id": "2",
                "first_name": "admin",
                "last_name": "admin",
                "family_name": null,
                "created_at": "2021-04-15 06:42:08",
                "created_by": "1",
                "updated_at": "2021-04-15 06:42:08",
                "updated_by": "1",
                "deleted_at": null,
                "deleted_by": null
              }
            }
          ],
          "included": {}
        }

        """
        return await super(UsersController, cls).get(request)

    @classmethod
    async def post(cls, request: Request) -> Response:
        """
        @api {post} /users Crate new user
        @apiName UsersCreate
        @apiGroup Users
        @apiDescription Create new users

        @apiExample json request body example
        {
          "data": {
            "attributes": {
              "first_name": "Bogdan",
              "last_name": "Parshintsev",
              "nickname": "asdf",
              "password": "asdfasdf"
            }
          }
        }

        @apiSuccessExample response body example
        {
          "data": {
            "id": 4,
            "model_type": "users",
            "attributes": {
              "id": "4",
              "first_name": "Bogdan",
              "last_name": "Parshintsev",
              "family_name": null,
              "created_at": "2021-04-15 11:35:19",
              "created_by": "2",
              "updated_at": "2021-04-15 11:35:19",
              "updated_by": null,
              "deleted_at": null,
              "deleted_by": null
            }
          },
          "included": {}
        }
        """
        request_data = await RequestData.create(request)
        await UserValidator.post(request_data)

        bm = UsersBusinessModel(request_data)
        entity = await bm.create()
        return ResponseSerializer() \
            .serialize_object(entity) \
            .response

    @classmethod
    async def put(cls, request: Request) -> Response:
        """
        @api {put} /users/{id} Update users
        @apiName UsersUpdate
        @apiGroup Users
        @apiDescription Update user by id

        @apiExample json request body example
        {
          "data": {
            "attributes": {
              "first_name": "Bogdann"
            }
          }
        }

        @apiSuccessExample response body example
        {
          "data": {
            "id": 4,
            "model_type": "users",
            "attributes": {
              "id": "4",
              "first_name": "Bogdann",
              "last_name": "Parshintsev",
              "family_name": null,
              "created_at": "2021-04-15 11:35:19",
              "created_by": "2",
              "updated_at": "2021-04-15 11:38:49",
              "updated_by": "2",
              "deleted_at": null,
              "deleted_by": null
            }
          },
          "included": {}
        }
        """
        request_data = await RequestData.create(request)
        await UserValidator.put(request_data)

        bm = UsersBusinessModel(request_data)
        entity = await bm.update()
        return ResponseSerializer() \
            .serialize_object(entity) \
            .response

    @classmethod
    async def delete(cls, request: Request) -> Response:
        """
        @api {delete} /users/{id} Delete user
        @apiName UsersDelete
        @apiGroup Users
        @apiDescription Delete user by id

        @apiSuccessExample response body example
        {
          "data": {
            "id": 4,
            "model_type": "users",
            "attributes": {
              "id": "4",
              "first_name": "Bogdann",
              "last_name": "Parshintsev",
              "family_name": null,
              "created_at": "2021-04-15 11:35:19",
              "created_by": "2",
              "updated_at": "2021-04-15 11:38:49",
              "updated_by": "2",
              "deleted_at": "2021-04-15 11:40:02",
              "deleted_by": "2"
            }
          },
          "included": {}
        }
        """
        return await super(UsersController, cls).delete(request)

from base import BaseController
from aiohttp.web import Request, Response


class OrdersController(BaseController):
    """Class defines handlers for order instance"""

    @classmethod
    async def get_by_id(cls, request: Request) -> Response:
        """
        @api {get} /orders/{id} Get order by id
        @apiName OrdersGetByID
        @apiGroup Orders
        @apiDescription Get order by id if exists else 400

        @apiSuccessExample response body example
        {
          "data": {
            "id": 3,
            "model_type": "orders",
            "attributes": {
              "id": "3",
              "user_id": "1",
              "created_at": "2021-04-15 11:22:24",
              "created_by": "2",
              "updated_at": "2021-04-15 11:22:24",
              "updated_by": null,
              "deleted_at": null,
              "deleted_by": null
            }
          },
          "included": {}
        }
        """
        return await super(OrdersController, cls).get_by_id(request)

    @classmethod
    async def get(cls, request: Request) -> Response:
        """
        @api {get} /orders Get orders array
        @apiName OrdersGet
        @apiGroup Orders
        @apiDescription Get all orders in array

        @apiSuccessExample response body example
        {
          "data": [
            {
              "id": 3,
              "model_type": "orders",
              "attributes": {
                "id": "3",
                "user_id": "1",
                "created_at": "2021-04-15 11:22:24",
                "created_by": "2",
                "updated_at": "2021-04-15 11:22:24",
                "updated_by": null,
                "deleted_at": null,
                "deleted_by": null
              }
            }
          ],
          "included": {}
        }
        """
        return await super(OrdersController, cls).get(request)

    @classmethod
    async def post(cls, request: Request) -> Response:
        """
        @api {post} /orders Crate new order
        @apiName OrdersCreate
        @apiGroup Orders
        @apiDescription Create new order

        @apiExample json request body example
        {
          "data": {
            "attributes": {
              "user_id": 2
            }
          }
        }

        @apiSuccessExample response body example
        {
          "data": {
            "id": 1,
            "model_type": "orders",
            "attributes": {
              "id": "1",
              "user_id": "2",
              "created_at": "2021-04-15 11:17:17",
              "created_by": "2",
              "updated_at": "2021-04-15 11:17:17",
              "updated_by": null,
              "deleted_at": null,
              "deleted_by": null
            }
          },
          "included": {}
        }
        """
        return await super(OrdersController, cls).post(request)

    @classmethod
    async def put(cls, request: Request) -> Response:
        """
        @api {put} /orders/{id} Update order
        @apiName OrdersUpdate
        @apiGroup Orders
        @apiDescription Update order by id

        @apiExample json request body example
        {
          "data": {
            "attributes": {
              "user_id": 1
            }
          }
        }

        @apiSuccessExample response body example
        {
          "data": {
            "id": 1,
            "model_type": "orders",
            "attributes": {
              "id": "1",
              "user_id": "1",
              "created_at": "2021-04-15 11:17:17",
              "created_by": "2",
              "updated_at": "2021-04-15 11:20:01",
              "updated_by": "2",
              "deleted_at": null,
              "deleted_by": null
            }
          },
          "included": {}
        }
        """
        return await super(OrdersController, cls).put(request)

    @classmethod
    async def delete(cls, request: Request) -> Response:
        """
        @api {delete} /orders/{id} Delete order
        @apiName OrdersDelete
        @apiGroup Orders
        @apiDescription Delete order by id

        @apiSuccessExample response body example
        {
          "data": {
            "id": 1,
            "model_type": "orders",
            "attributes": {
              "id": "1",
              "user_id": "1",
              "created_at": "2021-04-15 11:17:17",
              "created_by": "2",
              "updated_at": "2021-04-15 11:20:01",
              "updated_by": "2",
              "deleted_at": "2021-04-15 11:21:41",
              "deleted_by": "2"
            }
          },
          "included": {}
        }
        """
        return await super(OrdersController, cls).delete(request)

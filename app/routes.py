from controllers import UsersController, OrdersController
from base import BaseController
from aiohttp.web import Application


models_controllers = [
    # users
    ('GET', '/users', UsersController.get),
    ('GET', '/users/{id}', UsersController.get_by_id),
    ('POST', '/users', UsersController.post),
    ('PUT', '/users/{id}', UsersController.put),
    ('DELETE', '/users/{id}', UsersController.delete),

    # orders
    ('GET', '/orders', OrdersController.get),
    ('GET', '/orders/{id}', OrdersController.get_by_id),
    ('POST', '/orders', OrdersController.post),
    ('PUT', '/orders/{id}', OrdersController.put),
    ('DELETE', '/order/{id}', OrdersController.delete),
]


def register_routes(app: Application):
    """
    Register five base routes for all controllers which inherited from AbstractController
    and also register specific routes defined in app_routes variable
    """
    for model_controller in models_controllers:
        app.router.add_route(*model_controller)

    app.router.add_route('GET', '/{entity_type}', BaseController.get)
    app.router.add_route('GET', '/{entity_type}/{id}', BaseController.get_by_id)
    app.router.add_route('POST', '/{entity_type}', BaseController.post)
    app.router.add_route('PUT', '/{entity_type}/{id}', BaseController.put)
    app.router.add_route('DELETE', '/{entity_type}/{id}', BaseController.delete)

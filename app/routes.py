from controllers import *
from aiohttp.web import Application
from utils.abstract_controller import AbstractController


app_routes = [
    # if you need specific route for some reason, add it here as tuple. For example:
    # ('GET', UserController.entity_route + '/your_specific_route', UserController.specific_handler)
    ('GET', UsersController.entity_route + '/followers', UsersController.followers),
    ('PUT', UsersController.entity_route + '/follow/{id}', UsersController.follow),
]


def register_routes(app: Application):
    """
    Register five base routes for all controllers which inherited from AbstractController
    and also register specific routes defined in app_routes variable
    """
    for route in app_routes:
        app.router.add_route(*route)

    controllers = AbstractController.__subclasses__()
    for controller in controllers:
        app.router.add_route('PUT', controller.entity_route, controller.put)
        app.router.add_route('POST', controller.entity_route, controller.post)
        app.router.add_route('GET', controller.entity_route + '/{id}', controller.get)
        app.router.add_route('PATCH', controller.entity_route + '/{id}', controller.patch)
        app.router.add_route('DELETE', controller.entity_route + '/{id}', controller.delete)

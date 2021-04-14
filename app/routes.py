from controllers import *
from base import BaseController
from aiohttp.web import Application


models_controllers = [
]


def register_routes(app: Application):
    """
    Register five base routes for all controllers which inherited from AbstractController
    and also register specific routes defined in app_routes variable
    """
    for model_controller in models_controllers:
        app.router.add_view(*model_controller)

    app.router.add_route('GET', '/{entity_type}/{id}', BaseController.get_by_id)
    app.router.add_route('POST', '/{entity_type}', BaseController.post)
    app.router.add_route('PUT', '/{entity_type}/{id}', BaseController.put)
    app.router.add_route('DELETE', '/{entity_type}/{id}', BaseController.delete)

from aiohttp import web
from routes import register_routes
from middlewares import middleware_list


__all__ = ['app']


app = web.Application(middlewares=middleware_list)
register_routes(app)

from aiohttp import web
from routes import register_routes
from database import PGContextSession
from middlewares import middleware_list


__all__ = ['app']


app = web.Application(middlewares=middleware_list)
app.on_startup.append(PGContextSession.setup)
register_routes(app)

from aiohttp import web
from routes import register_routes
from database import PostgresDatabase
from middlewares import middleware_list


__all__ = ['app']


app = web.Application(middlewares=middleware_list)
app.on_startup.append(PostgresDatabase.startup_setup)
register_routes(app)

from aiohttp import web
from application import app
from logger import logger


def run_server(host: str = '127.0.0.1', port: int = 8000) -> None:
    logger.info(f'Start APP host={host} port={port}')
    web.run_app(app, host=host, port=port)
    logger.info(f'Stop APP host={host} port={port}')


if __name__ == '__main__':
    run_server()

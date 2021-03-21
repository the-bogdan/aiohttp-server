import asyncio

from logger import logger
from server import run_server
from argparse import ArgumentParser
from database import create_db_tables


parser = ArgumentParser(description='Start rest app based on aiohttp')
parser.add_argument('-r', '--run', action='store_true', help='Run app')
parser.add_argument('-m', '--migrate', action='store_true', help='Create all tables')
args = parser.parse_args()


def main():
    if args.migrate:
        logger.info('Create all database tables')
        asyncio.run(create_db_tables())

    elif args.run:
        run_server()


if __name__ == '__main__':
    main()

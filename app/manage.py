import asyncio

from logger import logger
from server import run_server
from argparse import ArgumentParser
from database import PostgresDatabase


parser = ArgumentParser(description='Start rest app based on aiohttp')
parser.add_argument('-r', '--run', action='store_true', help='Run app')
parser.add_argument('-m', '--migrate', action='store_true', help='Create all tables')
args = parser.parse_args()


def main():
    if args.migrate:
        # Drop all existing tables and create new
        logger.info('Create all database tables')
        asyncio.run(PostgresDatabase.renew_db_tables())

    elif args.run:
        # run server
        run_server()


if __name__ == '__main__':
    main()

import os

from config import config
from server import run_server
from argparse import ArgumentParser
from database.alembic.alembic_agent import AlembicAgent


manage_file_path = os.path.abspath(os.path.dirname(__file__))
if os.getcwd() != manage_file_path:
    os.chdir(manage_file_path)


# working with migrations
parser = ArgumentParser(description='Start rest app based on aiohttp')
parser.add_argument('--makemigrations', action='store_true', help='Create migration file')
parser.add_argument('--upgrade', action='store_true', help='Update database revision to the head')
parser.add_argument('--downgrade', action='store_true', help='Downgrade revision to 1')
parser.add_argument('-m', '--message', help='Message for migration')

# running app
parser.add_argument('-r', '--run', action='store_true', help='Run app')
parser.add_argument('--port', help='Application port')
parser.add_argument('--host', help='Application port')
args = parser.parse_args()


def main():
    if args.makemigrations:
        # Create migrations file
        alembic_agent = AlembicAgent.setup(manage_file_path)
        alembic_agent.make_migrations(args.message)

    if args.upgrade:
        # upgrade to latest revision
        alembic_agent = AlembicAgent.setup(manage_file_path)
        alembic_agent.upgrade()

    if args.downgrade:
        # upgrade to latest revision
        alembic_agent = AlembicAgent.setup(manage_file_path)
        alembic_agent.downgrade()

    elif args.run:
        # run server
        host = args.host or config['server']['host']
        port = args.port or config['server']['port']
        run_server(host=host, port=port)


if __name__ == '__main__':
    main()

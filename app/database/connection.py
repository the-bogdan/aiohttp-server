from config import config
from sqlalchemy import insert
from database import Base, User
from aiohttp.web import Application
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine


class PGContextSession:
    def __init__(self):
        self.__session_instance: AsyncSession = None

    async def __aenter__(self) -> AsyncSession:
        self.__session_instance = PostgresDatabase.sessionmaker()
        return self.__session_instance

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__session_instance.close()


class PostgresDatabase:
    __engine: AsyncEngine = None
    sessionmaker: sessionmaker = None

    @classmethod
    async def startup_setup(cls, app: Application):
        """Method creates db tables which not exist and setup engine and sessionmaker"""
        cls.__engine = create_async_engine(URL(**config['postgres']))
        await cls.create_db_tables(cls.__engine)
        cls.sessionmaker = sessionmaker(
            bind=cls.__engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            class_=AsyncSession
        )

    @classmethod
    async def renew_db_tables(cls):
        """Method drop all db tables and creates new"""
        engine = create_async_engine(URL(**config['postgres']))
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            await cls._create_default_users(conn)

    @staticmethod
    async def create_db_tables(engine: AsyncEngine) -> None:
        """Method crates db tables on startup if they don't exist"""
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def _create_default_users(conn):
        """Create default users on renew_db_tables() method call"""
        default_users = [
            # first_name, last_name, nickname, password
            ('Система', 'System', 'system', 'system'),
            ('admin', 'admin', 'admin', 'admin')
        ]

        for fist_name, last_name, nickname, password in default_users:
            await conn.execute(insert(User).values(
                first_name=fist_name,
                last_name=last_name,
                nickname=nickname,
                password=password,
                created_by=1,
                updated_by=1
            ))

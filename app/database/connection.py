from config import config
from aiohttp.web import Application
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class PGContextSession:
    """Context manager to open postgres session"""
    def __init__(self):
        self.__session_instance: AsyncSession = None

    async def __aenter__(self) -> AsyncSession:
        self.__session_instance = self.__sessionmaker()
        return self.__session_instance

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__session_instance.close()

    @classmethod
    async def setup(cls, app: Application):
        cls.__engine = create_async_engine(URL(**config['postgres']))
        cls.__sessionmaker = sessionmaker(
            bind=cls.__engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            class_=AsyncSession
        )

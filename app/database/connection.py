from aiohttp import web
from database import Base
from config import config
from sqlalchemy import text
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


__all__ = ['context_session', 'engine', 'create_db_tables']


engine = create_async_engine(URL(**config['postgres']))
context_session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession
)


async def create_db_tables():
    """Method create database tables on startup"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(
            text("INSERT INTO users (last_name, first_name, _nickname, _password) VALUES "
                 "('admin', 'админ', 'admin', 'admin')")
        )

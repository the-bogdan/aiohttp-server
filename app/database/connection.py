from config import config
from sqlalchemy import insert
from database import Base, User
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
        await _create_default_users(conn)


async def _create_default_users(conn):
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

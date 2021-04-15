from .models import Base
from sqlalchemy import func
from typing import Iterable
from sqlalchemy.future import select, Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import BinaryExpression


class DatabaseAgent:
    @classmethod
    async def count(cls, session: AsyncSession, entity_model: Base,
                    filters: Iterable[BinaryExpression] = None) -> int:
        """
        Method prepares and executes count function and return integer.
        You can provide filters to this function. Filters must be a list of SQLAlchemy
        BinaryExpression objects (for example [User.id == 10])
        """
        count = func.count(entity_model.id)
        count = cls.add_base_filters(count, entity_model)

        if filters:
            for filter_ in filters:
                count = count.filter(filter_)

        result = await session.execute(select(count))
        return result.scalar()

    @classmethod
    async def get_one(cls, session: AsyncSession, entity_model: Base,
                      filters: Iterable[BinaryExpression] = None) -> Base:
        """Method prepares and executes query for getting one database entity with some filters"""
        stmt = select(entity_model)
        stmt = cls.add_base_filters(stmt, entity_model)

        if filters:
            for filter_ in filters:
                stmt = stmt.filter(filter_)

        result = await session.execute(stmt)
        return result.scalar()

    @classmethod
    async def get_all(cls, session: AsyncSession, entity_model: Base,
                      filters: Iterable[BinaryExpression] = None) -> Iterable[Base]:
        """Get all entities"""
        # TODO add filters support and pagination
        stmt = select(entity_model)
        stmt = cls.add_base_filters(stmt, entity_model)

        if filters:
            for filter_ in filters:
                stmt = stmt.filter(filter_)

        result = await session.execute(stmt)
        return result.scalars()

    @classmethod
    async def get_by_id(cls, session: AsyncSession, entity_model: Base, entity_id: int) -> Base:
        """Method prepares and executes query for getting database entity by its id"""
        stmt = select(entity_model).filter(entity_model.id == entity_id,)
        stmt = cls.add_base_filters(stmt, entity_model)

        result = await session.execute(stmt)
        return result.scalar()

    @staticmethod
    def add_base_filters(stmt: Select, entity_model: Base) -> Select:
        """Filter deleted entities"""
        return stmt.filter(
            entity_model.deleted_at.is_(None),
            entity_model.deleted_by.is_(None)
        )

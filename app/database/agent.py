from .models import Base
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import BinaryExpression


class DatabaseAgent:
    @classmethod
    async def count(cls, session: AsyncSession, entity_model: Base, filters: list[BinaryExpression] = None) -> int:
        """
        Method prepare and execute count function and return integer.
        You can provide filters to this function. Filters must be a list of SQLAlchemy
        BinaryExpression objects (for example [User.id == 10])
        """
        count = func.count(entity_model.id).filter(
            entity_model.deleted_at.is_(None),
            entity_model.deleted_by.is_(None)
        )
        if filters:
            for filter_ in filters:
                count = count.filter(filter_)
        result = await session.execute(select(count))
        return result.scalar()

    @classmethod
    async def get_by_id(cls, session: AsyncSession, entity_model: Base, entity_id: int):
        stmt = select(entity_model).filter(
            entity_model.id == entity_id,
            entity_model.deleted_at.is_(None),
            entity_model.deleted_by.is_(None)
        )

        result = await session.execute(stmt)
        return result.scalar()

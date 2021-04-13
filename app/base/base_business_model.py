from database import Base
from aiohttp.web import Request
from .request_data import RequestData
from sqlalchemy.ext.asyncio import AsyncSession


class BaseBusinessModel:
    def __init__(self, request_data: RequestData):
        """Init business model and save user_id and db_session which added to request in middlewares"""
        self._request_data: RequestData = request_data

    @property
    def request_data(self) -> RequestData:
        """Returns request object"""
        return self._request_data

    async def get_by_id(self) -> Base:
        """Get database entity by id"""
        entity_id = self.request_data.entity_id
        entity_model = self.request_data.entity_model

        entity = await self.request_data.pg_session.get(entity_model, entity_id)
        return entity

    async def search(self) -> list[Base]:
        """Get filtered and ordered database entities"""
        pass

    async def update(self) -> Base:
        """Update database entity by id"""
        pass

    async def create(self) -> Base:
        """Create database entity"""
        pass

    async def delete(self) -> Base:
        """Delete database entity by id"""
        pass

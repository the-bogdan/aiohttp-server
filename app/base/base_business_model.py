from .request_data import RequestData
from database import Base, DatabaseAgent
from sqlalchemy.ext.asyncio import AsyncSession


class BaseBusinessModel:
    def __init__(self, request_data: RequestData):
        """Init business model and save user_id and db_session which added to request in middlewares"""
        self._request_data: RequestData = request_data
        self._pg_session: AsyncSession = request_data.pg_session

    @property
    def request_data(self) -> RequestData:
        """Returns request object"""
        return self._request_data

    @property
    def session(self) -> AsyncSession:
        """Returns postgres session object"""
        return self._pg_session

    async def get_by_id(self) -> Base:
        """Get database entity by id"""
        entity = await DatabaseAgent.get_by_id(
            session=self.session,
            entity_id=self.request_data.entity_id,
            entity_model=self.request_data.entity_model
        )
        return entity

    async def search(self) -> list[Base]:
        """Get filtered and ordered database entities"""
        pass

    async def create(self) -> Base:
        """Create database entity"""
        entity = self.request_data.entity_model()
        for attribute, value in self.request_data.payload['data']['attributes'].items():
            if attribute != 'id' and attribute not in entity.system_fields:
                setattr(entity, attribute, value)
        entity.label_created(self.request_data.user_id)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self) -> Base:
        """Update database entity by id"""
        entity = await DatabaseAgent.get_by_id(
            session=self.session,
            entity_id=self.request_data.entity_id,
            entity_model=self.request_data.entity_model
        )
        for attribute, value in self.request_data.payload['data']['attributes'].items():
            if attribute != 'id' and attribute not in entity.system_fields:
                setattr(entity, attribute, value)
        entity.label_updated(self.request_data.user_id)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def delete(self) -> Base:
        """Delete database entity by id"""
        entity = await DatabaseAgent.get_by_id(
            session=self.session,
            entity_id=self.request_data.entity_id,
            entity_model=self.request_data.entity_model
        )
        entity.label_deleted(self.request_data.user_id)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

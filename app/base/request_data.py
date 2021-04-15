from database import Base
from typing import Optional
from aiohttp.web import Request
from database.mapper import ModelMapper
from sqlalchemy.ext.asyncio import AsyncSession
from utils.custom_exception import ExecutionException


class RequestData:
    """Container with all request data"""
    def __init__(
            self,
            headers: dict,
            request: Request,
            user_id: Optional[int],
            payload: Optional[dict],
            params: Optional[dict],
            pg_session: AsyncSession,
            entity_id: Optional[int],
            entity_type: Optional[str],
            entity_model: Optional[Base]
    ):
        self._request = request
        self._headers: dict = headers
        self._params: Optional[dict] = params
        self._payload: Optional[dict] = payload

        self._user_id: Optional[int] = user_id
        self._entity_id: Optional[int] = entity_id
        self._entity_type: Optional[str] = entity_type
        self._entity_model: Optional[Base] = entity_model
        self._pg_session: AsyncSession = pg_session

    @property
    def request(self) -> Request:
        """aiohttp Request instance"""
        return self._request

    @property
    def pg_session(self) -> AsyncSession:
        """async postgres session instance"""
        return self._pg_session

    @property
    def headers(self) -> dict:
        """dict with request headers"""
        return self._headers

    @property
    def user_id(self) -> Optional[int]:
        """id of user who make request"""
        return self._user_id

    @property
    def entity_id(self) -> Optional[int]:
        """entity id from match_info (query str)"""
        return self._entity_id

    @property
    def entity_type(self) -> Optional[str]:
        """string with entity type from match_info or query str"""
        return self._entity_type

    @property
    def entity_model(self) -> Optional[Base]:
        """string with entity type from match_info or query str"""
        return self._entity_model

    @property
    def payload(self) -> Optional[dict]:
        """dict with request payload if it exists"""
        return self._payload

    @property
    def params(self) -> Optional[dict]:
        """dict with query params if it exists"""
        return self._params

    @classmethod
    async def create(cls, request: Request) -> 'RequestData':
        """Build RequestData instance from request"""
        body = await cls._get_body(request)
        entity_id: str = request.match_info.get('id')
        entity_type, entity_model = cls._get_entity_type(request)

        return cls(
            payload=body,
            request=request,
            entity_type=entity_type,
            entity_model=entity_model,
            user_id=request['user_id'],
            params=dict(request.query),
            headers=dict(request.headers),
            pg_session=request['postgres_session'],
            entity_id=int(entity_id) if entity_id and entity_id.isdigit() else None
        )

    @staticmethod
    async def _get_body(request: Request) -> Optional[dict]:
        """Get json body if it exists"""
        if request.body_exists:
            if request.content_type == 'application/json':
                return await request.json()
            else:
                raise ExecutionException(
                    error='content-type-error',
                    message='only body with application/json content_type supported',
                    http_code=415
                )
        return None

    @staticmethod
    def _get_entity_type(request: Request) -> tuple[Optional[str], Optional[Base]]:
        """Get entity type and model from url"""
        entity_type = request.match_info.get('entity_type')
        if entity_type:
            return entity_type, ModelMapper.get_table(entity_type)

        for part in request.url.path.split('/'):
            if part and ModelMapper.get_table(part):
                return part, ModelMapper.get_table(part)
        return None, None

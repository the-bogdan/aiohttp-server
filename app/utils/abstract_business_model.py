from typing import Any
from aiohttp.web import Request
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractBusinessModel:
    def __init__(self, request: Request):
        self._request: Request = request
        self._user_id: int = request['user_id']
        self._session: AsyncSession = request['db_session']

    @property
    def request(self):
        return self._request

    @property
    def session(self):
        return self._session

    @property
    def user_id(self):
        return self._user_id

    def get(self) -> Any:
        pass

    def search(self) -> Any:
        pass

    def update(self) -> Any:
        pass

    def create(self) -> Any:
        pass

    def delete(self) -> Any:
        pass

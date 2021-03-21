from abc import ABC, abstractmethod
from aiohttp.web import Request
from utils.custom_exception import ExecutionException


__all__ = ['AbstractController']


class AbstractController(ABC):
    """Abstract controller which implements base handlers for HTTP methods"""

    message = 'HTTP method not allowed'

    @property
    @abstractmethod
    async def entity_route(self) -> str:
        """This is route to get access for http methods defined by controller"""
        pass

    @classmethod
    async def get(cls, request: Request) -> None:
        """Base get handler"""
        raise ExecutionException('not-implemented', cls.message, 405)

    @classmethod
    async def post(cls, request: Request) -> None:
        """Base post handler"""
        raise ExecutionException('not-implemented', cls.message, 405)

    @classmethod
    async def patch(cls, request: Request) -> None:
        """Base patch handler"""
        raise ExecutionException('not-implemented', cls.message, 405)

    @classmethod
    async def delete(cls, request: Request) -> None:
        """Base delete handler"""
        raise ExecutionException('not-implemented', cls.message, 405)

    @classmethod
    async def put(cls, request: Request) -> None:
        """Base put handler"""
        raise ExecutionException('not-implemented', cls.message, 405)

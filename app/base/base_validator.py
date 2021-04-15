from .request_data import RequestData
from utils.validation_utils import ValidationUtils


class BaseValidator:
    @classmethod
    async def get_by_id(cls, request_data: RequestData):
        """Validating for method get by id (get one entity by id) /{entity_type}/{id}"""
        ValidationUtils.check_entity_type_correct(request_data)
        await ValidationUtils.check_entity_exists_by_id(request_data)

    @classmethod
    async def get(cls, request_data: RequestData):
        """Validating for method get (get list of entities) /{entity_type}"""
        ValidationUtils.check_entity_type_correct(request_data)

    @classmethod
    async def post(cls, request_data: RequestData):
        """Validating for method post (creating entity) /{entity_type}"""
        ValidationUtils.check_entity_type_correct(request_data)
        ValidationUtils.check_create_json_schema(request_data)

    @classmethod
    async def put(cls, request_data: RequestData):
        """Validating for method put (update entity) /{entity_type}/{id}"""
        ValidationUtils.check_entity_type_correct(request_data)
        await ValidationUtils.check_entity_exists_by_id(request_data)
        ValidationUtils.check_update_json_schema(request_data)

    @classmethod
    async def delete(cls, request_data: RequestData):
        """Validating for method delete (delete entity) /{entity_type}/{id}"""
        ValidationUtils.check_entity_type_correct(request_data)
        await ValidationUtils.check_entity_exists_by_id(request_data)


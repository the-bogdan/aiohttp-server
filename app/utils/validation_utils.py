from base import RequestData
from database import DatabaseAgent, ModelMapper
from jsonschema import validate, ValidationError
from utils.custom_exception import ExecutionException


class ValidationUtils:
    _request_body_json_schema = {
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "attributes": {
                        "type": "object"
                    }
                },
                "required": ['attributes']
            }
        },
        "required": ["data"],
        "additionalProperties": False
    }

    @classmethod
    def check_entity_type(cls, request_data: RequestData) -> None:
        if not request_data.entity_type:
            cls.raise_validation_error("Can't find database table with name you have provided")
        if not request_data.entity_model:
            cls.raise_validation_error(f"Can't find database table with name = {request_data.entity_type}")

    @classmethod
    def check_create_json_schema(cls, request_data: RequestData) -> None:
        attributes_schema = ModelMapper.get_json_schema(request_data.entity_type)
        cls._check_json_schema(request_data, attributes_schema)

    @classmethod
    def check_update_json_schema(cls, request_data: RequestData) -> None:
        attributes_schema = {**ModelMapper.get_json_schema(request_data.entity_type)}
        del attributes_schema['required']
        cls._check_json_schema(request_data, attributes_schema)

    @classmethod
    async def check_entity_exists_by_id(cls, request_data: RequestData) -> None:
        if not request_data.entity_id:
            cls.raise_validation_error("Can't get entity id. It must be in query string and be integer")
        result = await DatabaseAgent.count(
            session=request_data.pg_session,
            entity_model=request_data.entity_model,
            filters=[request_data.entity_model.id == request_data.entity_id]
        )
        if not result == 1:
            cls.raise_validation_error(f"Entity with id = {request_data.entity_id} doesn't exists"
                                       f"in table = {request_data.entity_type}")

    @staticmethod
    def raise_validation_error(message: str, http_code: int = 400) -> None:
        raise ExecutionException(
            error='validation-error',
            message=message,
            http_code=http_code
        )

    @classmethod
    def _check_json_schema(cls, request_data: RequestData, attributes_schema: dict):
        if not request_data.payload:
            cls.raise_validation_error("Method requires body with application/json content_type "
                                       "and object with data inside", http_code=415)
        body_schema = {**cls._request_body_json_schema}
        body_schema["properties"]["data"]["properties"]["attributes"] = attributes_schema
        cls._validate_json_schema(request_data.payload, body_schema)

    @classmethod
    def _validate_json_schema(cls, data: dict, schema: dict) -> None:
        try:
            validate(data, schema)
        except ValidationError as e:
            message = ""
            for part in e.path:
                message = message + part + ' -> '
            message = message + e.message
            cls.raise_validation_error(message)

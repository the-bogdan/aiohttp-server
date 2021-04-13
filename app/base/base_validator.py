from .request_data import RequestData
from utils.custom_exception import ExecutionException


class BaseValidator:
    @classmethod
    def get_by_id(cls, request_data: RequestData):
        if not request_data.entity_id:
            cls._raise_validation_error("Can't get entity id. It must be in query string and be integer")
        if not request_data.entity_type:
            cls._raise_validation_error("Can't find database table with name you have provided")
        if not request_data.entity_model:
            cls._raise_validation_error(f"Can't find database table with name = {request_data.entity_type}")

    @staticmethod
    def _raise_validation_error(message: str):
        raise ExecutionException(
            error='validation-error',
            message=message,
            http_code=400
        )

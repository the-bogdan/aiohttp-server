from base import RequestData
from base import BaseValidator
from utils.validation_utils import ValidationUtils


class UserValidator(BaseValidator):
    @classmethod
    async def post(cls, request_data: RequestData):
        await super(UserValidator, cls).post(request_data)

        # check password length
        password = request_data.payload['data']['attributes']['password']
        if len(password) < 8:
            ValidationUtils.raise_validation_error(
                "Password length must be 8 or more characters"
            )

    @classmethod
    async def put(cls, request_data: RequestData):
        await super(UserValidator, cls).put(request_data)

        password = request_data.payload['data']['attributes'].get('password')
        if password and len(password) < 8:
            ValidationUtils.raise_validation_error(
                "Password length must be 8 or more characters"
            )


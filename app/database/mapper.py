from .models import *
from typing import Optional
from datetime import datetime
from collections import defaultdict
from sqlalchemy.inspection import inspect


_types_mapper = {
    str: "string",
    int: "integer",
    datetime: "string"
}


class ModelMapper:
    """Class provide methods for map model_type to class object"""
    _model_type_to_class = {}
    _model_columns = defaultdict(dict)
    _model_json_schema = defaultdict(dict)

    for class_ in Base.__subclasses__():
        _model_type_to_class[class_.__tablename__] = class_

        json_schema = {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }

        for column in inspect(class_).column_attrs:
            _model_columns[class_.__tablename__][column.key] = {
                'python_type': column.expression.type.python_type,
                'is_required': not column.expression.nullable
            }
            json_schema["properties"][column.key] = {
                "type": _types_mapper.get(column.expression.type.python_type)
            }
            if column.key != 'id' and not column.expression.nullable:
                json_schema["required"].append(column.key)

        _model_json_schema[class_.__tablename__] = json_schema

    @classmethod
    def get_table(cls, model_type: str) -> Optional[Base]:
        """Return table model object by model_type"""
        return cls._model_type_to_class.get(model_type)

    @classmethod
    def get_columns(cls, model_type: str) -> Optional[dict]:
        """Return all table columns dict by model_type"""
        return cls._model_columns.get(model_type)

    @classmethod
    def get_json_schema(cls, model_type: str) -> Optional[dict]:
        return cls._model_json_schema.get(model_type)

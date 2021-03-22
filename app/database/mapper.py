from .models import *
from typing import Optional
from collections import defaultdict
from sqlalchemy.inspection import inspect


class ModelMapper:
    """Class provide methods for map model_type to class object and backward"""
    _model_type_to_class = {}
    _model_columns = defaultdict(dict)

    for class_ in Base.__subclasses__():
        _model_type_to_class[class_.__tablename__] = class_
        for column in inspect(class_).column_attrs:
            _model_columns[class_.__tablename__][column.key] = {
                'python_type': column.expression.type.python_type,
                'is_required': not column.expression.nullable
            }

    @classmethod
    def get_table(cls, model_type: str) -> Optional[Base]:
        """Return table model object by model_type"""
        return cls._model_type_to_class.get(model_type)

    @classmethod
    def get_columns(cls, model_type: str) -> Optional[dict]:
        """Return all table columns dict by model_type"""
        return cls._model_columns.get(model_type)

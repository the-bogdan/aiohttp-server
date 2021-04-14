from datetime import datetime
from collections import defaultdict
from sqlalchemy.inspection import inspect
from typing import Iterable, Tuple, Optional
from aiohttp.web import json_response, Response
from database import Base as SqlalchemyBase, ModelMapper


class ResponseSerializer:
    def __init__(self):
        self._data: defaultdict = None
        self._included: defaultdict = defaultdict(dict)

        self._is_collection: bool = False

    @property
    def response(self) -> Response:
        if self._is_collection:
            data = []
            for model_type, entities in self._data.items():
                data = []
                for entity_id, entity in entities.items():
                    data.append(self._serialize_object(entity))
        else:
            data = self._data

        included = defaultdict(list)
        for model_type, entities in self._included.items():
            for entity_id, entity in entities.items():
                included[model_type].append(self._serialize_object(entity))

        result = {
            'data': data,
            'included': included
        }
        return json_response(result)

    def serialize_object(self, entity: SqlalchemyBase) -> 'ResponseSerializer':
        self._is_collection = False
        if entity and isinstance(entity, SqlalchemyBase):
            self._data = self._serialize_object(entity)
        else:
            self._data = {
                'id': None,
                'model_type': None,
                'attributes': {}
            }
        return self

    def serialize_collection(self, entities: Iterable[SqlalchemyBase]) -> 'ResponseSerializer':
        self._is_collection = True
        self._data = defaultdict(dict)
        for entity in entities:
            if entity and isinstance(entity, SqlalchemyBase):
                entity_id, model_type = self._get_entity_params(entity)
                self._data[model_type][entity_id] = entity
        return self

    def append_object_in_included(self, entity: SqlalchemyBase) -> 'ResponseSerializer':
        if entity and isinstance(entity, SqlalchemyBase):
            entity_id, model_type = self._get_entity_params(entity)
            self._included[model_type][entity_id] = entity
        return self

    def append_collection_in_included(self, entities: Iterable[SqlalchemyBase]):
        for entity in entities:
            if entity and isinstance(entity, SqlalchemyBase):
                entity_id, model_type = self._get_entity_params(entity)
                self._included[model_type][entity_id] = entity
        return self

    @staticmethod
    def _get_entity_params(entity: SqlalchemyBase) -> Tuple[Optional[int], Optional[str]]:
        """Return SQLAlchemy model type and id"""
        model_type = getattr(entity, '__tablename__', None)
        entity_id = getattr(entity, 'id', None)
        return entity_id, model_type

    @staticmethod
    def _serialize_object(entity: SqlalchemyBase) -> dict:
        """Serialize SQLAlchemy model into dict object"""
        data = {
            'id': getattr(entity, 'id', None),
            'model_type': getattr(entity, '__tablename__', None),
            'attributes': {}
        }
        attrs = ModelMapper.get_columns(getattr(entity, '__tablename__', None))
        hidden_attrs = getattr(entity, '_hidden', set())
        if attrs:
            for key, _ in attrs.items():
                if key in hidden_attrs:
                    continue
                value = getattr(entity, key, None)
                if isinstance(value, datetime):
                    data['attributes'][key] = value.strftime('%Y-%m-%d %H:%M:%S')
                elif value is None:
                    data['attributes'][key] = value
                else:
                    data['attributes'][key] = str(value)

        return data

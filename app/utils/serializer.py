from database import Base
from collections import defaultdict
from typing import Iterable, Tuple, Optional
from aiohttp.web import json_response, Response


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

    def serialize_object(self, entity: Base) -> 'ResponseSerializer':
        self._is_collection = False
        if entity and isinstance(entity, object):
            self._data = self._serialize_object(entity)
        else:
            self._data = {
                'id': None,
                'model_type': None,
                'attributes': {}
            }
        return self

    def serialize_collection(self, entities: Iterable[object]) -> 'ResponseSerializer':
        self._is_collection = True
        self._data = defaultdict(dict)
        for entity in entities:
            if entity and isinstance(entity, object):
                entity_id, model_type = self._get_entity_params(entity)
                self._data[model_type][entity_id] = entity
        return self

    def append_object_in_included(self, entity: object) -> 'ResponseSerializer':
        if entity and isinstance(entity, object):
            entity_id, model_type = self._get_entity_params(entity)
            self._included[model_type][entity_id] = entity
        return self

    def append_collection_in_included(self, entities: Iterable[object]):
        for entity in entities:
            if entity and isinstance(entity, object):
                entity_id, model_type = self._get_entity_params(entity)
                self._included[model_type][entity_id] = entity
        return self

    @staticmethod
    def _get_entity_params(entity: object) -> Tuple[Optional[int], Optional[str]]:
        """Return SQLAlchemy model type and id"""
        model_type = getattr(entity, '__tablename__', None)
        entity_id = getattr(entity, 'id', None)
        return entity_id, model_type

    @staticmethod
    def _serialize_object(entity: Base) -> dict:
        """Serialize SQLAlchemy model into dict object"""
        data = {
            'id': getattr(entity, 'id', None),
            'model_type': getattr(entity, '__tablename__', None),
            'attributes': {}
        }
        for key, value in entity.__dict__.items():
            if not key.startswith('_'):
                if isinstance(value, Base):
                    pass
                elif isinstance(value, list) and isinstance(next(iter(value), []), Base):
                    pass
                else:
                    data['attributes'][key] = value
        return data

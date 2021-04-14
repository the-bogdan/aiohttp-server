import networkx as nx

from typing import List
from .mapper import ModelMapper
from sqlalchemy.inspection import inspect


class ModelGraph:
    """Class builds graph for models and their relations"""
    g = nx.DiGraph()

    for model in getattr(ModelMapper, '_model_type_to_class').values():
        relations = (rel.mapper.class_ for rel in inspect(model).relationships)
        for relation in relations:
            g.add_edge(model.__tablename__, relation.__tablename__)

    @classmethod
    def shortest_path(cls, start: str, end: str) -> List[str]:
        """Get shortest path from one model to other by model_type"""
        path = nx.shortest_path(cls.g, start, end)
        return path

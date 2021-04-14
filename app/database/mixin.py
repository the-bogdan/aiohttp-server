from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, DateTime, Integer, ForeignKey, text


class MixinCRUD:
    """
    Add common fields for all tables
    """
    system_fields = {
        'created_at', 'updated_at', 'deleted_at',
        'created_by', 'updated_by', 'deleted_by'
    }

    def label_created(self, user_id: int):
        """Label entity as created"""
        setattr(self, 'created_at', datetime.utcnow())
        setattr(self, 'created_by', user_id)

    def label_updated(self, user_id: int):
        """Label entity as updated"""
        setattr(self, 'updated_at', datetime.utcnow())
        setattr(self, 'updated_by', user_id)

    def label_deleted(self, user_id: int):
        """Label entity as deleted"""
        setattr(self, 'deleted_at', datetime.utcnow())
        setattr(self, 'deleted_by', user_id)

    @declared_attr
    def created_at(self):
        """Database field - entity creating time"""
        return Column(DateTime, nullable=True, server_default=text('now()'))

    @declared_attr
    def created_by(self):
        """Database field = user_id who created the entity"""
        return Column(Integer,  ForeignKey('users.id'), nullable=True)

    @declared_attr
    def updated_at(self):
        """Database field = entity updating time"""
        return Column(DateTime, nullable=True, server_default=text('now()'))

    @declared_attr
    def updated_by(self):
        """Database field = user_id who updated the entity"""
        return Column(Integer,  ForeignKey('users.id'), nullable=True)

    @declared_attr
    def deleted_at(self):
        """Database field = entity deleting time"""
        return Column(DateTime, nullable=True, server_default=None)

    @declared_attr
    def deleted_by(self):
        """Database field = user_id who deleted the entity"""
        return Column(Integer,  ForeignKey('users.id'), nullable=True)

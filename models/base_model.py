#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import storage

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        storage.delete(self)

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy.pop('_sa_instance_state', None)
        return dict_copy

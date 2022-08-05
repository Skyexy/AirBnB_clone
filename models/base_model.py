#!/usr/bin/python3
""" base_model Module for BaseModule and other classes"""
from datetime import datetime
import models
import uuid
from json import JSONEncoder


class BaseModel:
    """ BaseModel class """
    def __init__(self, **kwargs):
        """ init """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                        value,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ save dict to dict_repr dictionary"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.isoformat()
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def __str__(self):
        """ string representation of the class """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel
    """

    def default(self, o):
        """ default"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)

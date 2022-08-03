from datetime import datetime
from models import storage
import uuid
from json import JSONEncoder


class BaseModel:
    def __init__(self, **kwargs):
        if kwargs:
            self.id = kwargs['id']
            self.name = kwargs['name']
            self.my_number = kwargs['my_number']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dicta = {'my_number': self.my_number, 'name': self.name, '__class__': __class__.__name__,
                 'updated_at': self.updated_at.isoformat(), 'id': self.id, 'created_at': self.created_at.isoformat()}
        return dicta

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel
    """

    def default(self, o):
        """ default"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)

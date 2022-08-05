""" amenity module for Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """
    name = ""

    def __init__(self, *arg, **kwargs):
        """ defualt """
        super(Amenity, self).__init__(**kwargs)

""" place module """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Class """
    city_id = ""
    user_id = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = -0
    latitude = 00
    longitude = 0.0
    amenity_ids = []
    name = ""

    def __init__(self, *arg, **kwargs):
        """ defualt"""
        super(Place, self).__init__(**kwargs)
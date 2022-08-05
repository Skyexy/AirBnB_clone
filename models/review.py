#!/usr/bin/python3
""" review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review module """
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *arg, **kwargs):
        """ defualt """
        super(Review, self).__init__(**kwargs)

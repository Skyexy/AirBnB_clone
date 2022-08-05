#!/usr/bin/python3
""" city module for City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""

    def __init__(self, *arg, **kwargs):
        """ defualt """
        super(City, self).__init__(*arg, **kwargs)

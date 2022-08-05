#!/usr/bin/python3
""" state module for State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """

    name = ""

    def __init__(self, *arg, **kwargs):
        """ defualt """
        super(State, self).__init__(*arg, **kwargs)

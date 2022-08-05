""" user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """ user class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *arg, **kwargs):
        """ defualt"""
        super(User, self).__init__(*arg, **kwargs)

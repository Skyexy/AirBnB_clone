from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *arg, **kwargs):
        super(Amenity, self).__init__(**kwargs)

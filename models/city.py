from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *arg, **kwargs):
        super(City, self).__init__(*arg, **kwargs)
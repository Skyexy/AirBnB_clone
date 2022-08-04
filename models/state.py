from models.base_model import BaseModel

class State(BaseModel):

    name = ""

    def __init__(self, *arg, **kwargs):
        super(State, self).__init__(*arg, **kwargs)